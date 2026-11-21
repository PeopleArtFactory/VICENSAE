"""VICENSAE Voice — reproducible consolidation; first chorus upgraded only."""
import base64, hashlib, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
H = ROOT / 'history'
OUT = ROOT / 'release'
NAME = 'QSONG_VICENSAE_EL_PORVENIR_NO_ESTA_ESCRITO'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def decode(p, sr=44100):
    return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ac','2','-ar',str(sr),'-f','f32le','-']), dtype='<f4').reshape(-1,2).copy()
def rms(a): return float(np.sqrt(np.mean(a.astype('float64')**2)))
def build():
    OUT.mkdir(exist_ok=True)
    # Run frozen v0.9 in isolation: never overwrite historical source bytes.
    with tempfile.TemporaryDirectory() as t:
        w = Path(t)
        inputs = ['VICENSAE_PROSODIC_RENDER_v0.9.py','VICENSAE_ESTRIBILLO_v05_PHONETIC_PROFILE.json','VICENSAE_ESTRIBILLO_G_v08_TRACTO.mp3','VICENSAE_ESTRIBILLO_G_v08_ARTICULATORIA.mp3',NAME+'_v0.1.mp3',NAME+'_v0.1.qseed.json']
        for f in inputs: shutil.copy2(H/f,w/f)
        subprocess.run([sys.executable,str(w/inputs[0]),str(w)],check=True)
        for f in sorted(w.glob('VICENSAE_ESTRIBILLO_H_v09_*')):
            shutil.copy2(f,OUT/f.name.replace('H_v09','I_v10'))
    # Full-song preservation demo: only first chorus replaced. Other vocal sections remain v0.2.
    original = H/(NAME+'_v0.2_CANTADA.mp3')
    original_seed = H/(NAME+'_v0.2_CANTADA.qseed.json')
    chorus = OUT/'VICENSAE_ESTRIBILLO_I_v10_PROSODIA.mp3'
    score = json.loads(original_seed.read_text())
    profile = json.loads((H/'VICENSAE_ESTRIBILLO_v05_PHONETIC_PROFILE.json').read_text())
    sr=44100; a=decode(original,sr); b=decode(chorus,sr)
    origin=profile['source']['startSource']; n=round(origin*sr); length=round(profile['source']['duration']*sr)
    b=b[:length]; length=len(b); assert n+length<=len(a) and length>sr
    old=a[n:n+length].copy(); b*=rms(old)/max(rms(b),1e-9)
    fade=min(round(.12*sr),length//2); env=np.ones(length,dtype='float32'); env[:fade]=np.linspace(0,1,fade); env[-fade:]=np.linspace(1,0,fade)
    a[n:n+length]=old*(1-env[:,None])+b*env[:,None]
    # Do not alter the rest of the decoded signal; cap only the new region if necessary.
    a[n:n+length]=np.clip(a[n:n+length],-.98,.98)
    assert np.isfinite(a).all()
    mp3=OUT/(NAME+'_v1.0_HYBRID.mp3')
    subprocess.run(['ffmpeg','-y','-v','error','-f','f32le','-ar',str(sr),'-ac','2','-i','-','-codec:a','libmp3lame','-b:a','192k',str(mp3)],input=a.astype('<f4').tobytes(),check=True)
    # Preserve wire version; additive provenance, no authoritative DFD or commercial admission.
    score['payload']['audio'].update(sha256=sha(mp3),sourceV02MixSha256=sha(original),vocalStemSha256=None)
    score['payload']['provenance'].update(revision='1.0',status='experimental hybrid full-song preview; first chorus only rendered with frozen v0.9 parametric voice; no DFD',voiceRelease={'version':'1.0','scope':'first chorus only','startSeconds':origin,'endSeconds':origin+length/sr,'otherSections':'v0.2 singing, re-encoded','sourceProfileSha256':sha(H/'VICENSAE_ESTRIBILLO_H_v09_PROFILE.json'),'generatedChorusSha256':sha(chorus),'crossfadeSeconds':fade/sr,'karaoke':'original word windows; approximate alignment','neural':False})
    score['payload']['provenance']['vocalSynthesis']='hybrid v0.2 + parametric v0.9 first chorus'; score['payload']['provenance'].pop('vocalSynthesisFallbackCount',None)
    seed=OUT/(NAME+'_v1.0_HYBRID.qseed.json'); seed.write_text(json.dumps(score,ensure_ascii=False,indent=2)+'\n')
    html=(H/(NAME+'_v0.2_CANTADA.html')).read_text()
    html=re.sub(r'data:audio/[^;]+;base64,[A-Za-z0-9+/=]+','data:audio/mpeg;base64,'+base64.b64encode(mp3.read_bytes()).decode(),html,count=1)
    html,count=re.subn(r'(<script[^>]*id="seed"[^>]*>).*?(</script>)',lambda m:m[1]+json.dumps(score,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+m[2],html,count=1,flags=re.S); assert count==1
    html=html.replace('Vocal v0.2','Vocal v1.0 · demo híbrida').replace('v0.2_CANTADA','v1.0_HYBRID')
    html=html.replace('Negentropía fiduciaria · Freedom as an Invariant','Negentropía fiduciaria · Freedom as an Invariant · Primer estribillo paramétrico; resto v0.2')
    hp=OUT/(NAME+'_v1.0_HYBRID.html'); hp.write_text(html)
    embedded=re.search(r'data:audio/mpeg;base64,([A-Za-z0-9+/=]+)',html).group(1); assert hashlib.sha256(base64.b64decode(embedded)).hexdigest()==sha(mp3)
    match=re.search(r'<script[^>]*id="seed"[^>]*>(.*?)</script>',html,re.S); assert json.loads(match[1])==score
    js=re.findall(r'<script>(.*?)</script>',html,re.S)
    for j in js: subprocess.run(['node','--check','-'],input=j,text=True,check=True)
    out=decode(mp3,sr); assert abs(len(out)-len(a))<=1152
    manifest={'status':'validated locally; no perceptual validation','durationSeconds':len(out)/sr,'firstChorusStartSeconds':origin,'firstChorusEndSeconds':origin+length/sr,'durationPreservedWithinSamples':abs(len(out)-len(a)),'audioEmbeddedSha256Matches':True,'seedEmbeddedMatches':True,'nodeSyntaxPassed':True,'python':sys.version.split()[0],'numpy':np.__version__,'scipy':__import__('scipy').__version__,'ffmpeg':subprocess.check_output(['ffmpeg','-version'],text=True).splitlines()[0],'files':{x.name:{'bytes':x.stat().st_size,'sha256':sha(x)} for x in sorted(OUT.iterdir()) if x.name!='MANIFEST_v1.0.json'}}
    (OUT/'MANIFEST_v1.0.json').write_text(json.dumps(manifest,indent=2)+'\n'); print(json.dumps(manifest,indent=2))
if __name__=='__main__': build()

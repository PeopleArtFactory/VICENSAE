import json, subprocess, hashlib, sys
from pathlib import Path
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.signal import butter,sosfilt
from scipy.io.wavfile import write
from scipy.interpolate import interp1d
P=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
SR=22050; DT=.005; rng=np.random.default_rng(697658446)
source=P/'VICENSAE_ESTRIBILLO_v05_PHONETIC_PROFILE.json'; old=P/'VICENSAE_ESTRIBILLO_G_v08_TRACTO.mp3'; ref=P/'VICENSAE_ESTRIBILLO_G_v08_ARTICULATORIA.mp3'; instrumental=P/'QSONG_VICENSAE_EL_PORVENIR_NO_ESTA_ESCRITO_v0.1.mp3'
p=json.loads(source.read_text()); duration=p['source']['duration']; N=round(duration*SR); t=np.arange(N)/SR; tf=np.arange(0,duration+DT,DT)
# F1,F2,F3, periodic gain, noise gain, noise class. These are engineering targets, not measured physiology.
V={'a':(730,1250,2700),'e':(450,2050,2800),'i':(300,2250,3000),'o':(420,900,2550),'u':(300,750,2400)}
C={'l':(350,1250,2700,.58,.025,0),'r':(400,1550,2600,.55,.09,0),'n':(270,1650,2500,.49,.035,0),'m':(250,950,2400,.48,.025,0),'B':(350,1100,2300,.42,.12,0),'D':(400,1500,2600,.42,.16,1),'j':(310,2200,3000,.65,.035,0),'w':(310,800,2350,.67,.025,0),'s':(350,1700,3000,.015,.85,2),'T':(400,1500,2700,.025,.63,1),'f':(380,1300,2600,.02,.48,1),'p':(400,1050,2300,0,.28,0),'t':(400,1800,3000,0,.65,2),'k':(450,1550,2750,0,.58,1),'d':(400,1700,2700,.17,.40,1)}
F=np.tile([500.,1500.,2700.],(len(tf),1)); voiced=np.zeros(len(tf)); noise=voiced.copy(); bands=np.zeros((len(tf),3)); midi=np.full(len(tf),65.); blend=voiced.copy(); events=[]
scorefile=P/'QSONG_VICENSAE_EL_PORVENIR_NO_ESTA_ESCRITO_v0.1.qseed.json'
score=json.loads(scorefile.read_text())['payload']; chords=next(x['notes'] for x in score['arrangement']['tracks'] if x['id']=='strings'); bpm=score['bpm']; origin=p['source']['startSource']
# Manually marked lexical stress (zero based vowel nucleus); monosyllables are not all accented.
stress={1:2,2:0,4:0,5:0,7:1,9:2,12:1,15:1,17:3,19:0,21:1,24:2,25:0,26:1,28:2,29:1,31:2,33:2,35:1,36:1,38:2,40:0,41:4}
phrase_end={4,9,15,21,26,31,36,41}; content=set(stress)|{10,11,34,39}; phrase_gain=[.92,1.0,1.02,.91,1.04,1.09,1.12,1.04]
pg=np.ones(len(tf)); vib=np.zeros(len(tf)); breath=np.zeros(len(tf)); accents=[]; ornament_count=0
for wi,w in enumerate(p['events']):
 a=w['start']; b=a+w['duration']; wix=(tf>=a)&(tf<b); midi[wix]=w['midi']; pg[wix]=phrase_gain[sum(x<wi for x in phrase_end)]
 phones=w['phonemes']; vi=[j for j,x in enumerate(phones) if x['vowel']]; st=stress.get(wi,0); assert st<len(vi)
 # Redistribute the vowel budget within each word; boundaries and consonant durations unchanged.
 dur=np.array([x['targetDuration'] for x in phones]); before=dur.copy(); weights=np.ones(len(vi)); weights[st]=1.40 if wi in stress else 1.0
 if wi in phrase_end: weights[-1]*=1.22
 if len(vi)>1:
  weighted=dur[vi]*weights; dur[vi]=weighted*sum(dur[vi])/sum(weighted)
 starts=np.r_[0,np.cumsum(dur)[:-1]]; assert abs(sum(dur)-w['duration'])<.0003,(wi,sum(dur),w['duration'])
 # One optional chord-tone neighbor on a non-tonic nucleus, selected from the backing harmony.
 addnote={}; candidates=[j for j in range(len(vi)) if j!=st and dur[vi[j]]>=.08]
 if candidates and wi in {1,2,4,7,9,12,15,17,19,21,24,26,28,29,31,33,35,36,38,40,41}:
  j=min(candidates,key=lambda j:abs(j-st)); jj=vi[j]; mid=(origin+a+starts[jj]+dur[jj]/2)*bpm/60
  pcs={n['midi']%12 for n in chords if n['startBeat']<=mid<n['startBeat']+n['durationBeats']+.05}
  opts=[w['midi']+d for d in [-2,2,-3,3,-4,4] if (w['midi']+d)%12 in pcs]
  if opts: addnote[jj]=opts[0]; ornament_count+=1
 accents.append(dict(word=w['word'],tonicNucleus=st if wi in stress else None,originalVowelDurations=before[vi].tolist(),newVowelDurations=dur[vi].tolist(),anchorMidi=w['midi'],phraseEnd=wi in phrase_end))
 for pi,ph in enumerate(phones):
  raw=ph['phoneme']; phn=raw if raw!='**' else 'r'; start=a+starts[pi]; end=start+dur[pi]; ix=np.flatnonzero((tf>=start)&(tf<end)); z=np.clip((tf[ix]-start)/max(end-start,1e-6),0,1)
  if ph['vowel']:
   letters=[c.lower() for c in phn if c.lower() in V] or ['a']; f1=np.array(V[letters[0]]); f2=np.array(V[letters[-1]]); ramp=np.clip((z-.22)/.65,0,1); F[ix]=f1+(f2-f1)*ramp[:,None]; is_tonic=(pi==vi[st] and wi in content); voiced[ix]=(.99 if is_tonic else .80)*( .82+.18*np.sin(np.pi*z)); noise[ix]=.027; bands[ix,0]=1; blend[ix]=.57
   midi[ix]=addnote.get(pi,w['midi']); vib[ix]=np.clip((z-.30)/.45,0,1)*(.25 if is_tonic else .09)
   # Short grace-to-anchor melismas on selected cadential vowels, only where duration allows.
   if wi in {9,21,31,41} and pi==vi[st] and dur[pi]>.17:
    mid=(origin+start+dur[pi]*.15)*bpm/60; pcs={n['midi']%12 for n in chords if n['startBeat']<=mid<n['startBeat']+n['durationBeats']+.05}; opts=[w['midi']+d for d in [-2,2,-3,3] if (w['midi']+d)%12 in pcs]
    if opts: midi[ix[z<.24]]=opts[0]; ornament_count+=1
  else:
   f1,f2,f3,vg,ng,band=C[phn]; F[ix]=[f1,f2,f3]; voiced[ix]=vg; noise[ix]=ng; bands[ix,band]=1; blend[ix]=.26
   if phn in 'ptkd':
    burst=np.exp(-.5*((z-.84)/.16)**2); noise[ix]*=burst; voiced[ix]*=np.clip((z-.68)*4,0,1)
   if phn=='r': voiced[ix]*=1-.68*np.exp(-.5*((z-.5)/.12)**2)
  events.append(dict(word=w['word'],phoneme=raw,modelPhone=phn,start=start,end=end,voiced=bool(ph['vowel']),midiTargets=sorted(set(midi[ix].tolist())),tonic=bool(ph['vowel'] and pi==vi[st] and wi in stress)))
 if wi in phrase_end and wi+1<len(p['events']):
  nxt=p['events'][wi+1]['start']; gap=nxt-b
  if gap>.13:
   ix=(tf>b+.035)&(tf<nxt-.035); z=(tf[ix]-b-.035)/(gap-.07); breath[ix]=.055*np.sin(np.pi*z)**2
# Fill pitch/formants across short gaps by nearest known targets; preserve silent longer gaps in excitation envelopes.
active= (voiced+noise)>0; active_i=np.flatnonzero(active)
for c in range(3): F[:,c]=np.interp(tf,tf[active_i],F[active_i,c])
midi=np.interp(tf,tf[active_i],midi[active_i]); F=gaussian_filter1d(F,2.2,axis=0); voiced=gaussian_filter1d(voiced,1.05); noise=gaussian_filter1d(noise,.65); bands=gaussian_filter1d(bands,1.,axis=0); blend=gaussian_filter1d(blend,1.4)
midi=gaussian_filter1d(midi,1.6); vib=gaussian_filter1d(vib,1.5); f0=440*2**((midi-69+(vib*np.sin(2*np.pi*5.15*tf)+.025*np.sin(2*np.pi*2.2*tf)))/12)
f0s=np.interp(t,tf,f0); phase=2*np.pi*np.cumsum(f0s)/SR
# Continuous harmonic source, formant weighting, no phase restarts at phoneme boundaries.
ks=np.arange(1,49); freq=f0[:,None]*ks; amp=ks[None,:]**(-1.25)*(.10+sum(g*np.exp(-.5*((freq-F[:,i,None])/bw)**2) for i,(g,bw) in enumerate([(1.9,125),(1.4,175),(.85,250)])))
amp*=np.clip((SR*.47-freq)/(SR*.03),0,1); amp/=np.sqrt(np.sum(amp**2,axis=1,keepdims=True)+1e-9); y=np.zeros(N)
for i,k in enumerate(ks): y+=np.interp(t,tf,amp[:,i])*np.sin(k*phase+0.35*k)
y*=np.interp(t,tf,voiced)*.105
for i,(lo,hi) in enumerate([(300,2600),(1400,5800),(3500,9000)]):
 z=sosfilt(butter(2,[lo,hi],fs=SR,btype='bandpass',output='sos'),rng.standard_normal(N)); z/=np.std(z); y+=z*np.interp(t,tf,noise*bands[:,i])*.075
# Phrase dynamics and discrete breaths are added to the continuous parametric voice.
y*=np.interp(t,tf,gaussian_filter1d(pg,8))
z=sosfilt(butter(2,[900,5200],fs=SR,btype='bandpass',output='sos'),rng.standard_normal(N)); z/=np.std(z); y+=z*np.interp(t,tf,breath)*.10

def load(path,channels=1,start=0):
 cmd=['ffmpeg','-v','error','-ss',str(start),'-i',str(path),'-t',str(duration),'-ac',str(channels),'-ar',str(SR),'-f','f32le','-']; z=np.frombuffer(subprocess.check_output(cmd),dtype='<f4').reshape(-1,channels); return np.pad(z,((0,max(0,N-len(z))),(0,0)))[:N].astype(float)
def rms(x):return np.sqrt(np.mean(x*x))
def db(x):return float(20*np.log10(max(rms(x),1e-12)))
prev=load(old)[:,0]; y*=rms(prev)/rms(y); inst=load(instrumental,2,origin); refmix=.76*prev[:,None]+.57*inst; mix=.76*y[:,None]+.57*inst
# Shared gain across the two mixes after individual voice RMS matching so backing is unchanged.
gain=min(1,.95/max(np.max(np.abs(mix)),np.max(np.abs(refmix)))); mix*=gain; refmix*=gain
base='VICENSAE_ESTRIBILLO_H_v09_'; files={}
for name,x in [('PROSODIA',mix),('LOGOS',y),('REFERENCIA_PARAM_v08',refmix)]:
 assert np.all(np.isfinite(x)); assert np.max(np.abs(x))<1
 path=P/(base+name+'.mp3'); a=x.astype('<f4'); subprocess.run(['ffmpeg','-y','-v','error','-f','f32le','-ar',str(SR),'-ac',str(1 if a.ndim==1 else a.shape[1]),'-i','-','-codec:a','libmp3lame','-b:a','160k',str(path)],input=a.tobytes(),check=True); files[path.name]={'rms_dbfs_preencode':db(x),'peak_dbfs_preencode':float(20*np.log10(np.max(np.abs(x)))),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
profile={'status':'experimental continuous parametric singing; lexical stress and phrase prosody; no listening validation; no neural model','duration':N/SR,'sampleRate':SR,'wordCount':len(accents),'vowelCount':sum(len(a['newVowelDurations']) for a in accents),'polysyllabicStressCount':len(stress),'ornaments':ornament_count,'phraseEnds':sorted(phrase_end),'breaths':int(np.sum(np.diff((breath>0).astype(int))==1)),'events':events,'accentPlan':accents,'files':files,'sources':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in [source,old,instrumental,scorefile]},'limitations':['original word windows preserved; consonant durations unchanged','new melodic notes are selected from chord at nucleus midpoint, not guaranteed chord tones at all moments','approximate phone boundaries inherited from v0.5','comparison uses standalone parametric v0.8, not hybrid v0.8; multiple prosodic factors changed']}
(P/(base+'PROFILE.json')).write_text(json.dumps(profile,ensure_ascii=False,indent=2)); print(json.dumps({k:v for k,v in profile.items() if k not in ['events','accentPlan','sources']},indent=2))

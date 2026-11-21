import json, subprocess, hashlib, sys
from pathlib import Path
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.signal import butter,sosfilt
from scipy.io.wavfile import write
from scipy.interpolate import interp1d
P=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
SR=22050; DT=.005; rng=np.random.default_rng(697658446)
source=P/'VICENSAE_ESTRIBILLO_v05_PHONETIC_PROFILE.json'; old=P/'VICENSAE_ESTRIBILLO_F_v07_LOGOS.mp3'; ref=P/'VICENSAE_ESTRIBILLO_F_v07_GLOTICA.mp3'; instrumental=P/'QSONG_VICENSAE_EL_PORVENIR_NO_ESTA_ESCRITO_v0.1.mp3'
p=json.loads(source.read_text()); duration=p['source']['duration']; N=round(duration*SR); t=np.arange(N)/SR; tf=np.arange(0,duration+DT,DT)
# F1,F2,F3, periodic gain, noise gain, noise class. These are engineering targets, not measured physiology.
V={'a':(730,1250,2700),'e':(450,2050,2800),'i':(300,2250,3000),'o':(420,900,2550),'u':(300,750,2400)}
C={'l':(350,1250,2700,.58,.025,0),'r':(400,1550,2600,.55,.09,0),'n':(270,1650,2500,.49,.035,0),'m':(250,950,2400,.48,.025,0),'B':(350,1100,2300,.42,.12,0),'D':(400,1500,2600,.42,.16,1),'j':(310,2200,3000,.65,.035,0),'w':(310,800,2350,.67,.025,0),'s':(350,1700,3000,.015,.85,2),'T':(400,1500,2700,.025,.63,1),'f':(380,1300,2600,.02,.48,1),'p':(400,1050,2300,0,.28,0),'t':(400,1800,3000,0,.65,2),'k':(450,1550,2750,0,.58,1),'d':(400,1700,2700,.17,.40,1)}
F=np.tile([500.,1500.,2700.],(len(tf),1)); voiced=np.zeros(len(tf)); noise=voiced.copy(); bands=np.zeros((len(tf),3)); midi=np.full(len(tf),65.); blend=voiced.copy(); events=[]
for w in p['events']:
 a=w['start']; b=a+w['duration']; midi[(tf>=a)&(tf<b)]=w['midi']
 for ph in w['phonemes']:
  raw=ph['phoneme']; phn=raw if raw!='**' else 'r'; start=a+ph['targetStart']; end=start+ph['targetDuration']; ix=np.flatnonzero((tf>=start)&(tf<end)); z=np.clip((tf[ix]-start)/max(end-start,1e-6),0,1)
  if ph['vowel']:
   letters=[c.lower() for c in phn if c.lower() in V] or ['a']; f1=np.array(V[letters[0]]); f2=np.array(V[letters[-1]]); ramp=np.clip((z-.22)/.65,0,1); F[ix]=f1+(f2-f1)*ramp[:,None]; voiced[ix]=.95; noise[ix]=.025; bands[ix,0]=1; blend[ix]=.57
  else:
   f1,f2,f3,vg,ng,band=C[phn]; F[ix]=[f1,f2,f3]; voiced[ix]=vg; noise[ix]=ng; bands[ix,band]=1; blend[ix]=.26
   if phn in 'ptkd':
    burst=np.exp(-.5*((z-.84)/.16)**2); noise[ix]*=burst; voiced[ix]*=np.clip((z-.68)*4,0,1)
   if phn=='r': voiced[ix]*=1-.68*np.exp(-.5*((z-.5)/.12)**2)
  events.append(dict(word=w['word'],phoneme=raw,modelPhone=phn,start=start,end=end,voiced=bool(ph['vowel'])))
# Fill pitch/formants across short gaps by nearest known targets; preserve silent longer gaps in excitation envelopes.
active= (voiced+noise)>0; active_i=np.flatnonzero(active)
for c in range(3): F[:,c]=np.interp(tf,tf[active_i],F[active_i,c])
midi=np.interp(tf,tf[active_i],midi[active_i]); F=gaussian_filter1d(F,2.2,axis=0); voiced=gaussian_filter1d(voiced,1.05); noise=gaussian_filter1d(noise,.65); bands=gaussian_filter1d(bands,1.,axis=0); blend=gaussian_filter1d(blend,1.4)
midi=gaussian_filter1d(midi,2.5); f0=440*2**((midi-69+(0.22*np.sin(2*np.pi*5.15*tf)+.035*np.sin(2*np.pi*2.2*tf)))/12)
f0s=np.interp(t,tf,f0); phase=2*np.pi*np.cumsum(f0s)/SR
# Continuous harmonic source, formant weighting, no phase restarts at phoneme boundaries.
ks=np.arange(1,49); freq=f0[:,None]*ks; amp=ks[None,:]**(-1.25)*(.10+sum(g*np.exp(-.5*((freq-F[:,i,None])/bw)**2) for i,(g,bw) in enumerate([(1.9,125),(1.4,175),(.85,250)])))
amp*=np.clip((SR*.47-freq)/(SR*.03),0,1); amp/=np.sqrt(np.sum(amp**2,axis=1,keepdims=True)+1e-9); y=np.zeros(N)
for i,k in enumerate(ks): y+=np.interp(t,tf,amp[:,i])*np.sin(k*phase+0.35*k)
y*=np.interp(t,tf,voiced)*.105
for i,(lo,hi) in enumerate([(300,2600),(1400,5800),(3500,9000)]):
 z=sosfilt(butter(2,[lo,hi],fs=SR,btype='bandpass',output='sos'),rng.standard_normal(N)); z/=np.std(z); y+=z*np.interp(t,tf,noise*bands[:,i])*.075
# Use original vocal to retain articulation in hybrid; standalone tract is also exported.
def load(path,channels=1,start=0):
 cmd=['ffmpeg','-v','error','-ss',str(start),'-i',str(path),'-t',str(duration),'-ac',str(channels),'-ar',str(SR),'-f','f32le','-']; z=np.frombuffer(subprocess.check_output(cmd),dtype='<f4').reshape(-1,channels); return np.pad(z,((0,max(0,N-len(z))),(0,0)))[:N].astype(float)
def rms(x):return np.sqrt(np.mean(x*x))
def db(x):return float(20*np.log10(max(rms(x),1e-12)))
v=load(old)[:,0]; tr=y*rms(v)/max(rms(y),1e-9); mixcoef=np.interp(t,tf,blend); hybrid=v*(1-mixcoef)+tr*mixcoef; hybrid*=rms(v)/rms(hybrid)
inst=load(instrumental,2,p['source']['startSource']); reference=load(ref,2); mix=.76*hybrid[:,None]+.57*inst; mix*=rms(reference)/rms(mix)
# Equal RMS comparison for both isolated voices; avoid clipping.
base='VICENSAE_ESTRIBILLO_G_v08_'; files={}
for name,x in [('ARTICULATORIA',mix),('LOGOS',hybrid),('TRACTO',tr)]:
 x=x*min(1,.96/max(np.max(np.abs(x)),1e-9)); path=P/(base+name+'.mp3'); a=x.astype('<f4'); subprocess.run(['ffmpeg','-y','-v','error','-f','f32le','-ar',str(SR),'-ac',str(1 if a.ndim==1 else a.shape[1]),'-i','-','-codec:a','libmp3lame','-b:a','160k',str(path)],input=a.tobytes(),check=True); files[path.name]={'rms_dbfs_preencode':db(x),'peak_dbfs_preencode':float(20*np.log10(np.max(np.abs(x)))),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
profile={'status':'experimental parametric continuous formant vocoder, not neural or physical vocal tract; independent synthetic consonants and vowels; hybrid retains v0.7; no perceptual validation','duration':N/SR,'sampleRate':SR,'controlFrameSeconds':DT,'controlFrames':len(tf),'events':events,'maxHarmonics':48,'nominalVowelSyntheticMix':.57,'nominalConsonantSyntheticMix':.26,'referenceRmsDbfs':db(reference),'files':files,'sources':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in [source,old,ref,instrumental]},'constraints':['word-level melody retained','five ** phones mapped to r by lexical context','noise and formants approximate; no phonetic ground-truth alignment']}
(P/(base+'PROFILE.json')).write_text(json.dumps(profile,ensure_ascii=False,indent=2)); print(json.dumps({k:v for k,v in profile.items() if k not in ['events','sources']},indent=2)); print('phonemes',len(events))

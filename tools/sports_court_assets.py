"""Build a seamless, distant school sports bed from two documented CC0 sources."""
from pathlib import Path
import hashlib,json,subprocess
import numpy as np
import imageio_ffmpeg

R=Path(__file__).resolve().parent.parent
S=R/'source/audio_revision_20261107'
FF=imageio_ffmpeg.get_ffmpeg_exe()
RATE=44100
def decode(name,start,duration,filters):
    raw=subprocess.check_output([FF,'-v','error','-ss',str(start),'-t',str(duration),'-i',str(S/'originals'/(name+'.mp3')),'-af',filters,'-ar',str(RATE),'-ac','2','-f','f32le','-'])
    return np.frombuffer(raw,dtype='<f4').reshape(-1,2).copy()

voices=decode('school_playground',90,48,'highpass=f=160,lowpass=f=3200,afftdn=nr=8:nf=-45,loudnorm=I=-26:TP=-5:LRA=8')
kick=decode('soccer_kick',0,0.8,'highpass=f=110,lowpass=f=4200,loudnorm=I=-21:TP=-5:LRA=8,afade=t=in:d=0.008,afade=t=out:st=0.55:d=0.25')
mix=voices*.55
times=[2.8,6.3,9.6,11.5,16.9,20.0,22.8,28.6,32.0,36.9,40.7,44.2]
gains=[.34,.26,.31,.22,.32,.24,.30,.25,.33,.23,.28,.24]
for when,gain in zip(times,gains):
    offset=int(when*RATE);mix[offset:offset+len(kick)]+=kick*gain
fade=int(1.5*RATE)
# Equal-power overlap: the end leads into the beginning without a hard cut.
theta=np.linspace(0,np.pi/2,fade,dtype=np.float32)[:,None]
seam=mix[-fade:]*np.cos(theta)+mix[:fade]*np.sin(theta)
loop=np.concatenate((seam,mix[fade:-fade]))
out=R/'audio/ambience/sports_court_day.ogg';out.parent.mkdir(parents=True,exist_ok=True)
filters='loudnorm=I=-24:TP=-4:LRA=8,alimiter=limit=0.60:level=false:latency=true'
subprocess.run([FF,'-v','error','-y','-f','f32le','-ar',str(RATE),'-ac','2','-i','-','-af',filters,'-ar',str(RATE),'-ac','2','-c:a','libvorbis','-q:a','5',str(out)],input=loop.astype('<f4').tobytes(),check=True)
raw=subprocess.check_output([FF,'-v','error','-i',str(out),'-ar',str(RATE),'-ac','2','-f','f32le','-'])
a=np.frombuffer(raw,dtype='<f4');assert np.isfinite(a).all() and np.max(np.abs(a))<1
proof=dict(status='PASS',file=out.relative_to(R).as_posix(),sources=['school_playground','soccer_kick'],voices_start=90,voices_duration=48,kick_times=times,kick_gains=gains,crossfade_seconds=1.5,processing=filters,seconds=len(a)/2/RATE,peak_dbfs=float(20*np.log10(np.max(np.abs(a)))),rms_dbfs=float(20*np.log10(np.sqrt(np.mean(a*a)))),sha256=hashlib.sha256(out.read_bytes()).hexdigest())
(S/'sports_processed.json').write_text(json.dumps(proof,indent=2),encoding='utf-8')
print('SPORTS_AUDIO_ASSET_PASS',proof['seconds'],proof['peak_dbfs'],flush=True)

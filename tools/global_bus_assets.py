"""Prepare the licensed public HQ recordings for the paced bus sequence."""
from pathlib import Path
import hashlib,json,subprocess,sys
import imageio_ffmpeg
R=Path(__file__).resolve().parent.parent
S=R/'source/audio_revision_20261107'
OUT=R/'audio/sfx/bus';OUT.mkdir(parents=True,exist_ok=True)
FF=imageio_ffmpeg.get_ffmpeg_exe()
def make(name,original,start,duration,filters,loop=False):
    target=OUT/(name+'.ogg')
    command=[FF,'-hide_banner','-loglevel','error','-y','-ss',str(start),'-t',str(duration),'-i',str(S/'originals'/(original+'.mp3'))]
    if loop:
        fade=.25 if duration<10 else 1.5
        graph='[0:a]'+filters+',asplit=2[a][b];[a][b]acrossfade=d='+str(fade)+':c1=qsin:c2=qsin,atrim=start='+str(duration-fade)+':duration='+str(duration-fade)+',asetpts=PTS-STARTPTS[out]'
        command+=['-filter_complex',graph,'-map','[out]']
    else:command+=['-af',filters+',alimiter=limit=0.60:level=false:latency=true']
    command+=['-ar','44100','-ac','2','-c:a','libvorbis','-q:a','5',str(target)]
    subprocess.run(command,check=True)
    return dict(file=target.relative_to(R).as_posix(),source=original,start=start,duration=duration,processing=filters,loop=loop,sha256=hashlib.sha256(target.read_bytes()).hexdigest())
selected=set(sys.argv[1:])
previous=json.loads((S/'processed.json').read_text(encoding='utf-8')) if (S/'processed.json').exists() else []
prepare=make
def make(name,*args,**kwargs):
    if selected and name not in selected:
        return next(row for row in previous if row['file']==('audio/sfx/bus/'+name+'.ogg'))
    return prepare(name,*args,**kwargs)
rows=[]
rows.append(make('engine_distant_loop','engine_clean',1.0,7.0,'highpass=f=45,lowpass=f=420,afftdn=nr=10:nf=-45,loudnorm=I=-23:TP=-4:LRA=8',True))
rows.append(make('engine_near_loop','engine_clean',1.0,7.0,'highpass=f=45,lowpass=f=2600,afftdn=nr=10:nf=-45,loudnorm=I=-23:TP=-4:LRA=8',True))
rows.append(make('air_brake_stop','air_bleed',0,0.38,'highpass=f=90,lowpass=f=7000,atempo=0.8,loudnorm=I=-23:TP=-4:LRA=9,afade=t=in:d=0.012,afade=t=out:st=0.34:d=0.13'))
rows.append(make('pneumatic_door_open','door_open',0,2.02,'highpass=f=65,lowpass=f=7000,loudnorm=I=-22:TP=-4:LRA=9,afade=t=in:d=0.015,afade=t=out:st=1.86:d=0.16'))
rows.append(make('pneumatic_door_close','door_close',0,1.94,'highpass=f=65,lowpass=f=7000,loudnorm=I=-22:TP=-4:LRA=9,afade=t=in:d=0.025,afade=t=out:st=1.70:d=0.24'))
rows.append(make('departure_fading','engine_clean',0.5,8.3,'highpass=f=45,lowpass=f=2600,afftdn=nr=10:nf=-45,asetrate=48000*1.08,aresample=44100,loudnorm=I=-23:TP=-4:LRA=9,afade=t=in:d=0.25,afade=t=out:st=3.8:d=3.8'))
rows.append(make('uncanny_drone_loop','drone',20,45,'highpass=f=28,lowpass=f=1900,loudnorm=I=-24:TP=-3:LRA=8',True))
rows.append(make('female_chuckle_behind','female_chuckle',0,1.02,'highpass=f=100,lowpass=f=6500,loudnorm=I=-20:TP=-3:LRA=7,afade=t=in:d=0.015,afade=t=out:st=0.88:d=0.14'))
rows.append(make('uncanny_knock_sting','drone',20,8,'highpass=f=28,lowpass=f=1900,loudnorm=I=-24:TP=-3:LRA=8,afade=t=in:d=0.6,afade=t=out:st=5.5:d=2.5'))
(S/'processed.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('BUS_AUDIO_ASSETS',len(rows),flush=True)

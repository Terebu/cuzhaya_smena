"""Idempotent staging patch after day-four generation."""
from pathlib import Path
R=Path(__file__).resolve().parent.parent
P=R/'days/day04'
def edit(name,fn):
 p=P/name;s=p.read_text(encoding='utf8');s=fn(s);p.write_text(s,encoding='utf8')
def before(s,line,code):
 target='    cs_narrator "'+line+'"'
 if code+'\n'+target not in s:s=s.replace(target,code+'\n'+target,1)
 return s
def overlay(name):return '    show cs_d4_document '+name+' at cs_d4_document_center zorder 40\n    with dissolve'
def hide():return '    hide cs_d4_document\n    with dissolve'
def scene(name):return '    $ cs_director_scene("'+name+'")\n    scene '+name+'\n    $ cs_frame_focus([])\n    with dissolve'
def one(s):
 s=before(s,'На стене висели фотографии.',scene('cs_d4_old_photo_room'))
 s=before(s,'На центральной фотографии стоял пионерский отряд.',overlay('photo1963'))
 s=before(s,'Потом снова на коридор.',hide())
 return s
def three(s):
 s=s.replace('bg int_catacombs_living','cs_d4_old_bunker')
 s=before(s,'Я медленно раскрыла папку.',scene('cs_d4_old_archive'))
 s=before(s,'Сначала увидела таблицу с фамилиями.',overlay('roster1971'))
 s=before(s,'Там находилась фотография.',hide()+'\n'+overlay('photo1971'))
 s=before(s,'1963.',hide()+'\n'+overlay('photo1963'))
 s=before(s,'Остальные документы вернула на место.',hide())
 # After the reunion illustration, Darya is visible in the supplied sports outfit.
 marker='    scene cs_d4_old_stairs'
 pos=s.find(marker,s.find('scene cs_cg_lena_darya_bunker_reunion'))
 if pos!=-1 and "show cs_darya worried sport normal" not in s:
  tail=s[pos:];tail=tail.replace("$ cs_d4_scene_cast = []","show cs_darya worried sport normal at cs_darya_normal_center\n    $ cs_d4_scene_cast = ['cs_darya']",1);s=s[:pos]+tail
 return s
def four(s):
 s=s.replace("$ cs_d4_scene_cast = []","show cs_darya neutral sport normal at cs_darya_normal_center\n    $ cs_d4_scene_cast = ['cs_darya']",1)
 s=s.replace("$ cs_d4_scene_cast = ['cs_semen']","show cs_darya neutral sport normal at cs_darya_normal_right\n    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']",1)
 return s
def five(s):
 s=s.replace("$ cs_d4_scene_cast = ['cs_semen']","show cs_darya neutral sport normal at cs_darya_normal_right\n    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']",1)
 marker="    $ cs_d4_scene_cast = ['cs_darya']"
 if 'show cs_darya smile pioneer normal' not in s:s=s.replace(marker,'    show cs_darya smile pioneer normal at cs_darya_normal_center\n'+marker,1)
 return s
for name,fn in [('01_scene.rpy',one),('03_scene.rpy',three),('04_scene.rpy',four),('05_scene.rpy',five)]:
 p=P/name
 # Do not repeat the costume insertions on already patched scripts.
 if name in ['04_scene.rpy','05_scene.rpy'] and 'show cs_darya neutral sport normal' in p.read_text(encoding='utf8'):continue
 edit(name,fn)
edit('resources.rpy',lambda s:s.replace('old_camp_stairs_down.png','old_camp_stairwell_down.png'))

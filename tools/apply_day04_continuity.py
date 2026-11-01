"""Authored location/voice corrections; safe to reapply after generation."""
from pathlib import Path
R=Path(__file__).resolve().parent.parent
P=R/'days/day04'
def frame(bg,cast='[]'):
 return '    $ cs_director_scene("'+bg+'")\n    scene '+bg+'\n    $ cs_d4_scene_cast = '+cast+'\n    $ cs_frame_focus(cs_d4_scene_cast)\n    with Dissolve(0.7)'
def before(s,text,code):
 target='    cs_narrator "'+text+'"'
 if code+'\n'+target not in s:s=s.replace(target,code+'\n'+target,1)
 return s
def edit(name,fn):
 p=P/name;s=p.read_text(encoding='utf8');p.write_text(fn(s),encoding='utf8')
def one(s):
 return before(s,'Я всмотрелась в коридор.',frame('cs_d4_old_corridor'))
def two(s):
 # The first block is still inside the photo room; the later exit is preserved.
 return s.replace('cs_d4_old_corridor','cs_d4_old_photo_room',2)
def three(s):
 s=s.replace('    cs_d4_voice "Лена?!"','    cs_da "Лена?!"')
 s=s.replace('    cs_d4_voice "','    cs_d4_unknown_girl "')
 s=before(s,'Из коридора донеслись быстрые шаги.',frame('cs_d4_old_bunker'))
 s=before(s,'В коридоре никого не было.',frame('bg int_catacombs_entrance'))
 # Reorder the return from darkness so the lit room appears on arrival.
 target='    cs_narrator "Добравшись до освещённого коридора, я почти ввалилась в техническую комнату."'
 room=frame('cs_d4_old_bunker')
 s=s.replace(target+'\n'+room,room+'\n'+target)
 s=before(s,'И почти добралась до лестницы наверх, когда услышала шаги.',frame('cs_d4_old_stairs'))
 s=before(s,'Она остановилась на ступеньке.','    show cs_darya worried sport normal at cs_darya_normal_center\n    $ cs_d4_scene_cast = ["cs_darya"]\n    $ cs_frame_focus(cs_d4_scene_cast)\n    with cs_sprite_change')
 s=s.replace('В коридоре стало тихо.','На лестничной площадке стало тихо.')
 return s
def eleven(s):
 old=frame('bg ext_square_sunset',"['cs_darya', 'cs_zhenya', 'cs_semen', 'el']")
 cue='    cs_narrator "И наконец я увидела знакомую фигуру."'
 if old+'\n'+cue in s:
  s=s.replace(old+'\n'+cue,"    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen', 'el']\n    $ cs_frame_focus(cs_d4_scene_cast)\n    with cs_sprite_change\n"+cue,1)
 s=before(s,'Я оглядела площадь.',frame('bg ext_square_sunset',"['cs_darya', 'cs_zhenya']"))
 return s
def twelve(s):
 s=before(s,'Мы направились к своему домику.',frame('cs_camp_path_night',"['cs_darya']"))
 # Warm lamp/night backgrounds require the matching time state for actors.
 needle='    $ cs_director_scene("cs_library_interior_night")'
 if '    $ night_time()\n'+needle not in s:s=s.replace(needle,'    $ night_time()\n    $ persistent.sprite_time = "night"\n'+needle,1)
 return s
edit('01_scene.rpy',one)
# Limit the initial room correction to the pre-corridor section for idempotence.
p=P/'02_scene.rpy';s=p.read_text(encoding='utf8');a=s.index('    cs_narrator "Я осторожно вышла в коридор."');head=s[:a];pos=head.rfind('    $ cs_director_scene("cs_d4_old_corridor")');initial=head[:pos] if pos>0 else head
if s.startswith('#') and 'cs_d4_old_photo_room' not in s[:500]:s=two(s)
p.write_text(s,encoding='utf8')
edit('03_scene.rpy',three)
edit('11_scene.rpy',eleven)
edit('12_scene.rpy',twelve)
edit('resources.rpy',lambda s:s.replace('    cs_d4_voice = Character(None,','    cs_d4_voice = Character(None,') if 'cs_d4_unknown_girl = ' in s else s.replace('init 20 python:', 'init 20 python:\n    cs_d4_unknown_girl = Character(u"???", color="#b8a8d8", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")',1))

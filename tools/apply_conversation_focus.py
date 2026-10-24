"""Explicit POV beats chosen from the story, independent of speaker/line count.

Keep all participants in shared conversation. The only edits here are a look
around a room, finding Zhenya in a crowd, and greeting those now in focus.
RenPy guidance: https://www.renpy.org/doc/html/displaying_images.html#hide-statement
"""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parent.parent
plans={
 'days/day01/part10/54_librarian.rpy':[
  ('cs_narrator "Я огляделась."',[], 'Lena examines the room, not her companions'),
  ('cs_narrator "За столом сидела девушка в очках."',['cs_zhenya'],'Lena finds the librarian at her desk'),
  ('cs_narrator "Дарья поздоровалась следом."',['cs_zhenya','cs_darya'],'Darya joins the greeting; keep both throughout the conversation')],
 'days/day03/part03/90_scene.rpy':[
  ('cs_narrator "У столовой уже собирался народ."',[],'Lena looks for Zhenya among the crowd'),
  ('cs_narrator "Дарья пошла рядом."',['cs_darya','cs_zhenya'],'The three meet and converse together')]
}
for name,cues in plans.items():
 p=R/name;s=p.read_text(encoding='utf8')
 for i,(line,tags,reason) in enumerate(cues):
  marker='# cs_authored_pov_'+str(i)
  if marker in s:continue
  assert s.count('    '+line+'\n')==1,(name,line)
  block='    '+marker+': '+reason+'\n    $ cs_frame_focus('+json.dumps(tags)+')\n    with cs_sprite_change\n'
  s=s.replace('    '+line+'\n',block+'    '+line+'\n')
 p.write_text(s,encoding='utf8')
# Reviewed story beats. Each pair marks turning inward and looking up again.
# These are authoring anchors, not a runtime rule based on how many lines pass.
inward=[
 ('days/day01/part09/50_no_saves.rpy','cs_narrator','Отсюда открывался вид на деревья и несколько домиков, освещённых вечерним солнцем.','cs_narrator','Дарья заметила моё выражение лица.'),
 ('days/day01/part09/50_no_saves.rpy','cs_narrator','А я вдруг подумала, что, возможно, именно в этом и заключается самая большая разница между игрой и происходящим.',None,None),
 ('days/day02/part06/46_scene.rpy','cs_narrator','Я достала сложенный листок.','cs_ls','Что записать в качестве заключения?'),
 ('days/day02/part08/57_scene.rpy','cs_th','Да.',None,None),
 ('days/day02/part09/65_scene.rpy','cs_th','И всё-таки наш плакат сработал.','cs_narrator','Дарья посмотрела на меня.'),
 ('days/day02/part10/69_scene.rpy','cs_th','Забавно.','cs_narrator','Дарья подошла ближе.'),
 ('days/day03/part02/84_scene.rpy','cs_th','Вот теперь действительно заметен прогресс.','cs_ls','Всё, готово.'),
 ('days/day03/part02/88_scene.rpy','cs_th','А ещё начинаю понимать, что хорошее утро необязательно должно содержать какое-нибудь невероятное событие.','cs_da','Что?'),
 ('days/day03/part04/96_scene.rpy','cs_th','Забавно.','cs_narrator','Семён посмотрел на часы.'),
 ('days/day03/part05/110_scene.rpy','cs_narrator','Посмотрела на часы.','cs_narrator','Дарья шла рядом.'),
 ('days/day03/part06/120_scene.rpy','cs_narrator','Я посмотрела на небо.','cs_narrator','Дарья посмотрела на меня.'),
 ('days/day03/part07/125a_scene.rpy','cs_th','Четыре девушки.','cs_narrator','Через некоторое время Тихонова сама нарушила молчание.'),
 ('days/day02/reading_interlude/59_05_scene.rpy','cs_narrator','И вернулась к чтению.',None,None)
]
active_beats={0,2,12}
updates={}
for number,(name,who,start,endwho,end) in enumerate(inward):
 p=R/name;s=updates.get(p,p.read_text(encoding='utf8'))
 marker='# cs_inward_beat_'+str(number)
 if number not in active_beats:
  s=re.sub(r'    '+re.escape(marker)+r':[^\n]*\n    \$ cs_pov_begin\(\)\n    with cs_sprite_leave\n','',s)
  if endwho:
   last='    '+endwho+' '+json.dumps(end,ensure_ascii=False)+'\n'
   s=s.replace('    # Return to the same conversation, with the same cast and placement.\n    $ cs_pov_end()\n    with cs_sprite_change\n'+last,last)
  updates[p]=s
  continue
 if marker in s:continue
 first='    '+who+' '+json.dumps(start,ensure_ascii=False)+'\n'
 assert first in s,(name,start)
 at=s.index(first)
 entry='    '+marker+': attention turns inward\n    $ cs_pov_begin()\n    with cs_sprite_leave\n'
 s=s[:at]+entry+s[at:]
 if endwho:
  last='    '+endwho+' '+json.dumps(end,ensure_ascii=False)+'\n'
  at=s.index(last,at+len(entry)+len(first))
  s=s[:at]+'    # Return to the same conversation, with the same cast and placement.\n    $ cs_pov_end()\n    with cs_sprite_change\n'+s[at:]
 updates[p]=s
for p,s in updates.items():p.write_text(s,encoding='utf8')
(R/'source/authored_pov_beats.json').write_text(json.dumps([x for i,x in enumerate(inward) if i in active_beats],ensure_ascii=False,indent=2),encoding='utf8')
# The next chapter starts while both are still reading. Its previous entry
# showed Darya for five lines before clearing her again, without looking up.
p=R/'days/day02/reading_interlude/59_06_scene.rpy'
s=p.read_text(encoding='utf8')
if '# cs_reading_entry_pov' not in s:
 first,rest=s.split('    cs_narrator "Прошло ещё немного времени."',1)
 first=first.replace('    show cs_darya neutral pioneer normal at cs_darya_normal_right\n','    # cs_reading_entry_pov: both continue reading independently.\n    $ cs_frame_focus([])\n')
 first=first.replace('$ cs_reading_cast = ["cs_darya"]','$ cs_reading_cast = []').replace('$ cs_frame_focus(["cs_darya"])','$ cs_frame_focus([])')
 s=first+'    cs_narrator "Прошло ещё немного времени."'+rest
 p.write_text(s,encoding='utf8')
print('Calmer direction: 5 observation cues, 3 extended inward/reading beats; short thoughts keep the cast.')

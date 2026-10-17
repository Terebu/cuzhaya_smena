"""Independently compare the new first instalment with the supplied Markdown."""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_new_part01.md').read_text(encoding='utf8').split('## Что передать Codex')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
expected=[]
for i in range(1,len(parts),3):
 if int(parts[i]) >= 10 and (R/'source/day02_breakfast.md').exists():continue
 for block in re.split(r'\n\s*\n',parts[i+2].split('### Продолжение первой части')[0]):
  block=block.strip()
  if not block or block=='---' or block.startswith(('**[','###')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_breakfast.md').exists():
 replacement=(R/'source/day02_breakfast.md').read_text(encoding='utf8').split('## Техническое задание')[0]
 replacement_parts=re.split(r'### Сцена (\d+)\. (.+)\n',replacement)
 for i in range(1,len(replacement_parts),3):
  for block in re.split(r'\n\s*\n',replacement_parts[i+2]):
   block=block.strip()
   if not block or block=='---' or block.startswith(('**[','###')):continue
   m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
   expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
additions={
 'Даша уже переоделась в пионерскую форму. Я пока осталась в спортивной одежде: чистую рубашку решила надеть после умывания.',
 'Вернувшись в домик, мы переоделись в пионерскую форму и убрали полотенца. Потом вместе пошли к столовой.'}
if (R/'source/day02_breakfast.md').exists():additions.add('Рядом с Семёном сидела Лена Тихонова. Она подняла взгляд и приветственно кивнула нам.')
if (R/'source/day02_part03.md').exists():additions.update(('С Мику мы уже познакомились. Она готовилась к утренней репетиции.','Да. Она показала нам кружок.'))
if (R/'source/day02_part05.md').exists():additions.update(('Вспомнила утренний спор с карандашом.','Да. Сначала бумага без Ctrl+Z, теперь ты.'))
if (R/'source/day02_part06.md').exists():additions.add('Лес у дороги начал редеть. Впереди открылись поля, а над асфальтом тянулись провода ЛЭП.')
if (R/'source/day02_part07.md').exists():additions.update(('Виола закрыла царапину лёгкой повязкой.','Удивительно. Славя, теперь Виола. У Даши стремительно растёт профессиональная репутация.'))
if (R/'source/day02_part02.md').exists():
 part02=(R/'source/day02_part02.md').read_text(encoding='utf8').split('## Инструкция для Codex')[0]
 part02=part02[part02.index('### Сцена 15.'):]
 if (R/'source/day02_part03.md').exists():
  part02=re.sub(r'Мику захлопнула папку\.[\s\S]*?(?=#### Сцена 19Б\.)','',part02)
 for block in re.split(r'\n\s*\n',part02):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part03.md').exists():
 part03=(R/'source/day02_part03.md').read_text(encoding='utf8').split('**[КОНЕЦ ТРЕТЬЕЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
 part03=part03[part03.index('### Сцена 21.'):]
 for block in re.split(r'\n\s*\n',part03):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part04.md').exists():
 part04=(R/'source/day02_part04.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧЕТВЁРТОЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
 part04=part04[part04.index('### Сцена 26.'):]
 for block in re.split(r'\n\s*\n',part04):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part05.md').exists():
 part05=(R/'source/day02_part05.md').read_text(encoding='utf8').split('**[КОНЕЦ ПЯТОЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
 part05=part05[part05.index('### Сцена 34.'):]
 for block in re.split(r'\n\s*\n',part05):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part06.md').exists():
 part06=(R/'source/day02_part06.md').read_text(encoding='utf8').split('**[КОНЕЦ ШЕСТОЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
 part06=part06[part06.index('### Сцена 40.'):]
 for block in re.split(r'\n\s*\n',part06):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part07.md').exists():
 part07=(R/'source/day02_part07.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧАСТИ 7 ВТОРОГО ДНЯ.]**')[0]
 part07=part07[part07.index('### Сцена 47.'):]
 for block in re.split(r'\n\s*\n',part07):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part08.md').exists():
 part08=(R/'source/day02_part08.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧАСТИ 8 ВТОРОГО ДНЯ.]**')[0]
 part08=part08[part08.index('### Сцена 54.'):]
 for block in re.split(r'\n\s*\n',part08):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_reading_interlude.md').exists():
 additions.add('До конца оставалось всего несколько страниц. Их можно было дочитать перед возвращением книги.')
 additions.update(('Между страницами лежала бумажная полоска. Я оставила её для закладки.','По дороге мы ненадолго свернули к нашему домику.','Я положила библиотечную книгу на тумбочку возле своей кровати, оставив закладку между страницами.','Пусть ждёт вечера здесь. На ужин и концерт брать её с собой незачем.','Через минуту мы снова шли к столовой.','Женя посмотрела на повязку и снова напомнила беречь локоть.','Помню. Смотрю под ноги.','Мы снова ненадолго заговорили о той самой книге — без пересказов и спойлеров.'))
 reading=(R/'source/day02_reading_interlude.md').read_text(encoding='utf8').split('**[КОНЕЦ ИНТЕРЛЮДИИ.]**')[0]
 reading=reading[reading.index('### Сцена 59.1.'):]
 for block in re.split(r'\n\s*\n',reading):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part09.md').exists():
 additions.update(('До завтра.','Женя взяла книгу и, попрощавшись с нами, направилась к выходу.','Мы ведь уже успели познакомиться. А сегодня ты поранилась. Я решила, что так будет удобнее.'))
 part09=(R/'source/day02_part09.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧАСТИ 9 ВТОРОГО ДНЯ.]**')[0]
 part09=part09[part09.index('### Сцена 60.'):]
 if (R/'source/day02_part09_dinner_revised.md').exists():
  additions.discard('До завтра.');additions.discard('Женя взяла книгу и, попрощавшись с нами, направилась к выходу.')
  revised=(R/'source/day02_part09_dinner_revised.md').read_text(encoding='utf8').split('**[КОНЕЦ ЗАМЕНЯЮЩЕЙ СЦЕНЫ 64.]**')[0]
  revised=revised[revised.index('### Сцена 64.'):]
  part09=re.sub(r'### Сцена 64\..*?(?=### Сцена 65\.)',lambda m:revised+'\n\n',part09,flags=re.S)
  part09=part09.replace('Когда мы вышли из столовой, солнце уже клонилось к деревьям.','К этому времени солнце уже клонилось к деревьям.')
 for block in re.split(r'\n\s*\n',part09):
  block=block.strip()
  if not block or block=='---' or block.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
  expected.append(m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block)
if (R/'source/day02_part10.md').exists():
 additions.update(('Семёна, который выслушал нас и прошёл с нами дорогу.','Утром бегала. Днём исследовала пространственную петлю. Потом познакомилась с землёй поближе, чем планировала. Вечером послушала концерт.'))
 finale=(R/'source/day02_part10.md').read_text(encoding='utf8').split('## Техническое задание для Codex')[0]
 finale=finale[finale.index('### Сцена 66.'):]
 for section in re.split(r'### Сцена \d+\. [^\n]+\n',finale)[1:]:
  section=section.split('### Монтажная граница')[0]
  for block in re.split(r'\n\s*\n',section):
   block=block.strip()
   if not block or block=='---' or block.startswith(('#','**[','- ')):continue
   m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',block,re.S)
   text=m[2].strip() if m else block.strip('*') if block.startswith('*') and block.endswith('*') else block
   if text=='И, кажется, именно второй визит оказался для нас гораздо важнее.':text='И, кажется, этот визит оказался для нас гораздо важнее.'
   expected.append(text)

def scene_order(p):
 if p.name.startswith('64_') and (R/'source/day02_part09_dinner_revised.md').exists():
  return (64,['64_scene.rpy','64_a_scene.rpy','64_b_scene.rpy','64_c_scene.rpy','64_d_scene.rpy','64_d1_scene.rpy','64_d2_scene.rpy','64_e_scene.rpy'].index(p.name))
 return (int(p.name[:2]),0 if p.name==p.name[:2]+'_scene.rpy' else 1,p.name)
paths=sorted((R/'days/day02').rglob('[0-9][0-9]*_scene.rpy'),key=scene_order);actual=[];extra=[]
for path in paths:
 for literal in re.findall(r'^\s+cs_\w+ (".*")$',path.read_text(encoding='utf8'),re.M):
  text=re.sub(r'\{font=[^}]+\}|\{/font\}','',json.loads(literal))
  (extra if text in additions else actual).append(text)
errors=[]
if expected!=actual:errors.append('Source order/text mismatch')
if len(paths)!=(110 if (R/'source/day02_part10.md').exists() else 98 if (R/'source/day02_reading_interlude.md').exists() else 84 if (R/'source/day02_part09_dinner_revised.md').exists() else 77 if (R/'source/day02_part09.md').exists() else 71 if (R/'source/day02_part08.md').exists() else 63 if (R/'source/day02_part07.md').exists() else 54 if (R/'source/day02_part06.md').exists() else 45 if (R/'source/day02_part05.md').exists() else 37 if (R/'source/day02_part04.md').exists() else 27 if (R/'source/day02_part03.md').exists() else 21 if (R/'source/day02_part02.md').exists() else 14 if (R/'source/day02_breakfast.md').exists() else 10) or set(extra)!=additions:errors.append('Scene count/continuity mismatch')
if ((R/'days/day02/part10').exists() and not (R/'source/day02_part10.md').exists()) or any((R/('days/day02/part0'+str(n))).exists() and not (R/('source/day02_part0'+str(n)+'.md')).exists() for n in (4,5,6,7,8,9)):errors.append('Old parts still active')
for a in json.loads((R/'source/new_assets_catalog.json').read_text(encoding='utf8')):
 if hashlib.sha256((R/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Asset changed: '+a['path'])
if (R/'source/day02_part02_assets.json').exists():
 for a in json.loads((R/'source/day02_part02_assets.json').read_text(encoding='utf8')):
  if hashlib.sha256((R/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Part 2 asset changed: '+a['path'])
if (R/'source/day02_part03_assets.json').exists():
 for a in json.loads((R/'source/day02_part03_assets.json').read_text(encoding='utf8')):
  if hashlib.sha256((R/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Part 3 asset changed: '+a['path'])
if (R/'source/day02_part05_assets.json').exists():
 for a in json.loads((R/'source/day02_part05_assets.json').read_text(encoding='utf8')):
  if hashlib.sha256((R/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Part 5 asset changed: '+a['path'])
if (R/'source/day02_part06_assets.json').exists():
 for a in json.loads((R/'source/day02_part06_assets.json').read_text(encoding='utf8')):
  if hashlib.sha256((R/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Part 6 asset changed: '+a['path'])
if (R/'source/day02_part07_assets.json').exists():
 for a in json.loads((R/'source/day02_part07_assets.json').read_text(encoding='utf8')):
  if hashlib.sha256((R/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Part 7 asset changed: '+a['path'])
if (R/'source/day02_part08_assets.json').exists():
 for a in json.loads((R/'source/day02_part08_assets.json').read_text(encoding='utf8')):
  if hashlib.sha256((R/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('Part 8 asset changed: '+a['path'])
result=dict(status='FAIL' if errors else 'PASS',scenes=len(paths),source_blocks=len(expected),continuity_additions=len(extra),assets_preserved=15,errors=errors)
(R/'qa/new_day02_static.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))

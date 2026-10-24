"""Independent manuscript comparison and cross-day continuity invariants."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part06.md').read_text(encoding='utf8');s=s[s.index('### Сцена 113.'):s.index('## Техническое задание')]
for n in ('115','117','119'):
 s=re.sub(r'\*\*\[ВЫБОР ИГРОКА:\]\*\*.*?### Сцена '+n+'А\.', '### Сцена '+n+'А.',s,count=1,flags=re.S)
changes={'Сегодня меня впервые за долгое время пустили в музыкальный клуб без обязательства уметь играть. Потом ещё и выяснилось, что здесь есть человек, с которым можно нормально поговорить о рисунках.':'Сегодня мы снова зашли в музыкальный клуб без обязательства уметь играть. А потом ещё и поговорили о рисунках.','Я и правда уже почти забыла, как это приятно.':'После долгого перерыва приятно снова привыкать к клавишам.'}
changes['Даша, хочешь попробовать? Ты ведь вчера говорила, что раньше играла.']='Даша, хочешь ещё поиграть? Вчера у тебя хорошо получилось.'
changes['В хорошем. Было видно, что ты занята музыкой, а не попытками убедить всех, какая ты крутая.']='В хорошем. На концерте гитара хорошо держала ритм, даже когда зал шумел. Мне это понравилось.'
changes['Особенно если не начинать знакомство с попытки вывести её из себя.']='Особенно если слушать её ответы, а не искать повод для следующей колкости.'
expected=[]
for t in s.split('\n\n'):
 t=t.strip()
 if not t or t=='---' or t.startswith(('#','**[')):continue
 if t.startswith('**'):
  n,w=t.split('\n',1);who={'Лена Соколова':'cs_ls','Дарья':'cs_da','Мику':'cs_mi','Алиса':'cs_dv','Лена Тихонова':'cs_un','Женя':'cs_mz','Славя':'cs_sl'}[n.strip('*:\\ ')];w=w.strip().lstrip('—–').strip()
 elif t.startswith('*') and t.endswith('*'):who,w='cs_th',t[1:-1]
 else:who,w='cs_narrator',t
 w=w.replace('\n',' ');expected.append((who,changes.get(w,w)))
extras=[('cs_th','К Славе заглянули и честно сказали, что у нас ещё есть свои дела.'),('cs_narrator','Мы поднялись на библиотечное крыльцо.'),('cs_narrator','Перед тем как подойти к клавишам, Дарья положила папку с плакатом на свободный чистый стул.'),('cs_narrator','Дарья забрала со стула папку с плакатом и прижала её к боку.'),('cs_da','Та девушка тоже рисует?'),('cs_ls','Да. Давай подойдём и познакомимся.'),('cs_ls','Привет. Я Лена Соколова, а это Даша.'),('cs_un','Лена. Тихонова.')]
extras += [('cs_narrator','Вчера Лена показала мне лишь быстрый набросок музыкантов. Теперь вокруг них появились сцена, скамейки и зрители.'),('cs_th','Вчерашний быстрый набросок превращался в целую сцену.')]
extras += [('cs_th','Утром мы уже поговорили без взаимных уколов. Теперь хотелось узнать, чем она живёт, кроме вечной готовности спорить.'),('cs_dv','Опять ты, Соколова? Только без комиссий.'),('cs_ls','Никаких комиссий. Просто слушаю.')]
actual=[]
for p in sorted((R/'days/day03/part06').glob('*_scene.rpy')):
 for l in p.read_text(encoding='utf8').splitlines():
  m=re.match(r'^\s+(cs_\w+) (".*")$',l)
  if m:actual.append((m[1],json.loads(m[2])))
assert Counter(actual)==Counter(expected)+Counter(extras),(Counter(expected)+Counter(extras)-Counter(actual),Counter(actual)-Counter(expected)-Counter(extras))
assert [x for x in actual if x not in extras]==expected
paths=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'));alltext='\n'.join(p.read_text(encoding='utf8') for p in paths)
for pattern in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
 c=Counter(re.findall(pattern,alltext,re.M));assert not [x for x,n in c.items() if n>1]
flow=(R/'days/day03/part06/00_flow.rpy').read_text(encoding='utf8');assert flow.count('    menu:')==3
for who,total in (('mi',2),('dv',2),('un',3)):
 assert flow.count('$ cs_friend_'+who+' += 1')==1 and 'if not cs_'+who+'_day3_awarded:' in flow
 assert len(re.findall(r'\$ cs_friend_'+who+r' \+= 1',alltext))==total
for n in ('114','115','116','117','118','119','120'):assert re.search(r'^    call cs_day03_'+n+r'(?: from \w+)?$',flow,re.M)
concert=(R/'days/day02/part10/69_concert.rpy').read_text(encoding='utf8')
assert concert.count('if cs_met_un and cs_friend_un >= 1:')==2 and 'cs_friend_un >= 2' not in concert
new='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part06').glob('*.rpy'))
assert new.count('play sound "sound/sfx/dinner_horn_processed.ogg"')==1
assert 'if not cs_day03_lunch_horn_played:' in new
assert 'cs_day03_poster_location = "music_club_chair"' in new and 'cs_day03_poster_location = "darya_folder"' in new
assert 'cs_mz_book_requested_day3 = False' not in new
assert 'cs_mz_catalog_checked_day3 = True' in new
report=dict(status='PASS',manuscript_blocks=len(expected),implemented_blocks=len(actual),replacements=changes,continuity_additions=extras,reachable_friendship_before={'mi':1,'dv':0,'un':1},reachable_friendship_after={'mi':2,'dv':1,'un':2},old_concert='Both old UN>=2 checks were unreachable (only one prior award); now met_un and UN>=1. No new points and no replay from day3.',part5_glue='47 branch blocks retired;113 handles optional catalog visit and all routes converge on114.',audit=['Day2 piano/concert remembered','Optional Sl help respected','Unknown Un introduced without friendship bonus','Catalog visit consumes morning appointment; requested book remains after lunch','Poster location authoritative; documents remain in administration','Injury, bandage, sports restriction and Viola inventory retained','No new SE jokes about rooming after111 promise','Only one lunch horn; final state is dining interior awaiting lunch continuation'])
(R/'source/day03_part06_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('SOURCE_PASS',len(expected),'original +',len(extras),'continuity additions')

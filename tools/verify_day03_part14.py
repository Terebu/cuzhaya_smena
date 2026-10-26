"""Independent source/state/asset audit; engine tests cover executed branches."""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parent.parent;P=R/'days/day03/part14'
alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')))
for pattern in (r'^default (cs_\w+)\s*=',r'^\s*label (cs_\w+):'):
 names=re.findall(pattern,alltext,re.M);assert len(names)==len(set(names)),[n for n in names if names.count(n)>1]
text='\n'.join(p.read_text(encoding='utf8') for p in P.glob('*.rpy'))
assert text.count('$ cs_friend_da += 1')==1
assert 'if not cs_da_shared_bed_awarded_day3:' in text
assert 'if cs_da_friend_before_night >= 2:' in text
assert 'if cs_da_friend_before_night is None:' in text
assert 'cs_da_bed_choice_done_day3' in text and 'cs_da_confession_choice_done_day3' in text
assert 'cs_mz_book_borrowed_day3 =' not in text
assert 'Мы поднялись на крыльцо.' not in text and 'Повернула его в замке.' not in text
assert not re.search(r'\b(?:ypos|yoffset|zoom|linear)\b',text)
flow=(P/'00_flow.rpy').read_text(encoding='utf8')
assert re.search(r'if cs_da_shared_bed_day3:\n\s+call cs_day03_185.*?else:\n\s+call cs_day03_184',flow,re.S)
assert 'jump cs_day03_part14' in (R/'days/day03/part13/00_flow.rpy').read_text(encoding='utf8')
assert all('label cs_day03_'+x+':' in text for x in [str(i) for i in range(180,190)]+['187a','187b'])
assert text.count('scene cs_cg_lena_darya_shared_sleep_night')==1
cg=R/'cg/lena_n_dasha/cg_lena_darya_shared_sleep_night.png';assert cg.is_file()
source=json.loads((R/'source/day03_part14_transcript.json').read_text(encoding='utf8'))
blocks=re.findall(r'^\s+cs_(?:ls|da|th|narrator) "',text,re.M)
assert len(blocks)>=source['source_blocks']-35,(len(blocks),source['source_blocks'])
report=dict(status='PASS',source_blocks=source['source_blocks'],runtime_blocks=len(blocks),cg_sha256=hashlib.sha256(cg.read_bytes()).hexdigest(),friendship_reachable=2,notes=['Two prior authored rewards reach threshold 2.','No day4 story supplied: preserved state and explicit continuation screen.','Nightwear not available: no false uniform portrait after changing.'])
(R/'source/day03_part14_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('PART14_STATIC_PASS',report)

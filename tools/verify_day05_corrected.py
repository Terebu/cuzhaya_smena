"""Verify complete corrected prose, speaker attribution and branch structure."""
from pathlib import Path
import ast
import hashlib
import json
import re
from day05_corrected_layer import apply_corrected

R=Path(__file__).resolve().parent.parent
P,B,M,A,skip,before,replacements,scenes,speakers,art,thoughts,dialogue,variants=apply_corrected(R,'cs_da_shared_bed_day3 and cs_da_love_confession_day3')
emitted=json.loads((R/'source/day05/emitted_paragraphs.json').read_text())
assert set(emitted)==art and len(emitted)==len(art)
assert len(scenes)==20 and len(M)==5 and len(dialogue)==1217
assert sum('cs_d5_choose(' in s for value in M.values() for option in value[1] for s in option[3])==10
actual=[]
runtime=[]
for file in sorted((R/'days/day05').glob('*_scene.rpy')):
    for line in file.read_text(encoding='utf-8').splitlines():
        match=re.match(r'^\s*(cs_\w+) (".*")$',line)
        if not match:continue
        text=ast.literal_eval(match[2])
        assert '\n' not in text and not text.startswith(('[','Сцена ','Вариант ','Выбор ','Приложение.'))
        runtime.append((match[1],text))
        if match[1] not in ('cs_narrator','cs_th'):actual.append((match[1],text))
expected=[('cs_d5_voice' if w=='voice' else 'cs_'+w,t) for i,(w,t) in sorted(dialogue.items())]
assert actual==expected, 'A spoken paragraph was lost, duplicated, reordered or attributed incorrectly'
source=Path('C:/Users/Admin/.codex/attachments/dac2e80c-fdfc-447a-ae0c-3c71bfed351f/Вставленный текст.txt')
assert source.read_bytes()==(R/'source/day05/corrected_source.txt').read_bytes()
assert B[2369][1][0][0]=='cs_d5_slavya_volunteer'
assert B[2395][1][0][0]=='cs_friend_dv >= 4'
assert B[2417][1][0][0]=='cs_friend_mi >= 4 and cs_d5_miku_volunteer'
assert A[445]==['cs_sl_day4_notice_offer = False','cs_d5_notice_completed = True']
assert A[1520]==['cs_mi_followup_invitation_day3 = False','cs_d5_miku_intro_heard = True']
earlier=Path('Q:/day05_literary_20261106/source_snapshot')
unchanged=[]
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
    rel=p.relative_to(R)
    if 'day05' not in rel.parts:
        assert p.read_bytes()==(earlier/rel).read_bytes(),str(rel)
        unchanged.append(str(rel))
result=dict(status='PASS',source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),scenes=20,menus=5,
            indexed_paragraphs=len(art),dialogue_paragraphs=len(dialogue),runtime_says=len(runtime),
            earlier_runtime_files_unchanged=len(unchanged),missing_or_duplicate_paragraphs=0,
            cast_conditions_independent=True,explicit_speakers=True)
(R/'source/day05/corrected_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('DAY05_CORRECTED_VERIFY_PASS',json.dumps(result))

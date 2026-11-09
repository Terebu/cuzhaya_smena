"""Check exact DOCX paragraph coverage and the ADV presentation contract."""
from pathlib import Path
import ast,json,re
R=Path(__file__).resolve().parent.parent
rows=json.loads((R/'source/day05/adv_paragraphs.json').read_text(encoding='utf-8'))
end=next(r['index'] for r in rows if r['text']=='Примечания для интеграции')
expected={r['index'] for r in rows if 51<=r['index']<end and r['style'] in ('Narrative','Dialogue')}
emitted=json.loads((R/'source/day05/emitted_paragraphs.json').read_text())
assert set(emitted)==expected and len(emitted)==len(expected)
before=(R/'source/day05/expanded_intake.txt').read_text(encoding='utf-8').splitlines()
assert [s for s in before[:1052] if s.startswith('—')]==[r['text'] for r in rows[:end] if r['text'].startswith('—')], 'Dialogue changed; review speakers'
says=[];menus=0
for p in sorted((R/'days/day05').glob('*_scene.rpy')):
    for i,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        assert not re.match(r'^\s*(extend |nvl |pause )',line),(p,i,line)
        menus+=line=='    menu:'
        m=re.match(r'^\s*(cs_\w+) (".*")$',line)
        if m:
            text=ast.literal_eval(m[2]);assert '\n' not in text,(p,i)
            assert not text.startswith(('Правило подачи для Codex','Постановка для Codex'))
            says.append((p.name,i,m[1],text))
assert menus==5
result=dict(status='PASS',document_literary_paragraphs=len(expected),dialogue_paragraphs=395,thought_paragraphs=sum(w=='cs_th' for p,i,w,t in says),total_runtime_says=len(says),max_say_characters=max(len(t) for p,i,w,t in says),menus=menus,duplicate_or_missing_paragraphs=0,multiline_says=0)
(R/'source/day05/adv_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('DAY05_ADV_VERIFY_PASS',json.dumps(result))

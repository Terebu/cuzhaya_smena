"""Verify the attributed manuscript, ADV boundaries and authored branches."""
from pathlib import Path
import ast,json,re
from day05_pov_layer import NAMES
R=Path(__file__).resolve().parent.parent
rows=json.loads((R/'source/day05/pov_paragraphs.json').read_text(encoding='utf-8'))
end=next(r['index'] for r in rows if r['text']=='Примечания для интеграции')
expected={r['index'] for r in rows if 52<=r['index']<end and r['style'] in ('Narrative','Dialogue')}
emitted=json.loads((R/'source/day05/emitted_paragraphs.json').read_text())
assert set(emitted)==expected and len(emitted)==len(expected)
speakers=json.loads((R/'source/day05/speakers.json').read_text())
dialogue=[r for r in rows[:end] if r['style']=='Dialogue']
assert len(speakers)==len(dialogue)
for r in dialogue:
    who=NAMES[r['text'].split(':',1)[0]] if r['index']!=94 else 'da'
    assert speakers[str(r['index'])]==who,(r,who)
says=[];menus=0;spoken=[]
for p in sorted((R/'days/day05').glob('*_scene.rpy')):
    for i,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        assert not re.match(r'^\s*(extend |nvl |pause )',line),(p,i,line)
        menus+=line=='    menu:'
        m=re.match(r'^\s*(cs_\w+) (".*")$',line)
        if not m:continue
        text=ast.literal_eval(m[2]);assert '\n' not in text,(p,i)
        assert not text.startswith(('Правило подачи для Codex','Постановка для Codex'))
        says.append((p.name,i,m[1],text))
        if m[1] not in ('cs_narrator','cs_th'):spoken.append((m[1],text))
expected_speech=[]
for r in dialogue:
    who=speakers[str(r['index'])]
    expected_speech.append(('cs_d5_voice' if who=='voice' else 'cs_'+who,r['text'].split(':',1)[1].strip()))
assert spoken==expected_speech,'Runtime speech does not match the explicit POV document'
assert menus==5
assert len(says)==len(expected)+5, 'Only the two costume bridge paragraphs and three optional helper actions are additional'
result=dict(status='PASS',document_literary_paragraphs=len(expected),dialogue_paragraphs=len(dialogue),background_dialogue=sum(r['text'].split(':',1)[0] in ('Пионер','Другой пионер','Повариха','Девочка','Ульяна') for r in dialogue),thought_paragraphs=sum(w=='cs_th' for p,i,w,t in says),total_runtime_says=len(says),max_say_characters=max(len(t) for p,i,w,t in says),menus=menus,duplicate_or_missing_paragraphs=0,multiline_says=0,editorial_speaker_corrections=[94])
(R/'source/day05/pov_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('DAY05_POV_VERIFY_PASS',json.dumps(result))

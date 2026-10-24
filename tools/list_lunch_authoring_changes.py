from pathlib import Path
from zipfile import ZipFile
import json
R=Path(__file__).resolve().parent.parent
backup=R.parents[2]/'mod_backups/day03_part07_revision_20261024/code_before.zip'
paths=list((R/'tools').rglob('*'))+list((R/'source').rglob('*'))
changes=[]
with ZipFile(backup) as z:
    names=set(z.namelist())
    for p in paths:
        if not p.is_file() or '__pycache__' in p.parts:continue
        rel=p.relative_to(R).as_posix()
        if rel not in names or z.read(rel)!=p.read_bytes():changes.append(rel)
changes=sorted(set(changes)|{'source/lunch_revision_authoring_changed_files.json'})
(R/'source/lunch_revision_authoring_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'DAY03_LUNCH_REVISION_REPORT.md'
text=p.read_text(encoding='utf8').split('\n## Файлы авторинга и проверок')[0]
text+='\n## Файлы авторинга и проверок\n\nСледующие рабочие файлы также изменены или созданы; они не включены в игровой пакет:\n\n'
text+=''.join('- `'+name+'`\n' for name in changes)
p.write_text(text,encoding='utf8')
print('Authoring change list:',len(changes))

"""Archive verified source identity, native tests and inspected contact sheets."""
from pathlib import Path
import hashlib,json,re,shutil,zipfile
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part11_20261025')
final=Path(str(stage)+'_final')
old=Path('D:/stean/release_chuzaya_smena/day03_part10_20261025_final')
engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
routes=read(stage/'full_render_walkthrough_results.json')
matrix=read(stage/'part11_native_results.json')
assert {r['case'] for r in matrix}==set(map(str,range(12)))|{'guard'}
assert len(routes)==2 and all(r['status']=='PASS' for r in routes+matrix)
assert read(stage/'part11_cross_save_result.json')['status']=='PASS'
assert {r['case'] for r in read(stage/'revision_native_results.json')}=={'camera'}
assert {r['case'] for r in read(stage/'part07_native_results.json')}=={'attention','camera'}
prefixes=('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_p11_',
          'p6_revision_camera_','p6_p7_attention_','p6_p7_camera_')
folders=[p.rstrip('_')+'_contacts' for p in prefixes]
ledger=read(stage/'reviewed_contact_pages.json');pages=[];frames=[]
for name in folders:
    folder=engine/name
    for item in read(folder/'index.json'):
        p=folder/item['sheet'];assert ledger.get(str(p))==sha(p),'Unreviewed contact page: '+str(p)
        pages.append(str(p));frames+=item['frames']
assert len(frames)==len(set(frames))
(stage/'visual_review.json').write_text(json.dumps(dict(all_contact_pages_reviewed=True,pages=len(pages),frames=len(frames),contact_pages=pages,scope='Both complete routes; twelve chapter11 combinations; guard/save/load; actual previous-version save; all-actor camera and attention. Contact sheets and selected full-size frames inspected.'),indent=2),encoding='utf8')
lint=(stage/'lint.log').read_text(encoding='utf-8-sig',errors='replace')
locations=re.findall(r'^([^\n]+?\.rpyc?:\d+)[ :]',lint,re.M)
assert not [x for x in locations if NAMESPACE in x or 'chuzaya_smena' in x]
(stage/'lint_diagnostics.json').write_text(json.dumps(dict(status='PASS',mod_diagnostic_locations=0,base_diagnostic_locations=len(locations)),indent=2),encoding='utf8')
identity=[];changes=[]
for p in sorted((final/'source_snapshot').rglob('*.rpy')):
    rel=p.relative_to(final/'source_snapshot');assert sha(p)==sha(R/rel)==sha(work/rel),str(rel)
    identity.append(dict(file=rel.as_posix(),sha256=sha(p)))
    previous=old/'source_snapshot'/rel
    if not previous.exists() or sha(previous)!=sha(p):changes.append(rel.as_posix())
assert len(identity)==380
assets=0
for rel,entry in read(final/'release_manifest.json')['files'].items():
    if rel.endswith('.rpyc'):continue
    assert sha(work.parent/rel)==entry['sha256'],rel
    assets+=1
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for p in list(stage.glob('*.json'))+list(stage.glob('*.log')):
    if p.name!='release_manifest.json':shutil.copy2(p,out/p.name)
for p in stage.glob('*fixture_diagnostic.txt'):
    (out/'diagnostics').mkdir(exist_ok=True)
    shutil.copy2(p,out/'diagnostics'/p.name)
for p in stage.glob('*_diagnostic.png'):
    (out/'diagnostics').mkdir(exist_ok=True)
    shutil.copy2(p,out/'diagnostics'/p.name)
images=out/'native_frames';images.mkdir(exist_ok=True)
for name in frames:shutil.copy2(engine/name,images/name)
for name in folders:
    folder=engine/name;dest=out/name;dest.mkdir(exist_ok=True)
    shutil.copy2(folder/'index.json',dest/'index.json')
    for item in read(folder/'index.json'):shutil.copy2(folder/item['sheet'],dest/item['sheet'])
(out/'tested_source_identity.json').write_text(json.dumps(dict(status='PASS',scripts=len(identity),assets=assets,frames=len(frames),sources=identity),indent=2),encoding='utf8')
(R/'source/day03_part11_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
backup=Path('D:/stean/steamapps/common/Everlasting Summer/mod_backups/day03_part11_20261025/code_before.zip')
author=[]
with zipfile.ZipFile(backup) as z:
    names=set(z.namelist())
    for base,pattern in ((R/'tools','*.py'),(R/'tools','*.txt'),(R/'source','*.md')):
        for p in sorted(base.glob(pattern)):
            rel=p.relative_to(R).as_posix()
            if rel not in names or hashlib.sha256(z.read(rel)).hexdigest()!=sha(p):author.append(rel)
routeframes=sum(r['screenshots']+1 for r in routes)
report=f'''# День 3. Часть 11 — «Библиотечный допуск»

Интегрированы сцены 154–162, включая 159А/159Б и 161А/161Б: 961 блок присланного текста, 970 реплик и описаний с редакторскими вариантами. Ужин продолжается непосредственно после части 10. Затем девушки помогают Жене либо идут гулять и возвращаются к домику на закате. Третий день ещё не завершён.

## Логика и редактура

- Дружба с Женей фиксируется при начале ужина. Её встречи, инициативы и доверие зависят от этого снимка; новое очко не открывает прежние бонусы задним числом. При 0 очков общение сдержанное, без персонального разговора. При 1–2 оно постепенно теплеет.
- Короткое объятие возможно только при прежней дружбе от 3 и уже полученном приглашении приходить без книги. Лена спрашивает разрешение и сразу отпускает Женю по её просьбе. Объятие не даёт очков и не повторяется при повторном входе.
- В одном меню помощь с возвращёнными книгами даёт +1 Жене один раз. Отказ сохраняет дружбу. Работа выполняется только в выбранной ветке; отдельный флаг завершения ставится после действительной помощи, а не при обещании. Повторный вызов обработчика и сцены работы не начисляет награду и не повторяет работу.
- Приглашения Мику и Алисы проверяются независимо. При открытой дружбе девушки договариваются о дне 4; оба прежних приглашения остаются активными. Новые музыкальные встречи не объявляются уже пройденными.
- Книга Гончарова, блокнот и сохранённый плакат остаются дома. Новая выдача или возврат романа не происходят. Повязка, запрет спорта, запасные материалы и состояние документов сохраняются. Новый сигнал горна не звучит.
- Убраны обещания слишком быстрого чтения, неточные сроки и воспоминания о событиях, которые могли не состояться. Благодарность за подбор книги зависит от действительного выбора в библиотеке. История про карандаш теперь явно рассказана Дашей Жене, поэтому библиотекарь не знает её необъяснимым образом. Семён вспоминается более открытым только после личного разговора. Шутки не предполагают право нарушать чужие границы.
- Место у окна упоминается как постоянное только при существующем флаге. Новая помощь не создаёт такое право автоматически. Дарья остаётся обычной девушкой из Москвы 2026 года, отношения не объявляются официальными.

## Персонажи и постановка

Сверены [официальные описания Soviet Games](https://soviet.games/everlasting-summer/) и реплики установленной оригинальной игры, собранные в `source/original_character_reference.json`. Сохранены прямота и сухой юмор Жени, музыкальная увлечённость Мику, резкость Алисы, самостоятельные ответы Семёна. Новые личные подробности не выдаются за канон.

Использована общая система всех персонажей: одиночный собеседник по центру, группа на раздельных позициях, плавный уход к фону при продолжительной рефлексии и возвращение к разговору. Короткие мысли не вызывают мерцание. Сидение не меняет высоту, масштаб или видимость спрайта. Последовательные внутренние планы сохраняют состав собеседников для возврата. Система повторно проверена на 13 наборах персонажей. Новые PNG не создавались; вечерняя библиотека — существующий интерьер с умеренным затемнением. Домик сохраняет стандартный масштаб.

## Фактически выполненные проверки

- Независимая сверка 961 исходного блока и условных вариантов, уникальности меток/defaults, снимка дружбы, условий согласия на объятие, единственной награды, независимых музыкальных приглашений и сохранности предметов.
- 12 нативных случаев Ren’Py: дружба с Женей 0–5 × помощь/отказ. Проверены старое приглашение и его отсутствие при пороговой дружбе, тихое место, самостоятельный выбор книги, музыкальные приглашения по отдельности и вместе. Сохранение/загрузка выполнены в каждом случае. Прямые реплики дополнительно проверяют наличие говорящего спрайта; одиночный кадр — центрирование.
- Отдельный тест сохраняет и загружает новое меню, повторяет обработчик выбора, дважды вызывает помощь и повторно входит в приветствие и завершённую часть. Начисление и работа однократны; нового объятия после очка нет.
- Реальное сохранение предыдущей сборки с её конечного модального экрана загружено и пройдено до нового конца. Библиотека, рисование и горн не повторяются; предметы, дружба и приглашения сохранены. Все исторические сохранения не перебирались.
- В тестовом сборщике обнаружено неверное ожидание аргумента диалога; оно исправлено по API установленного движка. Отдельное ожидание меню пропускало его ускоренным кликом: исправлен способ остановки теста. Повторные проверки пройдены; для этих исправлений runtime-код не менялся. Первичные диагностические журналы сохранены отдельно.
- На первичных снимках найден чёрный фон столовой: ошибочное имя `bg int_dining_hall_people_sunset` заменено зарегистрированным `bg int_dining_hall_sunset`. В нативную матрицу и полные проходы добавлена проверка регистрации показываемого фона. После исправления проверки и визуальный просмотр повторены.
- Два полных ускоренных прохода от пролога до конца части 11: положительные и нейтральные решения, **{routeframes} снимков**. Это не перебор всех сочетаний прежних выборов. В полных проходах переходы отключены; целевая матрица новой части проверяется с переходами.
- Повторены общая камера 13 наборов персонажей, группа, короткая мысль, продолжительная рефлексия с сохранением/загрузкой и возвратом внимания.
- Просмотрены **{len(pages)} контактных листов, {len(frames)} кадров**, а также выбранные полноразмерные снимки. Проверены составы групп, одиночный центр, библиотека вечером, возврат из рефлексии, переход старого сохранения и отсутствие портретов поверх CG. Хеши просмотренных страниц зафиксированы.
- Lint: **0 диагностических адресов мода**, {len(locations)} адресов исходной базовой игры. Чистый Lint всей установки не заявляется.
- Чистая компиляция **{len(identity)} runtime-скриптов**, локальный запуск и два запуска только с RPYC по Workshop-пути. Исходники и {assets} ресурсов совпадают по SHA-256 с тестовой копией. QA, рабочие исходники и снимки не включены в публикационный ZIP.

Проверки выполнялись в изолированной установке; пользовательские сохранения не менялись. Известных нерешённых ошибок проверенных маршрутов нет. Публикация не выполнялась. Следующая часть должна продолжить вечер третьего дня и сохранить обе договорённости на день 4.

## Файлы и воспроизведение

Архив: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Кадры, контактные листы и журналы: `{out.as_posix()}`.

Резервная копия: `{backup.as_posix()}`.

Генератор: `tools/build_day03_part11.py`; независимая проверка: `tools/verify_day03_part11.py`; полный цикл: `tools/run_day03_part11_final_checks.py`. Генераторы прежних частей вызывают новое продолжение и не восстанавливают заглушку.

Изменённые runtime-файлы относительно части 10 ({len(changes)}):

'''+''.join('- `'+p+'`\n' for p in changes)+'\nАвторские исходники и инструменты:\n\n'+''.join('- `'+p+'`\n' for p in sorted(set(author)))
(R/'DAY03_PART11_REPORT.md').write_text(report,encoding='utf8')
shutil.copy2(R/'DAY03_PART11_REPORT.md',out/'DAY03_PART11_REPORT.md')
print('PART11_REPORT_PASS',routeframes,'route frames;',len(frames),'archived frames;',len(changes),'changed runtime files')

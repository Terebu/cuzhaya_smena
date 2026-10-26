"""Archive verified source identity, native tests and inspected contact sheets."""
from pathlib import Path
import hashlib,json,re,shutil,zipfile
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part10_20261025')
final=Path(str(stage)+'_final')
old=Path('D:/stean/release_chuzaya_smena/day03_part08_09_20261025_final')
engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
routes=read(stage/'full_render_walkthrough_results.json')
matrix=read(stage/'part10_native_results.json')
assert {r['case'] for r in matrix}==set(map(str,range(8)))|{'guard'}
assert len(routes)==2 and all(r['status']=='PASS' for r in routes+matrix)
assert read(stage/'part10_cross_save_result.json')['status']=='PASS'
assert {r['case'] for r in read(stage/'revision_native_results.json')}=={'camera'}
assert {r['case'] for r in read(stage/'part07_native_results.json')}=={'attention','camera'}
prefixes=('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_p10_',
          'p6_revision_camera_','p6_p7_attention_','p6_p7_camera_')
folders=[p.rstrip('_')+'_contacts' for p in prefixes]
ledger=read(stage/'reviewed_contact_pages.json');pages=[];frames=[]
for name in folders:
    folder=engine/name
    for item in read(folder/'index.json'):
        p=folder/item['sheet'];assert ledger.get(str(p))==sha(p),'Unreviewed contact page: '+str(p)
        pages.append(str(p));frames+=item['frames']
assert len(frames)==len(set(frames))
(stage/'visual_review.json').write_text(json.dumps(dict(all_contact_pages_reviewed=True,pages=len(pages),frames=len(frames),contact_pages=pages,scope='Both complete routes; eight chapter10 combinations; guard/save/load; actual previous-version save; all-actor camera and attention. Contact sheets and selected full-size frames inspected.'),indent=2),encoding='utf8')
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
assert len(identity)==366
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
(R/'source/day03_part10_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
backup=Path('D:/stean/steamapps/common/Everlasting Summer/mod_backups/day03_part10_20261025/code_before.zip')
author=[]
with zipfile.ZipFile(backup) as z:
    names=set(z.namelist())
    for base,pattern in ((R/'tools','*.py'),(R/'tools','*.txt'),(R/'source','*.md')):
        for p in sorted(base.glob(pattern)):
            rel=p.relative_to(R).as_posix()
            if rel not in names or hashlib.sha256(z.read(rel)).hexdigest()!=sha(p):author.append(rel)
routeframes=sum(r['screenshots']+1 for r in routes)
report=f'''# День 3. Часть 10 — «Конкуренция с русской классикой»

Добавлены сцены 146–153, включая 148А/148Б: 935 блоков присланного сценария, 938 реплик/описаний с условными редакторскими вариантами. Возвращение после совместного или самостоятельного рисования ведёт к одному продолжению. Прежние художественные сцены не повторяются. Часть заканчивается у столовой вечером третьего дня; сам ужин ещё не написан.

## Что реализовано

- Лена продолжает читать уже выданную «Обыкновенную историю». После встречи с Тихоновой времени меньше; самостоятельная ветка позволяет читать дольше. День плавно переходит в вечер: дневной домик, тот же интерьер на закате, крыльцо, дорожка и столовая. Масштаб домика стандартный.
- Подходящего счётчика Даши в проекте не было: добавлен единственный `cs_friend_da`. В сцене 148 один выбор. Интерес к музыке даёт +1, тихое совместное время сохраняет счётчик. Исходы имеют отдельные флаги для будущего дня 4. Повторный вход в обработчик не показывает выбор снова и не начисляет второе очко.
- Поцелуй в щёку происходит в обеих ветках как небольшой знак привязанности. Он не включает обязательный романтический маршрут и не объявляет отношения официальными. Отсутствующий CG не создавался.
- Воспоминания о Жене зависят от дружбы при выдаче книги, а не от очка, заработанного позже. Для самостоятельного выбора нет ложной благодарности за персональную рекомендацию. Разговор о романе относится к посещению библиотеки сегодня, а не к утру.
- Воспоминания о Мику и Алисе проверяются независимо. Незавершённые приглашения сохранены; повторные музыкальные события не помечаются выполненными. При личном рисунке Тихоновой Лена не пересказывает его содержание. Семён вспоминается более открытым только после соответствующего разговора.
- Убраны неточности рукописи: Даша не знает, сколько времени девушки не замечали часов при рисовании, поскольку сама была в клубе; Лена не утверждает, что три дня назад уже началась лагерная история; после рисования нет обещания нескольких часов чтения. Исправлена фраза о половице.
- Книга и блокнот остаются на столе дома, папка с плакатом сохраняет прежнее место. Повязка, запрет спорта, материалы Виолы и документы не сбрасываются. Сигнал горна охраняется отдельным флагом и звучит один раз.

## Персонажи и постановка

Сверены [официальные описания Soviet Games](https://soviet.games/everlasting-summer/) и реплики оригинальной игры в `source/original_character_reference.json`: Мику увлекается музыкой, Алиса ценит содержательный разговор, Тихонова делится личным постепенно. Дарья остаётся обычной девушкой из 2026 года; её близость с Леной развивается через внимание, самостоятельные занятия и спокойное доверие.

Использована действующая общая система для всех персонажей: один собеседник центрируется; группа распределяется по свободным позициям; длительное чтение и рефлексия переводят фокус на фон. На коротких мыслях спрайт не мерцает. При возврате к диалогу Дарья возвращается в кадр, даже если по тексту сидит. Вертикальная позиция, масштаб, пропорции и непрозрачность не меняются. Новые соседние рефлексивные блоки не перезаписывают сохранённый состав пустым кадром. Общая runtime-система постановки не переписывалась; её повторно проверили на всех 13 наборах персонажей.

## Реально выполненные проверки

- Независимая сверка всех 935 исходных блоков; уникальность меток/defaults, одна защищённая награда Даши, один защищённый горн, отсутствие новых начислений остальным персонажам и сброса приглашений.
- 8 нативных комбинаций: обе ветви Даши × совместное/самостоятельное рисование × низкие/высокие дружеские последствия. MZ на момент выдачи 0/1/2/3, личный рисунок, музыка, предметы и сохранение/загрузка после новой сцены проверены. Все прямые реплики Даши дополнительно проверяют наличие её спрайта; снимки проверяют центр, непрозрачность и отсутствие портретов поверх CG.
- Отдельный тест сохраняет и загружает новое меню, повторно вызывает обработчик выбора, дважды проходит сцену с горном и повторно входит в уже завершённую часть. Счётчик растёт один раз; горн звучит один раз.
- Реальное сохранение предыдущей сборки с её модального экрана части 9 загружено в новую. Переход до конца части 10 прошёл без повторения библиотеки или рисования. Дружба, роман, плакат, повязка, материалы, документы и приглашения сохранены. Это проверка известной предыдущей сборки, а не всех исторических промежуточных сохранений.
- Первый тест переноса пропустил конечную метку уже завершившегося ускоренного маршрута и ожидал её повторно. Ожидание заменено проверкой существующего конечного экрана; повторный запуск прошёл. Для исправления этого тестового ожидания runtime-код не менялся.
- При просмотре промежуточных кадров переноса выяснилось, что ускорение было включено ещё внутри перехода загрузки: renderer захватывал прежний экран меню, хотя сцена и состояние уже обновлялись. Для окончательной визуальной проверки сначала дождались обычной интерактивной реплики после загрузки, затем включили ускорение. Исправленный тест снова пройден, новые кадры просмотрены; диагностический снимок прежнего теста хранится отдельно.
- Два полных ускоренных прохода от пролога до нового конца части 10: положительные и нейтральные решения; **{routeframes} снимков**. Это не перебор всех комбинаций прежних выборов. Полные проходы отключают переходы, целевые тесты новой части выполняются с ними.
- Отдельно повторены общая камера 13 наборов, группа, короткая мысль, длительная рефлексия с загрузкой и возвратом внимания; ушедший персонаж не возвращается.
- Просмотрены **{len(pages)} контактных листов**, охватывающих **{len(frames)} кадров**, и выбранные полноразмерные кадры. На проверенных снимках не найдено наложений, вертикального скачка, обрезанной головы или зависшей полупрозрачности. Хеши просмотренных страниц сохранены.
- Lint: **0 диагностических адресов мода**; {len(locations)} адресов относятся к исходной базовой игре. Полностью чистый Lint всей установки не заявляется.
- Чистая компиляция {len(identity)} runtime-скриптов, локальный запуск и два запуска только с RPYC по Workshop-пути. Исходники и {assets} ресурсов совпадают по SHA-256 с тестовой копией. QA и рабочие файлы в публикационный архив не включены.

Пользовательские сохранения не менялись: проверки выполнялись в изолированной установке. Известных нерешённых ошибок проверенных маршрутов нет. Публикация не выполнялась; вечер третьего дня остаётся открытым для следующей части.

## Файлы и воспроизведение

Архив: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Кадры, контактные листы, результаты и журналы: `{out.as_posix()}`.

Резервная копия: `{backup.as_posix()}`.

Генератор: `tools/build_day03_part10.py`; независимая проверка: `tools/verify_day03_part10.py`; полный цикл: `tools/run_day03_part10_final_checks.py`. Генератор предыдущих частей вызывает новое продолжение и не восстанавливает устаревшую заглушку.

Runtime-файлы относительно предыдущей проверенной сборки ({len(changes)}):

'''+''.join('- `'+p+'`\n' for p in changes)+'\nАвторские исходники и инструменты:\n\n'+''.join('- `'+p+'`\n' for p in sorted(set(author)))
(R/'DAY03_PART10_REPORT.md').write_text(report,encoding='utf8')
shutil.copy2(R/'DAY03_PART10_REPORT.md',out/'DAY03_PART10_REPORT.md')
print('PART10_REPORT_PASS',routeframes,'route frames;',len(frames),'archived frames;',len(changes),'changed runtime files')

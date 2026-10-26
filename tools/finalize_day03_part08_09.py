"""Verify and archive completed native checks and manually inspected screenshots."""
from pathlib import Path
import hashlib,json,re,shutil,zipfile
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part08_09_20261025')
final=Path(str(stage)+'_final')
old=Path('D:/stean/release_chuzaya_smena/day03_part07_revision_20261024_final')
engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
routes=read(stage/'full_render_walkthrough_results.json')
matrix=read(stage/'late_native_results.json')
assert {r['case'] for r in matrix}==set(map(str,range(9)))|{'guard'}
assert len(routes)==2 and all(r['status']=='PASS' for r in routes+matrix)
assert read(stage/'late_cross_save_result.json')['status']=='PASS'
assert {r['case'] for r in read(stage/'revision_native_results.json')}=={'camera'}
assert {r['case'] for r in read(stage/'part07_native_results.json')}=={'attention','camera'}
prefixes=('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_late_',
          'p6_revision_camera_','p6_p7_attention_','p6_p7_camera_')
folders=[p.rstrip('_')+'_contacts' for p in prefixes]
ledger=read(stage/'reviewed_contact_pages.json');pages=[];frames=[]
for name in folders:
    folder=engine/name
    for item in read(folder/'index.json'):
        p=folder/item['sheet']
        assert ledger.get(str(p))==sha(p),'Unreviewed or changed contact page: '+str(p)
        pages.append(str(p));frames+=item['frames']
assert len(frames)==len(set(frames))
(stage/'visual_review.json').write_text(json.dumps(dict(all_contact_pages_reviewed=True,pages=len(pages),frames=len(frames),contact_pages=pages,scope='Both complete routes, nine late-day branches, repeat/save guard, old-save migration, all-actor camera and attention tests; inspected contact sheets and selected full-size frames.'),indent=2),encoding='utf8')
lint=(stage/'lint.log').read_text(encoding='utf-8-sig',errors='replace')
locations=re.findall(r'^([^\n]+?\.rpyc?:\d+)[ :]',lint,re.M)
assert not [x for x in locations if NAMESPACE in x or 'chuzaya_smena' in x]
(stage/'lint_diagnostics.json').write_text(json.dumps(dict(status='PASS',mod_diagnostic_locations=0,base_diagnostic_locations=len(locations)),indent=2),encoding='utf8')
identity=[];changes=[]
for p in sorted((final/'source_snapshot').rglob('*.rpy')):
    rel=p.relative_to(final/'source_snapshot')
    assert sha(p)==sha(R/rel)==sha(work/rel),str(rel)
    identity.append(dict(file=rel.as_posix(),sha256=sha(p)))
    previous=old/'source_snapshot'/rel
    if not previous.exists() or sha(previous)!=sha(p):changes.append(rel.as_posix())
assert len(identity)==354
assets=0
for rel,entry in read(final/'release_manifest.json')['files'].items():
    if rel.endswith('.rpyc'):continue
    assert sha(work.parent/rel)==entry['sha256'],rel
    assets+=1
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for p in list(stage.glob('*.json'))+list(stage.glob('*.log')):
    if p.name!='release_manifest.json':shutil.copy2(p,out/p.name)
images=out/'native_frames';images.mkdir(exist_ok=True)
for name in frames:shutil.copy2(engine/name,images/name)
for name in folders:
    folder=engine/name;dest=out/name;dest.mkdir(exist_ok=True)
    shutil.copy2(folder/'index.json',dest/'index.json')
    for item in read(folder/'index.json'):shutil.copy2(folder/item['sheet'],dest/item['sheet'])
diag=out/'diagnostics';diag.mkdir(exist_ok=True)
for p in stage.glob('*fixture_diagnostic.txt'):shutil.copy2(p,diag/p.name)
if (stage/'guard_fixture_diagnostic.txt').exists():shutil.copy2(stage/'guard_fixture_diagnostic.txt',diag/'guard_fixture_diagnostic.txt')
for name in ('late_cross_progress.txt','late_cross_diagnostic.png'):
    if (engine/name).exists():shutil.copy2(engine/name,diag/name)
(out/'tested_source_identity.json').write_text(json.dumps(dict(status='PASS',scripts=len(identity),assets=assets,frames=len(frames),sources=identity),indent=2),encoding='utf8')
(R/'source/day03_part08_09_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
backup=Path('D:/stean/steamapps/common/Everlasting Summer/mod_backups/day03_part08_09_20261025/code_before.zip')
author_changes=[]
with zipfile.ZipFile(backup) as z:
    names=set(z.namelist())
    for base,pattern in ((R/'tools','*.py'),(R/'tools','*.txt'),(R/'source','*.md')):
        for p in sorted(base.glob(pattern)):
            rel=p.relative_to(R).as_posix()
            if rel not in names or hashlib.sha256(z.read(rel)).hexdigest()!=sha(p):author_changes.append(rel)
routeframes=sum(r['screenshots']+1 for r in routes)
report=f'''# День 3. Части 8–9 — библиотека, Семён и рисование

Интегрированы «Читательский билет в новую жизнь» и «Сёмочка и другие последствия социализации»: 22 файла сцен, сцены 128–145 с условными ответвлениями. Новая часть 9 заменяет короткую встречу 137–138 из части 8, поэтому повторного знакомства на площади нет. После сцены 127 Лена идёт в библиотеку одна; Дарья возвращается после музыкального клуба.

## Сюжет, предметы и дружба

- MZ 0/1/2/3 определяет самостоятельный выбор, помощь, подготовленный роман и постоянное место. Пороги фиксируются при входе. Новое очко за разговор не открывает прежние привилегии задним числом. Один роман — «Обыкновенная история» Гончарова; фактическая выдача происходит один раз в сцене 135. Книга затем лежит на столе в домике; заём остаётся действующим. Старая книга второго дня не подменяется.
- Один выбор с Женей и один с Семёном дают по одному защищённому очку. Отказ от разговора не штрафует. Личная открытость Семёна и подсказка места для рисования зависят от дружбы до нового выбора. Романтического маршрута с ним не добавлено; Лена останавливает неприятную ему шутку.
- При назначенной встрече происходит совместное рисование с Тихоновой. При высокой дружбе она сама показывает личный рисунок. Без договорённости Лена рисует самостоятельно. Новые очки UN за эти сцены не начисляются.
- Приглашения Мику и Алисы проверяются независимо и остаются активными для следующих частей. Повторное музыкальное событие ещё не считается состоявшимся. Славя благодарит за инвентарь только при фактической помощи.
- Повязка, запрет спорта, запасные материалы, документы сохранены. Папка с плакатом перемещается из рук Дарьи на стол дома только при наличии папки. Дублирования держателей нет. Дарья остаётся обычной девушкой из 2026 года.
- Для сохранения прежней проверенной сборки с Паустовским предусмотрен явный переход: сборник остаётся в библиотеке, Женя предлагает роман. Обед не повторяется. Сохранены 309 постоянных возвратов вызовов и таблица 1119 известных старых адресов.

## Редактура и изображение

Сверены [официальные описания Soviet Games](https://soviet.games/everlasting-summer/) и реплики установленной оригинальной игры (`source/original_character_reference.json`). Женя сохраняет прямоту и сухой юмор, Тихонова проявляет инициативу постепенно, Семён может ответить на подколы сам. Исправлены ложные воспоминания о вчерашнем разговоре, благодарность за выбор книги в ветке самостоятельного выбора, помощь Виоле при отказе от неё и знание Тихоновой о ещё не сообщённом месте встречи. Роман проверен по [Culture.ru](https://www.culture.ru/books/301/obyknovennaya-istoriya) и [тексту Гончарова](https://rvb.ru/19vek/goncharov/pssp/vol1/text/oi.html).

Общая система постановки уже применяется ко всем 13 наборам персонажей: одиночный собеседник центрируется; группа распределяется по свободным местам. Длительная рефлексия и чтение переводят внимание на фон. Короткие мысли, смена говорящего, сидение и лежание не вызывают автоматических скрытий или смещения вниз. Масштаб, вертикальная позиция и пропорции сохранены; портретов поверх полноэкранных CG нет. В новых сценах используются те же общие функции, существующие эмоции, фоны и музыка. Новых изображений в задании не было, файлы ресурсов не переименовывались.

## Фактически выполненные проверки

- Независимая сверка: 1702 блока присланного сценария, 1717 runtime-блоков с редакторскими условными вариантами. Уникальность меток/defaults, защищённые начисления, выдача книги, независимость музыкальных приглашений и исключение двух одновременных веток рисования.
- 9 нативных комбинаций: MZ 0/1/2/3, обе ветви книжного разговора, SE 0/1/2/3, обе ветви общения с ним, тихое место есть/нет, рисование вместе/в одиночку, UN 2/3, приглашения MI/DV отдельно/вместе. Проверены пороги до нового очка, отсутствие двойной выдачи, сохранность предметов.
- Отдельный нативный тест повторных меню и выдачи книги: MZ/SE растут один раз. Сохранение и загрузка на выборе проходят.
- Реальное сохранение предыдущей сборки с её старого модального экрана загружено в новую. Полный переход к концу части 9 прошёл с ожидаемыми дружбой, романом, плакатом и рисованием, без повтора обеда.
- Два полных ускоренных прохода от пролога до нового конца части 9 — положительные и нейтральные решения: **{routeframes} снимков**. Это не перебор всех сочетаний прежних выборов. Полные проходы отключают переходы; целевые проверки новых сцен выполняются с переходами.
- Камера всех 13 наборов персонажей, группа, краткая мысль, длительная рефлексия, сохранение/возврат внимания и отсутствие возврата ушедшего персонажа проверены отдельно.
- Просмотрены **{len(pages)} контактных листов**, охватывающих **{len(frames)} нативных кадров**, и выбранные полноразмерные кадры. Наложений, зависших полупрозрачных спрайтов и прежнего вертикального скачка на проверенных кадрах не обнаружено. Хеши просмотренных страниц сохранены.
- Lint: **0 диагностических адресов мода**; {len(locations)} относятся к исходной базовой игре (её CG/старые экраны/переводы). Полностью чистый Lint всей установки не заявляется.
- Чистая компиляция {len(identity)} runtime-скриптов, локальный запуск, два запуска только с RPYC по Workshop-пути. Все исходники и {assets} ресурсов совпадают с проверенной копией по SHA-256. Рабочие файлы и QA-сценарии в публикационный архив не включены.

Два сбоя относились к тестовым ожиданиям: повторное меню требовало явного шага между проверками; при переносе сохранения ускоренный маршрут уже достиг финального экрана до ожидания его метки. Тесты исправлены и повторно пройдены. Диагностика сохранена отдельно; для этих исправлений runtime-код не менялся.

Пользовательские сохранения не трогались: использована изолированная установка. Третий день остаётся открытым для продолжения вечера. Публикация не выполнялась. Известных нерешённых ошибок в проверенных маршрутах нет; непроверенные комбинации и произвольные исторические промежуточные сохранения не объявляются покрытыми.

## Артефакты и изменённые файлы

Архив: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Снимки, листы и журналы: `{out.as_posix()}`.

Резервная копия: `{backup.as_posix()}`.

Генерация: `tools/build_day03_part08_09.py`; проверка: `tools/verify_day03_part08_09.py`; полный цикл: `tools/run_day03_late_final_checks.py`. Старый генератор части 7 вызывает новый и не восстанавливает прежнюю временную библиотечную сцену.

Runtime-файлы относительно предыдущей проверенной сборки ({len(changes)}):

'''+''.join('- `'+p+'`\n' for p in changes)+'\nАвторские исходники и инструменты:\n\n'+''.join('- `'+p+'`\n' for p in sorted(set(author_changes)))
(R/'DAY03_PART08_09_REPORT.md').write_text(report,encoding='utf8')
shutil.copy2(R/'DAY03_PART08_09_REPORT.md',out/'DAY03_PART08_09_REPORT.md')
print('DAY03_LATE_REPORT_PASS',routeframes,'route frames;',len(frames),'archived frames;',len(changes),'changed runtime files')

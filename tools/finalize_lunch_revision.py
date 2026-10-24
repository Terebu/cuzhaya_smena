"""Archive evidence after the native pipeline and visual review are complete."""
from pathlib import Path
import hashlib,json,re,shutil
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part07_revision_20261024')
final=Path(str(stage)+'_final')
old=Path('D:/stean/release_chuzaya_smena/day03_medpoint_revision_20261024_final')
engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
routes=read(stage/'full_render_walkthrough_results.json')
matrix=read(stage/'lunch_revision_results.json')
assert {r['case'] for r in matrix}==set(map(str,range(8)))|{'guard'}
assert len(routes)==2 and all(r['status']=='PASS' for r in routes+matrix)
assert read(stage/'lunch_cross_save_result.json')['status']=='PASS'
assert {r['case'] for r in read(stage/'revision_native_results.json')}=={'camera'}
assert {r['case'] for r in read(stage/'part07_native_results.json')}=={'attention','camera'}
assert any(r['test']=='cs_day03_p6_costume' and r['status']=='PASS' for r in read(stage/'part06_native_results.json'))
assert read(stage/'visual_review.json')['all_contact_pages_reviewed'] is True
lint=(stage/'lint.log').read_text(encoding='utf-8-sig',errors='replace')
locations=re.findall(r'^([^\n]+?\.rpyc?:\d+)[ :]',lint,re.M)
mod=[x for x in locations if NAMESPACE in x or 'chuzaya_smena' in x]
assert not mod,mod
lintresult=dict(status='PASS',mod_diagnostic_locations=mod,base_diagnostic_locations=len(locations))
(stage/'lint_diagnostics.json').write_text(json.dumps(lintresult,indent=2),encoding='utf8')
identity=[];changes=[]
for p in sorted((final/'source_snapshot').rglob('*.rpy')):
    rel=p.relative_to(final/'source_snapshot')
    assert sha(p)==sha(R/rel)==sha(work/rel),str(rel)
    identity.append(dict(file=rel.as_posix(),sha256=sha(p)))
    previous=old/'source_snapshot'/rel
    if not previous.exists() or sha(previous)!=sha(p):changes.append(rel.as_posix())
assets=0
for rel,entry in read(final/'release_manifest.json')['files'].items():
    if rel.endswith('.rpyc'):continue
    assert sha(work.parent/rel)==entry['sha256'],rel
    assets+=1
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for p in list(stage.glob('*.json'))+list(stage.glob('*.log')):
    if p.name!='release_manifest.json':shutil.copy2(p,out/p.name)
images=out/'native_frames';images.mkdir(exist_ok=True);frames=[]
prefixes=('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_lunch_revision_',
          'p6_revision_camera_','p6_p7_attention_','p6_p7_camera_','p6_costume_','p6_lunch_cross_save_')
for prefix in prefixes:
    for p in sorted(engine.glob(prefix+'*.png')):
        shutil.copy2(p,images/p.name);frames.append(p.name)
contact_names={p.rstrip('_')+'_contacts' for p in prefixes}
for folder in engine.glob('*_contacts'):
    if not (folder/'index.json').exists():continue
    if folder.name not in contact_names:continue
    dest=out/folder.name;dest.mkdir(exist_ok=True)
    shutil.copy2(folder/'index.json',dest/'index.json')
    for page in read(folder/'index.json'):shutil.copy2(folder/page['sheet'],dest/page['sheet'])
diagnostic=stage/'lunch_cross_fixture_early_save_diagnostic.txt'
if diagnostic.exists():
    (out/'diagnostics').mkdir(exist_ok=True)
    shutil.copy2(diagnostic,out/'diagnostics'/diagnostic.name)
(out/'tested_source_identity.json').write_text(json.dumps(dict(status='PASS',scripts=len(identity),assets=assets,frames=len(frames),sources=identity),indent=2),encoding='utf8')
(R/'source/lunch_revision_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
routeframes=sum(r['screenshots']+1 for r in routes)
report=f'''# День 3. Часть 7 — «Тишина тоже сближает»

Новая обеденная сцена заменяет прежнюю часть 7. Интегрированы 770 блоков присланного сценария в отдельных файлах сцен 121–127, включая 125А/125Б. Сцена 128 — короткий переход к библиотеке с реальным выбором книги; дальнейшее чтение и третий день остаются открытыми.

## Сюжет и последствия

- Дарью у входа на минуту задерживает Ольга Дмитриевна. Она возвращается к столу позже Лены; отдельного повторного разговора с вожатой нет. Уходят последовательно Тихонова, Женя, затем Дарья к Мику. Лена идёт в библиотеку одна.
- MZ=0: обычные правила библиотеки; MZ=1: помощь знакомой посетительнице; MZ≥2: Женя заранее выбирает книгу и объясняет свой выбор; MZ≥3: сама предлагает дальний стол. Это не дополнительные начисления дружбы. Порог 3 достижим: помощь с книгами в день 1, благодарность на площади в день 2, просьба о рекомендации утром дня 3 — по одному очку, с существующими защитами.
- В библиотеке выбран сборник Паустовского с рассказом «Тёплый хлеб». Книга остаётся на читальном столе, не выдаётся на руки и не подменяет данные о вчерашней книге. Повторный вход не выдаёт второй экземпляр. Для высокого доверия не повторяется вопрос о предпочтениях. Дальний стол используется без нового запроса разрешения.
- Единственное приглашение Тихоновой на обед сохраняет однократный +1. При прежнем приглашении к рисованию героини договариваются на время ближе к вечеру; установлен `cs_un_sketch_time_agreed_day3`. При достаточной дружбе без прежнего приглашения Тихонова сама предлагает рисовать вместе. Рисование ещё не считается состоявшимся.
- Две независимые проверки открывают приглашения Мику и Алисы: одновременно достижимы оба флага. Приглашения сохранены для следующих частей, сами повторные музыкальные встречи пока не происходили.
- Сохранены результаты прежних дней: повязка, запрет спорта, запасные материалы Виолы, документы, проверенные утром каталоги, дружба и папка с плакатом. Папка временно лежит на стуле, затем Дарья забирает её с собой.

## Редактура и постановка

Сверены [описания персонажей разработчика Soviet Games](https://soviet.games/everlasting-summer/) и выписки из первых двух дней установленной оригинальной игры (`source/original_character_reference.json`). Женя говорит прямо и без романтического подтекста; при нулевой дружбе её реакция сдержаннее. Тихонова не навязывает совместное занятие. Дарья остаётся обычным человеком из 2026 года, со своими делами; отношения с Леной не объявлены официальными.

Устранены ложные воспоминания: предпочтения обсуждались утром третьего дня, а не вчера; упоминание возвращённой книги проверяет реальный флаг; художественный совет не приписывается ветке, где его не было. Рукописное `elif` между приглашениями Мику и Алисы заменено двумя `if`, как требует техническая сноска.

Общая режиссёрская система уже действует для всех персонажей: единственный собеседник центрируется, группа распределяется по свободным местам. Вертикальная позиция, масштаб и пропорции сохраняются. Длинные размышления используют общий рефлексивный кадр; короткая мысль и смена говорящего не вызывают скрытия. Сидение и еда не опускают и не скрывают персонажей. Реальный уход убирает персонажа из состава; портреты не выводятся поверх полноэкранных CG. Новая часть использует те же функции, без отдельной логики только для Даши.

Замена эмоции через тот же тег и переходы сверены с [документацией Ren’Py](https://www.renpy.org/doc/html/displaying_images.html#hide-statement). Скрытие на длительном внутреннем размышлении — авторская постановка, а не автоматическое правило движка.

## Реально выполненные проверки

- Независимая проверка сценария: 770 блоков исходника, 810 реплик/описаний с условными редакторскими вариантами и библиотечным переходом; уникальные метки/defaults; одно меню и одно защищённое начисление UN; отсутствие пассивных начислений MZ/MI/DV.
- 8 нативных маршрутов обеда: MZ 0/1/2/3, обе ветки обеда, прежнее/новое приглашение к рисованию, разговор/отказ утром, оба музыкальных условия по отдельности и вместе. Отдельный тест повторяет меню и библиотечный вход, проверяя отсутствие повторного очка и повторной книги. Сохранение/загрузка проверены на меню и после сцены.
- Общая камера повторно проверена для 13 наборов спрайтов: центр одиночного персонажа, неизменность вертикальной позиции/размера, рефлексия и возврат. Дополнительно проверены группа слушателей, короткая мысль, длительная рефлексия с загрузкой сохранения и отсутствие возврата ушедшего персонажа. Отдельно повторена сцена переодевания Даши утром третьего дня.
- Два полных ускоренных прохода от пролога до текущего конца мода: положительные и нейтральные решения, реальные строки и меню. **{routeframes} снимков полного прохода**, контактные листы и ключевые кадры просмотрены. Целевые тесты идут с включёнными переходами; полные проходы — с отключёнными переходами. Это не перебор всех комбинаций всех прежних выборов.
- Реальное сохранение прежней сборки на обеденном меню загружено в новую: выбор завершается, новые флаги появляются, дружба, повязка, материалы, документы и плакат сохранены. Старые именованные возвраты остаются действительными; таблица известных адресов дополнена предыдущей сборкой. Проверка касается известной сборки, а не любого исторического промежуточного сохранения.
- Первый запуск теста переноса сохранил игру на начальном переходе вместо меню. Тестовый сценарий исправлен: он явно ждёт метку меню и проверяет её достижение перед сохранением. Повторный запуск прошёл. Диагностический журнал этого сбоя тестового сценария сохранён отдельно в `qa_evidence/diagnostics/`; изменения runtime-кода для его исправления не потребовались.
- Lint: **0 диагностик мода**; {len(locations)} диагностических адресов относятся к исходной базовой игре (её отсутствующие CG/старые экраны/переводы). Полностью чистый Lint всей установки не заявляется.
- Чистая компиляция {len(identity)} скриптов; проверка внутренних идентификаторов; локальный запуск и два запуска только с RPYC по Workshop-пути пройдены. {assets} ресурсов и все исходники совпадают по SHA-256 с тестовой копией. Всего сохранено {len(frames)} нативных кадров. Рабочие файлы и тестовые сценарии в пакет не включены.

Пользовательские сохранения не изменялись: тесты работают в изолированной установке. Публикация не выполнялась.

## Файлы и воспроизведение

Архив: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Снимки, контактные листы, результаты и журналы: `{out.as_posix()}`.

Резервная копия до изменений: `D:/stean/steamapps/common/Everlasting Summer/mod_backups/day03_part07_revision_20261024/code_before.zip`.

Генератор: `tools/build_day03_part07.py` → `build_day03_part07_revision.py`. Проверка: `verify_day03_part07.py` → `verify_lunch_revision.py`. Нативная матрица: `build_lunch_revision_qa.py`, `run_lunch_revision_qa.py`. Полный проверочный цикл: `run_lunch_final_checks.py`. Генераторы сохраняют модульную структуру и постоянные возвраты вызовов.

Изменённые runtime-файлы относительно предыдущей проверенной сборки ({len(changes)}):

'''+''.join('- `'+p+'`\n' for p in changes)
(R/'DAY03_LUNCH_REVISION_REPORT.md').write_text(report,encoding='utf8')
print('LUNCH_REVISION_REPORT_PASS',routeframes,'route frames;',len(frames),'archived frames;',len(changes),'changed runtime files')

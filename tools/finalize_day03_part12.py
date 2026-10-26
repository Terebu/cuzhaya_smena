"""Archive verified source identity, native tests and inspected contact sheets."""
from pathlib import Path
import hashlib,json,re,shutil,zipfile
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part12_20261025')
final=Path(str(stage)+'_final')
old=Path('D:/stean/release_chuzaya_smena/day03_part11_20261025_final')
engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
routes=read(stage/'full_render_walkthrough_results.json')
matrix=read(stage/'part12_native_results.json')
assert {r['case'] for r in matrix}==set(map(str,range(18)))|{'guard'}
assert len(routes)==2 and all(r['status']=='PASS' for r in routes+matrix)
cross=read(stage/'part12_cross_save_results.json')
assert {r['case'] for r in cross}=={'help','nohelp','work','audio'} and all(r['status']=='PASS' for r in cross)
assert read(stage/'audio_location_audit.json')['status']=='PASS'
assert read(stage/'audio_save_compat.json')['dialogue_aliases']==17
assert read(stage/'generator_idempotence.json')['status']=='PASS'
assert {r['case'] for r in read(stage/'revision_native_results.json')}=={'camera'}
assert {r['case'] for r in read(stage/'part07_native_results.json')}=={'attention','camera'}
prefixes=('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_p12_',
          'p6_revision_camera_','p6_p7_attention_','p6_p7_camera_')
folders=[p.rstrip('_')+'_contacts' for p in prefixes]
ledger=read(stage/'reviewed_contact_pages.json');pages=[];frames=[]
for name in folders:
    folder=engine/name
    for item in read(folder/'index.json'):
        p=folder/item['sheet'];assert ledger.get(str(p))==sha(p),'Unreviewed contact page: '+str(p)
        pages.append(str(p));frames+=item['frames']
assert len(frames)==len(set(frames))
(stage/'visual_review.json').write_text(json.dumps(dict(all_contact_pages_reviewed=True,pages=len(pages),frames=len(frames),contact_pages=pages,scope='Both complete routes; eighteen chapter12 combinations; four actual old-save migrations; day3 ambience checks; guard/save/load; actual previous-version save; all-actor camera and attention. Contact sheets and selected full-size frames inspected.'),indent=2),encoding='utf8')
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
assert len(identity)==394
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
(R/'source/day03_part12_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
backup=Path('D:/stean/steamapps/common/Everlasting Summer/mod_backups/day03_part12_20261025/code_before.zip')
author=[]
with zipfile.ZipFile(backup) as z:
    names=set(z.namelist())
    for base,pattern in ((R/'tools','*.py'),(R/'tools','*.txt'),(R/'source','*.md')):
        for p in sorted(base.glob(pattern)):
            rel=p.relative_to(R).as_posix()
            if rel not in names or hashlib.sha256(z.read(rel)).hexdigest()!=sha(p):author.append(rel)
routeframes=sum(r['screenshots']+1 for r in routes)
report=f'''# День 3. Часть 12 — «Невиновность не доказана»

Добавлены сцены 163–170, включая 165А/165Б и 169А/169Б: 832 исходных блока, 852 реплики и описания с редакторскими вариантами. Новое продолжение заменяет прежние 161А/161Б/162. Свежая игра после сцены 160 ведёт к разговору в столовой, встрече с Семёном и Славей, возвращению за книгой и вечернему чтению в библиотеке. Третий день ещё не окончен: закрытие библиотеки и подготовка ко сну остаются следующей частью.

## Реализовано

- Один выбор со Славей: помощь даёт +1 один раз, отказ не штрафует. Предыдущее значение дружбы сохраняется отдельно. Предложение оформить объявление в день 4 доступно только при прежних двух очках и выбранной помощи. Новое очко не открывает его задним числом. Это предложение сохраняется отдельно от приглашений Мику и Алисы и не отменяет их.
- При высокой дружбе и состоявшемся личном разговоре Семён поддерживает представление. При низкой Лена прекращает шутку после просьбы и не продолжает длинную сцену ревности. Семён остаётся дружеским персонажем; дополнительных очков ему нет.
- Выбранная в части 11 помощь Жене выполняется здесь, после возвращения Лены. Даша ждёт в библиотеке; при отказе она идёт к Мику. Персонажи сверяют карточки, Женя сама проверяет и исправляет запись. Новых очков Жене нет. Выполненная работа охраняется флагом и не повторяется.
- При переносе старого сохранения предусмотрена связующая сцена: прежняя помощь сохраняется выполненной, девушки договариваются вернуться в библиотеку или встретиться позже. Старые метки и адреса возврата сохранены для загрузки внутри прежнего хвоста; в свежем маршруте он не воспроизводится.
- Роман сначала на столе дома, затем в сцене 166 Лена забирает его; после этого он учитывается как находящийся у неё. Блокнот и папка с плакатом остаются дома. Повязка, ограничения нагрузки, материалы Виолы и документы не сбрасываются.
- Исправлены бытовые неточности: книга берётся со стола, а не с кровати; плакат не перемещается сам на полку; Славя слышит, куда направилась Лена, прежде чем спрашивает про книгу. Персональная рекомендация Жени упоминается только при действительном подборе книги. Постоянный стол — только при прежнем флаге. Чтение не объявляется законченным.

Сверены [официальные описания Soviet Games](https://soviet.games/everlasting-summer/) и реплики оригинальной игры из `source/original_character_reference.json`. Славя остаётся ответственной, Семён способен ответить сам, Женя — прямой и сдержанной. Дарья остаётся обычной девушкой из Москвы 2026 года. Новых мистических происшествий и официального подтверждения пары нет.

## Исправление звука третьего дня

Причина бага после завтрака: сцена 95 меняла фон на улицу, но сохраняла `dining_hall_full.ogg`; смена звука находилась позднее, в уже неисполняемом фрагменте генератора.

Добавлен общий для третьего дня выбор звукового фона при действительной смене помещения. На улице — дневной или вечерний лагерь, в столовой — посуда и разговоры, в домике — тихий интерьер, в медпункте — его штатный фон, в библиотеке, музыкальном клубе и администрации — без унаследованного уличного шума. Если подходящий звук уже играет, он не запускается заново. CG и внутренние планы сохраняют звук текущей локации. Смена плавная; основной музыкальный канал не затрагивается.

Дополнительно исправлены прямые назначения уличного звука внутри домика в сценах 75 и 146, включая их генераторы. После загрузки фон восстанавливается по реально показанному помещению; проверено старое сохранение непосредственно с ошибочным звуком после завтрака. Первая и вторая смены дня этим обработчиком не изменяются.

Проверка старого сохранения выявила два отдельных случая: изменившиеся внутренние адреса реплик возвращали движок к началу сцены, а раннее восстановление звука происходило до окончательного восстановления кадра. Для неизменённого по SHA-256 сценария 95 добавлены 17 проверенных адресов реплик предыдущей сборки; существующие адреса и другие скрипты не переопределяются. Идемпотентная проверка при первом взаимодействии после загрузки восстанавливает окружение уже по окончательному фону. Повторный нативный перенос подтверждает прежний наружный кадр и `camp_center_day.ogg`.

## Спрайты

Сохранена действующая общая постановка для всех персонажей: один собеседник центрируется; группа занимает раздельные позиции; на продолжительных размышлениях Лены фокус переходит к фону, при прямом разговоре возвращается. Короткие мысли не вызывают постоянного скрытия. Сидение не меняет вертикальную позицию или масштаб. Используются зарегистрированные спрайты и эмоции, стандартный масштаб домика и прежний вечерний интерьер библиотеки. Новые изображения не требовались.

## Фактически выполнено

- Независимая сверка 832 блоков рукописи, уникальности меток/defaults, единственной награды Слави, снимка прежней дружбы, состояния предметов и исключения прежнего хвоста из свежего маршрута.
- 18 нативных сочетаний плюс отдельный защитный тест: помощь Жене/отказ, оба выбора Слави, прежняя дружба Слави 0/1/2, высокая/низкая дружба Семёна, дружба Жени 0–4, приглашение читать и его отсутствие, уже выполненная работа. В каждом случае выполнены сохранение и загрузка. Проверены спрайт говорящего, центр одиночного кадра, непрозрачность и отсутствие портретов поверх CG.
- Защитный тест сохраняет и загружает само меню, повторяет обработчик выбора и сцену помощи, повторно входит в завершённую часть: награды и работа не повторяются.
- Четыре настоящих сохранения предыдущей сборки: после части 11 с помощью/без помощи; внутри ещё не выполненной прежней сцены 161А; после завтрака с исходной ошибкой звука. Первые три доходят до нового конца без повторного ужина и новой библиотечной работы; четвёртое загружается уже с правильным лагерным фоном. Это не проверка всех исторических сохранений.
- Первое создание тестового сохранения внутри старой сцены остановилось из-за стандартного тайм-аута тестового движка: пауза ожидания была длиннее него. Для этого теста задан явный предел, повторный запуск выполнен. Runtime-код для исправления ожидания не менялся; первоначальный журнал сохранён отдельно.
- Проверены все 29 используемых идентификаторов фонов/CG третьего дня. На обоих полных маршрутах после каждой реплики третьего дня проверяется фактически играющий канал окружения против текущего помещения.
- Два полных ускоренных прохода от пролога до нового конца: положительные и нейтральные решения, **{routeframes} снимков**. Прежние сцены 161–162 не посещаются. Это не перебор всех старых выборов. Полные проходы отключают переходы; целевые проверки новой части выполняются с переходами.
- Повторены общая камера 13 наборов персонажей, группа, короткая мысль, продолжительная рефлексия с сохранением/загрузкой и возвратом внимания.
- Просмотрены **{len(pages)} контактных листов, охватывающих {len(frames)} кадров**, и выбранные полноразмерные снимки. Хеши просмотренных страниц сохранены.
- Lint: **0 диагностических адресов мода**, {len(locations)} адресов исходной базовой игры. Чистый Lint всей установки не заявляется.
- Чистая компиляция **{len(identity)} скриптов**, локальный запуск и два запуска только с RPYC по Workshop-пути. Исходники и {assets} ресурсов совпадают по SHA-256 с тестовой копией. Повторный запуск родительского генератора сохраняет все 394 runtime-файла без изменений.

Известных нерешённых ошибок проверенных маршрутов нет. Пользовательские сохранения не менялись; работа шла в изолированной установке. Публикация не выполнялась. Рабочие файлы и QA не включены в публикационный ZIP.

## Файлы

Архив: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Снимки и журналы: `{out.as_posix()}`.

Резервная копия: `{backup.as_posix()}`.

Воспроизведение: `tools/run_day03_part12_final_checks.py`. Независимые проверки: `tools/verify_day03_part12.py`, `tools/verify_day03_location_audio.py`.

Изменённые runtime-файлы относительно части 11 ({len(changes)}):

'''+''.join('- `'+p+'`\n' for p in changes)+'\nАвторские исходники и инструменты:\n\n'+''.join('- `'+p+'`\n' for p in sorted(set(author)))
(R/'DAY03_PART12_REPORT.md').write_text(report,encoding='utf8')
shutil.copy2(R/'DAY03_PART12_REPORT.md',out/'DAY03_PART12_REPORT.md')
print('PART12_REPORT_PASS',routeframes,'route frames;',len(frames),'archived frames;',len(changes),'changed runtime files')

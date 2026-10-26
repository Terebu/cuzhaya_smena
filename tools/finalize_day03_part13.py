"""Package the actually executed checks and visually inspected frames."""
from pathlib import Path
import hashlib,json,re,shutil,zipfile
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part13_20261026');final=Path(str(stage)+'_final')
old=Path('D:/stean/release_chuzaya_smena/day03_part12_20261025_final')
engine=stage/'validation/steamapps/common/Everlasting Summer';work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
matrix=read(stage/'part13_native_results.json');assert {x['case'] for x in matrix}==set(map(str,range(17)))|{'guard'}
cross=read(stage/'part13_cross_save_results.json');assert {x['case'] for x in cross}=={0,12,15}
routes=read(stage/'full_render_walkthrough_results.json');assert len(routes)==2
assert all(x['status']=='PASS' for x in matrix+cross+routes)
assert read(stage/'generator_idempotence.json')['status']=='PASS'
assert read(stage/'audio_location_audit.json')['status']=='PASS'
assert read(final/'BUILD_PASS.json')['scripts']==407
folders=[p+'_contacts' for p in ('p6_render_reviewed_high','p6_render_reviewed_low','p6_p13')]
ledger=read(stage/'reviewed_contact_pages.json');frames=[];pages=[]
for name in folders:
 for item in read(engine/name/'index.json'):
  p=engine/name/item['sheet'];assert ledger.get(str(p))==sha(p),'Unreviewed: '+str(p)
  pages.append(str(p));frames+=item['frames']
assert len(frames)==len(set(frames))
(stage/'visual_review.json').write_text(json.dumps(dict(status='PASS',pages=len(pages),frames=len(frames),scope='Two complete accelerated routes, chapter13 matrix and guard, three genuine preceding-release saves; contact sheets and selected full-size frames inspected.',contact_pages=pages),indent=2),encoding='utf8')
lint=(stage/'lint.log').read_text(encoding='utf-8-sig',errors='replace');locations=re.findall(r'^([^\n]+?\.rpyc?:\d+)[ :]',lint,re.M)
assert not [x for x in locations if NAMESPACE in x or 'chuzaya_smena' in x]
(stage/'lint_diagnostics.json').write_text(json.dumps(dict(status='PASS',mod_diagnostic_locations=0,base_diagnostic_locations=len(locations)),indent=2),encoding='utf8')
identity=[];changed=[]
for p in sorted((final/'source_snapshot').rglob('*.rpy')):
 rel=p.relative_to(final/'source_snapshot');assert sha(p)==sha(R/rel)==sha(work/rel),str(rel)
 identity.append(dict(file=rel.as_posix(),sha256=sha(p)))
 previous=old/'source_snapshot'/rel
 if not previous.exists() or sha(previous)!=sha(p):changed.append(rel.as_posix())
assert len(identity)==407
assets=0
for rel,entry in read(final/'release_manifest.json')['files'].items():
 if rel.endswith('.rpyc'):continue
 assert sha(work.parent/rel)==entry['sha256'],rel
 assets+=1
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for p in list(stage.glob('*.json'))+list(stage.glob('*.log')):
 if p.name!='release_manifest.json':shutil.copy2(p,out/p.name)
for p in stage.glob('*fixture_diagnostic.txt'):shutil.copy2(p,out/p.name)
for p in stage.glob('*fixture_diagnostic.png'):shutil.copy2(p,out/p.name)
images=out/'native_frames';images.mkdir(exist_ok=True)
for name in frames:shutil.copy2(engine/name,images/name)
for name in folders:
 dest=out/name;dest.mkdir(exist_ok=True);shutil.copy2(engine/name/'index.json',dest/'index.json')
 for item in read(engine/name/'index.json'):shutil.copy2(engine/name/item['sheet'],dest/item['sheet'])
(out/'tested_source_identity.json').write_text(json.dumps(dict(status='PASS',scripts=len(identity),assets=assets,sources=identity),indent=2),encoding='utf8')
(R/'source/day03_part13_changed_files.json').write_text(json.dumps(changed,indent=2),encoding='utf8')
backup=R.parents[2]/'mod_backups/day03_part13_20261026/code_before.zip';author=[]
with zipfile.ZipFile(backup) as z:
 names=set(z.namelist())
 for folder,pattern in ((R/'tools','*.py'),(R/'tools','*.txt'),(R/'source','*.md'),(R/'source','*.json')):
  for p in folder.glob(pattern):
   rel=p.relative_to(R).as_posix()
   if rel not in names or hashlib.sha256(z.read(rel)).hexdigest()!=sha(p):author.append(rel)
routeframes=sum(x['screenshots']+1 for x in routes)
v=read(R/'source/day03_part13_verification.json')
report=f'''# День 3. Часть 13 — «Последняя страница»

Добавлены сцены 171–179 и 178А/178Б непосредственно после сцены 170: {v['source_blocks']} блоков рукописи, {v['runtime_blocks']} реплик и описаний с редакторскими вариантами. Лена дочитывает «Обыкновенную историю», обсуждает финал, возвращает книгу Жене, встречает Дашу и идёт с ней домой. День ещё не помечен завершённым: по ТЗ следующая часть — разговор перед сном, затем день 4.

## Сюжет, редактура и состояние

- Учитываются низкая, средняя и высокая дружба с Женей, приглашение читать, прежний разговор о романе и библиотечная помощь. При низкой дружбе подробное обсуждение сокращено; личные привилегии не появляются сами.
- Реальный выбор романа проверяется по сохранённой дружбе **при первом приходе**. Новые очки не превращают самостоятельный выбор Лены в рекомендацию Жени.
- Прощание после прежнего объятия и первое объятие — взаимоисключающие ветви. Первое доступно при достаточной дружбе, после вопроса и согласия. Очков за него нет.
- Книга помечается прочитанной в сцене 172 и возвращённой только после записи Жени в сцене 174. `cs_mz_book_borrowed_day3=False`, местонахождение — `library`. Повторной выдачи нет. Плакат, блокнот, повязка, перевязочные материалы и документы сохранены.
- После помощи Даша выходит на воздух в сцене 171; без помощи приходит от Мику. В библиотеке и снаружи она не присутствует одновременно. Долгое чтение происходит до напоминания о закрытии; снаружи Даша ждёт только последние страницы и прощание.
- Меню 178: откровенный разговор даёт +1 доверия Даше один раз; тихая прогулка не меняет очки и не обижает её. Обе ветви приходят в сцену 179. Сохранены отдельные флаги для будущего отклика на четвёртом дне. Сам четвёртый день ещё не написан, поэтому его сцены не заявляются реализованными.
- Приглашения Мику и Алисы остаются независимыми; предложение Слави, рисунки Тихоновой, личный разговор с Семёном, разговор о музыке и совместная тишина сохранены. Новых встреч с этими героями нет. Отношения девушек не объявлены официальной парой, Дарья остаётся обычной девушкой из Москвы 2026 года.

Сверены [официальный обзор персонажей](https://soviet.games/everlasting-summer/), [справка о Жене](https://everlasting-summer.fandom.com/ru/wiki/%D0%96%D0%B5%D0%BD%D1%8F) и реплики установленной оригинальной игры (`source/original_character_reference.json`). Чужие модовые биографии Жени не использовались. Литературный разговор проверен по [эпилогу Гончарова](https://rvb.ru/19vek/goncharov/pssp/vol1/text/oi-13.html): дядя тревожится за жену, но по-прежнему радуется богатству племянника; это переоценка, а не полное нравственное преображение. Исправлена также реплика Даши об отсутствии шуток, которая противоречила только что произнесённой шутке о писателях. Постоянный читательский стол упоминается только при его флаге.

## Постановка и звук

Для всех персонажей продолжает работать общая система `presence_staging.rpy`: одиночный собеседник по центру; группа разделяется; длительные размышления и чтение переводят внимание к фону; прямой диалог возвращает персонажа. Короткая мысль не вызывает скрытие. Позиция по вертикали и масштаб не меняются из-за сидения. Новая часть использует существующие PNG Жени и Даши и их зарегистрированные эмоции.

Использованы имеющиеся ночные экстерьеры библиотеки и домика, ночная лагерная дорожка, стандартный интерьер домика. Ночной интерьер библиотеки — затемнённый существующий дневной фон; это трансформация, нового файла изображения нет. Музыка библиотеки затухает, на прогулке тихо играет существующая спокойная тема. Ночная улица теперь выбирает штатный `camp_center_night.ogg`; при входе в домик он сменяется интерьером. Исправление утечки столовой из части 12 сохранено. Музыка главного меню не используется.

## Фактически выполненные проверки

- Независимая сверка {v['source_blocks']} блоков источника, условий, уникальности меток/defaults, единственного начисления Даше, согласия на объятие, возврата книги и сохранности будущих событий.
- **18 нативных тестов**: 17 сочетаний дружбы Жени, помощи/отказа, прежнего объятия, раннего разговора и обеих новых ветвей; отдельный защитный тест с сохранением/загрузкой самого меню и повторным вызовом обработчика. Дополнительный случай проверяет высокую текущую дружбу при самостоятельном первоначальном выборе книги. В каждом маршруте выполнены сохранение и загрузка финального состояния.
- Проверяются наличие говорящего спрайта, центр одиночного кадра, непрозрачность, отсутствие портретов поверх CG, отсутствие посторонних героев, правильный звуковой фон. Объятие, возврат и награда не повторяются.
- Первый запуск защитного теста проверял конечный экран через фиксированные полсекунды, пока ещё шёл переход сцены 179. Ожидание в тесте заменено на достижение конечной метки; исходный диагностический журнал сохранён. После правки момента входа в домик вся матрица выполнена заново.
- Старые автоматизированные сохранения содержали ссылки на тестовые обработчики меню и персонажей. Для их распаковки в изолированной среде восстановлены исходные QA-обработчики. В runtime мода они не добавлялись. Первоначальная диагностика сохранена отдельно.
- При переносе старого QA-сохранения тестовое ожидание новой метки не остановило автоматические клики и вышло в меню, после чего сработал тайм-аут. Для этих трёх проверок убраны клики: сценарий выполняется автоматически, затем проверяются конечный экран и состояние. Runtime из-за поведения тестового драйвера не менялся.
- Визуальная проверка выявила устаревший кадр главного меню на промежуточных снимках загрузочного теста: ускорение запускалось ещё до первого обновления изображения после загрузки. Загрузочный тест переведён в игровой контекст через `Start`, сначала ожидает и снимает обычную реплику после загрузки, затем включает ускорение. Три загрузки и снимки повторены. Неверные кадры не включены в контрольные листы результата, один сохранён отдельно как диагностика.
- **Три настоящих сохранения предыдущей сборки**, созданные ранее в части 12: низкая дружба без помощи, высокая без помощи, высокая с выполненной помощью. Проверено продолжение через прежний экран ожидания без повторного ужина, Семёна, Слави и карточек, до нового конца с возвращённой книгой.
- **Два полных ускоренных прохода от пролога до текущего конца**, положительные и нейтральные решения: {routeframes} снимков. Выполнены все реплики этих маршрутов; это не перебор всех комбинаций старых выборов. Для полных проходов переходы отключены; целевые проверки новой части используют переходы.
- Просмотрены **{len(pages)} контактных листов, охватывающих {len(frames)} кадров**, и выбранные полноразмерные снимки. Хеши просмотренных страниц записаны. Проверенные постановки без наложений и обрезанных спрайтов.
- Аудит {len(read(stage/'audio_location_audit.json')['rooms'])} идентификаторов локаций/CG третьего дня. На полных проходах проверяется фактически играющее окружение после реплик третьего дня.
- Lint: **0 диагностических адресов мода**, {len(locations)} адресов базовой игры. Чистый Lint всей установки не заявляется.
- Чистая компиляция **407 скриптов**, проверка ресурсов, локальный запуск и два запуска только RPYC по Workshop-пути. SHA-256 исходников и {assets} ресурсов совпадают с тестовой копией. Родительский генератор воспроизводит runtime без изменений. Стабильные адреса возвратов включают часть 12.

Нерешённых ошибок проверенных маршрутов не обнаружено. Пользовательские сохранения не менялись; проверки изолированы. Публикация не выполнялась. Рабочие файлы и QA не включены в публикационный ZIP.

## Результаты и изменённые файлы

Архив: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Скриншоты и журналы: `{out.as_posix()}`.

Резервная копия: `{backup.as_posix()}`.

Проверки: `tools/run_day03_part13_qa.py`, `tools/run_day03_part13_final_checks.py`, `tools/verify_day03_part13.py`. При повторном создании архива выбрать новый каталог, существующая сборка сохраняется.

Runtime относительно части 12 ({len(changed)} файлов):

'''+''.join('- `'+p+'`\n' for p in changed)+'\nАвторские исходники и инструменты:\n\n'+''.join('- `'+p+'`\n' for p in sorted(set(author)))
(R/'DAY03_PART13_REPORT.md').write_text(report,encoding='utf8');shutil.copy2(R/'DAY03_PART13_REPORT.md',out/'DAY03_PART13_REPORT.md')
print('PART13_REPORT_PASS',routeframes,'route frames;',len(frames),'archived frames;',len(changed),'changed runtime files')

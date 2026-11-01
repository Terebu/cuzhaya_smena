"""Package actual results only after manual review of the final contact pages."""
from pathlib import Path
import json,hashlib,shutil,os,re
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day04_20261029');final=Path(str(stage)+'_final')
engine=stage/'validation/steamapps/common/Everlasting Summer';work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def archive(p,q):
 q.parent.mkdir(parents=True,exist_ok=True)
 if q.exists():assert sha(p)==sha(q);return
 try:os.link(p,q)
 except OSError:shutil.copy2(p,q)
matrix=read(stage/'day04_native_results.json');assert len(matrix)==4 and all(x['status']=='PASS' for x in matrix)
cross=read(stage/'day04_cross_save_results.json');assert len(cross)==2 and all(x['status']=='PASS' for x in cross)
routes=read(stage/'full_render_walkthrough_results.json');assert len(routes)==2 and all(x['status']=='PASS' and x['day4'] for x in routes)
assert read(stage/'day04_audio_audit.json')['status']=='PASS'
assert read(stage/'day04_generator_identity.json')['status']=='PASS'
assert (final/'BUILD_PASS.json').exists()
ledger=read(stage/'reviewed_contact_pages.json');pages=[];frames=set()
folders=['p6_render_reviewed_'+x+'_contacts' for x in ('high','low')]+['p6_day04_matrix_'+str(i)+'_contacts' for i in range(4)]+['p6_day04_cross_contacts']
for name in folders:
 for item in read(engine/name/'index.json'):
  p=engine/name/item['sheet'];assert ledger.get(str(p))==sha(p),'Unreviewed page: '+str(p)
  pages.append(p);frames.update(item['frames'])
scripts=[]
for p in (final/'source_snapshot').rglob('*.rpy'):
 rel=p.relative_to(final/'source_snapshot');assert sha(p)==sha(R/rel)==sha(work/rel),str(rel)
 scripts.append(dict(file=rel.as_posix(),sha256=sha(p)))
lint=(stage/'lint.log').read_text(encoding='utf-8-sig',errors='replace')
mod_lint=[l for l in lint.splitlines() if re.match(r'^.*(?:cs_scripts_5ea2d086|mods/chuzaya_smena).*\.rpyc?:\d+',l)]
assert not mod_lint,mod_lint
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for p in list(stage.glob('*.json'))+list(stage.glob('*.log')):shutil.copy2(p,out/p.name)
for name in frames:archive(engine/name,out/'native_frames'/name)
for name in folders:
 index=read(engine/name/'index.json')
 for item in index:archive(engine/name/item['sheet'],out/name/item['sheet'])
 shutil.copy2(engine/name/'index.json',out/name/'index.json')
result=dict(status='PASS',scripts=len(scripts),contact_pages=len(pages),reviewed_frames=len(frames),matrix_routes=4,cross_saves=2,full_routes=2,source_identity=scripts)
(out/'day04_final_results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
report=f'''# День 4 — «Те, кого здесь не было»

Интегрированы все двенадцать сцен третьей литературной редакции: 3396 блоков исходного диалога и повествования, семь меню, пять возможных начислений дружбы. Четвёртый день открывается после актуальной третьей ночи, с чёрным экраном «День 4», и завершается отдельным титром и экраном продолжения.

## Поведение и редактура

- Сохранены совместный сон, признание и раздельный сон третьего дня. Накопленные очки не обнуляются. Раздельная ветвь не получает чужую романтическую сцену; официальный статус пары не добавляется.
- Для Жени сохранён снимок дружбы до выбора: новое очко не открывает объятия задним числом. Требуется и прежнее разрешение. За выборы начисляется по одному очку Семёну, Виоле, Алисе, Жене и Даше; у каждого меню есть защита от повторной награды. Записка и подход к вожатой очков не дают.
- Состояние улик: недатированная фотография у Ольги Дмитриевны; фотография 1971 года, список и записи воспоминаний в запертом ящике библиотеки. Папка 1963 года не уносится. Повязка после осмотра снята; прежняя травма не объявляется мгновенно исчезнувшей.
- Приглашения Мику и Алисы сохраняются независимо и явно перенесены на завтра. Предложение Слави также остаётся отложенным. Прослушивания и оформление объявления не выдаются за состоявшиеся события.
- Исправлены пижама на стуле при спящей Даше, занятые предметами руки, форма Даши после возвращения, уход музыкантов от столовой обратно в клуб, занятый послеобеденный график, повторное запирание папки вместо ящика и неподтверждённая ссылка на конкретный эпизод Стругацких. Для новой книги выбрана «Ася» Тургенева; вечернее чтение Семёна описано как сборник фантастических рассказов.
- Общая система постановки применяется ко всем персонажам: одиночный собеседник в центре, группы распределены по кадру, длительная внутренняя рефлексия без портретов, возвращение к собеседникам при разговоре. Сидение не меняет высоту и масштаб спрайта. Смена эмоций привязана к отдельным смысловым точкам, а не каждой реплике.
- Пять новых фонов старого корпуса и CG встречи на лестнице переименованы и подключены. CG совместного сна показывается только в соответствующей ветви после переодевания; портретов поверх CG нет. Недостающие изображения и использованные замены перечислены в `DAY04_MISSING_ASSETS.md`.
- Устранены повторные регистрации ресурсов в старом `resources.rpy` и повторная установка корня в `paths.rpy`: старые имена файлов сохранены как совместимые заглушки, действующие определения остаются в `cs_runtime_resources.rpy` и `cs_asset_paths.rpy`.
- Для домика вожатой, убежища и ночного интерьера уточнены звуковые правила. Столовая при выходе сменяется уличным окружением. Музыка главного меню в сценах не используется.

Для редакторской сверки использованы реплики оригинала из `source/original_character_reference.json`, сведения о [Жене](https://everlasting-summer.fandom.com/ru/wiki/%D0%96%D0%B5%D0%BD%D1%8F) и [Семёне](https://everlasting-summer.fandom.com/ru/wiki/%D0%A1%D0%B5%D0%BC%D1%91%D0%BD). Сухая прямота Жени, сдержанные ответы Семёна и поведение других героев сохраняются; новые тайные биографии им не добавлены. Дарья и Лена Соколова остаются авторскими персонажами.

## Фактически выполненные проверки

- Четыре нативных маршрута нового дня: все первые / все вторые / смешанные выборы, дружба с Женей 0/2/3, наличие и отсутствие разрешения на объятие, три состояния третьей ночи. Проверены семь меню, пять отдельных наград, снимок дружбы, обе сцены объятия, сохранение и загрузка конца дня.
- Два настоящих сохранения прежней третьей ночи (`p14_2_end-LT1.save`, `p14_6_end-LT1.save`) загружены в новой версии; открывается четвёртый день, очки и романтические флаги сохраняются. Дополнительно выполнена запись и загрузка уже в начале нового дня. Пользовательские слоты не менялись: тесты используют изолированный каталог.
- Два полных ускоренных прохода от пролога до конца четвёртого дня, с положительными и нейтральными выборами. Это проверка двух сквозных маршрутов, а не перебор всех комбинаций мода.
- Просмотрены {len(pages)} контрольных листов, содержащих {len(frames)} кадров, и выбранные полноразмерные снимки. Хеши просмотренных листов сохранены. Проверены масштаб, композиция, одиночный центр, исчезновение во время длинных мыслей, CG без портретов и титр дня.
- Статический аудит двенадцати сцен, семи меню, пяти наград, уникальности меток/defaults и звуковых правил; повторная генерация четвёртого дня даёт те же runtime-файлы.
- Lint запущен; диагностик в скриптах мода не найдено. Общие предупреждения установленной оригинальной игры сохранены в журнале и не объявляются исправленными.
- Чистая сборка {len(scripts)} скриптов, проверка ресурсов, внутренних идентификаторов AST и путей. Локальный запуск и два запуска скомпилированного мода из изолированного каталога Workshop успешны. Исходники итоговой сборки совпадают с проверенной копией и рабочим проектом.

При первом просмотре обнаружен неверный идентификатор вечерней столовой: Ren’Py показывал чёрный фон с красной строкой вместо исключения. Исправлен на штатный `bg int_dining_hall_sunset`; проверка усилена до точного наличия изображения (`exact=True`), четыре маршрута повторены после исправления. Неполный сквозной запуск до исправления не засчитан; финальные результаты относятся к исправленной версии.

## Оставшиеся замечания

Технических ошибок и traceback на проверенных маршрутах не обнаружено. Сборка готова к ручному тестированию. Художественные пробелы остаются: прежде всего спортивные спрайты Даши, комната с фотографиями и точный фон технического архива. Поэтому полную визуальную постановку нельзя считать законченной; подробный список и текущие замены находятся в `DAY04_MISSING_ASSETS.md`.

Пятый день в переданном ТЗ отсутствует. Вместо выдуманного продолжения оставлен экран ожидания с сохранением/загрузкой; все договорённости сохранены. Публикация в Steam Workshop не выполнялась. Тесты, журналы, резервные копии и рабочие документы не включены в публикационный ZIP.

Сборка: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Скриншоты и журналы: `{out.as_posix()}`.

## Файлы

- `days/day04/00_flow.rpy`, `days/day04/resources.rpy`, `days/day04/01_scene.rpy`–`12_scene.rpy`.
- Связка: `days/day03/part14/00_flow.rpy`; аудио: `day03_location_audio.rpy`; устранение дублей: `resources.rpy`, `paths.rpy`; стабильные возвраты: `save_return_compat.rpy`.
- Переименованные пять фонов в `bg/old_camp` и CG `cg/lena_n_dasha/cg_lena_darya_bunker_reunion_morning.png`.
- `source/day04.md`, `source/day04_editorial.json`, `source/day04_verification.json`; `tools/build_day04.py`, `tools/build_day04_qa.py`, `tools/day04_test.rpy.txt`, `tools/run_day04_qa.py`, `tools/run_day04_cross_save.py`, `tools/run_day04_final_checks.py`, `tools/finalize_day04.py`; обновлён переход генератора части 14.

Предшествующий отчёт по части 14 относится к зафиксированной сборке от 26 октября. Результаты новой редакции рабочего проекта проверены отдельно в текущих сквозных проходах.
'''
(R/'DAY04_REPORT.md').write_text(report,encoding='utf8')
for name in ('DAY04_REPORT.md','DAY04_MISSING_ASSETS.md'):shutil.copy2(R/name,out/name)
(R/'source/day04_verification.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print('DAY04_FINAL_REPORT_PASS',len(pages),'pages;',len(frames),'frames;',len(scripts),'scripts')

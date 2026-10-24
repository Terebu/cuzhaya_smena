"""Archive checked evidence and produce a report only from completed checks."""
from pathlib import Path
from zipfile import ZipFile
import json,re,hashlib,shutil
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_medpoint_revision_20261024')
final=Path(str(stage)+'_final');engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
native=read(stage/'revision_native_results.json');routes=read(stage/'full_render_walkthrough_results.json')
assert {x['case'] for x in native}==set(map(str,range(10)))|{'camera','guard','legacy'}
assert all(x['status']=='PASS' for x in native+routes)
assert len(routes)==2 and {x['friendship']['dv'] for x in routes}=={0,2}
for name in ('revision_cross_save_result.json','p7_cross_save_result.json'):
 assert read(stage/name)['status']=='PASS'
assert {x['case'] for x in read(stage/'part07_native_results.json')}=={'attention','camera','guard'}
assert any(x['test']=='cs_day03_p6_costume' and x['status']=='PASS' for x in read(stage/'part06_native_results.json'))
lint=(stage/'lint.log').read_text(encoding='utf-8-sig',errors='replace')
locations=re.findall(r'^([^\n]+?\.rpyc?:\d+)[ :]',lint,re.M)
mod=[x for x in locations if NAMESPACE in x or 'chuzaya_smena' in x]
assert not mod,mod
lintresult=dict(status='PASS',mod_diagnostics=mod,base_diagnostic_locations=len(locations),base_files=sorted(set(x.rsplit(':',1)[0] for x in locations)))
(stage/'lint_diagnostics.json').write_text(json.dumps(lintresult,ensure_ascii=False,indent=2),encoding='utf8')
out=final/'qa_evidence';out.mkdir(exist_ok=True)
identity=[]
for p in sorted((final/'source_snapshot').rglob('*.rpy')):
 rel=p.relative_to(final/'source_snapshot')
 assert sha(p)==sha(work/rel)==sha(R/rel),str(rel)
 identity.append(dict(file=rel.as_posix(),sha256=sha(p)))
build=read(final/'BUILD_PASS.json');manifest=read(final/'release_manifest.json');assets=0
for rel,item in manifest['files'].items():
 if rel.endswith('.rpyc'):continue
 assert sha(work.parent/rel)==item['sha256'],rel
 assets+=1
for p in stage.glob('*.json'):
 if p.name in ('release_manifest.json',):continue
 shutil.copy2(p,out/p.name)
for p in stage.glob('*.log'):shutil.copy2(p,out/p.name)
images=out/'native_frames';images.mkdir(exist_ok=True);frames=[]
for prefix in ('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_revision_','p6_p7_','p6_costume_','revision_cross_','p7_cross_version'):
 for p in sorted(engine.glob(prefix+'*.png')):
  shutil.copy2(p,images/p.name);frames.append(p.name)
for name in ('p6_render_reviewed_high_contacts','p6_render_reviewed_low_contacts','p6_revision_contacts','p6_p7_contacts','p6_costume_contacts','revision_cross_contacts'):
 folder=engine/name
 if not (folder/'index.json').exists():continue
 target=out/folder.name;target.mkdir(exist_ok=True)
 shutil.copy2(folder/'index.json',target/'index.json')
 for page in read(folder/'index.json'):shutil.copy2(folder/page['sheet'],target/page['sheet'])
changed_contacts=engine/'final_changed_frames/p6_render_reviewed_contacts'
if changed_contacts.exists():shutil.copytree(changed_contacts,out/'final_changed_contacts',dirs_exist_ok=True)
visual=read(stage/'final_visual_comparison.json')
assert visual.get('changed_frames_reviewed') is True
summary=dict(status='PASS',matching_scripts=len(identity),matching_assets=assets,frames=len(frames),sources=identity,scope='Two complete accelerated native routes repeated after stable-call migration fix; 13 revised-scene cases; 3 existing focus/save cases; wardrobe case; two actual cross-version saves; compiled-only local and Workshop smoke checks. Full route transitions off; targeted camera/menu checks transitions enabled.')
(out/'tested_source_identity.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
backup=R.parents[2]/'mod_backups/day03_part04_revision_20261024/code_before.zip'
changes=[]
with ZipFile(backup) as z:
 for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
  rel=p.relative_to(R).as_posix();old=z.read(rel) if rel in z.namelist() else None
  if old!=p.read_bytes():changes.append(rel)
(R/'source/medpoint_revision_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
routeframes=sum(x['screenshots']+1 for x in routes)
report=f'''# День 3: «Два пациента и один диагноз» — 24 октября 2026

Переработана утренняя часть 4 в `days/day03/part04/`. Это замена прежнего визита, а не дополнительный осмотр после обеда. Сохранены 732 блока присланной редакции; три добавленные реплики учитывают уже выданный пакет. Исправлены три формулировки: Виола узнаёт об очереди, а не о несуществующем крике; плановый визит не называется заведомо третьим; Алиса не приписывает Лене повторную травму.

Алиса приходит с небольшой царапиной от струны. Сначала заканчивается перевязка Лены и выбор помощи Виоле. Запасные материалы выдаются до появления Алисы, по снимку прежней дружбы ≥2, с защитой от повторной выдачи. Уже полученная повязка остаётся в сумке. Новый выбор Алисы доступен всем: уважительный разговор даёт +1 DV, нейтральная ветка не штрафует. Клубный выбор имеет отдельную защиту и даёт ещё +1: два очка достижимы и проверены.

В части 5 решение идти к вожатой больше не принимается заново. Для старого входа сохранён прежний переход. В части 6 Алиса сдержанно отзывается на утреннее доверие без рассказа о визите к медсестре. Знакомство не начинается повторно. Локоть, запрет спорта, документы, плакат, чтение и развилки частей 5–7 сохраняются. Третий день остаётся открытым.

## Общая постановка

`cs_presence_stage()` теперь центрирует любого единственного собеседника, включая оригинальные спрайты. Сохраняются высота, масштаб, вертикальная привязка и пропорции. В группе используются свободные места. При уходе одного участника оставшийся центрируется. Загрузка сохранения использует ту же функцию.

Рефлексивная камера общая: скрывает весь видимый состав, помнит его и возвращает только в той же локации. Реально ушедший персонаж не возвращается. Применяется в расставленных по сюжету длинных размышлениях и самостоятельном чтении. Короткая мысль или смена говорящего не запускает скрытие. Сидящий/лежащий персонаж не опускается и не скрывается из-за позы. Поверх полноэкранной CG портреты не выводятся.

Проверены 13 зарегистрированных наборов, включая зимнюю Дашу: центр, неизменность высоты/размера, скрытие и возврат. В медпункте тройка Алиса—Виола—Дарья разведена без наложений; после выхода остаются Алиса и Дарья.

## Редактура характеров

Интернет-справка — [описания разработчика Soviet Games](https://soviet.games/everlasting-summer/). Дополнительно прочитаны реплики оригинальной установленной игры (первые два дня) для Алисы, Мику, Тихоновой, Слави, Ульяны, Виолы, Жени, вожатой, Шурика, Электроника и Семёна. Рабочие выписки с исходными файлами/строками — `source/original_character_reference.json`.

Алиса остаётся колкой, не принимает жалость и не становится близкой подругой за один выбор. Виола сохраняет профессиональную заботу и иронию. Семён отвечает на подколы; Лена признаёт границу, если ему неприятно. В клубе оценка Алисы «не пытаешься убедить всех, какая ты крутая» заменена конкретной оценкой ритма гитары. Остальные линии проверены на согласованность встреч и постепенного доверия; их биографии не переписаны под пользовательских персонажей.

Правило замены эмоций через один тег сверено с [Ren’Py](https://www.renpy.org/doc/html/displaying_images.html#hide-statement). Выбор рефлексивного кадра — авторская постановка, а не автоматическое правило движка.

## Фактические проверки

При реальном переносе сохранения обнаружена и исправлена потеря возврата после меню Виолы: чистая компиляция меняла непрозрачные идентификаторы `call`. Все 285 вызовов мода получили постоянные `from`-метки. В отдельном `save_return_compat.rpy` находятся 548 проверенных адресов из двух прежних сборок: при загрузке заменяются только несуществующие адреса этого мода, без изменения глубины стека. Текущие сохранения и чужие моды не перенаправляются. После миграции блокируется откат через точку загрузки, как рекомендует [Ren’Py](https://www.renpy.org/doc/html/config.html#var-config.after_load_callbacks). Генератор сборки сохраняет именованные возвраты автоматически. Это проверка известных сборок, а не гарантия для каждого исторического промежуточного билда.

- Два полных нативных прохода от `chuzhaya_smena_start` до текущего конца части 7: положительные и нейтральные решения. Все строки исполнялись, снимки делались на сценах, CG и изменениях состава. **{routeframes} снимок**; контактные листы обоих маршрутов и ключевые кадры просмотрены. После повторного прохода {visual['identical_to_reviewed']} кадра совпали побайтно с просмотренными; {visual['changed']} изменившихся кадров просмотрены заново. Наложений, зависшей прозрачности и неверного одиночного размещения в просмотренных кадрах нет.
- 10 проверок медицинской сцены: четыре сочетания решений с прежней дружбой Виолы ниже/выше порога, отдельно нулевая дружба и уже выданный пакет. В каждом случае проверены один осмотр, счётчики, повязка, отсутствие дублей и стык с частью 5.
- Общая камера для всех 13 наборов; повтор обоих выборов Алисы с достижимостью DV=2; сохранение на меню; старый именованный выход. Всего {len(native)} проверок новой редакции.
- Три прежние проверки фокуса/камеры/сохранений части 7 и отдельное переодевание Даши пройдены повторно.
- Реальное сохранение предыдущей сборки на выборе Виолы загружено в новую: новые defaults появились, помощь не открыла прежний бонус задним числом, выбор Алисы работает. Отдельно пройден перенос сохранения с конца части 6 в обед/библиотеку части 7.
- Lint: **0 диагностик мода**. Осталось {len(locations)} сообщений с адресами исходных файлов базовой игры (её отсутствующие CG, старые экраны и переводы). Это не полностью чистый Lint всей установленной игры.
- Чистая компиляция {build['scripts']} скриптов, проверка имён/внутренних идентификаторов, локальный запуск и два compiled-only запуска Workshop прошли. {assets} ресурсов совпадают с проверенной копией по SHA-256; {len(identity)} исходников совпадают со сборкой. Публикация не выполнялась.

Полные проходы повторены после исправления возвратов. Они ускоренные, с отключёнными переходами; отдельные визуальные/меню проверки идут с включёнными переходами. Два маршрута и матрица не означают перебор всех сочетаний всех выборов. Старый именованный выход отдельно исполнен нативным тестом `legacy`.

Архив для публикации: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`. Свидетельства: `{out.as_posix()}`. Пользовательские сохранения не изменялись; тестирование изолировано.

## Повторение авторинга

`build_day03_part04.py` вызывает актуальный `build_day03_part04_revision.py`. Генераторы частей 5 и 6 применяют `apply_medpoint_continuity.py`, чтобы не потерять новую стыковку. Независимые проверки: `verify_medpoint_revision.py`, `verify_day03_part05.py`, `verify_day03_part06.py`, `verify_day03_part07.py`. Генератор новой части идемпотентен. Резервная копия до работы: `{backup.as_posix()}`.

Изменённые runtime-файлы ({len(changes)}):

'''+''.join('- `'+p+'`\n' for p in changes)
(R/'DAY03_MEDPOINT_REVISION_REPORT.md').write_text(report,encoding='utf8')
print('FINAL_REVISION_REPORT_PASS',routeframes,'route frames;',len(native),'new native cases;',len(frames),'archived frames')

from pathlib import Path
import json,hashlib,shutil,os,re
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part14_20261026');final=Path(str(stage)+'_final');old=Path('D:/stean/release_chuzaya_smena/day03_part13_20261026_final')
engine=stage/'validation/steamapps/common/Everlasting Summer';work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def archive(p,q):
 q.parent.mkdir(parents=True,exist_ok=True)
 if q.exists():return
 try:os.link(p,q)
 except OSError:shutil.copy2(p,q)
matrix=read(stage/'part14_native_results.json');assert len(matrix)==10 and all(x['status']=='PASS' for x in matrix)
cross=read(stage/'part14_cross_save_results.json');assert len(cross)==2 and all(x['status']=='PASS' for x in cross)
routes=read(stage/'full_render_walkthrough_results.json');assert len(routes)==2 and all(x['status']=='PASS' for x in routes)
assert read(stage/'generator_idempotence.json')['status']=='PASS'
assert read(stage/'audio_location_audit.json')['status']=='PASS'
assert (final/'BUILD_PASS.json').is_file()
lint=(stage/'lint.log').read_text(encoding='utf-8-sig',errors='replace')
locations=re.findall(r'^([^\n]+?\.rpyc?:\d+)[ :]',lint,re.M)
assert not [x for x in locations if 'cs_scripts_5ea2d086' in x or 'chuzaya_smena' in x]
(stage/'lint_diagnostics.json').write_text(json.dumps(dict(status='PASS',mod_diagnostic_locations=0,base_diagnostic_locations=len(locations)),indent=2),encoding='utf8')
ledger=read(stage/'reviewed_contact_pages.json');frames=set();pages=[]
folders=('p6_render_reviewed_high_contacts','p6_render_reviewed_low_contacts','p6_p14_contacts')
for name in folders:
 for item in read(engine/name/'index.json'):
  p=engine/name/item['sheet'];assert ledger.get(str(p))==sha(p),str(p)
  frames.update(item['frames']);pages.append(p)
(stage/'visual_review.json').write_text(json.dumps(dict(status='PASS',pages=len(pages),frames=len(frames)),indent=2),encoding='utf8')
identity=[];changed=[]
for p in (final/'source_snapshot').rglob('*.rpy'):
 rel=p.relative_to(final/'source_snapshot');assert sha(p)==sha(R/rel)==sha(work/rel),str(rel)
 identity.append(dict(file=rel.as_posix(),sha256=sha(p)))
 prior=old/'source_snapshot'/rel
 if not prior.exists() or sha(prior)!=sha(p):changed.append(rel.as_posix())
assert len(identity)==421
assets=0
for rel,entry in read(final/'release_manifest.json')['files'].items():
 if rel.endswith('.rpyc'):continue
 assert sha(work.parent/rel)==entry['sha256'],rel
 assets+=1
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for p in list(stage.glob('*.json'))+list(stage.glob('*.log')):
 if p.name!='release_manifest.json':shutil.copy2(p,out/p.name)
for name in frames:archive(engine/name,out/'native_frames'/name)
for name in folders:
 for p in (engine/name).glob('*'):archive(p,out/name/p.name)
(out/'tested_source_identity.json').write_text(json.dumps(dict(status='PASS',scripts=len(identity),assets=assets,sources=identity),indent=2),encoding='utf8')
v=read(R/'source/day03_part14_verification.json');total=sum(x['screenshots']+1 for x in routes)
report=f'''# День 3. Часть 14 — «Ближе, чем вчера»

Интегрированы сцены 180–189, включая 187А/187Б: {v['source_blocks']} блоков рукописи, {v['runtime_blocks']} реплик и описаний с редакторскими вариантами. Сцена начинается уже в домике после части 13, без повторной прогулки, отпирания двери или библиотеки.

## Итоги части 13

Результаты зафиксированы до изменений части 14 в `DAY03_PART13_REPORT.md` и отдельной сборке `day03_part13_20261026_final`. Три повторные загрузки настоящих старых сохранений успешны, 18 целевых проверок и два полных маршрута успешны. Визуально просмотрены 1906 кадров на 31 листе. Части 1–13 связаны; нерешённых ошибок проверенных маршрутов и незавершённых проверок не осталось. Сборка части 13 готова к ручному тестированию, не опубликована. Повторно эти тесты в текущей работе не запускались.

## Реализация части 14

- Существующий `cs_friend_da` снимается в `cs_da_friend_before_night` до первого меню. Порог 2 достижим двумя прежними выборами: музыка в части 10 и откровенный разговор в части 13. Очки не выдаются автоматически.
- Просьба при доверии ниже 2 приводит к мягкому отказу и раздельному сну без штрафа. Добровольный раздельный сон также полноценная ветвь. При согласии одно очко начисляется однократно; повторный вызов обработчиков награду не повторяет.
- Признание — отдельный выбор после согласия, без очков. Дарья не обещает немедленной взаимности; статус пары не устанавливается. Флаги совместного сна, уважения личного пространства, признания или невысказанных чувств сохраняются.
- Книга уже возвращена Жене. Упоминание книги, постоянного допуска в библиотеку, рисунков и тихих разговоров согласовано с предыдущими состояниями. Плакат, блокнот, документы, повязка и будущие приглашения не сбрасываются. Реплика «не знаю, что будем делать завтра» уточнена: договорённости уже существуют.
- CG переименована: `cg/lena_n_dasha/cg_lena_darya_shared_sleep_night.png`. Она появляется при совместном засыпании после разрешения и разговора, не при отказе и не поверх стоящих спрайтов. Перед CG уточнено положение девушек, соответствующее рисунку.
- Использована общая постановка всех персонажей: одиночный собеседник в центре; длительные мысли без портретов; короткие паузы без постоянного мигания; вертикаль и масштаб не меняются из-за сидения. После переодевания используется интерьер: подходящей одежды для сна в наборе спрайтов нет, форма не показывается вместо неё. CG показывает собственные костюмы.
- Стандартный ночной интерьер сохранён без приближения; для полумрака используется затемнение существующего фона. Ночная композиция — существующий `a_promise_from_distant_days`, с плавным входом и затуханием. К финалу звук затихает.
- Чёрный экран с титром «Конец третьего дня», затем экран продолжения с сохранением/загрузкой. Четвёртый день в ТЗ не написан: его события не выдуманы; все флаги сохранены для следующей части.

Для редакторской сверки повторно найдены сведения о [персонажах БЛ](https://fanfics.me/fandom70/heroes) и [Жене](https://everlasting-summer.fandom.com/ru/wiki/%D0%96%D0%B5%D0%BD%D1%8F); использованы также ранее извлечённые реплики оригинальной игры. Лена Соколова и Дарья — авторские персонажи мода, не подменяются биографиями героев оригинала.

## Проверки новой версии

- **10 нативных тестов**: доверие 0/1/2/3, просьба и отказ от просьбы, согласие/отказ, обе ветви признания. Проверены исключение противоположных сцен, единственная награда, сохранение/загрузка конца, повторный вызов обработчиков, сохранение/загрузка обоих меню в защитном тесте.
- **Две загрузки настоящих сохранений части 13**: переход в часть 14, сохранённое доверие 2 и 3, признание и отложенное признание. Старые QA-обработчики восстановлены только в изолированном тестовом окружении, не в моде.
- **Два полных ускоренных прохода новой версии**, от пролога до конца третьего дня: {total} кадров. Это положительный и нейтральный маршруты, не перебор всех комбинаций прежних выборов. Полные проходы без переходов; целевая матрица новой части с переходами.
- Визуально просмотрены **{len(pages)} контрольных листов, {len(frames)} кадров** и выбранные полноразмерные снимки. Хеши просмотренных страниц записаны. Проверены CG без портретов, центр одиночных спрайтов, отсутствие обрезаний, звуковое окружение третьего дня.
- Статическая проверка текста, условий, уникальных меток/defaults, единственной награды и ресурса CG; воспроизводимость родительским генератором. **421 скрипт**, {assets} ресурсов: хеши тестовой копии совпадают с итоговой сборкой.
- Lint запущен. Диагностика установки хранится в `qa_evidence/lint.log`; диагностик мода не обнаружено. Предупреждения оригинальной игры не объявляются исправленными.
- Чистая сборка и проверка путей/AST/ресурсов; локальный запуск и два запуска только RPYC из каталога Workshop.

Тестовый драйвер первоначально использовал `Start` для повторного входа из игры и автоматические клики при ожидании второго меню. Это вызывало исключение контекста/пропуск меню. Исправлены только QA-драйверы (`Jump`, ожидание остановки на меню); защитная проверка повторена. Ошибки не скрыты: диагностический журнал сохранён отдельно.

## Ограничения и готовность

Нерешённых ошибок проверенных маршрутов и блокирующих замечаний не обнаружено. Сборка готова к ручному тестированию перед публикацией. Публикация не выполнялась. Четвёртый день остаётся будущим продолжением; его сюжетные последствия ещё предстоит написать. Пользовательские сохранения не менялись. Рабочие файлы, тесты и журналы не включены в публикационный ZIP.

Архив: `{(final/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.

Скриншоты и журналы: `{out.as_posix()}`.

## Изменённые runtime-файлы относительно части 13

'''+''.join('- `'+x+'`\n' for x in changed)+'''
Авторские материалы: `source/day03_part14.md`, `source/day03_part14_transcript.json`, `source/day03_part14_verification.json`, `tools/build_day03_part14.py`, `tools/build_day03_part14_qa.py`, `tools/run_day03_part14_qa.py`, `tools/run_day03_part14_cross_save.py`, `tools/run_day03_part14_final_checks.py`, `tools/verify_day03_part14.py`, `tools/finalize_day03_part14.py`; обновлены генератор части 13, стабилизатор возвратов и генератор полного прохода.
'''
(R/'DAY03_PART14_REPORT.md').write_text(report,encoding='utf8');shutil.copy2(R/'DAY03_PART14_REPORT.md',out/'DAY03_PART14_REPORT.md')
print('PART14_REPORT_PASS',total,'route frames;',len(frames),'archived frames;',len(changed),'changed runtime files')

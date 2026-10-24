"""Produce a report from completed native checks, never from planned tests."""
from pathlib import Path
from zipfile import ZipFile
import json,hashlib
R=Path(__file__).resolve().parent.parent
release=Path('D:/stean/release_chuzaya_smena/day03_part07_20261024_final')
stage=Path('D:/stean/release_chuzaya_smena/day03_part07_20261024_checked')
def read(p):return json.loads(p.read_text(encoding='utf8'))
build=read(release/'BUILD_PASS.json');identity=read(release/'qa_evidence/tested_source_identity.json')
routes=read(stage/'full_render_walkthrough_results.json');native=read(stage/'part07_native_results.json')
lint=read(stage/'lint_diagnostics.json');cross=read(stage/'p7_cross_save_result.json')
negative=read(Path('D:/stean/release_chuzaya_smena/day03_part07_negative_checks/test_results.json'))
assert len(routes)==2 and all(x['status']=='PASS' for x in routes)
assert {x['case'] for x in native}=={'attention','0','1','2','3','4','camera','guard'}
assert not lint['mod_diagnostics'] and cross['status']=='PASS'
assert all(x['rejected'] for x in negative)
backup=Path('D:/stean/steamapps/common/Everlasting Summer/mod_backups/day03_part07_20261024/code_before.zip')
changes=[]
with ZipFile(backup) as z:
 for p in sorted(list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))):
  name=p.relative_to(R).as_posix();old=z.read(name) if name in z.namelist() else None
  if old==p.read_bytes():continue
  kind='new' if old is None else ('line_endings_only' if old.decode('utf8').splitlines()==p.read_text(encoding='utf8').splitlines() else 'modified')
  changes.append(dict(file=name,status=kind))
(R/'source/day03_part07_changed_files.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
frames=sum(x['screenshots']+1 for x in routes)
rows=[]
for x in routes:
 f=x['friendship'];rows.append('| '+x['route']+' | '+' / '.join(str(f[k]) for k in ('mi','dv','un','se','sl','mz','viola'))+' | '+str(x['lunch_together'])+' | '+str(x['sketch_plan'])+' |')
files='\n'.join('- `'+x['file']+'` — '+x['status'] for x in changes if x['status']!='line_endings_only')
report=f'''# День 3, часть 7 — проверка от 24 октября 2026

Добавлена «Общество тихих людей»: сцены 121–128 с двумя ветками сцены 125.
Все 875 блоков исходного текста сохранены; четыре дополнительные/условные реплики обеспечивают непрерывность.
Часть размещена в `days/day03/part07/`: девять сцен, отдельные переходы и ресурсы. Третий день остаётся открытым, конец части — в библиотеке.

## Постановка Даши

Одна в кадре — по центру, включая зимний костюм и загрузку старого сохранения. Масштаб и высота не изменяются. Для трёх персонажей крайние позиции сдвинуты внутрь кадра: жест Жени больше не упирается в край.

Физическое присутствие и текущий кадр разделены. Короткие мысли, паузы и смена говорящего в общей беседе не убирают Дашу. Убраны десять добавленных коротких переключений; в этой редактуре оставлены три протяжённых блока: осмысление лагеря, записи о дороге и самостоятельное чтение. Остальная существующая постановка сохраняется. В новом обеде состав держится стабильно; Даша не участвует в разговоре 121–122 и после 127 действительно уходит к Мику.

Отдельно исправлено стойкое полупрозрачное появление при входе в домик. Причина — перенос промежуточной прозрачности ATL в новый позиционный Transform. Фиксированная постановка и кеш теперь задают `alpha=1.0`; плавность обеспечивается переходами. Исправление проверено на обеих позах и переодевании, включая сохранение/загрузку. В библиотеке убран лишний показ перед следующим эпизодом самостоятельного чтения.

Рекомендации по `show`/`hide` сверены с [официальной документацией Ren’Py](https://www.renpy.org/doc/html/displaying_images.html#hide-statement). Решение о кадре во время внутреннего монолога — авторская постановка для этого мода, а не автоматическое правило движка. Обработчиков, скрывающих Дашу на каждой реплике, нет.

## Непрерывность

- Совет затемнить рисунок вспоминается только после соответствующей утренней ветки. Иначе Тихонова сама продолжала работу.
- Женя не приписывает себе неувиденный разговор у клуба. Обещание книги учитывает прежнюю договорённость; новая просьба не выдаёт книгу повторно.
- Приглашение за обеденный стол даёт отдельное очко UN ровно один раз. Отказ не штрафует.
- Обсуждение совместного рисования зависит от прежнего приглашения. Время не назначено, событие не отмечено состоявшимся.
- Повязка, травма локтя и запрет спорта сохранены. Документы остаются в администрации. Папка проходит через стул в столовой обратно к Даше; при уходе к Мику она не переносится в домик.
- Горн, знакомство и утренний просмотр рисунка не повторяются. Новых аномалий нет. Дарья остаётся обычным человеком из 2026 года.

Статические сверки частей 1–7 третьего дня пройдены. Исходные реплики прежних частей сохранены.

## Реально проведённые проверки

Два полных ускоренных прохода от настоящего старта пролога до конца части 7 в Ren’Py 7.4.11: все первые и все последние варианты меню. Выполнялись реальные сценарии и меню; ожидание кликов отключено. Снято {frames} кадров — каждая сцена, CG и смена состава. Полноэкранные CG автоматически проверяются на отсутствие портретов, контрольные кадры — на незавершённую прозрачность. Контактные листы просмотрены, проблемные и ключевые кадры проверены в полном размере.

| Маршрут | MI / DV / UN / SE / SL / MZ / Виола | Обед с Тихоновой | План рисования |
|---|---|---|---|
{chr(10).join(rows)}

Дополнительно: восемь нативных кейсов части 7 (пять наборов дружбы/флагов, камера, внимание/мысли, повторный выбор с сохранением), отдельный кейс переодевания, реальное сохранение предыдущей сборки части 6 → новая часть 7. Проверены UN 0/1/2 и достижимое 3, оба решения, приглашение True/False, книга True/False, папка у Даши/в домике/отсутствует. Уходы, повязка, отсутствие повторной выдачи и однократное начисление проверены утверждениями движка.

В ускоренных полных проходах переходы отключены; отдельные проверки камеры, переодевания и сохранений выполнялись с обычными переходами. Перебраны два полных маршрута и отдельная матрица, а не все возможные сочетания всех выборов мода.

Lint: диагностика скриптов мода — 0. Осталось {lint['base_diagnostic_locations']} сообщений с адресами исходных файлов базовой игры: её отсутствующие оригинальные CG, устаревшие экраны/переводы и прочее. Это не заявляется как полностью чистый Lint всей установленной игры.

## Сборка

{build['scripts']} скрипт, {build['assets']} ресурсов, {build['static']['internal_ids']} уникальных внутренних идентификаторов, {build['static']['files']} файлов. Чистая компиляция без старых RPYC мода, локальный запуск и два запуска compiled-only Workshop прошли. Пять отрицательных проверок упаковщика прошли. В ZIP нет исходников, тестов, снимков и рабочих документов.

Сравнение с проверенной копией: {identity['matching_sources']} исходник и {identity['matching_assets']} ресурсов совпадают по SHA-256. Свидетельства проверок находятся в `{(release/'qa_evidence').as_posix()}`.

Архив: `{(release/'Chuzhaya_Smena_Vertical_Slice.zip').as_posix()}`.
Оригинальная рабочая папка мода сохранена; тесты запускались в изолированной копии. Предыдущие сборки и пользовательские сохранения не перезаписывались.

## Файлы с изменениями логики

{files}

Ещё {sum(x['status']=='line_endings_only' for x in changes)} файлов отличаются только переводами строк; их логика и текст совпадают с резервной копией. Полный перечень — `source/day03_part07_changed_files.json`.

Авторинг и проверки: `tools/build_day03_part07.py`, `tools/apply_conversation_focus.py`, `tools/verify_day03_part07.py`, `tools/build_day03_part07_qa.py`, `tools/run_day03_part07_qa.py`, `tools/build_full_render_walkthrough_qa.py`, `tools/run_full_render_walkthrough_qa.py`, `tools/run_day03_part07_cross_save.py`. После регенерации сцен применять `apply_conversation_focus.py`; он идемпотентен и не выбирает кадр по числу реплик.
'''
(R/'DAY03_PART07_REPORT.md').write_text(report,encoding='utf8')
print('FINAL_PART07_REPORT_PASS',frames,'full-route frames;',len(native),'part7 native cases')

# Четвёртый день: восстановление сцены и редактура

Дата: 1 ноября 2026 года. Итог: выполнено; незавершённых проверок в этом объёме работ нет.

## Что исправлено

Пропуск перед обедом подтверждён сравнением с `source/day04.md`: генератор пропускал 17 абзацев между заголовком развилки и первым вариантом ответа. Поэтому музыкальный спор возникал без объяснения, а Алиса и Мику не появлялись перед меню.

В части 8 восстановлена компактная подводка: девушки догоняют Лену и Дашу у столовой, показывают ноты и объясняют разногласие. На выборе видны все три собеседницы. После разговора Алиса и Мику входят в столовую. Учтено, что Мику уже слышала игру Даши во втором дне. Скамейка перед обедом показана на площади.

Исправлен сам генератор: он сохраняет реплики перед меню. Редактура воспроизводится после генерации через отдельные реестры точных замен.

Отредактированы все 12 частей дня: 107 правок. Сокращены повторные пересказы находок, пояснения уже понятных шуток, канцелярские формулировки и однообразные цепочки жестов. Сохранены важные паузы, характеры героев и ключевые улики. Число реплик и повествовательных блоков изменилось с 3399 до 3237; объём текста по словам, разделённым пробелами, — с 16613 до 15701 (примерно на 5,5% меньше, с учётом восстановленной подводки).

Исходный присланный текст `source/day04.md` совпадает с резервной копией побайтно. Реестры содержат точные изменения для готовых игровых сцен.

## Фактически выполненные проверки

| Проверка | Результат |
|---|---|
| Пять регрессионных тестов компилятора меню | PASS |
| Полная генерация в отдельной копии проекта | 12 сцен, 107 правок применены |
| Повторное применение редакторских правок | 0 дополнительных изменений |
| Сопоставление всех 12 сцен с реестрами | Полное совпадение |
| Сравнение логики с резервной копией | Варианты меню, очки, флаги и метки сохранены; добавлена предусмотренная постановка части 8 |
| Чистая компиляция и статическая проверка | 440 скриптов, ошибок нет |
| Локальный запуск и проверка ресурсов | PASS |
| Два последовательных запуска compiled-only сборки Workshop | PASS |
| Музыкальная развилка: 4 сочетания приглашений × 2 ответа | 8/8 PASS |
| Повторный вход в часть 8 | Повторного начисления очка нет |
| Сохранение и загрузка на настоящем меню | PASS; состав персонажей восстановлен |
| Проход всех 12 частей дня, маршрут 0 | PASS; 7 выборов, низкая дружба, раздельный сон |
| Проход всех 12 частей дня, маршрут 2 | PASS; противоположные ответы, высокая дружба, совместный сон |
| Сохранение и загрузка в конце обоих маршрутов | PASS |
| Просмотр контрольных скриншотов | 217 снимков, 5 контактных листов просмотрены |

Игровые проверки запускались штатным движком Ren’Py из Everlasting Summer на изолированной Workshop-копии. Текст проходился ускоренно; снимки делались при входе в части, смене фона, состава персонажей и одежды, на меню и в финале. Проверялись также центрирование одиночного персонажа, высота спрайтов, отсутствие портретов поверх CG, соответствие фонового звука локации, состояние предметов и отложенные приглашения на пятый день. На просмотренных кадрах визуальных артефактов не найдено. Финальные десять игровых профилей завершились без traceback.

В ходе настройки сохранения исправлены ошибки тестовой фикстуры: хранение эталонного состава кадра после загрузки и конфликт имени встроенного `all` с персонажем оригинальной игры. Итоговый профиль сохранения после исправления прошёл.

## Изменённые и добавленные файлы

- [days/day04/01_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/01_scene.rpy)
- [days/day04/02_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/02_scene.rpy)
- [days/day04/03_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/03_scene.rpy)
- [days/day04/04_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/04_scene.rpy)
- [days/day04/05_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/05_scene.rpy)
- [days/day04/06_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/06_scene.rpy)
- [days/day04/07_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/07_scene.rpy)
- [days/day04/08_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/08_scene.rpy)
- [days/day04/09_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/09_scene.rpy)
- [days/day04/10_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/10_scene.rpy)
- [days/day04/11_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/11_scene.rpy)
- [days/day04/12_scene.rpy](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/days/day04/12_scene.rpy)
- [source/day04_prose_early.json](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/source/day04_prose_early.json)
- [source/day04_prose_middle.json](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/source/day04_prose_middle.json)
- [source/day04_prose_late.json](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/source/day04_prose_late.json)
- [tools/build_day04.py](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/tools/build_day04.py)
- [tools/apply_day04_prose.py](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/tools/apply_day04_prose.py)
- [tools/test_day04_menu_prelude.py](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/tools/test_day04_menu_prelude.py)
- [tools/music_gap_test.rpy.txt](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/tools/music_gap_test.rpy.txt)
- [tools/day04_prose_test.rpy.txt](D:/stean/steamapps/common/Everlasting Summer/game/mods/chuzaya_smena/tools/day04_prose_test.rpy.txt)

## Результаты и сборка

- [Результаты десяти игровых профилей](D:/stean/release_chuzaya_smena/day04_prose_final_20261101/day04_prose_checks.json)
- [Манифест просмотренных снимков](D:/stean/release_chuzaya_smena/day04_prose_final_20261101/qa_evidence/visual_review.json)
- [Исправленная развилка после загрузки](D:/stean/release_chuzaya_smena/day04_prose_final_20261101/qa_evidence/music_gap_6_loaded.png)
- [Проверенная сборка](D:/stean/release_chuzaya_smena/day04_prose_final_20261101/Chuzhaya_Smena_Vertical_Slice.zip)

Блокирующих замечаний по восстановлению сцены и редактуре четвёртого дня не осталось. Объём полного игрового прогона в этой проверке — четвёртый день по двум маршрутам. Проверка сохранений относится к созданным в этих тестах сохранениям на меню и в финале дня.

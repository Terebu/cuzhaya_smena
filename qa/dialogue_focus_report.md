# Диалоги и визуальный фокус — 17 октября 2026

ТЗ: `source/editorial_staging_spec.md` и `source/reflective_shots_spec.md`. Принцип: собеседники видны на протяжении разговора и коротких реакций; самостоятельные действия/монологи и уходы имеют явные границы кадра. Ни один runtime callback production не решает видимость по имени говорящего или числу строк.

Найдены пять эпизодов с пропусками говорящих (42 потенциальные реплики по независимому поиску): утро перед пробежкой, возвращение с пробежки, разговоры около игры Даши на пианино, вопрос Дарьи после осмотра газет, ранний вопрос Семёна в клубе. Возврат из старого газетного POV ошибочно восстанавливал пустой состав.

Дополнительно исправлены: Дарья на наружном фоне до входа в домик; четыре портрета в трёх групповых эпизодах; отдельные завершения общения/уходы; Женя за чужим столом при отказе в компании; отсутствие общего выхода из рефлексивного кадра ужина в ветке нулевой дружбы.

Внесено 37 проверенных постановочных правок/уточнений по точным репликам; текущий общий план содержит 155 событий. Это число режиссёрских команд, а не число сюжетных ошибок. Все теги/эмоции взяты из реальных регистраций. PNG не изменялись.

Примеры до/после:

- День 2, сцена 02: сонный разговор с пустым экраном → обычный портрет Дарьи; нейтральная/мягкая/тревожная реакции без изменения размера и позиции. После ухода Лены из домика портрет убирается.
- День 2, сцена 07: Дарья на крыльце, затем пустой интерьер при разговоре → пустое крыльцо, Дарья появляется внутри при обращении к ней; после разговора зеркальный POV снова без портрета.
- День 2, сцена 18: только Мику до CG, затем пропавшая Даша → обе участницы обычного разговора видны, CG остаётся чистым, после него возвращаются обе.
- День 1, сцена 56: вопрос Дарьи без спрайта → Дарья возвращается из газетного POV. Женя подключается, когда поднимает голову и вступает в разговор.
- День 2, сцена 64: при нулевой дружбе девушки сидят отдельно от Жени, после самостоятельных мыслей есть общий возврат к Даше для всех вариантов.

Изменённые сценарии (19 RPY):

- `days/day01/11_state_machine.rpy`
- `days/day01/19_dining_hall.rpy`
- `days/day01/part07/39_future_in_pocket.rpy`
- `days/day01/part09/48_b_pass.rpy`
- `days/day01/part10/56_old_books.rpy`
- `days/day01/part11/61_scene.rpy`
- `days/day01/part11/64_scene.rpy`
- `days/day02/part01/02_scene.rpy`
- `days/day02/part01/06_scene.rpy`
- `days/day02/part01/07_scene.rpy`
- `days/day02/part02/18_scene.rpy`
- `days/day02/part04/26_scene.rpy`
- `days/day02/part05/37_scene.rpy`
- `days/day02/part06/44_scene.rpy`
- `days/day02/part09/64_c_scene.rpy`
- `days/day02/part09/64_e_scene.rpy`
- `days/day02/part09/65_scene.rpy`
- `days/prologue/03_stranger.rpy`
- `days/prologue/04_instagram.rpy`

Полный список всех 207 проверенных RPY и независимая сверка реплик/условий/счётчиков — `qa/dialogue_independent_audit.json`. Нет изменений сюжета, реплик и начисления дружбы.

Все новые границы, возвраты и эмоции:

| Файл | Точная точка | Действие/смысл |
| --- | --- | --- |
| `days/day02/part01/02_scene.rpy` | Вернулась к кровати Дарьи. | Face-to-face before the run; lying down does not hide Darya |
| `days/day02/part01/02_scene.rpy` | Она слегка улыбнулась, не открывая глаз. | Sleepy smile during continuous dialogue |
| `days/day02/part01/02_scene.rpy` | Только не уходи за территорию лагеря одна. | Serious warning in the waking dialogue |
| `days/day02/part01/02_scene.rpy` | Я закрыла дверь настолько осторожно, насколько позволяли старые петли. | Lena leaves the cabin; Darya stays inside |
| `days/day02/part01/07_scene.rpy` | Дарья всё ещё лежала, но уже не спала. | Return indoors: Darya participates despite lying down |
| `days/day02/part01/07_scene.rpy` | Дарья тихо рассмеялась. | Warm reaction during the uninterrupted morning conversation |
| `days/day02/part01/07_scene.rpy` | Её улыбка исчезла. | Bus disappearance is a serious subject |
| `days/day02/part01/07_scene.rpy` | Хороший план. | Morning plans agreed |
| `days/day02/part01/07_scene.rpy` | Я посмотрела на своё отражение в небольшом зеркале. | Mirror focus after the conversation |
| `days/day02/part02/18_scene.rpy` | Мелодия закончилась негромким аккордом. | Return from piano CG to both interlocutors |
| `days/day01/part10/56_old_books.rpy` | Ну что? | Return to direct interaction: Checking publication dates |
| `days/day01/part10/56_old_books.rpy` | Женя подняла взгляд. | Librarian rejoins the conversation |
| `days/day02/part04/26_scene.rpy` | Семён заглянул через моё плечо. | Semen joins the technical question |
| `days/day02/part04/26_scene.rpy` | Дарья подошла к столу. | Reverse shot for Darya, Shurik and Semen |
| `days/day02/part04/26_scene.rpy` | Я посмотрела на телефон. | Phone inspection after the technical discussion |
| `days/day02/part04/26_scene.rpy` | Ладно. Торопиться не будем. | Return to engineers and Darya |
| `days/day02/part04/26_scene.rpy` | Семён вспомнил об объявлении. | Companions plan the next errand |
| `days/day02/part01/06_scene.rpy` | Я продолжила путь. | Lena leaves Semen on the camp path |
| `days/day01/part11/61_scene.rpy` | Мы улыбнулись друг другу. Продолжать разговор только ради того, чтобы он не закончился, было уже необязательно. | Tikhonova farewell at the branch of the paths |
| `days/day01/part11/64_scene.rpy` | Я всё ещё не понимала, где мы оказались и что будет дальше. Но рубашка лежала на стуле, дверь была закрыта, а рядом спал человек, с которым утром предстояло идти в столовую. | Final private thought after goodnight |
| `days/day01/11_state_machine.rpy` | И только сейчас, когда появилась хотя бы минута ничего не делать, мозг начал нормально переваривать происходящее. | Private reflection before the next topic |
| `days/day01/part07/39_future_in_pocket.rpy` | Молодец, Лена. | Independent recap after the electronics errand |
| `days/day01/part09/48_b_pass.rpy` | Я поправила галстук. | Independent reflection after declining the acquaintance |
| `days/day02/part09/65_scene.rpy` | Впереди уже собирались остальные зрители. | Conversation ended; attention turns to the stage |
| `days/prologue/03_stranger.rpy` | Я отвернулась к окну. | Attention turns from the stranger to the bus window |
| `days/prologue/04_instagram.rpy` | На этом наша социальная активность закончилась. | The brief conversation is over |
| `days/day01/19_dining_hall.rpy` | Она стояла возле стены и о чём-то разговаривала с девочкой заметно ниже ростом. | Focus on the girls outside the canteen |
| `days/day01/19_dining_hall.rpy` | Девочки! В столовую, обедать! | Return to the counsellor calling the newcomers |
| `days/day02/part04/26_scene.rpy` | Шурик нахмурился. | Keep the technical reverse shot limited to three |
| `days/day02/part05/37_scene.rpy` | В этот момент мимо площади проходила Виола. | Viola and Darya conversation; others remain offscreen |
| `days/day02/part05/37_scene.rpy` | Она попрощалась и продолжила путь. | Farewell frame before the actual departure |
| `days/day02/part05/37_scene.rpy` | Семён тем временем собрал оставшиеся материалы. | Return to the group after Viola leaves |
| `days/day02/part04/26_scene.rpy` | Дарья посмотрела на меня. | Darya concludes the technical conversation; Semen listens offscreen |
| `days/day02/part09/64_c_scene.rpy` | Мы отошли к свободному столику возле окна. | Girls choose a separate table; Zhenya remains at her own table |
| `days/day02/part09/64_e_scene.rpy` | Дарья аккуратно помогла мне поднять поднос. | Common dialogue return after both dinner branches |
| `days/day01/part10/56_old_books.rpy` | Я посмотрела на Дарью. | Return to direct interaction: Book dates and shelf focus |
| `days/day01/part10/56_old_books.rpy` | Женя подняла голову. | Zhenya looks up and joins the book conversation |

QA дополнена независимой проверкой видимости говорящего и максимумом трёх портретов. Проверенные голоса из-за двери, издали и общие объявления — `source/offscreen_dialogue.json` (11 строк). Это не автоматическое разрешение скрывать собеседника.

Статическая диагностика после постановки: 186 файлов с диалогами, 0 непроверенных пропусков говорящего, 0 кандидатов на переполненный кадр.

Нативные результаты приведены ниже; проверка завершена 17 октября 2026.

Дополнительная коррекция эмоций: в `days/day02/part06/44_scene.rpy` две улыбки/V заменены на `thinking` в серьёзном обсуждении повторного опыта на дороге. Дистанция, положение и масштаб сохранены.

`cs_dialogue_focus` — PASS: обычные портреты в утреннем лежачем диалоге, пустое крыльцо, две участницы после CG, возврат из газетного POV, сохранение/загрузка и неизменность границ спрайта при смене эмоции.

`cs_dialogue_branch_matrix` — PASS: 11 вариантов (Тихонова 0/1, чтение с Женей 0/1/2, ужин 0/1/2 и отдельный флаг каталогов, концерт без/с дополнительными дружескими разговорами). 485 проверок видимости говорящих; во всех вариантах дружеские очки сохранились. Save/load выполнены до и после четырёх выбранных условных эпизодов. Это проверка исходов соответствующих условий, не полный декартов перебор всех игровых флагов.


Итоговые нативные проверки:

| Проверка | Результат |
| --- | --- |
| `cs_full_mod_staging` | PASS, exit 0; полностью от пролога до `cs_day02_complete`, свежий маркер 17 октября, 01:16:57 |
| Контроль отображения в полном проходе | 11246 проверок реплик; 1970 проверок говорящего; 458 рефлексивных проверок; 471 проверок CG; 0 ошибок |
| `cs_dialogue_branch_matrix` | PASS, exit 0; 11 вариантов, 485 проверок говорящих, дружба сохранена; save/load до и после выбранных ветвей |
| `cs_dialogue_night_and_road` | PASS, exit 0; ночной лежачий разговор, отдельная заключительная мысль, серьёзные выражения на дороге в far/normal |
| `cs_mod_image_registry` | PASS, exit 0; 192 изображения и 30 аудиопутей, отсутствующих ресурсов нет |
| Сверка исходного текста и логики | PASS; 207 RPY проверены, 19 изменены, реплики/условия/начисления не изменены |
| Повторная постановка | Идентичный результат, без накопления директив |
| Ren’Py Lint | exit 0; новых ошибок сценариев мода нет |

Lint не пустой: остаются прежние предупреждения установленной базовой игры и два предупреждения о не-ASCII именах старых файлов мода (`Пусть_часы_молчат.mp3`, `сп_ьфыл_oni.png`). Полный вывод — `qa/lint_dialogue_focus.txt`. Используемые ресурсы мода доступны по нативной проверке.

Визуально просмотрены свежие игровые PNG: `dialogue_morning_sleepy`, `dialogue_morning_return`, `dialogue_piano_dialogue`, `dialogue_library_return`, `dialogue_full_exterior`, `dialogue_full_returned`, `dialogue_full_piano_return`, `dialogue_branch_dinner_zero_separate`, `dialogue_branch_day1_tikhonova_1`, `dialogue_branch_concert_1`, `dialogue_branch_dinner_2_map_1`, `dialogue_day1_lying_conversation`, `dialogue_day1_final_private`, `dialogue_road_serious_far`, `dialogue_road_serious_normal`, `global_latest_end`.

По этим кадрам: собеседники видны, пустые планы не содержат лишних портретов, сидение/лежание не опускает персонажа, домик остаётся в масштабе 1.0, при смене эмоций нет дублирования. Ключевые сохранения загружены нативно. Неисправленных проблем, требующих новых изображений, в проверенных эпизодах не обнаружено.

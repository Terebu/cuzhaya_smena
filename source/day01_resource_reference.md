Для твоего мода «Бесконечное лето: Чужая смена» нашёл исходные определения ресурсов оригинальной игры, каталог спрайтов и специальные справочники для мододелов.

Самое удобное — использовать оригинальные BG, CG, музыку, эмбиент и SFX непосредственно через идентификаторы Ren'Py. Тогда не придётся дублировать сотни файлов в папке своего мода.

## 1. Основные источники ресурсов

[Славя бесконечное лето скриншоты - фото и картинки abrakadabra.fun](https://images.openai.com/static-rsc-4/jC_Re5rfFJSDGi_qfjh7pxA9wLSkubsENlXxvED_SIInvynZPFGRGOJa3S9nIcXhMVlzOqxYAWLSD90CQy1mxOwx-Gmkt096RO781ZxSwLONbykd9uXBOpbiFQYNv7_-Jj6Qvl1ROoht74b0wKJPIid1kEm4LFsKhTbmRLMo-SE?purpose=inline)

[resources.rpy — оригинальные ресурсы](https://github.com/IGRINI/decompile_everlasting_summer_all/blob/master/resources.rpy)

Главный справочник: 838 строк объявлений фонов, CG, музыки, эмбиентов и звуков. Содержит точные пути и идентификаторы для сценария.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



[Славя бесконечное лето скриншоты - фото и картинки abrakadabra.fun](https://images.openai.com/static-rsc-4/jFZpQRArw2thtx-vPIOqelYnPVVoGbiC4EIy5ngSZSoNscFO9jFbD5_A99rg6hlZbSsmU94j3-LNbW17ikdiWAhBwuDVGmkmuAbj7GeKtq1_p43Pj9b1Wign4nC5_YuyOf-GPJMukwnv_99esbmE_SStvmu-ANCkv-XzBPe-8FM?purpose=inline)

[sprites.rpy — все объявления спрайтов](https://github.com/IGRINI/decompile_everlasting_summer_all/blob/master/sprites.rpy)

Большой файл на 4492 строки: вариации персонажей, эмоции, костюмы, размеры и преобразования.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



[Everlasting Summer Screenshots · SteamDB](https://images.openai.com/static-rsc-4/RAs2tdZtIr3Xjf_DuiJ6oMCFKF46zucYfSfr3Q2LL2X__d5QNVXH99Gw80aRdvwqj_LCJvl0-VLfd5rP5-ptX59SY0-biXIYSNbY7ivXy9E6pE313bU7R3W2C2YQmiMx6jgXRPNAFZX-8DWgq_aaa8-nLeWnghR7R9bPvwh3wSc?purpose=inline)

[Support Lists for Modders — Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=833875151)

Специальный справочник с каталогами BG, CG, спрайтов, анимаций и аудио. Для игры версии 1.2 предусмотрен `lists1.2.rar`.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://steamcommunity.com\&sz=32)

Steam Community



[Прототип лагеря совенок - Zefirka.club фото и картинки](https://images.openai.com/static-rsc-4/MI6iMTNWV7Lv_KWC7FkDzaxW4DpP02JfCERr2WZ-rYCUC5kSXVoi6nGItzIpIbnJitGjCn-m7HB1hg95frrvnGXl7HbsNrRD7AHh20MqGNSI5z0Yl5ftH_6-X_xJTQ32TDlhVmt64XDA7nxXojZDAC0IwjhIynj5vo0pxrJwrSA?purpose=inline)

[Руководство по созданию мода — Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=2483357582)

Русскоязычное руководство со справочными файлами для локаций, CG, музыки, звуков, эмбиентов и спрайтов.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://steamcommunity.com\&sz=32)

Steam Community



## 2. Стандартные ресурсы по категориям

| Тип      | Путь внутри игры   | Использование                      |
| -------- | ------------------ | ---------------------------------- |
| BG       | `images/bg/`       | Фоны помещений и улиц              |
| CG       | `images/cg/`       | Полноэкранные сюжетные иллюстрации |
| Sprites  | `images/sprites/`  | Персонажи, эмоции, костюмы         |
| Misc     | `images/misc/`     | UI, предметы, служебная графика    |
| Music    | `sound/music/`     | Фоновая музыка                     |
| Ambience | `sound/ambiences/` | Шум леса, лагеря, помещений        |
| SFX      | `sound/sfx/`       | Двери, шаги, удары и события       |

Это пути внутри файловой системы Ren'Py. Физически содержимое может находиться в `.rpa`-архивах установленной игры.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



## 3. Оригинальные фоны (BG)

Вот подтверждённые идентификаторы из `resources.rpy`, которые особенно пригодятся в первой главе «Чужой смены».

| Локация               | Имя для Ren'Py              |
| --------------------- | --------------------------- |
| Остановка             | `bg bus_stop`               |
| Салон автобуса        | `bg int_bus`                |
| Ночной автобус        | `bg int_bus_night`          |
| Автобус с пассажирами | `bg int_bus_people_day`     |
| Ворота лагеря         | `bg ext_camp_entrance_day`  |
| Центральная площадь   | `bg ext_square_day`         |
| Ночная площадь        | `bg ext_square_night`       |
| Столовая              | `bg int_dining_hall_day`    |
| Домик вожатой         | `bg int_house_of_mt_day`    |
| Библиотека            | `bg int_library_day`        |
| Катакомбы             | `bg int_catacombs_entrance` |
| Подземный коридор     | `bg int_catacombs_door`     |

Все эти имена следует дополнительно сверить с файлами конкретной установленной версии игры.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

+1



Например:

```

scene bg ext_camp_entrance_day
with dissolve

"Перед нами стояли ворота лагеря «Совёнок»."

```

## 4. Стандартные персонажи и спрайты

| Персонаж          | ID   | Пример              |
| ----------------- | ---- | ------------------- |
| Славя             | `sl` | `sl normal pioneer` |
| Оригинальная Лена | `un` | `un shy pioneer`    |
| Алиса             | `dv` | `dv smile pioneer`  |
| Ульяна            | `us` | `us grin pioneer`   |
| Мику              | `mi` | `mi normal pioneer` |
| Ольга Дмитриевна  | `mt` | `mt normal pioneer` |
| Виола             | `cs` | `cs normal`         |
| Электроник        | `el` | `el normal pioneer` |
| Шурик             | `sh` | `sh normal pioneer` |

Образцы синтаксиса; точные комбинации эмоций и костюмов проверяй в [sprites.rpy](https://github.com/IGRINI/decompile_everlasting_summer_all/blob/master/sprites.rpy).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



Для появления Слави:

```

scene bg ext_camp_entrance_day
with dissolve

show sl normal pioneer at center
with dissolve

sl "Ой! Привет! Вы, наверное, только приехали?"

```

Лену Соколову в своём моде лучше по-прежнему обозначать отдельным `cs_lena`, чтобы не путать её с оригинальной `un`.

## 5. Оригинальные эмбиенты

Лес, день

`ambience_forest_day`

&#x20;Копировать

Лес, вечер

`ambience_forest_evening`

Лес, ночь

`ambience_forest_night`

Вход в лагерь, день

`ambience_camp_entrance_day`

Центр лагеря, день

`ambience_camp_center_day`

Пустая столовая

`ambience_dining_hall_empty`

Столовая с людьми

`ambience_dining_hall_full`

Катакомбы

`ambience_catacombs`

Холодный ветер

`ambience_cold_wind_loop`

Все перечисленные имена присутствуют в определениях ресурсов.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



Пример:

```

scene bg ext_camp_entrance_day
with dissolve

play ambience ambience_camp_entrance_day fadein 2.0

"За воротами слышались голоса пионеров."

```

## 6. Музыка и SFX

Из оригинальных композиций для твоей истории я бы начал с таких:

| Музыка                      | Идентификатор                 | Где попробовать           |
| --------------------------- | ----------------------------- | ------------------------- |
| 410                         | `410`                         | Автобус, загадка          |
| A Promise from Distant Days | `a_promise_from_distant_days` | Спокойные моменты         |
| Into the Unknown            | `into_the_unknown`            | Исследование неизвестного |
| Just Think                  | `just_think`                  | Размышления Лены          |
| Door to Nightmare           | `door_to_nightmare`           | Тревожные сцены           |
| Everyday Theme              | `everyday_theme`              | Бытовые сцены             |
| Sunny Day                   | `sunny_day`                   | Жизнь лагеря              |
| Timid Girl                  | `timid_girl`                  | Тихие разговоры           |

Это редакторские предложения по настроению, а не официальное назначение треков. Идентификаторы подтверждаются исходными объявлениями.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



```

play music music_list["into_the_unknown"] fadein 2.0

```

Полезные звуковые эффекты:

| Действие                     | Идентификатор          |
| ---------------------------- | ---------------------- |
| Открытие металлической двери | `sfx_open_metal_door`  |
| Открытие люка                | `sfx_open_metal_hatch` |
| Бег по лесу                  | `sfx_run_forest`       |
| Скрип кровати                | `sfx_bed_squeak1`      |
| Отдалённая сова              | `sfx_owl_far`          |
| Резкий тревожный акцент      | `sfx_scary_sting`      |
| Удар тела                    | `sfx_body_bump`        |

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

## 7. Где взять оригинальные файлы

Если нужны не только объявления в коде, но и исходные изображения и `.ogg`, рекомендую начинать с собственной установленной копии игры.

Самый удобный путь к справочнику версии 1.2 через Steam Workshop:

```

Steam/
└── steamapps/
    └── workshop/
        └── content/
            └── 331470/
                └── 833875151/
                    └── lists1.2.rar

```

Этот путь приведён автором справочного мода.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://steamcommunity.com\&sz=32)

Steam Community



Для непосредственной работы с ресурсами можно ориентироваться на [ES Doc Assets](https://github.com/sovue/es-doc-assets) — каталог документации, но не гарантированный полный архив игровых ассетов. Обращай внимание на лицензии: игровые материалы Soviet Games распространяются на условиях CC BY-NC-SA.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

sovue/es-doc-assets · GitHub



## 8. Что рекомендую конкретно для следующей главы «Чужой смены»

Теперь, когда Лена Соколова и Дарья встретили Славю у ворот, тебе не нужно рисовать абсолютно все локации заново.

Я бы использовал стандартные ресурсы для лагеря 1980-х, а собственные — только там, где твоя история отходит от оригинала: зимняя Москва 2026 года, современный автобус № 410, комната Лены, спрайты обеих девушек и совместные CG.

Так ты сохранишь узнаваемую визуальную стилистику «Бесконечного лета», но при этом у «Чужой смены» останется собственное лицо.

В частности, для следующей сцены уже есть всё основное: `bg ext_camp_entrance_day`, спрайт `sl normal pioneer`, `ambience_camp_entrance_day` и оригинальная музыка.

Полный реестр без сокращений бери из `resources.rpy` и `sprites.rpy`: они заметно удобнее, чем искать каждую переменную по отдельности.
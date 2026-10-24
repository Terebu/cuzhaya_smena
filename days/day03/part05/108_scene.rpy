# -*- coding: utf-8 -*-
label cs_day03_108:
    $ save_name = "Чужая смена — День 3: Славя и бумажная катастрофа"
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_108:
    cs_narrator "Славя обнаружилась возле клубов."
    cs_narrator "На столе перед ней лежали несколько листов."
    cs_narrator "Рядом стояли две коробки с оставшимися после концерта украшениями."
    cs_narrator "Чуть поодаль была сложена стопка деревянных планок."
    cs_narrator "Судя по всему, хозяйственная деятельность, которую я застала ранним утром, имела значительно больше этапов, чем предполагалось."
    cs_narrator "Славя подняла голову."
    cs_narrator "Увидела нас."
    cs_narrator "И улыбнулась."
    cs_sl "О, Лена! Даша! Доброе утро ещё раз!"
    cs_narrator "Я остановилась рядом."
    cs_ls "Доброе. Хотя при твоём расписании это уже, наверное, середина рабочего дня."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_sl "Почти."
    cs_narrator "Дарья посмотрела на бумаги."
    cs_da "Ольга Дмитриевна сказала, что тебе может понадобиться помощь."
    if renpy.showing("sl"):
        show sl surprise pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя немного удивилась."
    cs_sl "Правда?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Мы уже доставили документы в администрацию. Теперь прибыли выяснить, чем можно облегчить жизнь лагерного хозяйства."
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя улыбнулась."
    cs_sl "Спасибо. Вообще-то здесь осталось совсем немного."
    cs_narrator "Я посмотрела на стол."
    cs_narrator "На стопку листов."
    cs_narrator "На коробки."
    cs_narrator "Потом снова на неё."
    cs_ls "Славя, у нас с тобой несколько разные представления о слове «немного»."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_sl "Большую часть уже убрали. Нужно только сверить список и проверить, всё ли вернулось на место."
    cs_narrator "Я посмотрела на свою повязку."
    cs_ls "Только давай сразу договоримся: тяжелее карандаша мне сегодня ничего поднимать нельзя."
    if renpy.showing("sl"):
        show sl normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя кивнула."
    cs_sl "Конечно. Я помню про руку."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Она сегодня очень дисциплинированная."
    cs_narrator "Я повернулась к ней."
    cs_ls "Прошу не распространять слухи. Иначе завтра от меня будут ожидать невозможного."
    cs_narrator "Обе рассмеялись."
    cs_narrator "Славя аккуратно расправила лист."
    cs_sl "Тут просто нужно пересчитать то, что осталось после вчерашнего выступления."
    cs_narrator "Я посмотрела на список."
    cs_narrator "Разноцветные ленты."
    cs_narrator "Крепления."
    cs_narrator "Бумажные украшения."
    cs_narrator "Несколько деревянных подставок."
    cs_th "М-да."
    cs_th "Чтобы провести один музыкальный вечер, оказывается, требуется почти полноценная система материально-технического обеспечения."
    cs_ls "Слушай, а ты уверена, что не собираешься потом открыть собственную организацию?"
    cs_narrator "Славя посмотрела на меня."
    cs_sl "Почему?"
    cs_narrator "Я указала на список."
    cs_ls "У тебя уже есть учёт, имущество, отчётность и добровольные сотрудники."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_sl "Не хватает только начальника."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Вот уж с этим проблем точно не будет."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Она тебя имеет в виду."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя засмеялась."
    cs_sl "Тогда боюсь, у меня станет ещё больше работы."
    cs_narrator "Я приложила здоровую ладонь к груди."
    cs_ls "Неприятно, когда тебя настолько хорошо изучили за два дня."
    return

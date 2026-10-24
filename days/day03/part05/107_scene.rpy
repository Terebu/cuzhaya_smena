# -*- coding: utf-8 -*-
label cs_day03_107:
    $ save_name = "Чужая смена — День 3: Делопроизводство"
    $ cs_director_scene("cs_ext_administration_day")
    scene cs_ext_administration_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_107_exterior:
    cs_narrator "Мы поднялись на крыльцо административного корпуса."
    $ cs_director_scene("cs_int_administration_day")
    scene cs_int_administration_day
    with Dissolve(0.8)
    $ renpy.music.set_volume(0.07,delay=0.5,channel="ambience")
    label cs_check_day03_107_administration:
    cs_narrator "Административное помещение оказалось совсем не таким, каким я его себе представляла."
    cs_narrator "Никаких бесконечных коридоров."
    cs_narrator "Никаких секретарей с выражением лиц, говорящим: «Сначала принесите справку о наличии справки»."
    cs_narrator "Всего несколько столов."
    cs_narrator "Шкафы с папками."
    cs_narrator "Доска объявлений."
    cs_narrator "И человек, который, судя по всему, уже привык получать документы от самых разных жителей лагеря."
    $ cs_day03_documents_location = "administration"
    $ cs_day03_documents_delivered = True
    label cs_check_day03_107_delivered:
    cs_narrator "Дарья передала папку."
    cs_narrator "Я назвала Ольгу Дмитриевну."
    cs_narrator "Дежурный проверил бумаги, пролистал верхний лист и кивнул."
    cs_narrator "— Всё верно. Передайте Ольге Дмитриевне, что получили."
    cs_ls "Хорошо."
    $ cs_director_scene("cs_ext_administration_day")
    scene cs_ext_administration_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ renpy.music.set_volume(0.18,delay=1.0,channel="ambience")
    label cs_check_day03_107_back:
    cs_narrator "Мы вышли обратно на дорожку."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Ну вот."
    cs_da "Что?"
    cs_narrator "Я торжественно выпрямилась."
    cs_ls "Первое государственное поручение выполнено."
    cs_narrator "Она улыбнулась."
    cs_da "Справилась?"
    cs_narrator "Я задумалась."
    cs_ls "Даже подозрительно легко. Никто не потребовал дополнительное удостоверение личности, три копии заявления и подпись начальника отдела."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Ты разочарована?"
    cs_ls "Немного. У меня был целый запас саркастических замечаний о бюрократии."
    cs_narrator "Она улыбнулась."
    cs_da "Придётся оставить на другой раз."
    cs_narrator "Я кивнула."
    cs_ls "Да. Нельзя расходовать всё за одно утро."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы направились к клубам."
    cs_narrator "Оттуда как раз было удобно пройти к месту, где Славя разбирала оставшийся после концерта инвентарь."
    cs_th "Что ж."
    cs_th "Половина поручения выполнена."
    cs_th "Осталось выяснить, не поручат ли нам теперь построить новый корпус лагеря."
    return

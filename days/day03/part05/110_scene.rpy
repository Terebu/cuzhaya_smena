# -*- coding: utf-8 -*-
label cs_day03_110:
    $ save_name = "Чужая смена — День 3: Первый сувенир"
    if cs_sl_poster_saved_day3 and not cs_sl_poster_collected_day3:
        cs_narrator "Мы уже собирались уходить, когда Славя вдруг остановилась."
        cs_sl "Лена, подожди!"
        cs_narrator "Я повернулась."
        cs_ls "Да?"
        cs_narrator "Она указала на папку, лежавшую отдельно от остальных вещей."
        cs_sl "Я же обещала отдать вам ваш плакат."
        cs_narrator "Я удивлённо улыбнулась."
        cs_ls "Точно."
        cs_narrator "Славя осторожно открыла папку."
        cs_narrator "Достала знакомый лист."
        cs_narrator "Наш вчерашний рисунок сохранился почти без повреждений."
        cs_narrator "Только один угол немного загнулся."
        cs_narrator "Я посмотрела на него."
        cs_th "Надо же."
        cs_th "Вчера мы втроём сидели за столом и спорили о том, где разместить заголовок."
        cs_th "А сегодня этот лист уже выглядит как воспоминание о чём-то, что случилось давно."
        cs_narrator "Славя протянула папку Дарье."
        cs_sl "Держите. Так он не помнётся."
        $ cs_sl_poster_collected_day3 = True
        $ cs_day03_poster_location = "darya_folder"
        label cs_check_day03_110_poster_received:
        cs_narrator "Дарья осторожно взяла её."
        cs_da "Спасибо, Славя."
        cs_narrator "Я тоже улыбнулась."
        cs_ls "Правда, спасибо."
        cs_narrator "Она кивнула."
        cs_sl "Вы хорошо поработали. Было бы жалко выбрасывать."
        cs_narrator "Я посмотрела на плакат."
        cs_ls "Теперь у нас есть первый официальный сувенир из лагеря."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "Главное, потом его не потерять."
        cs_narrator "Я кивнула."
        cs_ls "Положим в домике. Подальше от моих попыток навести творческий порядок."
        if renpy.showing("sl"):
            show sl laugh pioneer
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Славя рассмеялась."
        cs_sl "Только не сворачивайте сильно."
        cs_da "Не будем."
        cs_narrator "Я посмотрела на рисунок ещё раз."
        cs_th "Забавная вещь."
        cs_th "Этот плакат совершенно ничего не объяснял о том, как мы здесь оказались."
        cs_th "Зато напоминал, что вчера у нас действительно был хороший вечер."
        cs_th "И, пожалуй, это тоже стоило сохранить."
    else:
        cs_narrator "Славя поправила список."
        cs_sl "Ладно, спасибо, что заглянули."
        cs_narrator "Я кивнула."
        cs_ls "Не за что."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_narrator "Мы попрощались."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_110_sl_left:
    cs_narrator "Я отошла от стола."
    cs_narrator "Посмотрела на часы."
    cs_th "Так."
    cs_th "День всё ещё только начинается."
    cs_th "А я уже успела сходить к врачу, получить официальное поручение и познакомиться с тонкостями хозяйственного учёта."
    cs_th "Если продолжу в таком темпе, к вечеру начну требовать трудовую книжку."
    cs_narrator "Дарья шла рядом."
    cs_da "Ты довольна?"
    cs_narrator "Я повернулась."
    cs_ls "Вполне."
    cs_da "Даже несмотря на то, что почти всё утро мы занимались чужими делами?"
    cs_narrator "Я задумалась."
    cs_ls "Знаешь, мне это даже понравилось."
    cs_narrator "Она улыбнулась."
    cs_da "Правда?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Вчера мы пытались понять, почему дорога не выпускает нас из лагеря."
    cs_narrator "Немного помолчала."
    if cs_helped_sl_day3:
        cs_ls "А сегодня хотя бы понятно, зачем нужно пересчитать шесть красных лент."
    else:
        cs_ls "А сегодня хотя бы понятно, зачем нужно отнести документы в администрацию."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Действительно. Очень приятная определённость."
    cs_narrator "Я улыбнулась."
    cs_ls "Именно."
    cs_narrator "Мы направились обратно к центральной дорожке."
    label cs_check_day03_110_result:
    return

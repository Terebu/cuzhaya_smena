# -*- coding: utf-8 -*-
label cs_day04_05:
    $ save_name = "Чужая смена — День 4: Переодевание и вопросы"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    show cs_darya neutral sport normal at cs_darya_normal_right
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "До нашего домика мы дошли втроём."
    cs_narrator "Семён поглядывал на папку у меня в руках. Даша шла впереди и то и дело оборачивалась — проверяла, не исчезла ли я снова."
    cs_narrator "После убежища я её не винила."
    cs_narrator "Возле крыльца я остановилась и внимательно осмотрела собственную одежду."
    cs_narrator "Картина была печальной."
    cs_narrator "Колени в земле, футболка в пыли. Кроссовки как после болотного марафона."
    cs_narrator "Я подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Мне нужно переодеться."
    cs_narrator "Семён окинул меня взглядом."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Давно пора."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка, ты сейчас очень опасно приблизился к комментарию о моей внешности."
    cs_narrator "Он показал на мои колени."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "У тебя грязь даже на шнурках."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Это художественный элемент образа."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Тогда художнику пора умыться."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А ведь ещё пять минут назад я искренне радовалась нашей встрече."
    cs_narrator "Даша рассмеялась."
    cs_narrator "Я поднялась на крыльцо, но перед дверью обернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Подождёшь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_semen") and renpy.get_attributes("cs_semen") != tuple("awkward pioneer normal".split()):
        show cs_semen awkward pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_sy "А у меня есть выбор?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Конечно. Можешь уйти, а потом снова слушать всю историю с самого начала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Подожду."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот и прекрасно. Удивительно, насколько легко мы находим общий язык."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "В домике всё было на своих местах: чистая рубашка на стуле, туфли у кровати. Я положила снимки на сухой край стола."
    cs_narrator "Ещё утром я собиралась на пробежку. Теперь принесла необъяснимый архив, а нужно прежде всего переодеться."
    cs_narrator "Я сняла грязную форму, застегнула чистую рубашку, отыскала юбку. Пуговицы и воротник хотя бы подчинялись понятным правилам."
    cs_narrator "С волосами пришлось повозиться дольше."
    cs_narrator "Пучок окончательно распался, и фиолетовые пряди торчали в разные стороны."
    cs_narrator "Я посмотрела в зеркало."
    cs_narrator "Из подземелья вернулась. С расчёской пока проигрываю."
    cs_narrator "Когда удалось привести причёску в относительно приличное состояние, я осторожно проверила локоть."
    cs_narrator "Повязка держалась, но её край заметно запачкался."
    cs_narrator "Виола будет в восторге."
    cs_narrator "Особенно от объяснения, где именно я успела испачкать перевязочный материал до завтрака."
    cs_narrator "Пока я расчёсывалась, Даша тоже переоделась в пионерскую форму."
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Я вышла из-за ширмы."
    cs_narrator "Даша подняла голову от фотографий на столе."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_darya") and renpy.get_attributes("cs_darya") != tuple("thinking pioneer normal".split()):
        show cs_darya thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_da "Лен, ты уверена, что Ольге Дмитриевне нужно рассказывать всё сразу?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не всё сразу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "А как?"
    cs_narrator "Я указала на снимок, найденный в верхнем корпусе."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сначала покажем фотографии. Потом спросим про старое здание. И только после этого — почему в документах разных лет встречаются одни и те же имена."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "А голос?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Расскажем и про него. Но, наверное, не стоит начинать разговор словами: «Доброе утро, с нами тут побеседовала неизвестная женщина из подземелья»."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Звучит не очень убедительно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Особенно если учесть, что мы сами пока не понимаем, что произошло."
    cs_narrator "Я взяла фотографию."
    cs_narrator "Вгляделась в лицо девушки в очках."
    cs_narrator "Женя."
    cs_narrator "Или кто-то невероятно похожий на неё."
    cs_narrator "Интересно, что она сама скажет, когда увидит снимок?"
    if cs_da_love_confession_day3 == True:
        cs_narrator "Даша помолчала."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Лен…"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Что?"
        cs_narrator "Она смотрела на меня необычно серьёзно."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Я помню, что ты вчера сказала."
        cs_narrator "Щёки предательски потеплели."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Знаю."
        cs_narrator "Даша провела пальцем по краю стола."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "И мне действительно важно, что ты мне доверяешь."
        cs_narrator "Я медленно опустила фотографию."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Поэтому мне и стоило предупредить тебя, куда я собираюсь."
        cs_narrator "Она кивнула."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Да. Я не прошу тебя рассказывать мне буквально обо всём. Просто…"
        cs_narrator "Она не закончила, но я поняла."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Ты не хочешь снова искать меня по заброшенным зданиям?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Очень не хочу."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Постараюсь больше не предоставлять тебе такую возможность."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Серьёзно?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Серьёзно."
        cs_narrator "И на этот раз я действительно собиралась сдержать слово."
    elif cs_da_shared_bed_day3 == True:
        cs_narrator "Даша посмотрела на меня и неожиданно улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Знаешь, вчера ты так осторожно устраивалась рядом, чтобы мне не мешать."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "И?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "А сегодня отправилась одна в заброшенное убежище."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        if renpy.showing("cs_darya") and renpy.get_attributes("cs_darya") != tuple("amused pioneer normal".split()):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_ls "У меня весьма широкий диапазон поведения."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Заметила."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Некоторые грани моей личности, к сожалению, довольно острые."
        cs_narrator "Даша рассмеялась, потом посерьёзнела."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Просто предупреждай меня в следующий раз."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Договорились."
    else:
        cs_narrator "Даша осторожно положила снимок на стол."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Лен, только в следующий раз скажи мне, если соберёшься куда-нибудь уходить."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Хорошо."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Особенно если это будет не обычная пробежка."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Справедливое уточнение."
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы аккуратно сложили документы и вышли наружу."
    cs_narrator "Семён сидел на ступеньке крыльца. При нашем появлении он поднялся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Всё?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Всё. Теперь я соответствую минимальным требованиям советского общества."
    cs_narrator "Он внимательно посмотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Почти."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Что на этот раз?"
    cs_narrator "Он показал на съехавший галстук. Я поправила узел."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Этот предмет одежды испытывает ко мне личную неприязнь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А может, ты просто не умеешь его завязывать?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка, прошу не разрушать красивую теорию скучными фактами."
    cs_narrator "Он усмехнулся."
    cs_narrator "Я подняла документы."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ладно. Теперь серьёзно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Идём к Ольге Дмитриевне."
    return

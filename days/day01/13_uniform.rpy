# -*- coding: utf-8 -*-
# Source: source/day01_part03.md.
label cs_day01_13:
    $ save_name = u"Чужая смена — День 1: Пионерская униформа"
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_daily fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.45, delay=1.0, channel="ambience")
    # cs_presence_keep: hide mt
    # cs_composition: regroup
    show sl smile pioneer at cs_actor_right
    # cs_darya_stage: present in story
    show cs_dasha_winter arms_crossed normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Славя вошла с охапкой одежды."
    cs_narrator "Я сразу поднялась."
    cs_ls "Спасение цивилизации прибыло."
    cs_narrator "Она положила вещи на кровать."
    cs_narrator "Две белые рубашки."
    cs_narrator "Две тёмные юбки."
    cs_narrator "Красные галстуки."
    cs_narrator "Носки."
    cs_narrator "И, наконец, обувь."
    cs_narrator "Я тут же взяла одну пару лёгких туфель."
    cs_ls "Прекрасно."
    cs_narrator "Я подняла их почти как драгоценную находку."
    cs_ls "Никогда больше не буду недооценивать летнюю обувь."
    cs_narrator "Дарья тем временем спокойно рассматривала свой комплект формы."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она — на меня."
    # cs_darya_variety: reaction
    show cs_dasha_winter hands_on_hips normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Даже не начинай."
    cs_ls "Я молчу."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты очень громко молчишь."
    cs_narrator "Я едва заметно улыбнулась."
    pause 0.7
    window hide dissolve
    $ cs_director_scene("black")
    scene black
    with dissolve
    pause 1.0
    $ cs_director_scene("bg int_house_of_mt_day")
    scene bg int_house_of_mt_day
    with Dissolve(1.0)
    window show dissolve
    cs_narrator "Через несколько минут мне пришлось признать одну вещь."
    cs_narrator "Пионерская форма была значительно удобнее зимней одежды в июльскую жару."
    cs_narrator "Я вышла из-за импровизированной перегородки, поправляя рубашку."
    cs_narrator "Юбка."
    cs_narrator "Белые носки."
    cs_narrator "Лёгкие туфли."
    cs_narrator "И красный галстук, который я пока держала в руках."
    cs_narrator "Я повертела его."
    cs_ls "Так."
    cs_narrator "Повернула другой стороной."
    cs_ls "А это как завязывается?"
    cs_narrator "Ольга Дмитриевна подошла ко мне."
    show mt normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Дай сюда."
    cs_narrator "Я послушно протянула ей галстук."
    cs_ls "Представитель государственного аппарата прибыл для регулирования моего внешнего вида."
    # cs_camp_emotion: text reaction
    show mt angry pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Стой спокойно."
    cs_narrator "Я подчинилась."
    cs_narrator "Она быстро и уверенно завязала галстук."
    cs_narrator "Я посмотрела вниз."
    cs_narrator "Затем подошла к зеркалу."
    $ cs_director_scene("cs_lena_pioneer_mirror")
    scene cs_lena_pioneer_mirror
    with dissolve
    label cs_check_day01_part03_mirror:
    cs_narrator "Фиолетовые волосы."
    cs_narrator "Зелёные глаза."
    cs_narrator "Пионерская форма."
    pause 1.0
    cs_narrator "Несколько секунд я молча рассматривала отражение."
    cs_ls "Охренеть."
    cs_mt "Лена!"
    $ cs_director_scene("bg int_house_of_mt_day")
    scene bg int_house_of_mt_day
    with dissolve
    show mt normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Я повернулась."
    cs_ls "Что?"
    # cs_camp_emotion: text reaction
    show mt angry pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_camp_olga_angry:
    cs_mt "Следи за выражениями. Здесь дети."
    cs_ls "Принято."
    cs_narrator "Небольшая пауза."
    cs_ls "В таком случае официально заявляю: результат впечатляет."
    cs_narrator "Ольга Дмитриевна только покачала головой."
    cs_narrator "И тут открылась дверь."
    label cs_check_day01_part03_pioneer:
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Вышла Дарья."
    cs_narrator "Я замолчала."
    cs_narrator "Белая рубашка."
    cs_narrator "Тёмно-синяя юбка."
    cs_narrator "Красный галстук."
    cs_narrator "Её алые волосы особенно выделялись на фоне белой ткани."
    cs_narrator "И, что самое неприятное для моей способности сохранять серьёзное выражение лица, форма действительно ей шла."
    cs_narrator "Настолько, будто кто-то специально разрабатывал этот образ для неё."
    cs_narrator "Я медленно подняла палец."
    cs_ls "Вот."
    # cs_darya_stage: present in story
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Нет."
    cs_ls "Я же говорила."
    cs_da "Не говори."
    # cs_darya_stage: present in story
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_darya_uniform_talk:
    cs_ls "Тебе очень идёт."
    # cs_darya_stage: present in story
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена."
    cs_ls "Всё, молчу."
    cs_narrator "Я повернулась к Ольге Дмитриевне."
    cs_ls "Официально заявляю: эксперимент признан успешным."
    cs_narrator "Дарья подошла к зеркалу."
    cs_narrator "Несколько секунд изучала себя."
    cs_narrator "Потом негромко произнесла:"
    # cs_darya_stage: present in story
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Непривычная одежда."
    cs_ls "Ты ещё школьную форму девяностых не видела."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И надеюсь, не придётся."
    cs_narrator "Я усмехнулась."
    stop music fadeout 2.0
    cs_narrator "Но потом мой взгляд снова остановился на окне."
    return

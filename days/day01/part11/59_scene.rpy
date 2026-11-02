# -*- coding: utf-8 -*-
label cs_day01_59:
    $ save_name = "Чужая смена — День 1: Короткая версия"
    label cs_check_d1_s59:
    # cs_presence_keep: hide mz
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience "sound/ambiences/library_day.ogg" fadeout 1.0 fadein 1.0
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    stop music fadeout 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Стул оказался низким. Пришлось подвинуться к столу, испортив торжественное начало объяснения. Женя терпеливо ждала."
    cs_narrator "Я положила ладони на стол. В памяти поездка была непрерывной; вслух получался набор вещей, которым никто не обязан верить."
    cs_ls "Если я начну путаться, поправляй меня, Даш."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо. Только я расскажу то, что сама помню."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вот так и рассказывайте. По очереди."
    cs_ls "Сегодня утром я вышла из дома за продуктами. В Москве. Там была зима. Села в автобус четыреста десятого маршрута, познакомилась с Дашей. Потом мы заснули. Проснулись уже возле ваших ворот."
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Обе одновременно?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена проснулась раньше и разбудила меня. Но дорогу до этого я помню. Снег, город, лес за окном."
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А дальше вы решили, что попали в игру?"
    cs_ls "Я узнала лагерь. Даша эту игру не проходила."
    cs_narrator "Женя повернулась к ней."
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "То есть ты веришь ей на слово?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Про игру — да. Про то, что утром я была в Москве, мне чужое слово не нужно."
    cs_narrator "Мне понравился её спокойный ответ. Без попытки выиграть спор."
    cs_narrator "Женя придвинула лежавшую на столе газету."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И вы считаете, что сейчас должен быть другой год."
    cs_ls "Две тысячи двадцать шестой. У нас дома."
    cs_narrator "Она посмотрела сначала на меня, потом на Дарью."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Звучит как начало фантастического рассказа."
    cs_ls "У рассказа обычно есть автор, которому можно пожаловаться на сюжет."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А ты всё-таки попробуй без шуток."
    cs_ls "Мы пока не знаем, что произошло. Я вижу совпадения со знакомой историей, но не могу объяснить их. Поэтому и полезла в газеты."
    cs_narrator "Женя постучала пальцем по краю стола."
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Газеты ты увидела. Теперь что?"
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Завтра попробуем разобраться с телефоном Лены. Шурик и Электроник обещали посмотреть, можно ли его зарядить."
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Уже успели к ним сходить?"
    cs_ls "Успели. Неудачный день для конспирации."
    cs_narrator "Женя вздохнула, но спорить больше не стала."
    return

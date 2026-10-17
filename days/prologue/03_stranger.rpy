# -*- coding: utf-8 -*-
# Source: source/prologue.md. Dialogue is preserved verbatim.
label cs_scene_03:
    $ save_name = u"Чужая смена — Незнакомка"
    $ cs_director_scene("cs_bus_n_stop")
    scene cs_bus_n_stop at cs_bus_ride
    with fade
    #play ambience cs_bus_idle fadein 1.5
    window show dissolve
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Внутри пахло мокрой одеждой, холодным металлом и отопителем, который работал так, будто собирался в одиночку победить глобальное похолодание."
    cs_narrator "Я прошла ближе к задней части салона и нашла свободное место у окна."
    cs_narrator "Села."
    cs_narrator "Устроилась поудобнее."
    cs_narrator "И только тогда обратила внимание на девушку рядом."
    $ cs_director_scene("cs_bus_city")
    scene cs_bus_city at cs_bus_ride
    with fade
    #play sound cs_bus_start
    play ambience cs_bus_moving fadein 2.0
    label cs_check_neutral:
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Красные волосы."
    cs_narrator "Очень красные."
    cs_narrator "Не тот дешёвый бордовый оттенок, который обычно получается после самостоятельного окрашивания в ванной."
    cs_narrator "Нет."
    cs_narrator "У неё были густые, немного растрёпанные волосы глубокого алого цвета. Отдельные пряди свободно спадали на плечи и грудь."
    cs_narrator "Довольно длинные."
    cs_narrator "И совершенно непослушные на вид."
    cs_narrator "Она сидела со стороны прохода, чуть откинувшись на спинку кресла."
    cs_narrator "Светлая рубашка виднелась из-под расстёгнутой зимней куртки. Тёмные брюки. Никаких броских украшений."
    cs_narrator "Ничего необычного."
    cs_narrator "Кроме самих волос."
    cs_narrator "И, пожалуй, лица."
    cs_narrator "Красивого настолько, что мой профессионально деформированный мозг автоматически начал оценивать освещение."
    cs_th "Окно слева."
    cs_th "Холодный зимний фон."
    cs_th "Алые волосы."
    cs_th "Если поставить выдержку примерно..."
    cs_narrator "Я мысленно остановилась."
    cs_narrator "Господи."
    cs_narrator "Я уже фотографирую незнакомого человека."
    cs_narrator "Причём даже камеру не достала."
    cs_narrator "Дожили."
    cs_narrator "Девушка немного повернула голову."
    cs_narrator "Зелёные глаза."
    cs_narrator "Необычный контраст с красными волосами."
    cs_narrator "Наши взгляды встретились."
    cs_narrator "На секунду."
    cs_narrator "Может, на две."
    # cs_director_begin: Attention turns from the stranger to the bus window
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_b35e64725d:
    # cs_director_end
    cs_narrator "Я отвернулась к окну."
    cs_narrator "Она ничего не сказала."
    cs_narrator "Вот и прекрасно."
    cs_narrator "Идеальная попутчица."
    return

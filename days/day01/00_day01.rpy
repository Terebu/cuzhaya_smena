# -*- coding: utf-8 -*-
default cs_slavya_known = False
default cs_olga_seen = False
default cs_day01_part02_done = False
default cs_day01_part03_done = False
default cs_day01_part04_done = False

init 20 python:
    cs_sl = DynamicCharacter("u'Славя' if cs_slavya_known else u'Девушка'", color="#ffd200", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_mt = DynamicCharacter("u'Ольга Дмитриевна' if cs_olga_seen else u'Женский голос'", color="#00ea32", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")

label cs_day01:
    call cs_day_title(1)
    $ day_time()
    $ persistent.sprite_time = "day"
    call cs_day01_01
    call cs_day01_02
    call cs_day01_03
    call cs_day01_04
    call cs_day01_05
    call cs_day01_06
    jump cs_day01_continuation

# The supplied chapter is unfinished. Save/menu stay available here;
# the next instalment will replace this hold, without ending day 1.
label cs_day01_continuation:
    hide screen cs_day01_pending
    call cs_day01_07
    call cs_day01_08
    call cs_day01_09
    $ cs_day01_part02_done = True
    jump cs_day01_next_part

# Keep the old label for saves made at the former end of part 1.
label cs_check_day01_pending:
    jump cs_day01_continuation

label cs_day01_next_part:
    jump cs_day01_part03

# Old saves at this label now continue into the supplied third part.
label cs_check_day01_part02_pending:
    jump cs_day01_part03

label cs_day01_part03:
    hide screen cs_day01_pending
    $ cs_olga_seen = True
    call cs_day01_10
    call cs_day01_11
    call cs_day01_12
    call cs_day01_13
    call cs_day01_14
    $ cs_day01_part03_done = True
    jump cs_day01_part04_pending

label cs_day01_part04_pending:
    jump cs_day01_part04

label cs_check_day01_part03_pending:
    jump cs_day01_part04

label cs_day01_part04:
    hide screen cs_day01_pending
    $ cs_olga_seen = True
    call cs_day01_15
    call cs_day01_16
    call cs_day01_17
    call cs_day01_18
    call cs_day01_19
    call cs_day01_20
    $ cs_day01_part04_done = True
    jump cs_day01_part05_pending

label cs_day01_part05_pending:
    jump cs_day01_part05

# Compatibility: old saves at the former hold now resume the same conversation.
label cs_check_day01_part04_pending:
    jump cs_day01_part05

screen cs_day01_pending():
    zorder 20
    frame:
        align (0.5, 0.85)
        background Solid("#15210eea")
        padding (35, 25)
        vbox:
            spacing 14
            text "Продолжение первого дня в разработке" size 32 color "#e1edc5" font "fonts/calibri.ttf"
            hbox:
                spacing 35
                # The latest completed part controls old-save continuation too.
                if not cs_day01_part10_done:
                    if cs_day01_part09_done:
                        textbutton "Продолжить" action Jump("cs_day01_part10")
                    elif cs_day01_part08_done:
                        textbutton "Продолжить" action Jump("cs_day01_part09")
                    elif cs_day01_part07_done:
                        textbutton "Продолжить" action Jump("cs_day01_part08")
                    elif cs_day01_part06_done:
                        textbutton "Продолжить" action Jump("cs_day01_part07")
                    elif cs_day01_part05_done:
                        textbutton "Продолжить" action Jump("cs_day01_part06")
                    elif cs_day01_part04_done:
                        textbutton "Продолжить" action Jump("cs_day01_part05")
                    elif cs_day01_part03_done:
                        textbutton "Продолжить" action Jump("cs_day01_part04")
                    elif cs_day01_part02_done:
                        textbutton "Продолжить" action Jump("cs_day01_part03")
                    else:
                        textbutton "Продолжить" action Jump("cs_day01_continuation")
                textbutton "Сохранить" action ShowMenu("save")
                textbutton "Загрузить" action ShowMenu("load")
                textbutton "Главное меню" action MainMenu()

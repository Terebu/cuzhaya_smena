# -*- coding: utf-8 -*-
label cs_qa_part04_probe:
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day
    with Dissolve(0.3)
    label cs_check_part04_probe:
    cs_narrator "Проверка оригинального фона медпункта."
    return

testcase cs_part04_probe:
    pause 1.0
    $ renpy.set_physical_size((1280, 720))
    $ _preferences.text_cps = 0
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/part04_registered_sprites.txt", "w").write(repr([x for x in renpy.list_images() if x.split()[0] in ("cs", "sh", "el")]))
    assert renpy.has_image("bg int_aidpost_day") and renpy.has_image("bg ext_aidpost_day")
    assert renpy.loadable("sound/ambiences/medstation_inside_day.ogg")
    assert renpy.loadable("sound/sfx/knock_door7_polite.ogg")
    run Start("cs_qa_part04_probe")
    click until label cs_check_part04_probe
    pause 0.5
    $ cs_qa_capture("part04_original_aidpost")
    run Quit(confirm=False)

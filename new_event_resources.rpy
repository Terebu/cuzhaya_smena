# -*- coding: utf-8 -*-
init -3 python:
    with renpy.file("mods/chuzaya_smena/sp/zhenya/metadata.json") as cs_zfile:
        cs_zmeta = json.load(cs_zfile)
    for cs_zentry in cs_zmeta:
        for cs_zdistance in ("normal", "far", "close"):
            renpy.image("cs_zhenya " + cs_zentry["pose"] + " pioneer " + cs_zdistance, cs_dasha_image(cs_zentry, cs_zdistance, 1500.0))
init 20 python:
    cs_mi = Character(u"Мику", color="#00deff", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_vi = Character(u"Виола", color="#a8ffff", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
image cs_cg_square_concert_close = im.Scale("mods/chuzaya_smena/cg/event/cg_square_concert_close.png", 1920, 1080)
image cs_cg_music_club_rehearsal = im.Scale("mods/chuzaya_smena/cg/event/cg_music_club_rehearsal.png", 1920, 1080)
image cs_cg_square_concert_evening = im.Scale("mods/chuzaya_smena/cg/event/cg_square_concert_evening.png", 1920, 1080)
image cs_cg_lena_darya_library_evening = im.Scale("mods/chuzaya_smena/cg/lena_n_dasha/cg_lena_darya_library_evening.png", 1920, 1080)
image cs_cg_lena_darya_bench_sunset = im.Scale("mods/chuzaya_smena/cg/lena_n_dasha/cg_lena_darya_bench_sunset.png", 1920, 1080)

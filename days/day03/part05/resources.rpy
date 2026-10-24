# -*- coding: utf-8 -*-
default cs_day03_part05_done = False
default cs_day03_part05_started = False
default cs_day03_part05_legacy_entry = False
default cs_sl_day3_awarded = False
default cs_helped_sl_day3 = False
default cs_sl_poster_collected_day3 = False
default cs_day03_documents_location = None
default cs_day03_documents_delivered = False
default cs_semen_privacy_respected_day3 = False
default cs_day03_part06_route = None
image cs_ext_administration_day = im.Scale(cs_root + "bg/admin_camp/ext_administration_day.png",1920,1080)
image cs_int_administration_day = im.Scale(cs_root + "bg/admin_camp/int_administration_day.png",1920,1080)
init -9 python:
    cs_state_defaults.update(cs_day03_part05_done=False,cs_day03_part05_started=False,
        cs_day03_part05_legacy_entry=False,cs_sl_day3_awarded=False,cs_helped_sl_day3=False,
        cs_sl_poster_collected_day3=False,cs_day03_documents_location=None,
        cs_day03_documents_delivered=False,cs_semen_privacy_respected_day3=False,
        cs_day03_part06_route=None)

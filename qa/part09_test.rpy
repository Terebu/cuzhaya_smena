# -*- coding: utf-8 -*-
default cs_qa_part09_audit = False
default cs_qa_part09_visits = []
init 45 python:
    def cs_qa_part09_images(event, **kwargs):
        if event != "show_done" or not cs_qa_part09_audit or not cs_part09_live:
            return
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [t for t in tags if renpy.showing(t)]
        if set(actual) != set(cs_part09_cast) or len(actual)>3:
            raise Exception("Part-9 cast mismatch: %r / %r" % (actual, cs_part09_cast))
        if (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) != cs_qa_part09_scores:
            raise Exception("Part 9 changed friendship scores")
    cs_qa_previous_label_callback = config.label_callback
    def cs_qa_part09_labels(name, abnormal):
        if cs_qa_previous_label_callback:
            cs_qa_previous_label_callback(name, abnormal)
        if getattr(store, "cs_qa_part09_audit", False) and name in ("cs_day02_60","cs_day02_61","cs_day02_62","cs_day02_63","cs_day02_64","cs_day02_65","cs_day02_64a","cs_day02_64b","cs_day02_64c","cs_day02_64d","cs_day02_64d1","cs_day02_64d2","cs_day02_64e"):
            cs_qa_part09_visits.append(name)
    config.all_character_callbacks.append(cs_qa_part09_images)
    config.label_callback = cs_qa_part09_labels

label cs_qa_part09_load:
    $ renpy.load("cs_part08_pass-end")
    return

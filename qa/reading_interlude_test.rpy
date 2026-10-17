# -*- coding: utf-8 -*-
default cs_qa_reading_audit = False
default cs_qa_reading_visits = []
init 46 python:
    def cs_qa_reading_images(event, **kwargs):
        if event != "show_done" or not cs_qa_reading_audit or not cs_reading_live:
            return
        tags=("cs_darya","cs_zhenya","cs_semen","mz","un","mi","dv","sl","us","mt","sh","el","cs","cs_dasha_winter","cs_dasha_pioneer")
        actual=[t for t in tags if renpy.showing(t)]
        if set(actual)!=set(cs_reading_cast) or len(actual)>2:
            raise Exception("Reading cast mismatch: %r / %r" % (actual, cs_reading_cast))
        if (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un)!=cs_qa_reading_scores:
            raise Exception("Reading changed friendship scores")
        if cs_mz_map_lead!=cs_qa_reading_map_before:
            raise Exception("Reading changed the independent map lead")
    cs_qa_reading_previous_label_callback=config.label_callback
    def cs_qa_reading_labels(name,abnormal):
        if cs_qa_reading_previous_label_callback:
            cs_qa_reading_previous_label_callback(name,abnormal)
        if getattr(store,"cs_qa_reading_audit",False) and name.startswith("cs_day02_reading_"):
            cs_qa_reading_visits.append(name)
    config.all_character_callbacks.append(cs_qa_reading_images)
    config.label_callback=cs_qa_reading_labels

label cs_qa_reading_load:
    $ renpy.load("cs_part08_pass-end")
    return

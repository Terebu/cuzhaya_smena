"""Native accelerated traversal: execute every line; render each scene and CG.

Dialogue requires no simulated mouse click. At every scene/CG/costume change the
real Ren'Py renderer displays the current dialogue and settles actor entry ATL.
All instrumentation is confined to an isolated QA script.
"""
from pathlib import Path
R=Path(__file__).resolve().parent.parent
out='''# -*- coding: utf-8 -*-
init 98 python:
    import re as cs_rw_re
    import json as cs_rw_json
    renpy.cs_rw_enabled = False
    cs_rw_original_args = config.say_arguments_callback
    cs_rw_original_labels = config.label_callback
    cs_rw_original_menu_args = config.menu_arguments_callback
    cs_rw_original_menu = menu
    def cs_rw_args(who, *args, **kwargs):
        if cs_rw_original_args:
            args,kwargs=cs_rw_original_args(who,*args,**kwargs)
        if renpy.cs_rw_enabled:
            kwargs["interact"]=False
            renpy.game.preferences.transitions=0
        return args,kwargs
    def cs_rw_menu(items,*args,**kwargs):
        if not renpy.cs_rw_enabled:
            return cs_rw_original_menu(items,*args,**kwargs)
        choices=[(label,value) for label,value in items if value is not None and (not callable(value) or renpy.display.behavior.is_sensitive(value))]
        label,value=choices[0 if renpy.cs_rw_positive else -1]
        with open(config.basedir+"/rw_"+renpy.cs_rw_route+"_choices.txt","ab") as f:
            f.write((label+"\\n").encode("utf8"))
        return value() if callable(value) else value
    def cs_rw_menu_args(*args,**kwargs):
        if cs_rw_original_menu_args:
            args,kwargs=cs_rw_original_menu_args(*args,**kwargs)
        if renpy.cs_rw_enabled:
            store.menu=cs_rw_menu
        return args,kwargs
    def cs_rw_labels(name,abnormal):
        if cs_rw_original_labels:
            cs_rw_original_labels(name,abnormal)
        if not renpy.cs_rw_enabled:
            return
        if cs_rw_re.match(r"^cs_(scene_\\d+|day0[123]_\\d+[a-z_]*)$",name):
            renpy.cs_rw_pending=name
            renpy.cs_rw_visited.append(name)
        elif name in ("cs_check_day03_83_underwear","cs_check_day03_83_hair_touch","cs_check_day03_83_turned_away","cs_check_day03_83_dressed","cs_check_day01_part03_phone_off"):
            renpy.cs_rw_pending=name
        if name=="cs_check_day03_part07_complete":
            assert cs_day01_done and cs_day02_done and cs_day03_part07_done and cs_day03_lunch_arrived
            assert bool(cs_un_day3_lunch_together)==renpy.cs_rw_positive
            assert bool(cs_un_sketch_plan_discussed_day3)==renpy.cs_rw_positive
            assert bool(cs_un_sketch_time_agreed_day3)==renpy.cs_rw_positive
            assert bool(cs_mz_quiet_reading_place_day3)==renpy.cs_rw_positive
            assert bool(cs_mi_followup_invitation_day3)==renpy.cs_rw_positive
            assert bool(cs_dv_followup_invitation_day3)==renpy.cs_rw_positive
            assert cs_day03_reading_book_selected and cs_day03_reading_book_id=="paustovsky_warm_bread"
            assert cs_day03_darya_destination=="music_club"
            assert not renpy.showing("cs_darya") and not renpy.showing("un")
            assert cs_friend_mz==3*int(renpy.cs_rw_positive) and cs_mz_book_requested_day3
            assert cs_friend_mi==2*int(renpy.cs_rw_positive) and cs_friend_dv==2*int(renpy.cs_rw_positive) and cs_friend_un==3*int(renpy.cs_rw_positive)
            assert bool(cs_un_sketch_invite_day3)==renpy.cs_rw_positive
            assert bool(cs_un_concert_sketch_seen)==renpy.cs_rw_positive
            assert cs_lena_elbow_injury_day2==2 and cs_lena_no_sport_day2
            with open(config.basedir+"/rw_"+renpy.cs_rw_route+"_state.json","w") as f:
                cs_rw_json.dump(dict(status="PASS",visited=renpy.cs_rw_visited,screenshots=renpy.cs_rw_count,friendship=dict(mi=cs_friend_mi,dv=cs_friend_dv,un=cs_friend_un,se=cs_friend_se,sl=cs_friend_sl,mz=cs_friend_mz,viola=cs_friend_viola),poster=cs_day03_poster_location,catalog=cs_mz_catalog_checked_day3,book_requested=cs_mz_book_requested_day3,documents=cs_day03_documents_location,lunch_together=cs_un_day3_lunch_together,sketch_plan=cs_un_sketch_plan_discussed_day3,darya_destination=cs_day03_darya_destination),f)
    def cs_rw_character(event,**kwargs):
        if not renpy.cs_rw_enabled or event!="show_done":
            return
        cg=tuple(sorted(t for t in renpy.get_showing_tags() if t.startswith("cs_cg_") or t in ("cs_sleep_winter","cs_sleep_summer","cs_lena_pioneer_mirror")))
        pending=renpy.cs_rw_pending
        cast=tuple(sorted(t for t in cs_presence_tags if renpy.showing(t)))
        if cast!=renpy.cs_rw_last_cast:
            pending=pending or ("cast_"+"_".join(cast) if cast else "cast_empty")
        renpy.cs_rw_last_cast=cast
        if cg and cg!=renpy.cs_rw_last_cg:
            pending=pending or cg[0]
        renpy.cs_rw_last_cg=cg
        if pending:
            renpy.cs_rw_pending=None
            renpy.cs_rw_count+=1
            renpy.pause(0.15,hard=True)
            cs_p6_capture("%03d_%s"%(renpy.cs_rw_count,pending))
    config.say_arguments_callback=cs_rw_args
    config.menu_arguments_callback=cs_rw_menu_args
    config.label_callback=cs_rw_labels
    config.all_character_callbacks.append(cs_rw_character)

'''
for positive in (True,False):
 route='high' if positive else 'low'
 out+='''testcase cs_render_walk_'''+route+''':
    pause 0.5
    $ persistent.font_size = "small"
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _preferences.transitions = 0
    $ _test.force = True
    $ _test.timeout = 120.0
    $ renpy.cs_rw_enabled = True
    $ renpy.cs_rw_positive = '''+str(positive)+'''
    $ renpy.cs_rw_route = "'''+route+'''"
    $ renpy.cs_p6_case = "render_reviewed_'''+route+'''"
    $ renpy.cs_rw_pending = None
    $ renpy.cs_rw_last_cg = ()
    $ renpy.cs_rw_last_cast = ()
    $ renpy.cs_rw_visited = []
    $ renpy.cs_rw_count = 0
    run Start("chuzhaya_smena_start")
    click until label cs_check_day03_part07_complete
    pause 0.5
    assert cs_day03_part06_done and cs_day03_lunch_horn_played and cs_day03_lunch_arrived
    $ cs_p6_capture("complete")
    $ open(config.basedir+"/rw_'''+route+'''_PASS.txt","w").write("PASS")
    run Quit(confirm=False)

'''
(R/'tools/full_render_walkthrough_test.rpy.txt').write_text(out,encoding='utf8')
print('Generated native render walkthroughs (both choice routes).')

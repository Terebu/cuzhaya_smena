from pathlib import Path
import re
R=Path(__file__).resolve().parent.parent
s='''# -*- coding: utf-8 -*-
init 106 python:
    renpy.cs_p14_fast=False
    renpy.cs_p14_auto=False
    cs_p14_old_say=config.say_arguments_callback
    cs_p14_old_labels=config.label_callback
    cs_p14_old_args=config.menu_arguments_callback
    def cs_p14_say(who,*args,**kwargs):
        if cs_p14_old_say:args,kwargs=cs_p14_old_say(who,*args,**kwargs)
        if renpy.cs_p14_fast:kwargs["interact"]=False
        return args,kwargs
    def cs_p14_menu(items,*args,**kwargs):
        values=[v for l,v in items if v is not None]
        yes=renpy.cs_p14_request if not cs_da_bed_choice_done_day3 else renpy.cs_p14_confess
        v=values[0 if yes else -1]
        return v() if callable(v) else v
    def cs_p14_args(*args,**kwargs):
        if cs_p14_old_args:args,kwargs=cs_p14_old_args(*args,**kwargs)
        if renpy.cs_p14_auto:store.menu=cs_p14_menu
        return args,kwargs
    def cs_p14_labels(name,abnormal):
        if cs_p14_old_labels:cs_p14_old_labels(name,abnormal)
        if not renpy.cs_p14_fast:return
        if name.startswith("cs_day03_18"):
            renpy.cs_p14_pending=name
            renpy.cs_p14_visited.append(name)
    def cs_p14_capture(event,**kwargs):
        if event!="show_done" or not renpy.cs_p14_fast:return
        target=cs_day03_audio_target(cs_day03_audio_location)
        if target is not False:assert renpy.music.get_playing(channel="ambience")==target
        cast=tuple(sorted(t for t in cs_presence_tags if renpy.showing(t)))
        assert not set(cast)-set(("cs_darya",)),"Uninvited actor"
        cg=renpy.showing("cs_cg_lena_darya_shared_sleep_night")
        if cg:assert cs_da_shared_bed_day3 and not cast
        bg=tuple(sorted((t,tuple(renpy.get_attributes(t) or ())) for t in renpy.get_showing_tags() if t not in cs_presence_tags))
        if renpy.cs_p14_pending or cast!=renpy.cs_p14_cast or bg!=getattr(renpy,"cs_p14_bg",()):
            renpy.cs_p14_count+=1
            renpy.pause(0.3,hard=True)
            cs_p6_capture("%02d_%s"%(renpy.cs_p14_count,renpy.cs_p14_pending or "cast"))
            if len(cast)==1:
                x,y,w,h=renpy.get_image_bounds(cast[0]);assert abs(x+w/2.0-960)<2
            renpy.cs_p14_cast=cast;renpy.cs_p14_pending=None;renpy.cs_p14_bg=bg
    config.say_arguments_callback=cs_p14_say
    config.menu_arguments_callback=cs_p14_args
    config.label_callback=cs_p14_labels
    config.all_character_callbacks.append(cs_p14_capture)

label cs_qa_p14_setup:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=cs_day03_started=True
    $ cs_day03_part13_done=True
    $ cs_friend_da=renpy.cs_p14_friend
    $ cs_friend_mz=3
    $ cs_friend_sl=2
    $ cs_friend_se=3
    $ cs_friend_mi=cs_friend_dv=cs_friend_un=2
    $ cs_mz_book_finished_day3=True
    $ cs_mz_book_borrowed_day3=False
    $ cs_day03_reading_book_id="goncharov_ordinary_story"
    $ cs_day03_reading_book_location="library"
    $ cs_day03_darya_destination="house"
    $ cs_day03_sketchbook_location=cs_day03_poster_location="house_table"
    $ cs_mi_followup_invitation_day3=cs_dv_followup_invitation_day3=cs_sl_day4_notice_offer=True
    $ cs_mi_followup_target_day=cs_dv_followup_target_day=4
    $ cs_un_sketch_completed_day3=cs_un_private_drawing_shown_day3=True
    $ cs_se_day3_personal_talk=cs_da_day3_music_talk=True
    $ cs_da_day3_shared_silence=cs_da_day3_quiet_walk=False
    $ cs_da_day3_fear_of_getting_used_to_camp=True
    $ cs_lena_elbow_bandaged=cs_viola_spare_bandage=True
    $ cs_lena_elbow_injury_day2=2
    $ cs_day03_documents_location="administration"
    $ set_mode_adv()
    $ night_time()
    return

label cs_qa_p14_route:
    call cs_qa_p14_setup
    jump cs_day03_part14

label cs_qa_p14_repeat:
    call cs_day03_bed_choice
    call cs_day03_confession_choice
    jump cs_day03_part14
'''
cases=[(0,True,False),(1,True,False),(2,True,True),(2,True,False),(3,True,True),(3,True,False),(0,False,False),(2,False,False),(3,False,False)]
for n,(friend,request,confess) in list(enumerate(cases))+[('guard',(2,True,True))]:
 shared=request and friend>=2
 s+='\ntestcase cs_p14_'+str(n)+':\n    pause 0.5\n    $ persistent.font_size="small"\n    $ renpy.set_physical_size((1280,720))\n    $ _preferences.text_cps=0\n    $ _preferences.transitions=2\n    $ _test.force=True\n    $ _test.timeout=120.0\n'
 vals=dict(fast=True,auto=n!='guard',friend=friend,request=request,confess=confess,count=0,cast=(),pending=None,visited=[])
 s+=''.join('    $ renpy.cs_p14_'+k+'='+repr(v)+'\n' for k,v in vals.items())
 s+='    $ renpy.cs_p6_case="p14_'+str(n)+'"\n    run Start("cs_qa_p14_route")\n'
 if n=='guard':s+='''    pause 25.0
    assert not cs_da_bed_choice_done_day3
    $ renpy.take_screenshot()
    $ renpy.save("p14_bed_menu")
    $ renpy.load("p14_bed_menu")
    pause 0.5
    "Сказать Даше, что сегодня хочется спать рядом с ней"
    pause 25.0
    assert cs_da_shared_bed_day3 and not cs_da_confession_choice_done_day3
    $ renpy.take_screenshot()
    $ renpy.save("p14_confess_menu")
    $ renpy.load("p14_confess_menu")
    pause 0.5
    "Сказать Даше: «Я тебя люблю»"
'''
 s+='    click until label cs_check_day03_part14_complete\n    pause 0.5\n'
 for k,v in dict(cs_da_friend_before_night=friend,cs_friend_da=friend+int(shared),cs_da_bed_request_day3=request,cs_da_shared_bed_day3=shared,cs_da_respected_space_day3=not request,cs_da_love_confession_day3=shared and confess,cs_da_unspoken_feelings_day3=shared and not confess,cs_da_shared_sleep_cg_seen_day3=shared).items():s+='    assert '+k+'=='+repr(v)+'\n'
 s+='''    assert cs_day03_part14_done and cs_day03_completed
    assert cs_mz_book_finished_day3 and not cs_mz_book_borrowed_day3
    assert cs_day03_reading_book_location=="library" and cs_day03_darya_destination=="house"
    assert cs_day03_sketchbook_location==cs_day03_poster_location=="house_table"
    assert cs_friend_sl==2 and cs_friend_se==3 and cs_friend_mi==cs_friend_dv==cs_friend_un==2 and cs_friend_mz==3
    assert cs_mi_followup_invitation_day3 and cs_dv_followup_invitation_day3 and cs_sl_day4_notice_offer
    assert cs_mi_followup_target_day==cs_dv_followup_target_day==4
    assert cs_un_sketch_completed_day3 and cs_un_private_drawing_shown_day3
    assert cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2==2 and cs_viola_spare_bandage
    assert cs_day03_documents_location=="administration"
    assert not renpy.music.get_playing(channel="ambience") and not renpy.music.get_playing(channel="music")
'''
 s+='    assert ("cs_day03_184" in renpy.cs_p14_visited)=='+repr(not shared)+'\n'
 s+='    assert ("cs_day03_185" in renpy.cs_p14_visited)=='+repr(shared)+'\n'
 s+='    assert ("cs_day03_187a" in renpy.cs_p14_visited)=='+repr(shared and confess)+'\n'
 s+='    $ renpy.take_screenshot()\n    $ renpy.save("p14_'+str(n)+'_end")\n    $ renpy.load("p14_'+str(n)+'_end")\n    pause 0.5\n'
 s+='    assert cs_friend_da=='+str(friend+int(shared))+' and cs_day03_completed\n'
 s+='    $ cs_p6_capture("complete")\n    run Jump("cs_qa_p14_repeat")\n    pause 1.0\n    assert cs_friend_da=='+str(friend+int(shared))+'\n    assert renpy.get_screen("cs_day04_wait_screen") is not None\n'
 s+='    $ open(config.basedir+"/p14_'+str(n)+'_PASS.txt","w").write("PASS")\n    run Quit(confirm=False)\n'
(R/'tools/day03_part14_test.rpy.txt').write_text(s,encoding='utf8')
print('PART14_QA_GENERATED',len(cases)+1,'cases')

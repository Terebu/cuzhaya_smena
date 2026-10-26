from pathlib import Path
R=Path(__file__).resolve().parent.parent
s='''# -*- coding: utf-8 -*-
init 99 python:
    renpy.cs_p11_fast=False
    renpy.cs_p11_auto=False
    cs_p11_old_say=config.say_arguments_callback
    cs_p11_old_labels=config.label_callback
    cs_p11_old_args=config.menu_arguments_callback
    def cs_p11_say(who,*args,**kwargs):
        if cs_p11_old_say:args,kwargs=cs_p11_old_say(who,*args,**kwargs)
        if renpy.cs_p11_fast:
            kwargs["interact"]=False
            for character,tag in ((cs_da,"cs_darya"),(cs_mz,"cs_zhenya"),(cs_sy,"cs_semen"),(cs_mi,"mi"),(cs_dv,"dv")):
                if who is character:assert renpy.showing(tag),"Speaking actor missing: "+tag
        return args,kwargs
    def cs_p11_menu(items,*args,**kwargs):
        choices=[v for l,v in items if v is not None]
        v=choices[0 if renpy.cs_p11_yes else -1]
        return v() if callable(v) else v
    def cs_p11_args(*args,**kwargs):
        if cs_p11_old_args:args,kwargs=cs_p11_old_args(*args,**kwargs)
        if renpy.cs_p11_auto:store.menu=cs_p11_menu
        return args,kwargs
    def cs_p11_labels(name,abnormal):
        if cs_p11_old_labels:cs_p11_old_labels(name,abnormal)
        if not renpy.cs_p11_fast:return
        if name=="cs_check_day03_155_hug":renpy.cs_p11_hugs+=1
        if name=="cs_check_day03_161_help_completed":renpy.cs_p11_helps+=1
        if name=="cs_check_day03_152_horn":raise AssertionError("Dinner horn replayed")
        if name.startswith("cs_day03_1") and name[9:].rstrip("ab").isdigit():renpy.cs_p11_pending=name
        if name=="cs_check_day03_part11_complete":renpy.cs_p11_pending=None
    def cs_p11_capture(event,**kwargs):
        if event!="show_done" or not renpy.cs_p11_fast:return
        if renpy.showing("bg"):
            assert renpy.has_image(("bg",)+tuple(renpy.get_attributes("bg"))),"Unregistered background"
        cast=tuple(sorted(t for t in cs_presence_tags if renpy.showing(t)))
        if renpy.cs_p11_pending or cast!=renpy.cs_p11_cast:
            renpy.cs_p11_count+=1
            renpy.pause(0.25,hard=True)
            cs_p6_capture("%02d_%s"%(renpy.cs_p11_count,renpy.cs_p11_pending or "cast"))
            if len(cast)==1:
                x,y,w,h=renpy.get_image_bounds(cast[0]);assert abs(x+w/2.0-960)<2
            renpy.cs_p11_cast=cast;renpy.cs_p11_pending=None
    config.say_arguments_callback=cs_p11_say
    config.menu_arguments_callback=cs_p11_args
    config.label_callback=cs_p11_labels
    config.all_character_callbacks.append(cs_p11_capture)

label cs_qa_p11_setup:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=True
    $ cs_friend_mz=renpy.cs_p11_mz
    $ cs_mz_friend_on_arrival_day3=min(cs_friend_mz,3)
    $ cs_mz_open_library_invitation_day3=renpy.cs_p11_open
    $ cs_mz_quiet_reading_place_day3=renpy.cs_p11_quiet
    $ cs_mz_day3_honest_book_talk=renpy.cs_p11_honest
    $ cs_mi_followup_invitation_day3=renpy.cs_p11_mi
    $ cs_dv_followup_invitation_day3=renpy.cs_p11_dv
    $ cs_friend_mi=2 if renpy.cs_p11_mi else 0
    $ cs_friend_dv=2 if renpy.cs_p11_dv else 0
    $ cs_friend_se=2
    $ cs_se_day3_personal_talk=renpy.cs_p11_se
    $ cs_mz_book_borrowed_day3=cs_day03_novel_selected=True
    $ cs_day03_reading_book_id="goncharov_ordinary_story"
    $ cs_day03_reading_book_location=cs_day03_sketchbook_location="house_table"
    $ cs_day03_poster_location="house_table" if renpy.cs_p11_mz%2 else None
    $ cs_day03_part10_done=cs_day03_dinner_horn_played=cs_day03_dinner_arrived=True
    $ cs_lena_elbow_bandaged=cs_lena_no_sport_day2=cs_viola_spare_bandage=True
    $ cs_lena_elbow_injury_day2=2
    $ cs_helped_viola_day3=cs_helped_sl_day3=renpy.cs_p11_honest
    $ cs_day03_documents_location="administration"
    $ set_mode_adv()
    $ sunset_time()
    $ persistent.sprite_time="sunset"
    return

label cs_qa_p11_route:
    call cs_qa_p11_setup
    jump cs_day03_part11

label cs_qa_p11_guard:
    call cs_qa_p11_setup
    call cs_day03_154
    call cs_day03_155
    call cs_day03_159
    call cs_day03_evening_library_choice
    call screen cs_qa_p11_gate
    call cs_day03_evening_library_choice
    call cs_day03_161a
    call cs_day03_161a
    call cs_day03_155
    call screen cs_qa_p11_gate
    $ cs_day03_part11_done=True
    jump cs_day03_part11

screen cs_qa_p11_gate():
    modal True
    textbutton "Продолжить проверку" action Return() align (0.5,0.5)
'''
for i in list(range(12))+['guard']:
    guard=i=='guard';n=5 if guard else i
    level=n//2;yes=True if guard else bool(n%2);mi=bool(n%4&1);dv=bool(n%4&2)
    opened=n>=8;quiet=n>=10;honest=bool(n%3==2);se=n%3==0
    s+='''
testcase cs_p11_'''+str(i)+''':
    pause 0.5
    $ persistent.font_size="small"
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps=0
    $ _preferences.transitions=2
    $ _test.force=True
    $ _test.timeout=90.0
    $ renpy.cs_p11_fast=True
    $ renpy.cs_p11_auto='''+repr(not guard)+'''
    $ renpy.cs_p11_yes='''+repr(yes)+'''
    $ renpy.cs_p11_mz='''+str(level)+'''
    $ renpy.cs_p11_open='''+repr(opened)+'''
    $ renpy.cs_p11_quiet='''+repr(quiet)+'''
    $ renpy.cs_p11_honest='''+repr(honest)+'''
    $ renpy.cs_p11_mi='''+repr(mi)+'''
    $ renpy.cs_p11_dv='''+repr(dv)+'''
    $ renpy.cs_p11_se='''+repr(se)+'''
    $ renpy.cs_p11_count=renpy.cs_p11_hugs=renpy.cs_p11_helps=0
    $ renpy.cs_p11_cast=()
    $ renpy.cs_p11_pending=None
    $ renpy.cs_p11_spoken=[]
    $ renpy.cs_p6_case="p11_'''+str(i)+'''"
    run Start("'''+('cs_qa_p11_guard' if guard else 'cs_qa_p11_route')+'''")
'''
    if guard:
        s+='''    pause 15.0
    pause 0.5
    $ renpy.take_screenshot()
    $ renpy.save("p11_menu")
    $ renpy.load("p11_menu")
    pause 0.5
    "Предложить Жене помощь с возвращёнными книгами"
    "Продолжить проверку"
    "Продолжить проверку"
    pause 0.5
    assert renpy.get_screen("cs_day03_part11_wait_screen") is not None
'''
    else:s+='''    click until label cs_check_day03_part11_complete
    pause 0.5
'''
    s+='''    assert cs_day03_part11_done and cs_friend_mz=='''+str(level+yes)+'''
    assert cs_mz_dinner_friend_on_arrival=='''+str(level)+'''
    assert bool(cs_mz_hug_allowed_day3)=='''+repr(level>=3 and opened)+'''
    assert renpy.cs_p11_hugs=='''+str(int(level>=3 and opened))+'''
    assert cs_mz_evening_help_day3==cs_mz_evening_help_completed_day3=='''+repr(yes)+'''
    assert renpy.cs_p11_helps=='''+str(int(yes))+'''
    assert cs_mz_open_library_invitation_day3=='''+repr(opened)+'''
    assert cs_mz_quiet_reading_place_day3=='''+repr(quiet)+'''
    assert cs_day03_reading_book_id=="goncharov_ordinary_story" and cs_mz_book_borrowed_day3
    assert cs_day03_reading_book_location==cs_day03_sketchbook_location=="house_table"
    assert cs_day03_poster_location=='''+repr('house_table' if level%2 else None)+'''
    assert cs_mi_followup_invitation_day3=='''+repr(mi)+''' and cs_dv_followup_invitation_day3=='''+repr(dv)+'''
    assert cs_day03_dinner_horn_played and cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2==2 and cs_viola_spare_bandage
    assert cs_day03_documents_location=="administration"
'''
    if not guard:s+='''    assert cs_mi_followup_target_day=='''+repr(4 if mi else None)+''' and cs_dv_followup_target_day=='''+repr(4 if dv else None)+'''
    assert cs_day03_dinner_finished and cs_day03_darya_destination=="home"
    assert renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
'''
    s+='''    $ renpy.take_screenshot()
    $ renpy.save("p11_'''+str(i)+'''_end")
    $ renpy.load("p11_'''+str(i)+'''_end")
    pause 0.5
    assert cs_friend_mz=='''+str(level+yes)+'''
    $ cs_p6_capture("complete")
    $ open(config.basedir+"/p11_'''+str(i)+'''_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/day03_part11_test.rpy.txt').write_text(s,encoding='utf8')
print('PART11_QA_GENERATED')

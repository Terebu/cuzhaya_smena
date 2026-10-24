"""Native branch matrix and shared camera regression checks, isolated from release."""
from pathlib import Path
R=Path(__file__).resolve().parent.parent
out='''# -*- coding: utf-8 -*-
init 96 python:
    import json as cs_rev_json
    renpy.cs_rev_fast=False
    cs_rev_old_say=config.say_arguments_callback
    cs_rev_old_menu_args=config.menu_arguments_callback
    cs_rev_old_label=config.label_callback
    def cs_rev_say(who,*args,**kwargs):
        if cs_rev_old_say:args,kwargs=cs_rev_old_say(who,*args,**kwargs)
        if renpy.cs_rev_fast:kwargs["interact"]=False
        return args,kwargs
    def cs_rev_menu(items,*args,**kwargs):
        choices=[(label,value) for label,value in items if value is not None]
        yes=renpy.cs_rev_viola if "Виоле" in choices[0][0] else renpy.cs_rev_alice
        value=choices[0 if yes else -1][1]
        return value() if callable(value) else value
    def cs_rev_menu_args(*args,**kwargs):
        if cs_rev_old_menu_args:args,kwargs=cs_rev_old_menu_args(*args,**kwargs)
        if renpy.cs_rev_fast:store.menu=cs_rev_menu
        return args,kwargs
    def cs_rev_labels(name,abnormal):
        if cs_rev_old_label:cs_rev_old_label(name,abnormal)
        if renpy.cs_rev_fast and name=="cs_check_day03_104":renpy.cs_rev_fast=False
        if renpy.cs_rev_fast and name in ("cs_check_day03_96_semen","cs_check_day03_96_semen_left","cs_check_day03_98","cs_check_day03_101_alice","cs_check_day03_102_outside","cs_check_day03_103_reflection","cs_check_day03_103_dialogue","cs_check_day03_116_alice_focus"):
            renpy.cs_rev_pending=name
        if renpy.cs_rev_fast and name=="cs_check_day03_102_spare_given":renpy.cs_rev_gifts+=1
        if renpy.cs_rev_fast and name=="cs_check_day03_99_examination":renpy.cs_rev_exams+=1
    def cs_rev_character(event,**kwargs):
        if event!="show_done" or not renpy.cs_rev_fast or not renpy.cs_rev_pending:return
        name=renpy.cs_rev_pending;renpy.cs_rev_pending=None
        renpy.pause(0.4,hard=True)
        cs_p6_capture(name)
        tags=set(t for t in cs_presence_tags if renpy.showing(t))
        if name=="cs_check_day03_101_alice":assert tags==set(("dv","cs","cs_darya"))
        if name=="cs_check_day03_102_outside":assert tags==set(("dv","cs_darya"))
        if name=="cs_check_day03_103_reflection":assert not tags
        if name=="cs_check_day03_103_dialogue":assert tags==set(("cs_darya",))
        if name=="cs_check_day03_96_semen_left":assert tags==set(("cs_darya",))
    config.say_arguments_callback=cs_rev_say
    config.menu_arguments_callback=cs_rev_menu_args
    config.label_callback=cs_rev_labels
    config.all_character_callbacks.append(cs_rev_character)

label cs_qa_revision:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=True
    $ cs_friend_viola=renpy.cs_rev_before
    $ cs_viola_spare_bandage=renpy.cs_rev_spare
    $ cs_lena_elbow_bandaged=True
    $ cs_lena_elbow_injury_day2=2
    $ cs_lena_no_sport_day2=True
    $ set_mode_adv()
    $ day_time()
    $ persistent.sprite_time="day"
    jump cs_day03_part04

label cs_qa_revision_guard:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=True
    $ day_time()
    $ set_mode_adv()
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    show dv normal pioneer at cs_actor_left
    $ cs_presence_stage()
    call cs_day03_alice_medpoint_choice
    call cs_day03_alice_medpoint_choice
    call cs_day03_alice_music_choice
    call cs_day03_alice_music_choice
    label cs_check_revision_guard_end:
    cs_narrator "Проверка повторных начислений завершена."
    return

label cs_qa_all_actor_camera:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=True
    $ set_mode_adv()
    $ day_time()
    python:
        for tag,(name,position) in sorted(cs_director_defaults.items()):
            cs_director_scene("black")
            renpy.scene()
            renpy.show("bg int_musclub_day")
            renpy.show(name,at_list=[getattr(store,position)])
            renpy.pause(0.4,hard=True)
            before=renpy.get_image_bounds(tag)
            cs_presence_stage()
            renpy.pause(0.4,hard=True)
            after=renpy.get_image_bounds(tag)
            assert abs(after[0]+after[2]/2.0-960)<1,(tag,after)
            assert before[1:]==after[1:],(tag,before,after)
            cs_p6_capture("solo_"+tag)
            cs_pov_begin()
            renpy.pause(0.25,hard=True)
            assert not any(renpy.showing(t) for t in cs_presence_tags)
            cs_p6_capture("inward_"+tag)
            cs_pov_end()
            renpy.pause(0.4,hard=True)
            assert renpy.showing(tag) and renpy.get_image_bounds(tag)==after
            cs_actor_exit([tag]);cs_pov_end()
            assert not renpy.showing(tag)
    label cs_check_revision_camera_end:
    cs_narrator "Проверка всех одиночных собеседников завершена."
    return

label cs_qa_revision_legacy_entry:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=True
    $ set_mode_adv()
    $ day_time()
    scene bg int_aidpost_day
    show cs custom serious medical normal at cs_viola_normal_left
    $ cs_presence_stage()
    call cs_check_day03_102_viola_left
    label cs_check_revision_legacy_end:
    cs_narrator "Старый выход из медпункта завершён."
    return

'''
setup='''    pause 0.5
    $ persistent.font_size="small"
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps=0
    $ _preferences.transitions=2
    $ _test.force=True
    $ _test.timeout=120.0
'''
cases=[]
for before in (1,2):
 for viola in (True,False):
  for alice in (True,False):cases.append((before,viola,alice,False))
cases += [(0,True,True,False),(2,True,True,True)]
for i,(before,viola,alice,spare) in enumerate(cases):
 out+='testcase cs_revision_%d:\n'%i+setup
 for key,value in dict(fast=True,before=before,viola=viola,alice=alice,spare=spare,pending=None,gifts=0,exams=0).items():out+='    $ renpy.cs_rev_%s=%r\n'%(key,value)
 out+='    $ renpy.cs_p6_case="revision_%d"\n'%i
 out+='''    run Start("cs_qa_revision")
    click until label cs_check_day03_104
    pause 0.5
    assert cs_friend_viola==renpy.cs_rev_before+int(renpy.cs_rev_viola)
    assert cs_friend_dv==int(renpy.cs_rev_alice)
    assert bool(cs_dv_medpoint_day3)==renpy.cs_rev_alice
    assert cs_viola_friend_before_day3==renpy.cs_rev_before
    assert cs_viola_spare_bandage==(renpy.cs_rev_spare or renpy.cs_rev_before>=2)
    assert renpy.cs_rev_gifts==int(renpy.cs_rev_before>=2 and not renpy.cs_rev_spare)
    assert renpy.cs_rev_exams==1 and cs_day03_viola_check_done
    assert cs_day03_medpoint_revision_done and cs_lena_elbow_bandaged
    assert cs_lena_elbow_injury_day2==2 and cs_lena_no_sport_day2
    $ renpy.take_screenshot()
    $ renpy.save("revision_after_medpoint")
    $ renpy.load("revision_after_medpoint")
    pause 0.4
    assert cs_friend_dv==int(renpy.cs_rev_alice)
    $ cs_p6_capture("bridge")
'''
 out+='    $ open(config.basedir+"/revision_%d_PASS.txt","w").write("PASS")\n    run Quit(confirm=False)\n\n'%i
out+='testcase cs_revision_camera:\n'+setup+'''    $ renpy.cs_p6_case="revision_camera"
    run Start("cs_qa_all_actor_camera")
    click until label cs_check_revision_camera_end
    $ open(config.basedir+"/revision_camera_PASS.txt","w").write("PASS")
    run Quit(confirm=False)

testcase cs_revision_guard:
'''+setup+'''    $ renpy.cs_p6_case="revision_guard"
    run Start("cs_qa_revision_guard")
    pause 0.5
    $ renpy.take_screenshot()
    $ renpy.save("revision_alice_menu")
    $ renpy.load("revision_alice_menu")
    pause 0.5
    "Спросить, всё ли в порядке, и не делать из этого представление"
    click until label cs_check_day03_102_result
    assert cs_friend_dv==1 and cs_dv_medpoint_day3
    pause 0.5
    "Спросить, всё ли в порядке, и не делать из этого представление"
    click until label cs_check_day03_102_result
    assert cs_friend_dv==1
    pause 0.5
    "Спросить Алису о её игре и честно обсудить звучание"
    click until label cs_check_day03_117_result
    assert cs_friend_dv==2
    pause 0.5
    "Спросить Алису о её игре и честно обсудить звучание"
    click until label cs_check_revision_guard_end
    assert cs_friend_dv==2
    $ cs_p6_capture("dv_two_points")
    $ open(config.basedir+"/revision_guard_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/medpoint_revision_test.rpy.txt').write_text(out,encoding='utf8')
out+='\ntestcase cs_revision_legacy:\n'+setup+'''    $ renpy.cs_p6_case="revision_legacy"
    run Start("cs_qa_revision_legacy_entry")
    pause 0.5
    assert _last_say_what=="Старый выход из медпункта завершён."
    assert not renpy.showing("cs")
    $ open(config.basedir+"/revision_legacy_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/medpoint_revision_test.rpy.txt').write_text(out,encoding='utf8')
print('Generated 10 branch cases, all-character camera and reward/save guard.')

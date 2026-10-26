from pathlib import Path
R=Path(__file__).resolve().parent.parent
out='''# -*- coding: utf-8 -*-
init 97 python:
    renpy.cs_late_fast=False
    renpy.cs_late_auto=False
    cs_late_say_old=config.say_arguments_callback
    cs_late_labels_old=config.label_callback
    cs_late_menu_old=config.menu_arguments_callback
    def cs_late_say(who,*args,**kwargs):
        if cs_late_say_old:args,kwargs=cs_late_say_old(who,*args,**kwargs)
        if renpy.cs_late_fast:kwargs["interact"]=False
        return args,kwargs
    def cs_late_menu(items,*args,**kwargs):
        choices=[(label,value) for label,value in items if value is not None]
        yes=renpy.cs_late_book_yes if renpy.cs_late_current_menu=="cs_check_day03_134_menu" else renpy.cs_late_se_yes
        val=choices[0 if yes else -1][1]
        return val() if callable(val) else val
    def cs_late_menu_args(*args,**kwargs):
        if cs_late_menu_old:args,kwargs=cs_late_menu_old(*args,**kwargs)
        if renpy.cs_late_auto:store.menu=cs_late_menu
        return args,kwargs
    def cs_late_labels(name,abnormal):
        if cs_late_labels_old:cs_late_labels_old(name,abnormal)
        if not renpy.cs_late_fast:return
        if name in ("cs_check_day03_134_menu","cs_check_day03_140_menu"):
            renpy.cs_late_current_menu=name
        if name=="cs_check_day03_135_loan":renpy.cs_late_loans+=1
        if name.startswith("cs_day03_") and name[9:10].isdigit():
            renpy.cs_late_visited.append(name)
            renpy.cs_late_pending=name
        if name=="cs_check_day03_part09_complete":
            renpy.cs_late_pending=None
        if name=="cs_day03_131":
            assert not renpy.showing("cs_darya")
        if name=="cs_day03_136":
            assert cs_mz_book_borrowed_day3 and cs_day03_reading_book_location=="lena"
        if name=="cs_day03_144":
            assert not renpy.showing("cs_darya") and cs_un_sketch_time_agreed_day3
    def cs_late_capture(event,**kwargs):
        if event!="show_done" or not renpy.cs_late_fast:return
        cast=tuple(sorted(t for t in cs_presence_tags if renpy.showing(t)))
        if cast!=renpy.cs_late_cast or renpy.cs_late_pending:
            renpy.cs_late_count+=1
            renpy.pause(0.25,hard=True)
            cs_p6_capture("%02d_%s"%(renpy.cs_late_count,renpy.cs_late_pending or "cast"))
            renpy.cs_late_cast=cast;renpy.cs_late_pending=None
    config.say_arguments_callback=cs_late_say
    config.label_callback=cs_late_labels
    config.menu_arguments_callback=cs_late_menu_args
    config.all_character_callbacks.append(cs_late_capture)

label cs_qa_day03_late:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=cs_un_name_known=True
    $ cs_friend_mz=renpy.cs_late_mz
    $ cs_friend_se=renpy.cs_late_se
    $ cs_friend_un=renpy.cs_late_un
    $ cs_mz_quiet_reading_place_day3=renpy.cs_late_quiet
    $ cs_mz_book_prepared_day3=cs_friend_mz>=2
    $ cs_un_sketch_invite_day3=cs_un_sketch_time_agreed_day3=renpy.cs_late_sketch
    $ cs_mi_followup_invitation_day3=renpy.cs_late_mi
    $ cs_dv_followup_invitation_day3=renpy.cs_late_dv
    $ cs_lena_elbow_injury_day2=2
    $ cs_lena_elbow_bandaged=cs_viola_spare_bandage=cs_lena_no_sport_day2=True
    $ cs_helped_viola_day3=cs_helped_sl_day3=renpy.cs_late_help
    $ cs_friend_sl=2
    $ cs_day03_documents_location="administration"
    $ cs_sl_poster_collected_day3=bool(renpy.cs_late_poster)
    $ cs_day03_poster_location=renpy.cs_late_poster
    $ cs_day03_part07_done=True
    $ cs_mz_book_requested_day3=True
    $ set_mode_adv()
    $ day_time()
    $ persistent.sprite_time="day"
    call cs_day03_128
    jump cs_day03_part08

label cs_qa_day03_late_guard:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=cs_un_name_known=True
    $ cs_friend_mz=cs_friend_se=1
    $ cs_un_sketch_time_agreed_day3=True
    $ set_mode_adv()
    $ day_time()
    call cs_day03_129
    call cs_day03_130
    call cs_day03_zhenya_novel_choice
    call screen cs_qa_late_gate("Продолжить проверку книги")
    call cs_day03_zhenya_novel_choice
    call cs_day03_135
    call cs_day03_135
    call screen cs_qa_late_gate("Перейти к проверке Семёна")
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    $ cs_frame_focus(["cs_darya","cs_semen"])
    call cs_day03_140
    call cs_day03_semen_square_choice
    call screen cs_qa_late_gate("Повторить выбор Семёна")
    call cs_day03_semen_square_choice
    call cs_day03_141
    call screen cs_qa_late_gate("Завершить проверку")
    label cs_check_late_guard_end:
    $ renpy.cs_late_fast=False
    cs_narrator "Конец проверки повторов."
    return

screen cs_qa_late_gate(caption):
    modal True
    textbutton caption align (0.5,0.5) action Return()
'''
setup='''    pause 0.5
    $ persistent.font_size="small"
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps=0
    $ _preferences.transitions=2
    $ _test.force=True
    $ _test.timeout=120.0
    $ renpy.cs_late_fast=True
    $ renpy.cs_late_pending=None
    $ renpy.cs_late_cast=()
    $ renpy.cs_late_count=0
    $ renpy.cs_late_loans=0
    $ renpy.cs_late_visited=[]
'''
cases=[]
for mz in range(4):
    for book in (False,True):
        i=len(cases);cases.append(dict(mz=mz,se=mz,book_yes=book,se_yes=not book,un=3 if i%2 else 2,
            sketch=i%3!=0,quiet=mz>=3,mi=i%4 in (1,3),dv=i%4 in (2,3),help=i%2==0,poster='darya_folder' if i%2 else None))
cases.append(dict(mz=3,se=3,book_yes=True,se_yes=True,un=3,sketch=True,quiet=False,mi=True,dv=True,help=True,poster='darya_folder'))
for i,case in enumerate(cases):
    out+='\ntestcase cs_day03_late_%d:\n'%i+setup
    out+=''.join('    $ renpy.cs_late_%s=%r\n'%(k,v) for k,v in case.items())
    out+='    $ renpy.cs_late_auto=True\n    $ renpy.cs_p6_case="late_%d"\n'%i
    out+='''    run Start("cs_qa_day03_late")
    click until label cs_check_day03_part09_complete
    pause 0.5
    assert cs_day03_part08_done and cs_day03_part09_done
    assert cs_day03_reading_book_id=="goncharov_ordinary_story"
    assert cs_day03_reading_book_location=="house_table" and cs_mz_book_borrowed_day3
    assert renpy.cs_late_loans==1
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2 and cs_viola_spare_bandage
    assert cs_lena_elbow_injury_day2==2 and cs_day03_documents_location=="administration"
    assert cs_friend_sl==2
    assert not any(renpy.showing(t) for t in cs_presence_tags)
'''
    for variable,value in dict(cs_friend_mz=case['mz']+int(case['book_yes']),cs_mz_friend_on_arrival_day3=case['mz'],
      cs_friend_se=case['se']+int(case['se_yes']),cs_se_friend_before_square_day3=case['se'],
      cs_un_sketch_completed_day3=case['sketch'],cs_un_private_drawing_shown_day3=case['sketch'] and case['un']>=3,
      cs_day03_solo_sketch_done=not case['sketch'],cs_se_sketch_spot_day3=case['se']>=2 and case['se_yes'] and case['sketch'],
      cs_mz_open_library_invitation_day3=case['mz']>=3 and case['quiet'],cs_mz_quiet_reading_place_day3=case['quiet'],
      cs_mi_followup_invitation_day3=case['mi'],cs_dv_followup_invitation_day3=case['dv'],
      cs_day03_poster_location='house_table' if case['poster'] else None,cs_day03_poster_stored_home=bool(case['poster'])).items():
        out+='    assert '+variable+'=='+repr(value)+'\n'
    out+='''    $ cs_p6_capture("complete")
    $ renpy.take_screenshot()
    $ renpy.save("late_complete")
    $ renpy.load("late_complete")
    pause 0.5
    assert cs_mz_book_borrowed_day3 and cs_day03_reading_book_location=="house_table"
'''
    out+='    $ open(config.basedir+"/late_%d_PASS.txt","w").write("PASS")\n    run Quit(confirm=False)\n'%i
out+='\ntestcase cs_day03_late_guard:\n'+setup+'''    $ renpy.cs_late_auto=False
    $ renpy.cs_p6_case="late_guard"
    run Start("cs_qa_day03_late_guard")
    click until label cs_check_day03_134_menu
    pause 0.5
    $ renpy.take_screenshot()
    $ renpy.save("late_book_menu")
    $ renpy.load("late_book_menu")
    pause 0.5
    "Спросить Женю, что ей самой нравится в этой истории"
    "Продолжить проверку книги"
    "Спросить Женю, что ей самой нравится в этой истории"
    "Перейти к проверке Семёна"
    click until label cs_check_day03_140_menu
    pause 0.5
    assert cs_friend_mz==2 and cs_mz_friend_on_arrival_day3==1
    assert not cs_mz_open_library_invitation_day3 and renpy.cs_late_loans==1
    $ renpy.take_screenshot()
    $ renpy.save("late_semen_menu")
    $ renpy.load("late_semen_menu")
    pause 0.5
    "Остаться и поговорить с Семёном по-настоящему"
    "Повторить выбор Семёна"
    "Остаться и поговорить с Семёном по-настоящему"
    "Завершить проверку"
    pause 0.5
    assert cs_friend_se==2 and cs_se_friend_before_square_day3==1
    assert not cs_se_sketch_spot_day3
    $ cs_p6_capture("no_repeat_or_retroactive_bonus")
    $ open(config.basedir+"/late_guard_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/day03_late_test.rpy.txt').write_text(out,encoding='utf8')
print('9 mixed threshold routes + real menu save/load and reward/loan repeat guard generated.')

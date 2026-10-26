from pathlib import Path
R=Path(__file__).resolve().parent.parent
cases=[]
for mz in range(4):
 for help in (False,True):
  for yes in (False,True):
   n=len(cases);cases.append(dict(name=str(n),mz=mz,help=help,yes=yes,sl=(n//2)%3,se=bool(n%3),opened=bool(mz>=3 and yes),quiet=bool(mz>=3 and yes),completed=False,legacy=False))
for sl,yes in ((1,True),(2,False)):
 cases.append(dict(name=str(len(cases)),mz=4,help=True,yes=yes,sl=sl,se=True,opened=True,quiet=False,completed=True,legacy=True))
cases.append(dict(name='guard',mz=2,help=True,yes=True,sl=1,se=False,opened=False,quiet=False,completed=False,legacy=False))
s='''# -*- coding: utf-8 -*-
init 101 python:
    renpy.cs_p12_fast=False
    renpy.cs_p12_auto=False
    cs_p12_old_say=config.say_arguments_callback
    cs_p12_old_labels=config.label_callback
    cs_p12_old_args=config.menu_arguments_callback
    def cs_p12_audio_check():
        if not cs_day03_started:return
        target=cs_day03_audio_target(cs_day03_audio_location) if cs_day03_audio_location else False
        if target is not False:
            assert renpy.music.get_playing(channel="ambience")==target, "Wrong room ambience: %r -> %r"%(cs_day03_audio_location,renpy.music.get_playing(channel="ambience"))
    def cs_p12_say(who,*args,**kwargs):
        if cs_p12_old_say:args,kwargs=cs_p12_old_say(who,*args,**kwargs)
        if renpy.cs_p12_fast:
            kwargs["interact"]=False
            for c,t in ((cs_da,"cs_darya"),(cs_mz,"cs_zhenya"),(cs_sy,"cs_semen"),(cs_sl,"sl")):
                if who is c:assert renpy.showing(t),"Speaking actor missing: "+t
        return args,kwargs
    def cs_p12_menu(items,*args,**kwargs):
        v=[v for l,v in items if v is not None][0 if renpy.cs_p12_yes else -1]
        return v() if callable(v) else v
    def cs_p12_args(*args,**kwargs):
        if cs_p12_old_args:args,kwargs=cs_p12_old_args(*args,**kwargs)
        if renpy.cs_p12_auto:store.menu=cs_p12_menu
        return args,kwargs
    def cs_p12_labels(name,abnormal):
        if cs_p12_old_labels:cs_p12_old_labels(name,abnormal)
        if not renpy.cs_p12_fast:return
        assert name not in ("cs_day03_161a","cs_day03_161b","cs_day03_162","cs_day03_154","cs_check_day03_152_horn"),"Old dinner replayed"
        if name=="cs_check_day03_169_help_completed":renpy.cs_p12_helps+=1
        if name=="cs_check_day03_166_book_taken":renpy.cs_p12_books+=1
        if name.startswith("cs_day03_16") or name=="cs_day03_170":renpy.cs_p12_pending=name
        if name=="cs_check_day03_part12_complete":renpy.cs_p12_pending=None
    def cs_p12_capture(event,**kwargs):
        if event!="show_done" or not renpy.cs_p12_fast:return
        cs_p12_audio_check()
        if renpy.showing("bg"):
            assert renpy.has_image(("bg",)+tuple(renpy.get_attributes("bg"))),"Unregistered background"
        cast=tuple(sorted(t for t in cs_presence_tags if renpy.showing(t)))
        background=tuple(sorted((t,tuple(renpy.get_attributes(t) or ())) for t in renpy.get_showing_tags() if t not in cs_presence_tags))
        if renpy.cs_p12_pending or cast!=renpy.cs_p12_cast or background!=getattr(renpy,"cs_p12_background",()):
            renpy.cs_p12_count+=1
            renpy.pause(0.25,hard=True)
            cs_p6_capture("%02d_%s"%(renpy.cs_p12_count,renpy.cs_p12_pending or "cast"))
            if len(cast)==1:
                x,y,w,h=renpy.get_image_bounds(cast[0]);assert abs(x+w/2.0-960)<2
            renpy.cs_p12_cast=cast;renpy.cs_p12_pending=None
            renpy.cs_p12_background=background
    config.say_arguments_callback=cs_p12_say
    config.menu_arguments_callback=cs_p12_args
    config.label_callback=cs_p12_labels
    config.all_character_callbacks.append(cs_p12_capture)

label cs_qa_p12_setup:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=cs_day03_started=True
    $ cs_friend_mz=renpy.cs_p12_mz+int(renpy.cs_p12_help)
    $ cs_mz_dinner_friend_on_arrival=renpy.cs_p12_mz
    $ cs_mz_friend_on_arrival_day3=min(cs_friend_mz,3)
    $ cs_mz_open_library_invitation_day3=renpy.cs_p12_open
    $ cs_mz_quiet_reading_place_day3=renpy.cs_p12_quiet
    $ cs_mz_evening_help_day3=renpy.cs_p12_help
    $ cs_mz_evening_help_completed_day3=renpy.cs_p12_completed
    $ cs_mz_evening_choice_done=True
    $ cs_friend_sl=renpy.cs_p12_sl
    $ cs_friend_se=2 if renpy.cs_p12_se else 0
    $ cs_se_day3_personal_talk=renpy.cs_p12_se
    $ cs_mi_followup_invitation_day3=cs_dv_followup_invitation_day3=True
    $ cs_mi_followup_target_day=cs_dv_followup_target_day=4
    $ cs_mz_book_borrowed_day3=cs_day03_novel_selected=True
    $ cs_day03_reading_book_id="goncharov_ordinary_story"
    $ cs_day03_reading_book_location=cs_day03_sketchbook_location="house_table"
    $ cs_day03_poster_location="house_table"
    $ cs_sl_poster_collected_day3=cs_day03_poster_stored_home=True
    $ cs_day03_part11_done=cs_day03_dinner_horn_played=cs_day03_dinner_arrived=cs_day03_dinner_finished=True
    $ cs_lena_elbow_bandaged=cs_lena_no_sport_day2=cs_viola_spare_bandage=True
    $ cs_lena_elbow_injury_day2=2
    $ cs_day03_documents_location="administration"
    $ set_mode_adv()
    $ sunset_time()
    $ persistent.sprite_time="sunset"
    return

label cs_qa_p12_route:
    call cs_qa_p12_setup
    if renpy.cs_p12_legacy:
        jump cs_day03_part12_from_legacy
    jump cs_day03_part12

label cs_qa_p12_guard:
    call cs_qa_p12_setup
    $ cs_day03_part12_started=True
    call cs_day03_163
    call cs_day03_164
    call cs_day03_165
    call cs_day03_slavya_evening_choice
    call screen cs_qa_p12_gate
    call cs_day03_slavya_evening_choice
    call cs_day03_166
    call cs_day03_167
    call cs_day03_168
    call cs_day03_169a
    call cs_day03_169a
    call cs_day03_170
    call screen cs_qa_p12_gate
    $ cs_day03_part12_done=True
    jump cs_day03_part12

screen cs_qa_p12_gate():
    modal True
    textbutton "Продолжить проверку" action Return() align (0.5,0.5)
'''
for c in cases:
 name=c['name'];guard=name=='guard'
 s+='\ntestcase cs_p12_'+name+':\n    pause 0.5\n    $ persistent.font_size="small"\n    $ renpy.set_physical_size((1280,720))\n    $ _preferences.text_cps=0\n    $ _preferences.transitions=2\n    $ _test.force=True\n    $ _test.timeout=100.0\n'
 vals=dict(fast=True,auto=not guard,yes=c['yes'],mz=c['mz'],help=c['help'],sl=c['sl'],se=c['se'],open=c['opened'],quiet=c['quiet'],completed=c['completed'],legacy=c['legacy'],count=0,helps=0,books=0,cast=(),pending=None)
 s+=''.join('    $ renpy.cs_p12_'+k+'='+repr(v)+'\n' for k,v in vals.items())
 s+='    $ renpy.cs_p6_case="p12_'+name+'"\n    run Start("'+('cs_qa_p12_guard' if guard else 'cs_qa_p12_route')+'")\n'
 if guard:s+='''    pause 15.0
    $ renpy.take_screenshot()
    $ renpy.save("p12_menu")
    $ renpy.load("p12_menu")
    pause 0.5
    "Предложить помочь сверить завтрашние поручения"
    "Продолжить проверку"
    "Продолжить проверку"
    pause 0.5
    assert renpy.get_screen("cs_day03_part12_wait_screen") is not None
'''
 else:s+='    click until label cs_check_day03_part12_complete\n    pause 0.5\n'
 expected=dict(cs_friend_sl=c['sl']+int(c['yes']),cs_sl_friend_before_evening_choice=c['sl'],cs_sl_evening_schedule_help_day3=c['yes'],cs_sl_day4_notice_offer=c['sl']>=2 and c['yes'],cs_friend_mz=c['mz']+int(c['help']),cs_friend_se=2 if c['se'] else 0,cs_mz_evening_help_completed_day3=c['help'],cs_day03_darya_destination='library' if c['help'] else 'music_club',cs_day03_reading_book_location='with_lena',cs_day03_sketchbook_location='house_table',cs_day03_poster_location='house_table',cs_mz_open_library_invitation_day3=c['opened'],cs_mz_quiet_reading_place_day3=c['quiet'])
 s+=''.join('    assert '+k+'=='+repr(v)+'\n' for k,v in expected.items())
 s+='''    assert cs_day03_part12_done and cs_day03_dinner_finished and cs_day03_evening_book_retrieved
    assert cs_mi_followup_invitation_day3 and cs_dv_followup_invitation_day3
    assert cs_mi_followup_target_day==cs_dv_followup_target_day==4
    assert cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2==2 and cs_viola_spare_bandage
    assert cs_day03_documents_location=="administration"
    assert not renpy.showing("cs_semen") and not renpy.showing("sl")
    assert not renpy.showing("cs_darya")
    $ open(config.basedir+"/p12_final_audio_state.txt","w").write(repr(([(t,renpy.get_attributes(t)) for t in renpy.get_showing_tags()],cs_day03_audio_location,renpy.music.get_playing(channel="ambience"))))
    assert renpy.music.get_playing(channel="ambience") is None
'''
 s+='    assert renpy.cs_p12_helps=='+str(int(c['help'] and not c['completed']))+'\n    assert renpy.cs_p12_books==1\n'
 s+='''    $ renpy.take_screenshot()
    $ renpy.save("p12_'''+name+'''_end")
    $ renpy.load("p12_'''+name+'''_end")
    pause 0.5
    assert cs_friend_sl=='''+str(c['sl']+int(c['yes']))+'''
    $ cs_p6_capture("complete")
    $ open(config.basedir+"/p12_'''+name+'''_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/day03_part12_test.rpy.txt').write_text(s,encoding='utf8')
print('PART12_QA_GENERATED',len(cases),'cases')

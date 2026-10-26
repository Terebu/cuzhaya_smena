from pathlib import Path
R=Path(__file__).resolve().parent.parent
cases=[]
for mz in range(4):
 for help in (False,True):
  for yes in (False,True):
   n=len(cases);cases.append(dict(name=str(n),mz=mz,help=help,yes=yes,hug=bool(mz>=3 and help),honest=bool(mz>=2 and yes),prior=mz,open=bool(mz>=3 and yes)))
cases.append(dict(name='16',mz=3,help=True,yes=True,hug=False,honest=True,prior=0,open=False))
cases.append(dict(name='guard',mz=3,help=True,yes=True,hug=True,honest=True,prior=3,open=True))
s='''# -*- coding: utf-8 -*-
init 104 python:
    renpy.cs_p13_fast=False
    renpy.cs_p13_auto=False
    cs_p13_old_say=config.say_arguments_callback
    cs_p13_old_labels=config.label_callback
    cs_p13_old_args=config.menu_arguments_callback
    def cs_p13_say(who,*args,**kwargs):
        if cs_p13_old_say:args,kwargs=cs_p13_old_say(who,*args,**kwargs)
        if renpy.cs_p13_fast:
            kwargs["interact"]=False
            if who is cs_da:assert renpy.showing("cs_darya"),"Speaking Darya missing"
            if who is cs_mz:assert renpy.showing("cs_zhenya"),"Speaking Zhenya missing"
        return args,kwargs
    def cs_p13_menu(items,*args,**kwargs):
        v=[v for l,v in items if v is not None][0 if renpy.cs_p13_yes else -1]
        return v() if callable(v) else v
    def cs_p13_args(*args,**kwargs):
        if cs_p13_old_args:args,kwargs=cs_p13_old_args(*args,**kwargs)
        if renpy.cs_p13_auto:store.menu=cs_p13_menu
        return args,kwargs
    def cs_p13_labels(name,abnormal):
        if cs_p13_old_labels:cs_p13_old_labels(name,abnormal)
        if not renpy.cs_p13_fast:return
        assert name not in ("cs_day03_154","cs_day03_163","cs_day03_164","cs_day03_169a","cs_day03_170"),"Prior meal/work replay"
        if name=="cs_check_day03_174_book_returned":renpy.cs_p13_returns+=1
        if name=="cs_check_day03_175_first_hug":renpy.cs_p13_hugs+=1
        if name.startswith("cs_day03_17"):renpy.cs_p13_pending=name
    def cs_p13_capture(event,**kwargs):
        if event!="show_done" or not renpy.cs_p13_fast:return
        target=cs_day03_audio_target(cs_day03_audio_location)
        if target is not False:assert renpy.music.get_playing(channel="ambience")==target
        cast=tuple(sorted(t for t in cs_presence_tags if renpy.showing(t)))
        assert not set(cast)-set(("cs_darya","cs_zhenya")),"Uninvited actor"
        if renpy.showing("cs_library_interior_night"):
            if cs_da_waiting_outside_library_day3 or not cs_mz_evening_help_completed_day3:assert "cs_darya" not in cast
        if renpy.showing("cs_library_exterior_night") or renpy.showing("cs_camp_path_night"):assert "cs_zhenya" not in cast
        background=tuple(sorted((t,tuple(renpy.get_attributes(t) or ())) for t in renpy.get_showing_tags() if t not in cs_presence_tags))
        if renpy.cs_p13_pending or cast!=renpy.cs_p13_cast or background!=getattr(renpy,"cs_p13_background",()):
            renpy.cs_p13_count+=1
            renpy.pause(0.25,hard=True)
            cs_p6_capture("%02d_%s"%(renpy.cs_p13_count,renpy.cs_p13_pending or "cast"))
            if len(cast)==1:
                x,y,w,h=renpy.get_image_bounds(cast[0]);assert abs(x+w/2.0-960)<2
            renpy.cs_p13_cast=cast;renpy.cs_p13_pending=None;renpy.cs_p13_background=background
    config.say_arguments_callback=cs_p13_say
    config.menu_arguments_callback=cs_p13_args
    config.label_callback=cs_p13_labels
    config.all_character_callbacks.append(cs_p13_capture)

label cs_qa_p13_setup:
    $ cs_reset_state()
    $ cs_active=cs_darya_known=cs_day03_started=True
    $ cs_day03_part11_done=cs_day03_part12_started=cs_day03_part12_done=True
    $ cs_friend_da=2
    $ cs_friend_mz=renpy.cs_p13_mz
    $ cs_friend_sl=2
    $ cs_friend_se=3
    $ cs_friend_mi=cs_friend_dv=cs_friend_un=2
    $ cs_mz_friend_on_arrival_day3=renpy.cs_p13_prior
    $ cs_mz_hug_allowed_day3=renpy.cs_p13_hug
    $ cs_mz_day3_honest_book_talk=renpy.cs_p13_honest
    $ cs_mz_open_library_invitation_day3=renpy.cs_p13_open
    $ cs_mz_quiet_reading_place_day3=renpy.cs_p13_open
    $ cs_mz_evening_help_day3=cs_mz_evening_help_completed_day3=renpy.cs_p13_help
    $ cs_mz_book_borrowed_day3=cs_day03_novel_selected=True
    $ cs_day03_reading_book_id="goncharov_ordinary_story"
    $ cs_day03_reading_book_location="with_lena"
    $ cs_day03_sketchbook_location=cs_day03_poster_location="house_table"
    $ cs_mi_followup_invitation_day3=cs_dv_followup_invitation_day3=cs_sl_day4_notice_offer=True
    $ cs_mi_followup_target_day=cs_dv_followup_target_day=4
    $ cs_un_sketch_completed_day3=cs_un_private_drawing_shown_day3=True
    $ cs_se_day3_personal_talk=cs_da_day3_music_talk=cs_da_day3_shared_silence=True
    $ cs_lena_elbow_bandaged=cs_viola_spare_bandage=True
    $ cs_lena_elbow_injury_day2=2
    $ cs_day03_documents_location="administration"
    $ set_mode_adv()
    $ sunset_time()
    return

label cs_qa_p13_route:
    call cs_qa_p13_setup
    jump cs_day03_part13

label cs_qa_p13_guard:
    call cs_qa_p13_setup
    call cs_day03_171
    call cs_day03_172
    call cs_day03_173
    call cs_day03_174
    call cs_day03_175
    call cs_day03_176
    call cs_day03_177
    call cs_day03_178
    call cs_day03_darya_night_choice
    call screen cs_qa_p13_gate
    call cs_day03_darya_night_choice
    call cs_day03_179
    $ cs_day03_part13_done=True
    jump cs_day03_part13

screen cs_qa_p13_gate():
    modal True
    textbutton "Продолжить проверку" action Return() align (0.5,0.5)
'''
for c in cases:
 name=c['name'];guard=name=='guard'
 s+='\ntestcase cs_p13_'+name+':\n    pause 0.5\n    $ persistent.font_size="small"\n    $ renpy.set_physical_size((1280,720))\n    $ _preferences.text_cps=0\n    $ _preferences.transitions=2\n    $ _test.force=True\n    $ _test.timeout=100.0\n'
 vals=dict(fast=True,auto=not guard,yes=c['yes'],mz=c['mz'],help=c['help'],hug=c['hug'],honest=c['honest'],prior=c['prior'],open=c['open'],count=0,returns=0,hugs=0,cast=(),pending=None)
 s+=''.join('    $ renpy.cs_p13_'+k+'='+repr(v)+'\n' for k,v in vals.items())
 s+='    $ renpy.cs_p6_case="p13_'+name+'"\n    run Start("'+('cs_qa_p13_guard' if guard else 'cs_qa_p13_route')+'")\n'
 if guard:s+='''    pause 15.0
    $ renpy.take_screenshot()
    $ renpy.save("p13_menu")
    $ renpy.load("p13_menu")
    pause 0.5
    "Рассказать Даше, почему меня задел финал книги"
    "Продолжить проверку"
    click until label cs_check_day03_part13_complete
    pause 0.5
    assert renpy.get_screen("cs_day03_part13_wait_screen") is not None
'''
 else:s+='    click until label cs_check_day03_part13_complete\n    pause 0.5\n'
 s+='    assert cs_friend_da=='+str(2+int(c['yes']))+'\n'
 s+='    assert cs_friend_mz=='+str(c['mz'])+'\n'
 for k,v in dict(cs_da_day3_fear_of_getting_used_to_camp=c['yes'],cs_da_day3_quiet_walk=not c['yes'],cs_mz_day3_final_discussion=c['honest'],cs_mz_hug_allowed_day3=c['hug'] or c['mz']>=3,cs_mz_evening_help_completed_day3=c['help']).items():s+='    assert '+k+'=='+repr(v)+'\n'
 s+='    assert renpy.cs_p13_hugs=='+str(int(c['mz']>=3 and not c['hug']))+'\n'
 s+='''    assert renpy.cs_p13_returns==1
    assert cs_day03_part13_done and cs_da_day3_night_choice_done
    assert cs_mz_book_finished_day3 and not cs_mz_book_borrowed_day3
    assert cs_day03_reading_book_location=="library" and cs_day03_darya_destination=="house"
    assert cs_day03_sketchbook_location==cs_day03_poster_location=="house_table"
    assert cs_friend_sl==2 and cs_friend_se==3 and cs_friend_mi==cs_friend_dv==cs_friend_un==2
    assert cs_mi_followup_invitation_day3 and cs_dv_followup_invitation_day3 and cs_sl_day4_notice_offer
    assert cs_mi_followup_target_day==cs_dv_followup_target_day==4
    assert cs_un_sketch_completed_day3 and cs_un_private_drawing_shown_day3
    assert cs_se_day3_personal_talk and cs_da_day3_music_talk and cs_da_day3_shared_silence
    assert cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2==2 and cs_viola_spare_bandage
    assert cs_day03_documents_location=="administration"
    assert not renpy.showing("cs_zhenya")
    assert not cs_da_waiting_outside_library_day3
    $ renpy.take_screenshot()
    $ renpy.save("p13_'''+name+'''_end")
    $ renpy.load("p13_'''+name+'''_end")
    pause 0.5
    assert cs_mz_book_finished_day3 and not cs_mz_book_borrowed_day3
    $ cs_p6_capture("complete")
    $ open(config.basedir+"/p13_'''+name+'''_PASS.txt","w").write("PASS")
    run Quit(confirm=False)
'''
(R/'tools/day03_part13_test.rpy.txt').write_text(s,encoding='utf8')
print('PART13_QA_GENERATED',len(cases),'cases')

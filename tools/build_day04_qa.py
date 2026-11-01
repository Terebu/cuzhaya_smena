from pathlib import Path
import re,subprocess,sys
R=Path(__file__).resolve().parent.parent
# Keep the earlier 3-day checkpoints, extend the same actual renderer traversal.
subprocess.run([sys.executable,str(R/'tools/build_full_render_walkthrough_qa.py')],check=True)
s=(R/'tools/full_render_walkthrough_test.rpy.txt').read_text(encoding='utf8')
s=s.replace('day0[123]','day0[1234]')
s=s.replace('renpy.has_image(("bg",)+tuple(renpy.get_attributes("bg")))','renpy.has_image(("bg",)+tuple(renpy.get_attributes("bg")),exact=True)')
at='    def cs_rw_character(event,**kwargs):'
extra='''        if name=="cs_check_day04_complete":
            assert cs_day04_done and cs_day04_started
            assert cs_d4_found_1971_records and cs_d4_unknown_girl_seen and cs_d4_heard_unknown_voice
            assert cs_d4_elbow_bandage_removed and not cs_lena_elbow_bandaged
            assert cs_d4_olga_has_undated_photo and cs_d4_mz_has_1971_photo
            assert cs_d4_undated_photo_location=="olga"
            assert cs_d4_photo1971_location==cs_d4_roster_location==cs_d4_dream_notes_location=="library_locked_drawer"
            assert cs_d4_mz_dream_record_written and cs_d4_dream_phrase_second
            assert cs_d4_mz_friend_before_choice==5*int(renpy.cs_rw_positive)
            assert cs_friend_mz==6*int(renpy.cs_rw_positive)
            assert cs_friend_se==5*int(renpy.cs_rw_positive)
            assert cs_friend_da==4*int(renpy.cs_rw_positive)
            assert cs_friend_dv==3*int(renpy.cs_rw_positive)
            assert bool(cs_d4_shared_bed)==renpy.cs_rw_positive
            assert not renpy.music.get_playing(channel="ambience") and not renpy.music.get_playing(channel="music")
            if renpy.cs_rw_positive:
                assert cs_mi_followup_invitation_day3 and cs_dv_followup_invitation_day3
                assert cs_mi_followup_target_day==cs_dv_followup_target_day==5
                assert cs_d4_sl_notice_deferred
            with open(config.basedir+"/rw_"+renpy.cs_rw_route+"_state.json","w") as f:
                cs_rw_json.dump(dict(status="PASS",visited=renpy.cs_rw_visited,screenshots=renpy.cs_rw_count,day4=True,friendship=dict(da=cs_friend_da,mz=cs_friend_mz,se=cs_friend_se,dv=cs_friend_dv,viola=cs_friend_viola)),f)
'''
s=s.replace(at,extra+at)
s=s.replace('click until label cs_check_day03_part14_complete','click until label cs_check_day04_complete')
# New day: capture each real location change even when the cast stays the same.
s=s.replace('        if pending:\n', '''        if cs_day04_started:
            bg=tuple(sorted((t,tuple(renpy.get_attributes(t) or ())) for t in renpy.get_showing_tags() if t not in cs_presence_tags))
            if bg!=getattr(renpy,"cs_rw_last_bg",()):
                pending=pending or "location"
            renpy.cs_rw_last_bg=bg
        if pending:
''')
(R/'tools/full_render_walkthrough_test.rpy.txt').write_text(s,encoding='utf8')

qa='''# -*- coding: utf-8 -*-
init 110 python:
    import json as cs_d4_qa_json
    renpy.cs_d4_qa=False
    cs_d4_qa_old_say=config.say_arguments_callback
    cs_d4_qa_old_args=config.menu_arguments_callback
    cs_d4_qa_old_labels=config.label_callback
    def cs_d4_qa_say(who,*args,**kwargs):
        if cs_d4_qa_old_say:args,kwargs=cs_d4_qa_old_say(who,*args,**kwargs)
        if renpy.cs_d4_qa:kwargs["interact"]=False
        return args,kwargs
    def cs_d4_qa_menu(items,*args,**kwargs):
        opts=[v for l,v in items if v is not None]
        i=renpy.cs_d4_qa_menu_count
        renpy.cs_d4_qa_menu_count+=1
        v=opts[renpy.cs_d4_qa_choices[i]]
        return v() if callable(v) else v
    def cs_d4_qa_args(*args,**kwargs):
        if cs_d4_qa_old_args:args,kwargs=cs_d4_qa_old_args(*args,**kwargs)
        if renpy.cs_d4_qa:store.menu=cs_d4_qa_menu
        return args,kwargs
    def cs_d4_qa_labels(name,abnormal):
        if cs_d4_qa_old_labels:cs_d4_qa_old_labels(name,abnormal)
        if renpy.cs_d4_qa and name=="cs_check_day_title":
            renpy.pause(0.2,hard=True)
            cs_p6_capture("day4_title")
        if renpy.cs_d4_qa and name.startswith("cs_day04_"):
            renpy.cs_d4_qa_pending=name
    def cs_d4_qa_capture(event,**kwargs):
        if not renpy.cs_d4_qa or event!="show_done":return
        if renpy.showing("bg"):
            assert renpy.has_image(("bg",)+tuple(renpy.get_attributes("bg")),exact=True),"Missing exact background"
        tags=tuple(sorted(renpy.get_showing_tags()))
        attrs=tuple((t,tuple(renpy.get_attributes(t) or ())) for t in tags)
        target=cs_day03_audio_target(cs_day03_audio_location) if cs_day03_audio_location else False
        if target is not False:assert renpy.music.get_playing(channel="ambience")==target
        if renpy.cs_d4_qa_pending or attrs!=getattr(renpy,"cs_d4_qa_frame",()):
            renpy.cs_d4_qa_count+=1
            renpy.pause(0.3,hard=True)
            cs_p6_capture("%03d_%s"%(renpy.cs_d4_qa_count,renpy.cs_d4_qa_pending or "cast"))
            for t in cs_presence_tags:
                if renpy.showing(t):
                    x,y,w,h=renpy.get_image_bounds(t)
                    assert y<300 and h>500,"Wrong actor vertical baseline"
            live=[t for t in cs_presence_tags if renpy.showing(t)]
            if len(live)==1:
                x,y,w,h=renpy.get_image_bounds(live[0]);assert abs(x+w/2.0-960)<2
            renpy.cs_d4_qa_frame=attrs;renpy.cs_d4_qa_pending=None
    config.say_arguments_callback=cs_d4_qa_say
    config.menu_arguments_callback=cs_d4_qa_args
    config.label_callback=cs_d4_qa_labels
    config.all_character_callbacks.append(cs_d4_qa_capture)

label cs_qa_day04:
    $ cs_reset_state()
    $ cs_active=cs_day03_started=cs_darya_known=cs_slavya_known=cs_olga_seen=True
    $ cs_day03_part14_done=cs_day03_completed=True
    $ cs_lena_elbow_bandaged=True
    $ cs_friend_mz=renpy.cs_d4_qa_mz
    $ cs_friend_da=2
    $ cs_friend_se=cs_friend_dv=cs_friend_viola=1
    $ cs_mz_hug_allowed_day3=renpy.cs_d4_qa_hug
    $ cs_da_shared_bed_day3=renpy.cs_d4_qa_shared
    $ cs_da_love_confession_day3=renpy.cs_d4_qa_confess
    $ cs_mi_followup_invitation_day3=cs_dv_followup_invitation_day3=cs_sl_day4_notice_offer=True
    $ set_mode_adv()
    jump cs_day04
'''
cases=[(0,False,False,False,[0]*7),(2,True,True,False,[0]*7),(3,True,True,True,[1]*7),(3,False,False,False,[0,1,0,1,0,1,0])]
for n,(mz,hug,shared,confess,choices) in enumerate(cases):
 qa+='\ntestcase cs_day04_matrix_'+str(n)+':\n    pause 0.5\n    $ persistent.font_size="small"\n    $ renpy.set_physical_size((1280,720))\n    $ _preferences.text_cps=0\n    $ _preferences.transitions=2\n    $ _test.force=True\n    $ _test.timeout=120.0\n'
 vals=dict(qa=True,qa_mz=mz,qa_hug=hug,qa_shared=shared,qa_confess=confess,qa_choices=choices,qa_menu_count=0,qa_count=0,qa_pending=None,qa_frame=())
 qa+=''.join('    $ renpy.cs_d4_'+k+'='+repr(v)+'\n' for k,v in vals.items())
 qa+='    $ renpy.cs_p6_case="day04_matrix_'+str(n)+'"\n    run Start("cs_qa_day04")\n    click until label cs_check_day04_complete\n    pause 0.5\n'
 qa+='    assert cs_day04_done and renpy.cs_d4_qa_menu_count==7\n'
 qa+='    assert cs_d4_mz_hug_09==cs_d4_mz_hug_12=='+repr(mz>=3 and hug)+'\n'
 for key,value in dict(cs_friend_se=1+int(choices[1]==0),cs_friend_viola=1+int(choices[3]==0),cs_friend_dv=1+int(choices[4]==0),cs_friend_mz=mz+int(choices[5]==0),cs_friend_da=2+int(choices[6]==0),cs_d4_mz_friend_before_choice=mz,cs_d4_left_note=choices[0]==0,cs_d4_shared_bed=shared).items():qa+='    assert '+key+'=='+repr(value)+'\n'
 qa+='''    assert cs_d4_elbow_bandage_removed and not cs_lena_elbow_bandaged
    assert cs_d4_photo1971_location==cs_d4_roster_location==cs_d4_dream_notes_location=="library_locked_drawer"
    assert cs_d4_undated_photo_location=="olga"
    assert cs_mi_followup_invitation_day3 and cs_dv_followup_invitation_day3
    assert cs_mi_followup_target_day==cs_dv_followup_target_day==5
    $ renpy.take_screenshot()
'''
 qa+='    $ renpy.save("day04_matrix_'+str(n)+'")\n    $ renpy.load("day04_matrix_'+str(n)+'")\n    pause 0.5\n    assert cs_day04_done\n    $ cs_p6_capture("complete")\n'
 qa+='    $ open(config.basedir+"/day04_matrix_'+str(n)+'_PASS.txt","w").write("PASS")\n    run Quit(confirm=False)\n'
(R/'tools/day04_test.rpy.txt').write_text(qa,encoding='utf8')
print('DAY04_QA_GENERATED',len(cases),'matrix routes + 2 full routes')

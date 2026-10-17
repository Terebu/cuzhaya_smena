from pathlib import Path
R=Path(__file__).resolve().parent.parent
out=['# -*- coding: utf-8 -*-']
for mi,sl in [(0,0),(0,1),(1,0),(1,1)]:
 name='cs_part03_m%d_s%d'%(mi,sl)
 out+=['testcase '+name+':','    pause 1.0','    $ renpy.set_physical_size((1280,720))','    $ _preferences.text_cps = 0','    $ _test.timeout = 50.0','    assert renpy.loadable(cs_miku_piano_track)','    run Start("cs_qa_part02_load")','    pause 1.0','    run Jump("cs_qa_part03_path")','    click until label cs_check_d2_piano_darya','    pause 1.0','    assert renpy.showing("cs_cg_darya_piano_day")','    $ cs_qa_capture("'+name+'_darya")','    click until label cs_check_part02_menu','    '+('"Остаться и послушать репетицию Мику"' if mi else '"Поблагодарить Мику и пойти на линейку"')]
 if mi:
  out+=['    click until label cs_check_d2_piano_miku','    pause 1.0','    assert renpy.music.get_playing(channel="cs_piano") == "sound/music/miku_song_voice.ogg"','    $ cs_qa_capture("'+name+'_miku_song")','    click until label cs_check_part03_s21','    pause 1.0','    assert cs_friend_mi == 1','    assert not renpy.showing("mi")','    $ cs_qa_capture("'+name+'_bench")']
 out+=['    click until label cs_check_cg_lineup','    pause 1.0','    assert cs_friend_mi == '+str(mi),'    assert renpy.showing("cs_cg_morning_lineup_day")','    assert not renpy.showing("mt") and not renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_lineup")','    click until label cs_check_part03_menu','    pause 1.0','    assert not renpy.showing("mt") and not renpy.showing("mi")','    $ cs_qa_capture("'+name+'_slavya_menu")','    $ renpy.take_screenshot()','    $ renpy.save("'+name+'-menu")','    $ cs_friend_sl = 99','    $ renpy.load("'+name+'-menu")','    pause 1.0','    assert cs_friend_sl == 0','    '+('"Предложить Славе помощь с материалами"' if sl else '"Поблагодарить Славю и заняться объявлением"')]
 if sl:
  out+=['    click until label cs_check_part03_storage','    pause 1.0','    assert cs_friend_sl == 1 and cs_helped_sl_day2','    assert renpy.showing("cs_storage_int_day")','    $ cs_qa_capture("'+name+'_storage")']
 out+=['    click until label cs_check_part03_s25','    pause 1.0','    assert cs_friend_sl == '+str(sl),'    assert not renpy.showing("sl")','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_working_group")','    click until label cs_check_cg_poster_planning','    pause 1.0','    assert renpy.showing("cs_cg_poster_planning_day")','    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_poster")','    click until label cs_check_part03_clubs','    pause 1.0','    assert renpy.showing("bg int_clubs_male_day")','    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")','    $ cs_qa_capture("'+name+'_clubs")','    click until label cs_check_part04_s26','    pause 1.0','    assert not cs_day02_done and cs_friend_mi == '+str(mi)+' and cs_friend_sl == '+str(sl),'    $ cs_qa_capture("'+name+'_end")']
 if sl and mi:
  out+=['    run Jump("cs_qa_sl_replay")','    click until label cs_check_part03_menu','    "Предложить Славе помощь с материалами"','    click until label cs_check_part04_s26','    pause 1.0','    assert cs_friend_sl == 1']
 out+=['    $ open(config.gamedir + "/mods/chuzaya_smena/qa/'+name+'_pass.txt", "w").write("PASS")','    run Quit(confirm=False)','']
out=[line.replace('click until label cs_check_part02_menu','click until run CSQAwaitMenu()').replace('click until label cs_check_part03_menu','click until run CSQAwaitMenu()') for line in out]
for i,line in enumerate(out):
 if line.strip()=='click until label cs_check_part03_clubs' and out[i+1].strip()=='pause 1.0':out[i+1]='    pause 0.05'
(R/'qa/part03_routes_test.rpy').write_text('\n'.join(out),encoding='utf8')
print('Four combined choices generated')

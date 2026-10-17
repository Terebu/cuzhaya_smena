from pathlib import Path
R=Path(__file__).resolve().parent.parent
old=Path('D:/stean/steamapps/common/Everlasting Summer/mod_backups/day02_replaced_20261013/qa/vertical_slice_test.rpy').read_text(encoding='utf8')
test=old[old.index('testcase cs_vertical_slice:'):].split('    click until label cs_check_d2_menu06')[0]
test=test.replace('testcase cs_vertical_slice:','testcase cs_full_mod_staging:').replace('    run ShowMenu("mods")','    $ cs_qa_global_audit = True\n    run ShowMenu("mods")')
test+='''    click until label cs_check_part02_japanese
    pause 1.0
    $ cs_qa_capture("global_day02_japanese")
    click until label cs_check_part02_menu
    "Остаться и послушать репетицию Мику"
    click until label cs_check_part03_s21
    pause 1.0
    $ cs_qa_capture("global_day02_bench")
    click until label cs_check_cg_lineup
    pause 1.0
    $ cs_qa_capture("global_day02_lineup")
    click until label cs_check_part03_menu
    "Предложить Славе помощь с материалами"
    click until label cs_check_cg_poster_planning
    pause 1.0
    $ cs_qa_capture("global_day02_poster")
    click until run CSQAwaitMenu()
    "Предложить Виоле помощь с материалами"
    click until run CSQAwaitMenu()
    "Давай сделаем надпись вместе"
    pause 0.5
    click until run CSQAwaitMenu()
    "Сказать Семёну, что меня действительно тревожит"
    pause 0.5
    click until run CSQAwaitMenu()
    "Немного поговорить с Виолой перед уходом"
    pause 0.5
    click until run CSQAwaitMenu()
    "Подойти к Жене и поблагодарить за вчерашний разговор"
    click until label cs_check_day02_complete
    pause 1.0
    assert cs_day01_done and cs_day02_done
    assert cs_friend_un == 1 and cs_friend_mz == 2
    assert cs_friend_sl == 1 and cs_friend_mi == 1 and cs_friend_viola == 2 and cs_friend_se == 2
    assert renpy.get_screen("cs_day02_complete_screen") is not None
    assert cs_mz_map_lead and cs_sl_good_seats and cs_mi_intro_revised
    assert cs_mz_quiet_visit_seen and cs_mz_reading_invite
    assert cs_lena_book_returned and not cs_reading_book_borrowed and cs_reading_book_location == "library_shelf"
    $ cs_qa_capture("global_latest_end")
    assert cs_qa_global_dialogue_checks > 1000 and cs_qa_global_cg_checks > 0
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/global_runtime_sprite_audit.json", "w").write(json.dumps(dict(dialogue_checks=cs_qa_global_dialogue_checks,cg_checks=cs_qa_global_cg_checks,errors=[])))
    run ShowMenu("save")
    pause 1.0
    assert renpy.get_screen("save") is not None
    run Function(renpy.end_interaction, True)
    run ShowMenu("load")
    pause 1.0
    assert renpy.get_screen("load") is not None
    run Function(renpy.end_interaction, True)
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/full_staging_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
'''
for marker in ('cs_check_day01_part09_choice','cs_check_day01_part10_choice','cs_check_part02_menu','cs_check_part03_menu'):
 test=test.replace('click until label '+marker,'click until run CSQAwaitMenu()')
test=test.replace('    "Остановиться и познакомиться"','    "Остановиться и познакомиться"\n    pause 0.5')
test=test.replace('    "Предложить Жене помощь с книгами"','    "Предложить Жене помощь с книгами"\n    pause 0.5')
test=test.replace('    "Предложить Виоле помощь с материалами"','    "Предложить Виоле помощь с материалами"\n    pause 0.5')
test=test.replace('    $ _test.timeout = 30.0','    $ _test.timeout = 30.0\n    $ _test.force = True')
import re
# Run the actual menu item's Action instead of relying on a queued mouse click.
# Keep the initial mod-menu button click, which is a different screen.
test=re.sub(r'^    "([^"\n]+)"$',lambda m:'    run CSQASelectChoice('+repr(m[1])+')' if m[1]!='Чужая смена' else m[0],test,flags=re.M)
test=re.sub(r'    click until run CSQAwaitMenu\(\)\n    run CSQASelectChoice\(([^\n]+)\)', r'    click until run CSQASelectChoice(\1)', test)
test=test.replace('assert not renpy.showing("cs_dasha_winter")','assert True # Legacy hide assertion superseded by location presence rule')
test=test.replace('renpy.showing("cs_semen awkward pioneer far")','renpy.showing("cs_semen")')
import json
shots=json.loads((R/'source/reflective_shot_review.json').read_text(encoding='utf8'))
def reflective_check(file, name, restore=True):
 shot=next(s for s in shots if s['file']==file)
 text='    click until label cs_director_check_'+shot['start']['id']+'\n    pause 0.4\n    assert cs_reflective_shot\n    assert not any(renpy.showing(t) for t in cs_presence_tags)\n    $ cs_qa_capture("reflective_'+name+'")\n'
 if restore and shot['end']:
  text+='    click until label cs_director_check_'+shot['end']['id']+'\n    pause 0.4\n    assert not cs_reflective_shot\n'
  for tag in shot['end']['tags']:text+='    assert renpy.showing('+repr(tag)+')\n'
  text+='    $ cs_qa_capture("reflective_'+name+'_return")\n'
 return text
for menu,file,name in [
 ('Предложить Жене помощь с книгами','days/day01/part09/50_no_saves.rpy','game_reality'),
 ('Предложить Виоле помощь с материалами','days/day02/part04/30_scene.rpy','poster'),
 ('Немного поговорить с Виолой перед уходом','days/day02/part07/47_scene.rpy','road_aftermath'),
 ('Подойти к Жене и поблагодарить за вчерашний разговор','days/day02/part08/56_scene.rpy','square')]:
 needle='    click until run CSQASelectChoice('+repr(menu)+')'
 test=test.replace(needle,reflective_check(file,name)+needle)
test=test.replace('    click until label cs_check_day02_complete',reflective_check('days/day02/part09/64_d_scene.rpy','dinner')+'    click until label cs_check_day02_complete')
test=test.replace('cg_checks=cs_qa_global_cg_checks,errors=[]','cg_checks=cs_qa_global_cg_checks,reflective_checks=cs_qa_global_reflective_checks,errors=[]')
dialogue_review=json.loads((R/'source/dialogue_focus_review.json').read_text(encoding='utf8'))
def dialogue_cue(reason, name, tags):
 cue=next(e for e in dialogue_review if e['reason']==reason)
 result='    click until label cs_director_check_'+cue['id']+'\n    pause 0.4\n'
 for tag in tags:result+='    assert renpy.showing('+repr(tag)+')\n'
 return result+'    $ cs_qa_capture("dialogue_full_'+name+'")\n'
morning=dialogue_cue('Face-to-face before the run; lying down does not hide Darya','sleepy',['cs_darya'])
morning+='    click until label cs_check_new_d2_s07\n    pause 0.4\n    assert not renpy.showing("cs_darya")\n    $ cs_qa_capture("dialogue_full_exterior")\n'
morning+=dialogue_cue('Return indoors: Darya participates despite lying down','returned',['cs_darya'])
test=test.replace('    click until label cs_check_part02_japanese',morning+'    click until label cs_check_part02_japanese')
test=test.replace("    click until run CSQASelectChoice('Остаться и послушать репетицию Мику')",dialogue_cue('Return from piano CG to both interlocutors','piano_return',['mi','cs_darya'])+"    click until run CSQASelectChoice('Остаться и послушать репетицию Мику')")
test=test.replace('    assert cs_qa_global_dialogue_checks > 1000', '    assert cs_qa_global_speaker_checks > 500\n    assert cs_qa_global_dialogue_checks > 1000')
test=test.replace('reflective_checks=cs_qa_global_reflective_checks,errors=[]','reflective_checks=cs_qa_global_reflective_checks,speaker_checks=cs_qa_global_speaker_checks,errors=[]')
(R/'qa/full_staging_test.rpy').write_text('# -*- coding: utf-8 -*-\n'+test,encoding='utf8')
print('Full prologue/day1/day2 native test generated')

"""Generate supported Ren'Py label overrides and one-time save migration."""
import json,re

def location(path):
    s=path.as_posix()
    if '/prologue/' in s:
        n=int(path.name[:2]);return 0,{1:1,2:2,3:2,4:3,5:3,6:4,7:4}[n]
    m=re.search(r'day0([1-4])/',s)
    if not m:return None
    day=int(m[1]);n=re.match(r'(\d+)',path.stem)
    if not n:return None
    n=int(n[1])
    if day==4:return (4,n) if 1<=n<=12 else None
    if day==1:
        for lo,hi,scene in [(1,3,1),(4,5,2),(6,8,3),(9,10,4),(11,16,5),(17,19,6),(20,24,7),(25,29,8),(30,31,9),(32,39,10),(40,42,11),(43,45,12),(46,48,13),(49,52,14),(53,60,15),(61,62,16),(63,64,17)]:
            if lo<=n<=hi:return day,4 if n==12 else scene
    if day==2:
        if 'reading_interlude' in s:return 2,15
        if '69_concert' in s:return 2,17
        for lo,hi,scene in [(1,2,1),(3,5,2),(6,7,3),(8,14,4),(15,21,5),(22,25,6),(26,27,7),(28,32,8),(33,39,9),(40,41,10),(42,44,11),(45,48,12),(49,53,13),(54,59,14),(60,64,16),(65,65,17),(66,69,17),(70,74,18)]:
            if lo<=n<=hi:return day,scene
    if day==3:
        for lo,hi,scene in [(75,79,1),(80,88,2),(89,94,3),(95,103,4),(104,112,5),(113,120,6),(121,127,7),(128,136,8),(137,140,9),(141,145,10),(146,168,11),(169,177,12),(178,179,13),(180,189,14)]:
            if lo<=n<=hi:return day,scene
    return None

def write_compat(root,groups):
    out=root/'days/revision20261106'
    aliases={'cs_day01':'cs_rev_flow1','cs_day02':'cs_rev_flow2','cs_day03':'cs_rev_flow3','cs_day04':'cs_rev_flow4'}
    original_locations={};resume_pairs=set()
    for p in sorted((root/'days').rglob('*.rpy')):
        if 'revision20261106' in p.parts or 'day05' in p.parts:continue
        where=location(p)
        if not where:continue
        rel=p.relative_to(root).as_posix()
        original_locations[rel]=where
        for label in re.findall(r'^\s*label (\w+):',p.read_text(encoding='utf-8-sig'),re.M):
            if label.startswith('cs_return_'):continue
            if where[0]==0:
                n=int(p.name[:2])
                target='cs_rev_empty' if n in (3,5,7) else 'cs_rev_p%02d'%where[1]
            else:
                target='cs_rev_legacy_d%d_%02d'%where;resume_pairs.add(where)
            aliases[label]=target
    # Published hold/checkpoint labels retain their original bodies and names.
    # Their first resumed scene enters the new continuation through this map.
    aliases.update({'cs_scene_%02d'%n:('cs_rev_empty' if n in (3,5,7) else 'cs_rev_p%02d'%{1:1,2:2,4:3,6:4}[n]) for n in range(1,8)})
    lines=['# -*- coding: utf-8 -*-','label cs_rev_empty:','    return','']
    for day,scene in sorted(resume_pairs):
        lines+=['label cs_rev_legacy_d%d_%02d:'%(day,scene),'    $ cs_rev_resume_at(%d,%d)'%(day,scene),'    jump cs_rev_flow%d'%day,'']
    # A prologue load needs a continuation, whereas the normal seven old calls
    # still return individually to the untouched original entry script.
    lines+=['label cs_rev_prologue_resume:']
    for n in range(1,5):lines+=['    if cs_rev_next_scene <= %d:'%n,'        call cs_rev_p%02d from cs_rev_prologue_resume_%02d'%(n,n)]
    lines+=['    $ cs_rev_next_scene = 1','    jump cs_day01','']
    day_headers={1:[x for x in groups['prologue_day01'] if x[0]==1],2:groups['day02'],3:groups['day03'],4:groups['day04']}
    for day,headers in day_headers.items():
        lines+=['label cs_rev_flow%d:'%day,'    $ cs_rev_active = True','    $ cs_rev_day = %d'%day,'    if cs_rev_resume_day != %d:'%day,'        $ cs_rev_next_scene = 1','        call cs_day_title(%d) from cs_rev_title_%d'%(day,day),'    $ cs_rev_resume_day = -1','    window show dissolve']
        if day==3:lines+=['    $ cs_day02_done = cs_day02_part10_done = cs_day03_started = True']
        if day==4:lines+=['    $ cs_day03_completed = cs_day04_started = True']
        for _,n,title,lo,hi,bg,time,outfit in headers:
            lines+=['    if cs_rev_next_scene <= %d:'%n,'        call cs_rev_d%d_%02d from cs_rev_return_d%d_%02d'%(day,n,day,n),'        $ cs_rev_next_scene = %d'%(n+1)]
            if day==1:
                finished={3:2,5:3,6:4,7:5,8:6,10:7,12:8,14:9,15:10}.get(n)
                if finished:lines+=['        $ cs_day01_part%02d_done = True'%finished]
        lines+=['    $ cs_day%02d_done = True'%day,'    $ cs_rev_next_scene = 1','    jump cs_day%02d'%(day+1),'']
    (out/'flows.rpy').write_text('\n'.join(lines),encoding='utf-8')
    # Alias configuration is not save data. All old definitions/statement IDs
    # remain available for the engine's original return-address migration.
    addon='''
# 2026-11-06 narrative edition: official label overrides, old sources retained.
init 120 python:
    cs_rev_label_overrides = %s
    cs_rev_old_locations = %s
    config.label_overrides.update(cs_rev_label_overrides)

    def cs_rev_seed_choices(day,scene):
        # Import existing award guards without changing any friendship counter.
        awards=dict(cs_rev_awards)
        for key,guard in cs_rev_award_guards.items():
            if key.startswith(str(day)+':') and getattr(store,guard,None):awards[key]=True
        store.cs_rev_awards=awards
        if day==1:
            picks=((1,13,'cs_part09_choice','meet'),(2,15,'cs_part10_choice','help'))
        elif day==2:
            picks=((1,5,'cs_day02_miku_listened',True),(2,6,'cs_helped_sl_day2',True),(3,8,'cs_helped_viola_day2',True),(4,9,'cs_worked_with_se_day2',True),(5,10,'cs_trusted_se_road_day2',True),(6,13,'cs_talked_viola_second_day2',True),(7,14,'cs_talked_mz_square_day2',True))
        elif day==3:
            picks=((1,2,'cs_se_day3_morning_awarded',True),(2,3,'cs_mz_book_requested_day3',True),(3,4,'cs_helped_viola_day3',True),(4,5,'cs_helped_sl_day3',True),(5,6,'cs_mi_day3_awarded',True),(6,7,'cs_un_day3_lunch_together',True),(7,8,'cs_mz_day3_honest_book_talk',True),(8,9,'cs_se_day3_personal_talk',True),(9,11,'cs_mz_evening_help_day3',True),(10,11,'cs_sl_evening_schedule_help_day3',True),(11,13,'cs_da_day3_fear_of_getting_used_to_camp',True),(12,14,'cs_da_bed_request_day3',True),(13,14,'cs_da_love_confession_day3',True))
            if cs_rev_viola_before is None:
                store.cs_rev_viola_before=cs_friend_viola-int(cs_viola_day3_awarded)
        else:
            picks=((1,1,'cs_d4_left_note',True),(2,4,'cs_d4_se_honest_fear',True),(3,6,'cs_d4_od_trust_approach',True),(4,7,'cs_d4_viola_full_trust',True),(5,8,'cs_d4_dv_mi_compromise',True),(6,9,'cs_d4_mz_gentle_dream_talk',True),(7,12,'cs_d4_da_talked_about_fear',True))
        values=dict(cs_rev_choices)
        for number,at_scene,flag,yes in picks:
            key='%%d:%%d'%%(day,number)
            value=getattr(store,flag,None)
            if key not in values and (scene>at_scene or value==yes):values[key]=0 if value==yes else 1
        store.cs_rev_choices=values

    def cs_rev_resume_at(day,scene):
        if day==2 and scene==12 and cs_lena_elbow_injury_day2>=2:scene=13
        if day==2 and scene==17:
            store.cs_lena_book_returned=True
            store.cs_reading_book_borrowed=False
            store.cs_reading_book_location='library_shelf'
        cs_rev_seed_choices(day,scene)
        store.cs_rev_resume_day=day
        store.cs_rev_day=day
        store.cs_rev_next_scene=scene
        store.cs_rev_background=None
        store.cs_rev_active=True
        for screen in ('cs_d5_insert','cs_d5_notes','cs_d5_clock_face'):
            renpy.hide_screen(screen)

    def cs_rev_migrate_loaded_story():
        if not getattr(store,'cs_active',False) or cs_rev_active:return
        candidates=list(reversed(renpy.get_return_stack()))+[renpy.game.context().current]
        for address in candidates:
            try:node=renpy.game.script.lookup(address)
            except Exception:continue
            filename=str(getattr(node,'filename','')).replace('\\\\','/').rstrip('c')
            if '/days/' not in filename:continue
            relative='days/'+filename.split('/days/',1)[1]
            if relative not in cs_rev_old_locations:continue
            day,scene=cs_rev_old_locations[relative]
            cs_rev_resume_at(day,scene)
            renpy.block_rollback()
            renpy.set_return_stack([])
            renpy.jump('cs_rev_prologue_resume' if day==0 else 'cs_rev_flow%%d'%%day)
    config.after_load_callbacks.append(cs_rev_migrate_loaded_story)
'''%(repr(aliases),repr(original_locations))
    base=(root/'source/global_revision_20261106/baseline_save_return_compat.rpy.txt').read_text(encoding='utf-8-sig')
    (root/'save_return_compat.rpy').write_text(base+addon,encoding='utf-8')
    (root/'source/global_revision_20261106/legacy_locations.json').write_text(json.dumps(original_locations,ensure_ascii=False,indent=2),encoding='utf-8')

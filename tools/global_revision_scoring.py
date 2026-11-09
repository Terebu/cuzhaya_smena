"""Music, CG and ambience score for the 6 November editions (prologue, days 1-4).

Restores the staging the generated layer lost: the published 0.1.2 build had
mood music and full-screen CG in every day, the generated layer kept only a
handful of cues. Sources, in priority order:
  1. the author's [Постановка: ...] remarks in source/global_revision_20261106/*.txt;
  2. staging_rules.txt (one theme per mood block, silence before alarms,
     diegetic music replaces the background theme, <= 3-4 new themes per chapter);
  3. the tracks and CG of the published GitHub build (Terebu/cuzhaya_smena 0.1.2).

Keys are paragraph indices of *_paragraphs.json, the same coordinates as
global_revision_staging.py. Cues run before the paragraph's text.
"""

DAILY = 'cs_day_music_daily'          # my_daily_life
EVERYDAY = 'cs_day_music_everyday'    # feeling_good
FRIENDS = 'cs_day_music_friends'      # lets_be_friends
HOME = 'cs_day_music_home'            # a_promise_from_distant_days
THINK = 'cs_day_music_think'          # just_think
DOUBT = 'cs_day_music_doubt'          # waltz_of_doubts
PLAY = 'cs_day_music_play'            # i_want_to_play
TALK = '"sound/music/get_to_know_me_better.ogg"'
MIKU = 'cs_miku_piano_track'


def M(track, volume, fadein=2.5):
    return '$ cs_rev_music(%s,%s,%s)' % (track, volume, fadein)


def Q(fade=1.5):
    return 'stop music fadeout %s' % fade


def V(volume, delay=1.5):
    return '$ renpy.music.set_volume(%s, channel="music", delay=%s)' % (volume, delay)


def SHOW(image):
    # Full-screen CG and the return to the room use the same verified helper:
    # it checks the image, keeps the room ambience for CG and clears portraits.
    return '$ cs_rev_room(%r)' % image


SCORE = {
    'prologue_day01': {
        # Prologue: calm room -> wind on the street -> phone feed -> wrong way.
        81: [Q(2.0)],
        99: [M('cs_music_After_Hours', 0.14, 1.0)],
        103: [M('cs_music_410', 0.16, 3.0)],
        # Day 1, chapter I: birds first, then recognition.
        185: [M(THINK, 0.14)],
        225: [Q(1.5)],
        230: [M(FRIENDS, 0.16)],
        260: [M(DAILY, 0.18)],
        # Chapter II: silence for the name, doubt for what Olga does not say.
        280: [Q(2.0)],
        297: [M(DOUBT, 0.14)],
        328: [M(DAILY, 0.16)],
        333: [SHOW('cs_lena_pioneer_mirror')],
        396: [M(THINK, 0.14)],
        # Chapter III: a quiet room, the twins, electronics, the confession.
        451: [Q(1.5)],
        483: [M(PLAY, 0.16)],
        502: [Q(1.5)],
        575: [Q(2.0)],
        581: [M(HOME, 0.12, 3.0)],
        614: [Q(2.0)],
        # Chapter IV.
        654: [M(FRIENDS, 0.14)],
        718: [M(THINK, 0.12)],
        739: [Q(1.5)],
    },
    'day02': {
        111: [M(DAILY, 0.16)],
        137: [Q(1.5)],
        192: [M(EVERYDAY, 0.14)],
        252: [M(FRIENDS, 0.16)],
        284: [Q(1.5)],
        293: [SHOW('cs_cg_darya_piano_day')],
        298: [SHOW('bg int_musclub_day')],
        313: [SHOW('cs_cg_miku_piano_day')],
        314: [SHOW('bg int_musclub_day')],
        368: [SHOW('cs_cg_morning_lineup_day')],
        370: [SHOW('bg ext_square_day')],
        470: [Q(1.5)],
        513: [SHOW('cs_cg_lena_darya_help_viola_day')],
        518: [SHOW('bg int_aidpost_day')],
        540: [M(DAILY, 0.16)],
        638: [M(HOME, 0.14, 3.0)],
        641: [SHOW('cs_cg_lena_darya_hand_in_hand_day')],
        645: [M(THINK, 0.14)],
        685: [V(0.08, 2.0)],
        699: [Q(2.0)],
        873: [SHOW('cs_cg_lena_semen_guess_who_day')],
        877: [SHOW('bg ext_square_day')],
        900: [M(TALK, 0.12)],
        952: [Q(1.5)],
        1037: [M(EVERYDAY, 0.14)],
        1140: [SHOW('cs_cg_square_concert_evening'), M(MIKU, 0.25, 1.0)],
        1149: [SHOW('cs_cg_square_concert_close')],
        1154: [Q(3.0)],
    },
    'day03': {
        132: [M(DAILY, 0.16)],
        216: [M(FRIENDS, 0.14)],
        241: [SHOW('cs_cg_lena_darya_medical_inventory_day')],
        242: [SHOW('bg int_aidpost_day')],
        261: [M(DAILY, 0.18)],
        335: [M(MIKU, 0.22, 1.0)],
        374: [M(EVERYDAY, 0.14)],
        422: [M(TALK, 0.12)],
        540: [M(HOME, 0.12, 3.0)],
        566: [M(EVERYDAY, 0.14)],
        622: [Q(1.5)],
        666: [M(THINK, 0.12)],
    },
    'day04': {
        # Old building: the theme grows outside, thins inside, stops at the voice.
        120: [V(0.18, 3.0)],
        162: [V(0.12, 2.0)],
        211: [V(0.10, 2.0)],
        317: [SHOW('cs_cg_lena_darya_bunker_reunion')],
        322: [SHOW('cs_d4_old_stairs')],
        404: [M(DAILY, 0.16)],
        560: [Q(1.5)],
        659: [M(DAILY, 0.16)],
        995: [M(TALK, 0.12)],
        1095: [V(0.07)],
        1154: [V(0.12)],
        1186: [V(0.06)],
        1224: [V(0.12)],
    },
}

# Backgrounds that follow the characters inside a scene: the generator set one
# room per scene, so exits, entrances and walks kept the previous location.
ROOMS = {
    'prologue_day01': {
        183: 'bg ext_camp_entrance_day',      # «Снаружи оказалось ещё жарче» — out of the bus
    },
    'day02': {
        187: 'bg ext_washstand_day',          # умывальники
        525: 'bg ext_aidpost_day',            # «На крыльце солнечный свет…»
        689: 'cs_road_powerlines_day',        # through the gate, on the road
        839: 'bg ext_aidpost_day',            # «На улице всё было по-прежнему»
        1028: 'bg ext_library_day',           # «На крыльце Дарья первой…»
        1047: 'bg int_dining_hall_sunset',    # «У раздачи я замерла»
    },
    'day03': {
        254: 'bg ext_aidpost_day',            # «Мы вышли из медпункта на солнце»
        336: 'bg int_musclub_day',            # inside the club after hearing the piano
        675: 'bg ext_square_night',           # «пошли к домику через площадь»
    },
    'day04': {
        393: 'bg ext_square_day',             # «Мы вышли на площадь»
        764: 'bg ext_aidpost_day',            # «у крыльца» after the aid post
        1145: 'bg ext_dining_hall_near_sunset',  # «Мы вышли из столовой»
        1294: 'cs_house_lena_darya_ext_night',   # «Домик уже виднелся»
    },
}

# Scene-opening backgrounds that contradicted the first lines of the scene.
HEADERS = {
    'day02': {
        2: 'cs_house_lena_darya_ext_day',     # starts on the cabin porch, then runs
        11: 'bg ext_camp_entrance_day',       # «У ворот Семён уже ждал»
        16: 'cs_camp_path_sunset',            # horn and the walk to dinner
    },
    'day03': {
        6: 'bg ext_musclub_day',              # «Из клуба доносилась музыка»
    },
}

# Generated cues replaced by the score above (index, exact line).
REPLACED = {
    'prologue_day01': [
        (575, '$ cs_rev_music("sound/music/get_to_know_me_better.ogg",0.14)'),
    ],
    'day02': [
        (685, 'stop music fadeout 1.5'),
        (685, "$ cs_rev_room('cs_road_powerlines_day')"),
        (1147, '$ cs_rev_music(cs_miku_piano_track,0.25)'),
        (1147, "$ cs_rev_room('cs_cg_square_concert_evening')"),
    ],
    'day03': [
        (335, "$ cs_rev_room('bg int_musclub_day')"),
    ],
    'day04': [
        (404, "$ cs_rev_room('bg ext_square_day')"),
    ],
}


def score(name, H, headers=None):
    for index, line in REPLACED.get(name, []):
        lines = H.get(index, [])
        assert line in lines, (name, index, line, lines)
        lines.remove(line)
        if not lines:
            del H[index]
    for index, image in ROOMS.get(name, {}).items():
        H.setdefault(index, []).append(SHOW(image))
    for index, lines in SCORE[name].items():
        H.setdefault(index, []).extend(lines)
    if headers is not None:
        for number, image in HEADERS.get(name, {}).items():
            for k, row in enumerate(headers):
                if row[1] == number:
                    headers[k] = row[:5] + (image,) + row[6:]
    return H

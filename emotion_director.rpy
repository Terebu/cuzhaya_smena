# -*- coding: utf-8 -*-
# Automatic expression changes for authored actors. Scripts rarely re-show a
# sprite between lines, so the speaker's pose is picked from the line itself.
# A pose set by a script is respected for the line it was set on; the director
# only takes over after that. Choice is a pure function of the text and the
# stored history, so rollback and loading replay the same expressions.
default cs_auto_emotions = True
default cs_emo_state = {}

init -5 python:
    import re
    import zlib

    # Pools are (mild, strong). Poses missing for a costume are filtered out.
    cs_emo_darya = {
        "calm": (["idle_neutral", "neutral", "shrug", "idle_thoughtful", "hands_on_hips", "thinking"], []),
        "explain": (["explaining", "reaching", "hands_on_hips", "forearm_hold", "idle_thoughtful"], ["wave"]),
        "curious": (["curious_curious", "curious_interested", "curious_thinking", "thinking", "curious_confused"], ["curious_suspicious"]),
        "smile": (["smile_gentle_smile", "smile_smile", "idle_soft_smile", "smile_playful", "smile_relieved", "smile", "amused"], ["smile_happy", "smile_excited"]),
        "laugh": (["laugh_cheerful", "laugh_teasing", "amused", "laugh_wink", "laugh_smug"], ["laugh_big_smile", "laugh_laugh"]),
        "shy": (["shy_smile", "ear_touch", "hair_touch", "tie_touch", "shy_bend"], ["cry_embarrassed"]),
        "surprise": (["surprised", "idle_surprised", "curious_surprised"], ["surprise_hand"]),
        "sad": (["idle_sad", "worried", "idle_tired", "cry_sad"], ["cry_anxious", "cry_hurt"]),
        "cry": (["cry_sad", "cry_teary", "cry_hurt"], ["cry_crying", "cry_anxious"]),
        "mad": (["mad_annoyed", "mad_serious", "mad_skeptical", "arms_crossed", "serious"], ["mad_offended", "mad_angry", "mad_furious"]),
    }
    cs_emo_semen = {
        "calm": (["neutral", "relaxed", "thinking", "arms_crossed", "thinking_alt"], []),
        "explain": (["explaining", "pointing", "confident", "thinking_down"], []),
        "curious": (["thinking", "thinking_alt", "thinking_down", "pointing"], []),
        "smile": (["smile", "relaxed", "grateful", "confident"], ["peace", "wave"]),
        "laugh": (["smile", "peace", "confident"], ["wave"]),
        "shy": (["shy", "awkward", "tie_touch", "awkward_alt"], []),
        "surprise": (["surprised", "startled"], []),
        "sad": (["awkward", "thinking_down", "awkward_alt", "serious"], []),
        "cry": (["awkward", "thinking_down", "serious"], []),
        "mad": (["serious", "arms_crossed"], ["pointing"]),
    }
    cs_emo_zhenya = {
        "calm": (["normal", "thoughtful", "shrug", "arms_crossed", "glasses_touch"], []),
        "explain": (["explaining", "glasses_touch", "thoughtful"], []),
        "curious": (["thinking", "thoughtful", "glasses_touch"], []),
        "smile": (["normal", "shy", "shrug"], []),
        "laugh": (["normal", "shrug"], []),
        "shy": (["shy", "glasses_touch"], []),
        "surprise": (["normal", "glasses_touch"], []),
        "sad": (["thoughtful", "shy", "thinking"], []),
        "cry": (["shy", "thoughtful"], []),
        "mad": (["arms_crossed", "angry"], ["angry"]),
    }
    cs_emo_viola = {
        "calm": (["serious", "thoughtful", "arms_crossed"], []),
        "explain": (["explaining", "serious", "thoughtful"], []),
        "curious": (["thoughtful", "serious", "eyes_closed"], []),
        "smile": (["warm_smile", "amused"], []),
        "laugh": (["amused", "warm_smile"], []),
        "shy": (["eyes_closed", "warm_smile"], []),
        "surprise": (["surprised"], []),
        "sad": (["eyes_closed", "thoughtful", "stern"], []),
        "cry": (["eyes_closed", "stern"], []),
        "mad": (["stern", "arms_crossed", "angry"], ["angry"]),
    }
    cs_emo_winter = {
        "calm": (["neutral", "neutral_alt", "shrug", "hands_on_hips"], []),
        "explain": (["explaining", "hands_on_hips", "arms_crossed"], []),
        "curious": (["interested", "thinking"], []),
        "smile": (["smile", "wave"], []),
        "laugh": (["smile", "wave"], []),
        "shy": (["shy"], []),
        "surprise": (["interested"], []),
        "sad": (["worried", "thinking"], []),
        "cry": (["worried"], []),
        "mad": (["arms_crossed", "hands_on_hips"], []),
    }

    # tag -> (pools, index of the pose inside get_attributes, name pattern in narration)
    cs_emo_actors = {
        "cs_darya": (cs_emo_darya, 0, u"дарь[яеиюй]|даш[аеиуой]|незнакомк"),
        "cs_dasha_winter": (cs_emo_winter, 0, u"дарь[яеиюй]|даш[аеиуой]|незнакомк"),
        "cs_semen": (cs_emo_semen, 0, u"семён|семен|семе[нн]а|семёна"),
        "cs_zhenya": (cs_emo_zhenya, 0, u"жен[яеиюй]\\b"),
        "cs": (cs_emo_viola, 1, u"виол[аеыу]"),
    }
    cs_emo_speakers = {
        "cs_da": ("cs_darya", "cs_dasha_winter"),
        "cs_sy": ("cs_semen",),
        "cs_mz": ("cs_zhenya",),
        "cs_vi": ("cs",),
    }

    # Speech cues, strongest first. Each word list is matched on lower-cased text.
    cs_emo_rules = [
        ("cry", re.compile(u"слёз|слез[аыуи]|плак|рыда|всхлип|разрев|дрожащ|захлёб", re.U)),
        ("mad", re.compile(u"злюсь|злит|бесит|бесишь|раздража|достал|надоел|идиот|дура[кц]|заткни|хватит|отстань|как ты смеешь|не смей|убирайся|прекрати|возмутитель|ненавиж|чёрт|черт ", re.U)),
        ("laugh", re.compile(u"ха-?ха|хих|хех|смеш|смеюсь|смех|рассмея|ржу|прикол|уморитель|шутк", re.U)),
        ("surprise", re.compile(u"ого\\b|ничего себе|вот это|не может быть|неужели|серьёзно\\?|правда\\?|вау|ух ты|что\\?!|как\\?!|ты что|в смысле|да ладно", re.U)),
        ("shy", re.compile(u"смущ|неловк|стесн|стыдно|краснею|покрасн|мило\\b|нравишься|ой\\b|э-?э|м-?м|ну\\.\\.\\.", re.U)),
        ("sad", re.compile(u"жаль|прости|извини|грустн|устал|тяжело|больно|боюсь|страшно|одинок|скучаю|не знаю|не могу|плохо|тревож|беспоко|переживаю", re.U)),
        ("smile", re.compile(u"рада|рад\\b|здорово|отлично|круто|класс\\b|спасибо|молодец|ура\\b|прекрасно|весело|улыб|хорошо|договорились|получилось|нравится|люблю|давай!", re.U)),
        ("explain", re.compile(u"потому что|значит|то есть|смотри|слушай|дело в том|сначала|во-первых|представь|например|объясню|на самом деле|короче|видишь|надо\\b|нужно\\b|должн|правило|инструкц", re.U)),
        ("curious", re.compile(u"почему|зачем|как так|интересно|а если|погоди|подожди|постой|кто\\b|откуда|куда\\b|чего\\b|вопрос|может\\b|вдруг|странно|подозр", re.U)),
    ]
    # Narration/thought about the actor: only explicit stage directions count.
    cs_emo_stage_cues = [
        ("cry", re.compile(u"заплакал|всхлип|слёзы|слезы|глаза (?:блеснули|повлажнели)", re.U)),
        ("mad", re.compile(u"нахмурил|разозлил|рассердил|сверкнул|скрестил[аи]? руки|сжал[аи]? (?:кулаки|губы)|фыркнул|раздражённо|раздраженно|холодно", re.U)),
        ("laugh", re.compile(u"рассмеял|засмеял|прыснул|хихикнул|фыркнул[аи]? от смеха|расхохотал|подмигнул", re.U)),
        ("surprise", re.compile(u"округлил[аи]? глаза|вздрогнул|замерл|опешил|удивлённо|удивленно|оторопел", re.U)),
        ("shy", re.compile(u"смутил|покраснел|отвёл[аи]? взгляд|отвел[аи]? взгляд|потупил|замялс|смущённо|смущенно|теребил", re.U)),
        ("sad", re.compile(u"вздохнул|опустил[аи]? (?:глаза|взгляд|плечи)|погрустнел|помрачнел|поникл|устало", re.U)),
        ("smile", re.compile(u"улыбнул|усмехнул|просиял|улыбк|заулыбал", re.U)),
        ("curious", re.compile(u"прищурил|склонил[аи]? голову|приподнял[аи]? бров|задумал|задумчиво", re.U)),
        ("explain", re.compile(u"развёл[аи]? руками|развел[аи]? руками|указал|показал[аи]? рукой|жестикулир", re.U)),
    ]

    def cs_emo_classify(text):
        low = text.lower()
        best, hits = None, 0
        for name, rule in cs_emo_rules:
            n = len(rule.findall(low))
            if n:
                best, hits = name, n
                break
        strong = hits >= 2 or "!" in low
        if best is None:
            if "?" in low:
                best = "curious"
            elif low.rstrip().endswith((u"…", u"...")):
                best = "sad" if len(low) < 60 else "curious"
            elif "!" in low:
                best = "explain"
            else:
                best = "calm"
        return best, strong

    def cs_emo_stage_category(text, name_pattern):
        low = text.lower()
        for name, cue in cs_emo_stage_cues:
            m = re.search(u"(?:%s)[^.!?…]{0,50}?(?:%s)" % (name_pattern, cue.pattern), low, re.U)
            if m:
                return name
        return None

    def cs_emo_category_of(pools, pose):
        for name, (mild, strong) in pools.items():
            if pose in mild or pose in strong:
                return name
        return None

    def cs_emo_choose(tag, text, category, strong, current, state):
        pools, index, pattern = cs_emo_actors[tag]
        recent = list(state.get("recent", []))
        mild, strong_pool = pools[category]
        attrs = tuple(renpy.get_attributes(tag) or ())
        base = list(attrs)
        def usable(pose):
            base[index] = pose
            return renpy.has_image((tag,) + tuple(base))
        pool = [p for p in (strong_pool + mild if strong else mild) if usable(p)]
        if not pool:
            return None
        # Prefer something that is neither the current pose nor a recent one.
        fresh = [p for p in pool if p != current and p not in recent[-3:]]
        if not fresh:
            fresh = [p for p in pool if p != current] or pool
        seed = zlib.adler32(text.encode("utf-8")) & 0x7fffffff
        return fresh[seed % len(fresh)]

    def cs_emo_apply(tag, text, category, strong, forced):
        pools, index, pattern = cs_emo_actors[tag]
        attrs = tuple(renpy.get_attributes(tag) or ())
        if len(attrs) <= index:
            return
        # Underwear and other one-off costumes only have a couple of authored poses.
        if "underwear" in attrs:
            return
        current = attrs[index]
        states = store.cs_emo_state
        state = states.get(tag, {})
        hold = state.get("hold", 0)
        if state.get("auto") != current:
            # The script just set this pose; keep it for the line it belongs to.
            new_state = {"auto": current, "hold": 1, "recent": (list(state.get("recent", [])) + [current])[-4:]}
            if not forced:
                store.cs_emo_state = dict(states, **{tag: new_state})
                return
            hold = 1
        same_mood = cs_emo_category_of(pools, current) == category
        if same_mood and hold < 2:
            store.cs_emo_state = dict(states, **{tag: {"auto": current, "hold": hold + 1, "recent": state.get("recent", [])}})
            return
        pose = cs_emo_choose(tag, text, category, strong, current, state)
        if pose is None or pose == current:
            store.cs_emo_state = dict(states, **{tag: {"auto": current, "hold": hold + 1, "recent": state.get("recent", [])}})
            return
        name = list(attrs)
        name[index] = pose
        renpy.show((tag,) + tuple(name))
        renpy.transition(cs_sprite_change)
        recent = (list(state.get("recent", [])) + [pose])[-4:]
        store.cs_emo_state = dict(states, **{tag: {"auto": pose, "hold": 1, "recent": recent}})
        cs_director_remember()

    def cs_emotion_at_line(event, **kwargs):
        if event != "begin" or not getattr(store, "cs_active", False):
            return
        if not getattr(store, "cs_auto_emotions", True) or getattr(store, "cs_reflective_shot", False):
            return
        if cs_full_frame_cg_showing():
            return
        text = getattr(store, "_last_raw_what", None)
        if not text:
            return
        who = getattr(store, "_last_say_who", None)
        spoken = cs_emo_speakers.get(who)
        if spoken:
            tag = None
            for candidate in spoken:
                if renpy.showing(candidate):
                    tag = candidate
                    break
            if tag is not None:
                category, strong = cs_emo_classify(text)
                cs_emo_apply(tag, text, category, strong, False)
        # Stage directions in narration move the named actor, even when silent.
        for tag, (pools, index, pattern) in cs_emo_actors.items():
            if spoken and tag in spoken:
                continue
            if not renpy.showing(tag):
                continue
            category = cs_emo_stage_category(text, pattern)
            if category:
                cs_emo_apply(tag, text, category, True, True)

init 41 python:
    config.all_character_callbacks.append(cs_emotion_at_line)

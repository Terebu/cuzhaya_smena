"""Editorial emotion choices shared by offline staging tools, never runtime text analysis."""
def reaction(text, speaker='cs_da', previous='', chapter=''):
    t=text.lower();p=previous.lower()
    # Narrative cues describe a physical gesture or a visible reaction.
    if speaker=='cs_narrator':
        if not ('дарь' in t or t.startswith(('она ','та '))):return None
        if any(w in t for w in ('рассме','засме','не выдержала')):return 'amused'
        if any(w in t for w in ('пожала плеч','покачала голов')):return 'shrug'
        if any(w in t for w in ('опустила взгляд','отвела взгляд')):return 'shy_bend'
        if 'волос' in t and any(w in t for w in ('поправ','провел','убрал')):return 'hair_touch'
        if any(w in t for w in ('помах','махнула')):return 'wave'
        if 'галстук' in t:return 'tie_touch'
        if 'руку' in t and any(w in t for w in ('протян','подала','потян')):return 'reaching'
        if 'руки на' in t and ('бок' in t or 'бедр' in t):return 'hands_on_hips'
        if any(w in t for w in ('скрестила','сложила руки')):return 'arms_crossed'
        if any(w in t for w in ('не ожидала','неожидан','моргнула','неподвижно')):return 'surprise_hand'
        if 'приподняла бров' in t:return 'ear_touch'
        if any(w in t for w in ('улыб','усмех')):return 'shy_smile' if chapter in ('41','42','45') else 'smile'
        if any(w in t for w in ('задум','размышля')):return 'thinking'
        if 'без улыбки' in t:return 'serious'
        return None
    if speaker!='cs_da':return None
    if any(w in t for w in ('тоже нравишься','мне с тобой интересно','рада, что','спасибо, что сказала')):return 'shy_smile'
    if any(w in t for w in ('насчёт всего остального','пока не знаю','мы знакомы всего','даже меньше','не торопишь','неожидала','не ожидала')):return 'forearm_hold'
    if t in ('лен…','немного.'):return 'shy_bend'
    if any(w in t for w in ('сейчас можно','тогда хорошо')):return 'reaching'
    if 'в каком смысле' in t:return 'surprise_hand'
    if any(w in t for w in ('красивая','выглядишь','очень идёт')):return 'ear_touch'
    if any(w in t for w in ('совсем?','это тот самый','тот самый семён','что это','кто?')):return 'surprised'
    if any(w in t for w in ('не отвечу','не уверена','страшно','беспокоит','вернуться','слишком много им','остались','единственная вещь')):return 'worried'
    if any(w in t for w in ('не думай','не делай из','не говори','ты даже не спросила','ты ужасно врёшь','я вижу твой взгляд')):return 'arms_crossed'
    if any(w in t for w in ('только не начинай','даже не начинай','неисправима','товарищ председатель','научному процессу','эпилеп')):return 'hands_on_hips'
    if any(w in t for w in ('многообещающе','минуты две','убедительнее','иногда?','не уверена, что это можно считать','годовой план')):return 'amused'
    if t in ('пока!','пока.','привет.'):return 'wave'
    if any(w in t for w in ('здесь есть','мы обе','то есть','потому что','на самом деле','для начала')):return 'explaining'
    if any(w in t for w in ('форма','галстук','одежд','переод')):return 'tie_touch'
    if any(w in t for w in ('волос','крашен')):return 'hair_touch'
    if any(w in t for w in ('скуч','дома','мама','обычной жизни')):return 'forearm_hold'
    if t in ('лена!','лен.'):return 'serious'
    if any(w in t for w in ('справедливо','хорошо.','логично','спасибо.','правильно','нормальные девчонки')):return 'smile'
    if '?' in t:
        if t in ('м?','да?','правда?'):return 'ear_touch'
        return 'thinking'
    if len(t)>100:return 'explaining'
    return 'shrug'

WINTER={'shy_smile':'smile','ear_touch':'shy','hands_on_hips':'hands_on_hips','hair_touch':'shy','tie_touch':'neutral_alt','amused':'smile','shy_bend':'shy','reaching':'explaining','forearm_hold':'worried','surprise_hand':'explaining','smile':'smile','surprised':'interested','serious':'arms_crossed','neutral':'shrug'}

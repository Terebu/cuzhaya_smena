"""Reviewed audible events, using only verified native archive resources.

Indices identify events as they happen, not dialogue recalling an earlier event.
Ordinary footsteps, birds and wind remain owned by the location ambience.
"""
SOUNDS={
 'prologue_day01':{
  344:('dinner_horn_processed',0.6),456:('close_door_1',0.35),486:('open_door_1',0.4),502:('close_door_1',0.4),725:('dinner_horn_processed',0.6),886:('click_3',0.2),899:('<from 0.0 to 0.7>bus_idle',0.12)},
 'day02':{
  107:('close_door_1',0.25),187:('dinner_horn_processed',0.6),368:('dinner_jingle_speaker',0.5),470:('medpunkt_door_open',0.4),733:('bodyfall_1',0.55),956:('close_door_1',0.35),1036:('dinner_horn_processed',0.6),1155:('concert_applause',0.4),1221:('click_3',0.2)},
 'day03':{
  75:('<from 0.0 to 0.7>bus_idle',0.12),103:('dinner_horn_processed',0.6),108:('open_door_1',0.35),371:('dinner_horn_processed',0.6),553:('dinner_horn_processed',0.6),708:('knocks:2',0.45)},
 'day04':{
  92:('open_door_1',0.25),99:('close_door_1',0.25),148:('door_squeak_light',0.3),150:('far_steps',0.25),173:('door_squeak_light',0.2),197:('knocks:1',0.35),214:('open_metal_door',0.45),219:('click_3',0.25),256:('metal_door_large_close_basement',0.4),281:('click_3',0.3),375:('metal_door_heavy_close',0.35),551:('knocks:1',0.45),828:('dinner_horn_processed',0.6),910:('open_door_clubs',0.35),1047:('dinner_horn_processed',0.6),1333:('close_door_1',0.3)},
 'day05':{
  65:('bed_squeak1',0.3),113:('open_door_1',0.35),297:('dinner_horn_processed',0.6),313:('water_splash',0.35),453:('open_door_1',0.4),553:('close_door_1',0.35),1289:('dinner_horn_processed',0.6),1746:('campus_door_rattle',0.3),1758:('far_steps',0.25),1798:('open_door_clubs',0.35),1892:('close_door_1',0.3),2102:('dinner_horn_processed',0.6),2226:('open_door_1',0.35),2240:('close_door_1',0.35),2353:('knocks:1',0.4),2358:('open_door_1',0.35),2653:('close_door_1',0.3)},
}

# 8 November: more camp atmosphere from the native archive (doors, steps,
# keys, water, owl, wind). Same rule: one sound per event, at the moment it happens.
EXTRA={
 'prologue_day01':{
  82:('street_traffic_outside',0.18),86:('bus_stop',0.3),105:('cellular_phone_error',0.35),193:('amb:<from 0 to 4>grasshoper_clean',0.22),
  225:('far_steps',0.3),260:('close_door_1',0.12),291:('open_door_1',0.3),328:('open_door_2',0.22),512:('open_door_clubs',0.3),
  739:('open_door_1',0.25),841:('lock_close',0.3),897:('owl_far',0.18)},
 'day02':{
  137:('close_door_1',0.12),188:('water_sink_stream',0.3),284:('open_door_clubs',0.3),430:('open_door_clubs_2',0.3),
  525:('close_door_1',0.25),839:('close_door_1',0.25),952:('open_door_1',0.25),1028:('close_door_1',0.25)},
 'day03':{
  254:('close_door_1',0.25),295:('open_door_squeak_2',0.3),422:('open_door_1',0.25),675:('owl_far',0.18)},
 'day04':{
  120:('wind_gust',0.3),127:('door_squeak_light',0.22),134:('wood_floor_squeak',0.25),250:('far_steps',0.3),295:('far_steps',0.35),
  912:('keys_rattle',0.3),1020:('key_drawer',0.3),1159:('click_3',0.2),1237:('lock_close',0.3),1325:('tree_branches',0.18)},
}
for _name,_extra in EXTRA.items():
    for _i,_v in _extra.items():
        assert _i not in SOUNDS[_name],(_name,_i)
        SOUNDS[_name][_i]=_v

def resource(token):
    folder='sound/sfx/'
    if token.startswith('amb:'):folder='sound/ambiences/';token=token[4:]
    if token.startswith('<'):
        prefix,token=token.split('>',1)
        return prefix+'>'+folder+token+'.ogg'
    return folder+token+'.ogg'

def cues(name):
    out={}
    for index,(sound,volume) in SOUNDS[name].items():
        if sound.startswith('knocks:'):
            out[index]=['$ cs_rev_knocks(%d,%s)'%(int(sound.split(':')[1]),volume)]
        else:out[index]=['$ cs_rev_sfx(%r,%s)'%(resource(sound),volume)]
    return out

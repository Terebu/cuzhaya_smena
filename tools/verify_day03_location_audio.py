"""Check that every authored day3 background has an ambient policy."""
from pathlib import Path
import re,json,textwrap,sys
R=Path(__file__).resolve().parent.parent
s=(R/'day03_location_audio.rpy').read_text(encoding='utf8')
a=s.index('    def cs_day03_audio_target(');b=s.index('    def cs_day03_location_audio(',a)
space={};exec(textwrap.dedent(s[a:b]),space);target=space['cs_day03_audio_target']
rooms={}
for p in (R/'days/day03').rglob('*.rpy'):
 for image in re.findall(r'cs_director_scene\("([^"]+)"\)',p.read_text(encoding='utf8')):
  sound=target(image)
  if image.startswith('cs_cg_'):assert sound is False
  else:assert sound is not False,image
  rooms[image]=dict(target=sound,inherits=sound is False)
assert 'dining_hall_full' in target('bg int_dining_hall_people_day')
assert 'camp_center_day' in target('bg ext_dining_hall_away_day')
assert target('bg int_library_day') is None and target('bg int_musclub_day') is None
assert 'int_cabin_day' in target('cs_house_lena_darya_int_day')
out=Path(sys.argv[1])/'audio_location_audit.json' if len(sys.argv)>1 else R/'source/day03_audio_location_audit.json'
out.write_text(json.dumps(dict(status='PASS',rooms=rooms,scope='All authored day3 scene requests, including retired compatibility tail. Native routes separately validate the playing ambience channel.'),indent=2),encoding='utf8')
print('DAY3_AUDIO_STATIC_PASS',len(rooms),'scene identifiers')

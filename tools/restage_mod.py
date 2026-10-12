"""Reapply user asset overrides, complete emotion palette and camera focus in order."""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
for script in ('integrate_camp_paths.py','stage_darya_variety.py','stage_composition.py','stage_speaker_visibility.py','stage_phone_focus.py','stage_scene_focus.py'):
    runpy.run_path(str(HERE/script),run_name='__main__')

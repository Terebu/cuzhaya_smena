"""Reapply the unified current staging without resurrecting old hide/show rules."""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
for script in ('stage_all_sprites.py','inventory_custom_sprites.py'):
    runpy.run_path(str(HERE/script),run_name='__main__')

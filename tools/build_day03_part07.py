"""Current part 7 generator; the old lunch is replaced, never appended."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build_day03_part07_revision.py')),run_name='__main__')
if (Path(__file__).resolve().parent.parent/'source/day03_part08.md').exists():
    runpy.run_path(str(Path(__file__).with_name('build_day03_part08_09.py')),run_name='__main__')

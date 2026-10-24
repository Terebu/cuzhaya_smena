"""The old lunch audit delegates to the current replacement audit."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('verify_lunch_revision.py')),run_name='__main__')

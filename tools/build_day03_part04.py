
# Reviewed readability is replayed only after the complete raw compiler chain.
import os as _cs_readability_os
if _cs_readability_os.environ.get("CS_READABILITY_RAW") != "1":
    from pathlib import Path as _CsReadabilityPath
    _cs_readability_root = _CsReadabilityPath(__file__).resolve().parent.parent
    if (_cs_readability_root / "source/readability_day03.json").is_file() or (_cs_readability_root / "source/readability_day04.json").is_file():
        import subprocess as _cs_readability_subprocess
        import sys as _cs_readability_sys
        raise SystemExit(_cs_readability_subprocess.call([_cs_readability_sys.executable, str(_cs_readability_root / "tools/regenerate_readability.py"), "--entry", _CsReadabilityPath(__file__).name]))

from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build_day03_part04_revision.py')))

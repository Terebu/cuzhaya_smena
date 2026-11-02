"""Regenerate in an isolated project, then publish only reviewed exact targets.

Usage: python tools/regenerate_readability.py --check
Direct day-three/day-four builders delegate here unless CS_READABILITY_RAW=1.
The raw flag is only for this wrapper's subprocesses and isolated diagnostics.
Unknown authoring output is rejected; this wrapper never refreshes its bridge or
target manifest automatically. Probes contain scripts/documents, never assets.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import uuid

from apply_readability_edits import apply, atomic_write, load, read_json, runtime_paths, sha

ROOT = Path(__file__).resolve().parent.parent
RAW_STAGES = tuple("build_day03_part%02d.py" % i for i in range(1, 8)) + ("apply_conversation_focus.py",)


def authoring_files(root: Path) -> list[Path]:
    builders = [p for p in (root / "tools").glob("build_day03_part*.py") if "_qa" not in p.stem]
    names = (
        "build_day04.py", "apply_conversation_focus.py", "apply_medpoint_continuity.py",
        "apply_rebuilt_day04_assets.py", "apply_day04_continuity.py", "apply_day04_prose.py",
        "stabilize_call_helpers.py", "apply_readability_edits.py", "regenerate_readability.py",
    )
    sources = list((root / "source").glob("day03_part*.md"))
    sources += [root / "source/day04.md"]
    sources += list((root / "source").glob("day04_prose_*.json"))
    sources += list((root / "source").glob("readability_*.json"))
    return sorted(set(builders + [root / "tools" / name for name in names] + sources))


def materialize(root: Path, stage: Path):
    for relative, source in runtime_paths(root).items():
        target = stage / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    for source in authoring_files(root):
        if not source.is_file():
            raise ValueError("Missing authoring input: " + str(source))
        target = stage / source.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    # This is the only asset-presence switch used by the historical compilers.
    # No image is read by generation; the same branch must run in the probe.
    if (root / "sp/darya_sport").is_dir():
        (stage / "sp/darya_sport").mkdir(parents=True)


def run_raw(stage: Path, log: Path):
    env = os.environ.copy()
    env.update(CS_READABILITY_RAW="1", PYTHONIOENCODING="utf-8")
    chunks = []
    for name in RAW_STAGES:
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(stage / "tools" / name)],
            cwd=stage, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            timeout=60,
        )
        output = result.stdout.decode("utf-8", errors="replace")
        chunks.append("## " + name + "\n" + output)
        print("RAW", name, "PASS" if result.returncode == 0 else "FAIL", flush=True)
        if result.returncode:
            log.write_text("\n".join(chunks), encoding="utf-8")
            raise RuntimeError("Raw stage failed: " + name + "; log=" + str(log) + "\n" + output[-3000:])
    log.write_text("\n".join(chunks), encoding="utf-8")


def check_exact(root: Path, targets: dict[str, str]):
    actual = runtime_paths(root)
    if set(actual) != set(targets):
        raise ValueError("Generated inventory differs: missing=" + repr(sorted(set(targets) - set(actual))) +
                         " extra=" + repr(sorted(set(actual) - set(targets))))
    wrong = [rel for rel, path in actual.items() if sha(path.read_bytes()) != targets[rel]]
    if wrong:
        raise ValueError("Generated files do not equal reviewed runtime: " + repr(wrong))


def regenerate(root: Path, *, check: bool, rounds: int, scratch: Path | None = None, entry: str = "") -> dict:
    manifest, _ = load(root)
    # A complete rollback-safe check precedes all raw generation. Partial or
    # unknown editorial files must not be treated as another baseline.
    apply(root, check=True, verify_all=True)
    start_hashes = {rel: sha(path.read_bytes()) for rel, path in runtime_paths(root).items()}
    inputs = {p.relative_to(root).as_posix(): sha(p.read_bytes()) for p in authoring_files(root)}
    if scratch is None:
        session = root / "source/readability_session.json"
        work = Path(read_json(session)["work"]) if session.is_file() else None
        scratch = work / "generation_checks" if work is not None and work.is_dir() else Path(tempfile.gettempdir()) / "chuzhaya_smena_generation"
    scratch = scratch.resolve()
    scratch.mkdir(parents=True, exist_ok=True)
    probe = scratch / ("readability-regeneration-" + uuid.uuid4().hex)
    probe.mkdir()
    materialize(root, probe)
    evidence = {"status": "RUNNING", "root": str(root), "probe": str(probe),
                "entry": entry, "runtime_files": len(start_hashes), "input_sha256": inputs, "rounds": []}
    output = probe.parent / (probe.name + "-results.json")
    try:
        for index in range(1, rounds + 1):
            run_raw(probe, probe.parent / (probe.name + "-round-%d.log" % index))
            report = apply(probe, bridge=True, verify_all=True)
            check_exact(probe, manifest["runtime_sha256"])
            no_op = apply(probe, bridge=True, verify_all=True, check=True)
            if no_op["changed_files"] != 0:
                raise ValueError("Second replay would alter reviewed runtime")
            evidence["rounds"].append({"number": index, "status": "PASS", "replay": report, "second_replay_changed_files": 0})
            print("ROUND", index, "EXACT", len(start_hashes), "FILES; SECOND REPLAY NO-OP", flush=True)
        # Never overwrite concurrent authoring, ledgers or runtime edits.
        if {rel: sha(path.read_bytes()) for rel, path in runtime_paths(root).items()} != start_hashes:
            raise ValueError("Live runtime changed during the isolated probe")
        if {p.relative_to(root).as_posix(): sha(p.read_bytes()) for p in authoring_files(root)} != inputs:
            raise ValueError("Authoring inputs changed during the isolated probe")
        published = []
        if not check:
            for rel, source in runtime_paths(probe).items():
                target = root / rel
                data = source.read_bytes()
                if target.read_bytes() != data:
                    atomic_write(target, data)
                    published.append(rel)
            check_exact(root, manifest["runtime_sha256"])
        evidence.update(status="PASS", check_only=check, published_files=published,
                        protected_sha256=manifest["protected_sha256"], final_runtime_sha256=manifest["runtime_sha256"])
        return evidence
    except Exception as exc:
        evidence.update(status="FAIL", error=str(exc))
        raise
    finally:
        output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("GENERATION_EVIDENCE", output, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true", help="Prove exact generation without changing the live runtime")
    parser.add_argument("--rounds", type=int, default=2)
    parser.add_argument("--scratch", type=Path)
    parser.add_argument("--entry", default="", help="Calling historical builder, for evidence only")
    args = parser.parse_args()
    if args.rounds < 1:
        parser.error("--rounds must be positive")
    report = regenerate(args.root.resolve(), check=args.check, rounds=args.rounds, scratch=args.scratch, entry=args.entry)
    print("READABILITY_GENERATION_PASS", report["runtime_files"], "runtime files;", len(report["rounds"]), "rounds; published", len(report["published_files"]))


if __name__ == "__main__":
    main()

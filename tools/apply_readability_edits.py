"""Strict replay of the reviewed readability ledgers; no heuristic text matching.

The manifest records exact pre-edit and final bytes, including BOM/newline style.
The optional generation bridge restores previously authored call/staging fixes
from one known raw compiler output before prose hunks are replayed. Unknown
content is an error. All files are planned and validated before any are written.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parent.parent
GROUPS = ("prologue", "day01", "day02", "day03", "day04")
# 95 has a published save/audio alias contract. 74a is generator-owned, but its
# two reviewed R8 name forms now belong to the day-two editorial replay.
PROTECTED = ("days/day03/part03/95_scene.rpy",)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def runtime_paths(root: Path) -> dict[str, Path]:
    return {p.relative_to(root).as_posix(): p for p in
            sorted(list(root.glob("*.rpy")) + list((root / "days").rglob("*.rpy")))}


def safe_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("Expected a relative POSIX file path: " + repr(relative))
    p = (root / relative).resolve()
    if p == root.resolve() or root.resolve() not in p.parents:
        raise ValueError("Path outside project: " + relative)
    return p


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def logical(data: bytes | str) -> str:
    text = data.decode("utf-8-sig") if isinstance(data, bytes) else data
    return text.replace("\r\n", "\n")


def text_format(data: bytes) -> dict:
    text = data.decode("utf-8-sig")
    crlf = text.count("\r\n")
    bare = text.count("\n") - crlf
    if crlf and bare:
        raise ValueError("Mixed newline styles require an explicit authoring decision")
    return {"bom": data.startswith(b"\xef\xbb\xbf"), "newline": "crlf" if crlf else "lf"}


def encode(text: str, spec: dict) -> bytes:
    text = text.replace("\r\n", "\n")
    if spec["newline"] == "crlf":
        text = text.replace("\n", "\r\n")
    return (b"\xef\xbb\xbf" if spec["bom"] else b"") + text.encode("utf-8")


def atomic_write(path: Path, data: bytes):
    if path.is_file() and path.read_bytes() == data:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, name = tempfile.mkstemp(prefix=".readability-", dir=path.parent)
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(data)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def record_manifest(root: Path, baseline: Path) -> dict:
    """Explicit maintainer action after reviewed ledgers/runtime are complete."""
    paths = runtime_paths(root)
    before_paths = runtime_paths(baseline)
    if set(paths) != set(before_paths):
        raise ValueError("Baseline/runtime inventory differs; review additions/removals first")
    registries = []
    files = {}
    for group in GROUPS:
        name = "source/readability_" + group + ".json"
        p = root / name
        if not p.is_file():
            continue
        entries = read_json(p)
        if not isinstance(entries, list):
            raise ValueError("Registry must be a list: " + name)
        registries.append({"group": group, "file": name, "sha256": sha(p.read_bytes()), "hunks": len(entries)})
        for relative in dict.fromkeys(e["file"] for e in entries):
            safe_path(root, relative)
            if relative in files:
                raise ValueError("A runtime file belongs to multiple registries: " + relative)
            base = before_paths[relative].read_bytes()
            target = paths[relative].read_bytes()
            extra = []
            approved = [e for e in entries if e["file"] == relative and
                        e.get("kind") == "approved_first_closeup"]
            if approved:
                altered = logical(base)
                for e in approved:
                    needle = logical(e["before"])
                    if altered.count(needle) != 1:
                        raise ValueError("Approved baseline removal is ambiguous: " + relative)
                    altered = altered.replace(needle, logical(e["after"]), 1)
                extra.append(sha(encode(altered, text_format(base))))
            files[relative] = {
                "registry": group, "baseline_sha256": sha(base),
                "accepted_baseline_sha256": [sha(base)] + extra,
                "approved_missing_sha256": extra,
                "target_sha256": sha(target), "target_format": text_format(target),
                "hunks": sum(e["file"] == relative for e in entries),
            }
    result = {
        "schema": 1, "description": "Reviewed exact readability targets; unknown text must not be overwritten.",
        "registries": registries, "files": files,
        "generation_bridge_sha256": sha((root / "source/readability_generation_bridge.json").read_bytes()),
        "runtime_sha256": {rel: sha(p.read_bytes()) for rel, p in paths.items()},
        "protected_sha256": {rel: sha(paths[rel].read_bytes()) for rel in PROTECTED},
    }
    for rel in PROTECTED:
        if paths[rel].read_bytes() != before_paths[rel].read_bytes():
            raise ValueError("Protected runtime changed: " + rel)
    return result


def load(root: Path):
    manifest = read_json(root / "source/readability_manifest.json")
    if manifest.get("schema") != 1:
        raise ValueError("Unsupported readability manifest")
    grouped = {}
    for item in manifest["registries"]:
        p = safe_path(root, item["file"])
        if sha(p.read_bytes()) != item["sha256"]:
            raise ValueError("Reviewed ledger changed; explicitly refresh the manifest: " + item["file"])
        entries = read_json(p)
        for e in entries:
            safe_path(root, e["file"])
            if not isinstance(e.get("before"), str) or not isinstance(e.get("after"), str):
                raise ValueError("Invalid before/after hunk: " + e["file"])
            grouped.setdefault(e["file"], []).append(e)
    if set(grouped) != set(manifest["files"]):
        raise ValueError("Manifest/ledger file set differs")
    return manifest, grouped


def plan(root: Path, *, bridge: bool = False, verify_all: bool = False) -> tuple[dict[str, bytes], dict]:
    """Return a fully checked transaction. This function does not write."""
    manifest, grouped = load(root)
    paths = runtime_paths(root)
    if set(paths) != set(manifest["runtime_sha256"]):
        raise ValueError("Runtime inventory changed: missing=" + repr(sorted(set(manifest["runtime_sha256"]) - set(paths))) +
                         " extra=" + repr(sorted(set(paths) - set(manifest["runtime_sha256"]))))
    staged = {rel: p.read_bytes() for rel, p in paths.items()}
    bridged = []
    if bridge:
        bridge_path = root / "source/readability_generation_bridge.json"
        if sha(bridge_path.read_bytes()) != manifest["generation_bridge_sha256"]:
            raise ValueError("Reviewed generation bridge changed; explicitly refresh the manifest")
        history = read_json(bridge_path)
        if history.get("schema") != 1:
            raise ValueError("Unsupported generation bridge")
        for e in history["files"]:
            rel = e["file"]
            safe_path(root, rel)
            data = staged[rel]
            digest = sha(data)
            if digest in (e["after_sha256"], manifest["runtime_sha256"][rel]):
                continue
            if digest != e["before_sha256"] or data.decode("utf-8") != e["before"]:
                raise ValueError("Unknown raw generator output; review the bridge rather than overwriting new work: " + rel)
            output = e["after"].encode("utf-8")
            if sha(output) != e["after_sha256"]:
                raise ValueError("Corrupt bridge target: " + rel)
            staged[rel] = output
            bridged.append(rel)
    edited = []
    skipped = []
    for rel, entries in grouped.items():
        spec = manifest["files"][rel]
        digest = sha(staged[rel])
        if digest == spec["target_sha256"]:
            skipped.append(rel)
            continue
        if digest not in spec["accepted_baseline_sha256"]:
            raise ValueError("Runtime is neither its reviewed baseline nor its final target: " + rel)
        text = logical(staged[rel])
        for number, e in enumerate(entries, 1):
            before, after = logical(e["before"]), logical(e["after"])
            count = text.count(before) if before else 0
            if count == 0 and e.get("kind") == "approved_first_closeup" and digest in spec["approved_missing_sha256"]:
                continue
            if count != 1:
                raise ValueError("Expected one contextual hunk, found %d at %s #%d" % (count, rel, number))
            text = text.replace(before, after, 1)
        output = encode(text, spec["target_format"])
        if sha(output) != spec["target_sha256"]:
            raise ValueError("Replay does not equal the reviewed final file: " + rel)
        staged[rel] = output
        edited.append(rel)
    for rel, digest in manifest["protected_sha256"].items():
        if sha(staged[rel]) != digest:
            raise ValueError("Protected file would change: " + rel)
    if verify_all:
        wrong = [rel for rel, digest in manifest["runtime_sha256"].items() if sha(staged[rel]) != digest]
        if wrong:
            raise ValueError("Final runtime differs from reviewed targets: " + repr(wrong))
    changes = {rel: data for rel, data in staged.items() if data != paths[rel].read_bytes()}
    return changes, {"bridged": bridged, "edited": edited, "already_final": skipped,
                     "changed_files": len(changes), "runtime_files": len(paths)}


def apply(root: Path, *, bridge: bool = False, verify_all: bool = False, check: bool = False) -> dict:
    changes, report = plan(root, bridge=bridge, verify_all=verify_all)
    if not check:
        for rel, data in changes.items():
            atomic_write(safe_path(root, rel), data)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--bridge", action="store_true", help="Restore known raw generator drift before editorial replay")
    parser.add_argument("--verify-all", action="store_true", help="Check every .rpy against its reviewed target hash")
    parser.add_argument("--check", action="store_true", help="Validate the whole transaction without writes")
    parser.add_argument("--record-manifest", action="store_true", help="Explicitly record completed reviewed ledgers and current target hashes")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--verbose", action="store_true", help="Print complete file lists instead of summary counts")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.record_manifest:
        baseline = args.baseline or Path(read_json(root / "source/readability_session.json")["baseline"])
        manifest = record_manifest(root, baseline.resolve())
        atomic_write(root / "source/readability_manifest.json", (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
        print("READABILITY_MANIFEST_RECORDED", len(manifest["runtime_sha256"]), "runtime files;", len(manifest["files"]), "edited files")
    else:
        report = apply(root, bridge=args.bridge, verify_all=args.verify_all, check=args.check)
        if not args.verbose:
            report = {k: len(v) if isinstance(v, list) else v for k, v in report.items()}
        print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

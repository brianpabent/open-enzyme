#!/usr/bin/env python3
"""Fetch and checksum the frozen public inputs for COMP-048.

This script only retrieves preregistered source bytes. It performs no
result-bearing analysis.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "inputs" / "source-manifest.json"
RULES_PATH = HERE / "inputs" / "design-rules.json"
DEST = HERE / ".comp-runtime-env" / "inputs"
RULES = json.loads(RULES_PATH.read_text())
CHUNK = int(RULES["runtime"]["hash_chunk_bytes"])
TIMEOUT = int(RULES["runtime"]["download_timeout_seconds"])
USER_AGENT = str(RULES["runtime"]["download_user_agent"])


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify(path: Path, expected_bytes: int, expected_sha: str) -> None:
    if path.stat().st_size != expected_bytes:
        raise RuntimeError(
            f"{path.name}: expected {expected_bytes} bytes, "
            f"found {path.stat().st_size}"
        )
    actual = sha256(path)
    if actual != expected_sha:
        raise RuntimeError(
            f"{path.name}: expected SHA-256 {expected_sha}, found {actual}"
        )


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        with destination.open("wb") as handle:
            shutil.copyfileobj(response, handle, CHUNK)


def fetch_direct(source: dict[str, object]) -> Path:
    target = DEST / str(source["local_name"])
    if target.exists():
        try:
            verify(target, int(source["bytes"]), str(source["sha256"]))
            return target
        except RuntimeError:
            target.unlink()
    with tempfile.NamedTemporaryFile(dir=DEST, delete=False) as temp:
        partial = Path(temp.name)
    try:
        download(str(source["url"]), partial)
        verify(partial, int(source["bytes"]), str(source["sha256"]))
        partial.replace(target)
    finally:
        partial.unlink(missing_ok=True)
    return target


def fetch_archive_member(source: dict[str, object]) -> Path:
    target = DEST / str(source["local_name"])
    if target.exists():
        try:
            verify(target, int(source["bytes"]), str(source["sha256"]))
            return target
        except RuntimeError:
            target.unlink()
    with tempfile.TemporaryDirectory(dir=DEST) as temp_dir:
        archive = Path(temp_dir) / "supplement.zip"
        download(str(source["url"]), archive)
        with zipfile.ZipFile(archive) as bundle:
            member = str(source["archive_member"])
            if member not in bundle.namelist():
                raise RuntimeError(f"Supplement member is absent: {member}")
            with bundle.open(member) as incoming, target.open("wb") as outgoing:
                shutil.copyfileobj(incoming, outgoing, CHUNK)
        verify(target, int(source["bytes"]), str(source["sha256"]))
    return target


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    DEST.mkdir(parents=True, exist_ok=True)
    fetched: list[dict[str, object]] = []
    receipt = DEST / "fetch-receipt.json"
    try:
        for source in manifest["sources"]:
            if source["id"] == "bausch_fluck_surfaceome":
                path = fetch_archive_member(source)
            else:
                path = fetch_direct(source)
            fetched.append(
                {
                    "id": source["id"],
                    "local_name": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    except Exception as exc:
        receipt.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "status": "FAILED",
                    "failure_type": type(exc).__name__,
                    "failure": str(exc),
                    "verified_sources": fetched,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
        print(f"Input fetch failed: {exc}", file=sys.stderr)
        return 2
    receipt.write_text(
        json.dumps(
            {"schema_version": 1, "status": "VERIFIED", "sources": fetched},
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    print(f"Verified {len(fetched)} frozen inputs in {DEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

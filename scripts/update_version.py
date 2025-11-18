#!/usr/bin/env python3
"""Utility to bump the SDK version.

Usage:
    python scripts/update_version.py 1.2.3

The script normalizes the provided version (strips a leading "v" if present),
validates it loosely against SemVer rules and writes the value into the
_version.py file that is consumed by setuptools. It prints the normalized
version to stdout for downstream tooling.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VERSION_PATTERN = re.compile(r"^v?(?P<num>\d+\.\d+\.\d+(?:[0-9A-Za-z.\-+_]*)?)$")
PROJECT_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = PROJECT_ROOT / "_version.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update _version.py")
    parser.add_argument(
        "version",
        help="New version string (e.g. 1.2.3 or v1.2.3).",
    )
    return parser.parse_args()


def normalize_version(raw: str) -> str:
    match = VERSION_PATTERN.fullmatch(raw.strip())
    if not match:
        raise ValueError(
            "Version must look like 1.2.3 (optionally prefixed with v). "
            f"Got: {raw!r}"
        )
    return match.group("num")


def update_file(version: str) -> None:
    VERSION_FILE.write_text(f'VERSION = "{version}"\n', encoding="utf-8")


def main() -> int:
    args = parse_args()
    try:
        normalized = normalize_version(args.version)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    update_file(normalized)
    print(normalized)
    return 0


if __name__ == "__main__":
    sys.exit(main())

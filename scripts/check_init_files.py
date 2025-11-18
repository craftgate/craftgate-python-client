#!/usr/bin/env python3
"""Fail if any python module lives outside a proper package.

Every directory underneath craftgate/ that contains Python sources must own
an __init__.py file so the module becomes importable once packaged. This
script walks through the package tree and ensures all ancestors satisfy that
constraint. It prints the offending directories and exits with code 1 on
failure, otherwise exits cleanly.
"""

from pathlib import Path
from typing import List, Set
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = PROJECT_ROOT / "craftgate"
IGNORED_PARTS = {"__pycache__"}


def _relevant_parents(module_path: Path) -> List[Path]:
    parents: List[Path] = []
    for parent in module_path.parents:
        if parent == PACKAGE_ROOT.parent:
            break
        if parent.name in IGNORED_PARTS:
            continue
        parents.append(parent)
    return parents


def main() -> int:
    missing: Set[Path] = set()

    if not PACKAGE_ROOT.exists():
        print("craftgate package root not found", file=sys.stderr)
        return 1

    for py_file in PACKAGE_ROOT.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        if any(part in IGNORED_PARTS for part in py_file.parts):
            continue

        for parent in _relevant_parents(py_file):
            init_file = parent / "__init__.py"
            if not init_file.exists():
                missing.add(parent.relative_to(PACKAGE_ROOT))

    if missing:
        print("Found python modules under directories missing __init__.py:", file=sys.stderr)
        for relative in sorted(missing):
            print(f"- craftgate/{relative.as_posix()}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

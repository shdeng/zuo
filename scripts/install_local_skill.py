from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the canonical repo skill into the local .codex skill directory."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("skills/zuo"),
        help="Canonical skill directory inside the repo.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path(".codex/skills/zuo"),
        help="Local Codex skill install path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    dest = args.dest.resolve()

    if not source.exists():
        raise SystemExit(f"Source skill not found: {source}")

    if dest.exists():
        shutil.rmtree(dest)

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, dest)

    print(f"Installed skill from {source}")
    print(f"to {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

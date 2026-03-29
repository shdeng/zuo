from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_transcript(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "answers" not in data or not isinstance(data["answers"], list):
        raise SystemExit(f"Invalid transcript format: {path}")
    return data


def count_chars(transcript: dict) -> int:
    if isinstance(transcript.get("total_chars"), int):
        return transcript["total_chars"]
    total = 0
    for item in transcript["answers"]:
        total += len(str(item.get("text", "")))
    return total


def summarize(path: Path) -> tuple[str, int, int]:
    transcript = load_transcript(path)
    agent = str(transcript.get("agent") or path.stem)
    turns = len(transcript["answers"])
    total_chars = count_chars(transcript)
    return agent, turns, total_chars


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Score one or two transcript export JSON files by visible character count."
    )
    parser.add_argument("baseline", type=Path)
    parser.add_argument("variant", type=Path, nargs="?")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_agent, base_turns, base_chars = summarize(args.baseline.resolve())

    print(f"{base_agent}: turns={base_turns}, total_chars={base_chars}")

    if not args.variant:
        return 0

    var_agent, var_turns, var_chars = summarize(args.variant.resolve())
    delta = var_chars - base_chars
    pct = 0.0 if base_chars == 0 else delta / base_chars * 100.0

    print(f"{var_agent}: turns={var_turns}, total_chars={var_chars}")
    print(f"delta_chars={delta}")
    print(f"delta_pct={pct:.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

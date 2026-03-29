# zuo

## 中文

`zuo` 者，Codex 之一 skill 也。其志惟一：使 agent 出辞更短、更劲、更近古文，而不伤技义。

此库所以公诸 GitHub，使众可共修 skill 之文，共定试法，共校结果，而徐得其优。

### 所图

- 不作一时 prompt，务成可传可复验之 skill。
- 代码、路径、指令、报错、标识，悉守原文。
- 凡自然语言，务求更俭。
- 以可复验之多轮会话，校诸变体之得失。

### 目录

- `skills/zuo/`
  此库所奉之正本。
- `sessions/`
  共用试题。
- `scripts/`
  安装与计分之小具。
- `docs/benchmark-protocol.md`
  校试之章程。
- `results/README.md`
  试录与简评。
- `variants/README.md`
  变体之置法与命名之例。

### 速用

1. 修 [skills/zuo/SKILL.md](/D:/Dev/zuo/skills/zuo/SKILL.md)。
2. 纳之于本地 Codex：

```powershell
python scripts/install_local_skill.py
```

3. 依共用二十轮会话而试之。
4. 导出 `baseline` 与 `with-skill` 之 transcript JSON。
5. 以此较之：

```powershell
python scripts/score_transcript.py baseline.json with-skill.json
```

### 共修之序

1. 修 `skills/zuo/`，或于 `variants/` 下立一新本。
2. 仍用 [sessions/sync-users-review-20.json](/D:/Dev/zuo/sessions/sync-users-review-20.json)。
3. 记其结果于 `results/`。
4. 发 PR，附 skill 之异同、试录之数、与简短一说。

### 今状

此库已具 skill 正本、校试章程、与初步试录。
今所用者，为固定之二十轮 code-review / sync-debugging 会话。

### 公开之前

此库未定许可证。
若将尽公于世，宜先择其 license；此事涉权责，不可妄代为断。

## English

`zuo` is a Codex skill project with one narrow aim:
make agent output shorter, harder, and closer to concise classical Chinese without breaking technical accuracy.

This repository is meant for public collaboration on GitHub.
Contributors can refine the skill text, propose variants, run the same benchmark session, and compare results in a shared format.

### Goals

- Build a reusable, publishable Codex skill rather than a one-off prompt.
- Preserve code, paths, commands, errors, and identifiers exactly.
- Compress natural-language output as much as possible.
- Measure changes with repeatable multi-turn sessions.

### Layout

- `skills/zuo/`
  Canonical skill source.
- `sessions/`
  Shared benchmark sessions.
- `scripts/`
  Utilities for local installation and scoring.
- `docs/benchmark-protocol.md`
  Benchmark rules.
- `results/README.md`
  Running notes and scoreboard.
- `variants/README.md`
  How to add and name experimental variants.

### Quick Start

1. Edit [skills/zuo/SKILL.md](/D:/Dev/zuo/skills/zuo/SKILL.md).
2. Install it into your local Codex workspace:

```powershell
python scripts/install_local_skill.py
```

3. Run the shared 20-turn benchmark session.
4. Export transcript JSON for both `baseline` and `with-skill`.
5. Compare them:

```powershell
python scripts/score_transcript.py baseline.json with-skill.json
```

### Contribution Loop

1. Improve `skills/zuo/` or add a variant under `variants/`.
2. Re-run [sessions/sync-users-review-20.json](/D:/Dev/zuo/sessions/sync-users-review-20.json).
3. Record the result in `results/`.
4. Open a PR with the skill diff, benchmark result, and a short note.

### Current State

This repository already contains a canonical skill, a benchmark protocol, and initial exploratory results.
The current benchmark uses a fixed 20-turn code-review / sync-debugging session.

### Before Public Release

This repository does not yet include a final license.
Choose one deliberately before making the project fully public.

# Contributing / 共修

## 中文

### 可改者

- 修 [skills/zuo/SKILL.md](/D:/Dev/zuo/skills/zuo/SKILL.md)。
- 于 `variants/<slug>/` 下立新本。
- 修 `sessions/` 中试题。
- 修 `scripts/` 中计分与安装之具。

### 不可轻动者

- 共用 session 未别立新案者，毋暗改而仍称可比。
- 模型不同者，毋伪作同场。
- 只呈一边之结果者，毋称比较。

### 变体命名

- 惟用小写字母、数字、连字符。
- 务短。
- 名须见其策。
- 例如：
  `hard-cut`
  `fewer-connectors`
  `more-technical-preserve`

### PR 所当具

- 所改 skill 或变体之名。
- 所用 benchmark session。
- 模型与环境。
- `baseline` transcript。
- `with-skill` transcript。
- `scripts/score_transcript.py` 之输出。
- 一语言其得失。

### 审核之准

- 辞更短，不足独为胜。
- 强变体若伤技义，则不可取。
- 若其压缩，实由删去应有之义，则非进也。

## English

### What You May Change

- Improve [skills/zuo/SKILL.md](/D:/Dev/zuo/skills/zuo/SKILL.md).
- Add a new candidate under `variants/<slug>/`.
- Improve benchmark sessions under `sessions/`.
- Improve scoring or installation scripts under `scripts/`.

### What Must Stay Stable

- Do not silently change the shared benchmark session and still claim comparability.
- Do not compare different models as if they were the same run.
- Do not report only one side of a comparison.

### Variant Naming

- Use lowercase letters, digits, and hyphens only.
- Keep names short.
- Let the name reflect the strategy.
- Examples:
  `hard-cut`
  `fewer-connectors`
  `more-technical-preserve`

### Required PR Payload

- Which skill or variant you changed.
- Which benchmark session you used.
- Model and environment.
- `baseline` transcript.
- `with-skill` transcript.
- Output from `scripts/score_transcript.py`.
- One short note about the tradeoff.

### Review Standard

- Shorter is not enough by itself.
- A stronger variant must not break technical accuracy.
- If compression comes from dropping required content, it is not an improvement.

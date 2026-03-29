# Benchmark Protocol / 校试章程

## 中文

### 旨

共守一法，使诸变体可同衡而相校。

### 所须

- 模型同。
- session 同。
- workspace 内容同。
- 只设二臂：
  `baseline`
  `with-skill`

### 正用之题

若 PR 非为试题设计而作，则用 [sessions/sync-users-review-20.json](/D:/Dev/zuo/sessions/sync-users-review-20.json)。

### 所当导出

每一臂各出一 JSON，其式如下：

```json
{
  "agent": "baseline",
  "answers": [
    { "turn": 1, "text": "..." }
  ],
  "total_chars": 1234
}
```

`total_chars` 者，诸轮可见答辞字符之总和也。

### 计分

首要之数：
- 可见输出字符总数

次要之数：
- 每轮长短
- 所需内容有无阙失
- 代码与标识有无改坏

进阶之数：
- input tokens
- output tokens
- total tokens

若得 token telemetry，则并附之。
若不得，毋妄造之。

### 所当上报

至少当具：

- 日期
- 模型
- 变体名
- baseline 总字符
- variant 总字符
- delta 字符
- delta 百分比
- 一语言其质变

### 废案之例

有下列情形者，其结果不可取：

- 两边所用 prompts 或轮数不同
- 一边删去应有之义
- 一边改坏本当保留之代码标识或指令文字

## English

### Purpose

Use one shared protocol so all variants can be compared on equal footing.

### Required Setup

- Same model on both sides.
- Same session file.
- Same workspace contents.
- Two arms only:
  `baseline`
  `with-skill`

### Canonical Session

Unless a PR is specifically about benchmark design, use [sessions/sync-users-review-20.json](/D:/Dev/zuo/sessions/sync-users-review-20.json).

### Required Export Format

Each arm should export one JSON object shaped like:

```json
{
  "agent": "baseline",
  "answers": [
    { "turn": 1, "text": "..." }
  ],
  "total_chars": 1234
}
```

`total_chars` is the sum of visible answer characters across all turns.

### Scoring

Primary metric:
- visible output character count

Secondary metrics:
- per-turn length
- whether required content was preserved
- whether code and identifiers stayed intact

Advanced metrics:
- input tokens
- output tokens
- total tokens

If token telemetry is available, include it.
If not, do not invent it.

### Reporting

At minimum, include:

- date
- model
- variant name
- baseline total chars
- variant total chars
- delta chars
- delta percent
- one sentence on quality impact

### Invalid Results

Reject a result if:

- the compared runs used different prompts or different turn counts
- one side omitted required content
- one side changed code identifiers or command text that should have been preserved

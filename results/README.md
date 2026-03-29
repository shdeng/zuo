# Results / 试录

## 中文

此皆初试之数，可为端倪，未可遽断。

### 记分

| 日期 | 法 | 模型 | 变体 | baseline 字数 | variant 字数 | 差值 | 百分比 | 备注 |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 2026-03-29 | sub-agent | gpt-5.4-mini | hard-cut | 2187 | 2044 | -143 | -6.54% | 压缩最强，辞亦最硬 |
| 2026-03-29 | sub-agent | gpt-5.4-mini | middle-tight | 2338 | 2247 | -91 | -3.89% | 收束较强，尚可读 |
| 2026-03-29 | sub-agent | gpt-5.4-mini | earliest-soft | 2331 | 2309 | -22 | -0.94% | 压缩较缓，较自然 |

### 读表法

- `delta` 为负者，于压缩为胜。
- 更短者，未必即更佳。
- 惟其既短且不伤技义者，可称优胜。

## English

These are exploratory results.
They are useful as signals, not as final truth.

### Scoreboard

| date | method | model | variant | baseline chars | variant chars | delta chars | delta % | note |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| 2026-03-29 | sub-agent | gpt-5.4-mini | hard-cut | 2187 | 2044 | -143 | -6.54% | strongest compression, harshest tone |
| 2026-03-29 | sub-agent | gpt-5.4-mini | middle-tight | 2338 | 2247 | -91 | -3.89% | tighter, still readable |
| 2026-03-29 | sub-agent | gpt-5.4-mini | earliest-soft | 2331 | 2309 | -22 | -0.94% | mild compression, more natural |

### How To Read The Table

- Negative `delta` is better for compression.
- Shorter is not automatically better.
- A variant matters only if it stays accurate while getting shorter.

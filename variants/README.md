# Variants / 变体

## 中文

凡欲试新本者，置于此。

其式宜如下：

```text
variants/
  your-variant/
    SKILL.md
    agents/
      openai.yaml
```

### 其法

- 共用之 benchmark session，非为试题设计之 PR，毋改。
- 变体之名，惟用小写字母、数字、连字符。
- 试后之数，记于 `results/`。

## English

Put experimental variants here.

Recommended layout:

```text
variants/
  your-variant/
    SKILL.md
    agents/
      openai.yaml
```

### Rules

- Keep the shared benchmark session unchanged unless the PR is explicitly about benchmark design.
- Name variants with lowercase letters, digits, and hyphens only.
- Record benchmark output in `results/`.

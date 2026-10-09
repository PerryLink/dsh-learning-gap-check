# dsh-learning-gap-check — 能力差距与培养计划核对

[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)

`dsh-learning-gap-check` 读取一份能力差距与培养计划台账——员工表头加每项能力一行——核对这份台账自身的算术与闭环：每条差距是否写明岗位与能力项、记录的两个等级是否可解析为数值、差距是否等于要求等级减现有等级、超过你配置阈值的差距是否填写培养措施、培养措施是否写明责任人与完成期限、完成日期是否不晚于完成期限、培养状态是否出自本机构口径的取值。

## 实际输出长什么样

![Terminal demo of dsh-learning-gap-check: real output over its LG-002 fixture](https://raw.githubusercontent.com/PerryLink/dsh-learning-gap-check/main/docs/assets/dsh-learning-gap-check-demo.png)

本插件对自己 `LG-002` 测试夹具的**真实输出**，不是示意图。规则库不伪造引文，因此每条发现都会同时写明所引条款，以及该条款原文本次未取得。

## 它回答什么问题

| 你会问 | 它怎么答 |
|---|---|
| 某行填了能力项，岗位栏空着，会被报出吗？ | `LG-001` 只在 `position` 与 `competency` 都为空时报出该行，填写其中任意一项即通过。它只核对这一行有没有写明岗位与能力项，不判断该岗位的能力要求是否合理、是否完整。 |
| 台账里的等级写成「熟练」「掌握」，或者写成 A、B、C，会怎么处理？ | `LG-002` 读 `actualLevel`，要求它可解析为数值，写成文字或字母会按不可解析报出。本插件不内置任何能力等级刻度：请把台账改成可比较的数字刻度，或连同 `LG-003` 一起停用。它只核对可解析性，不判断评估结果是否客观、是否准确。 |
| 差距栏写 `3`，但要求等级 `4` 减现有等级 `2` 得 `2`，这能查出来吗？ | 能。`LG-003` 按 `requiredLevel − actualLevel` 重算，容差为 `0`，与台账里存的 `gapLevel` 不符即报出该行。只有三个字段都是可解析数值时本条才执行，缺任一项即进 `skipped`。负值如实报出——可能是两栏填反了；差距大到什么程度才算问题，本条不作判断。 |
| 某行填了培养措施，但责任人和完成期限都空着。 | `LG-005` 要求凡填了 `action` 的行都必须有 `owner` 与 `dueAt`，缺任一项即报出该行。它只核对这两栏是否记录，不判断措施是否有效、期限是否合理。 |
| 某行的完成日期晚于完成期限，或者两栏填反了。 | `LG-006` 逐行比较 `dueAt` 与 `completedAt`，完成期限早于完成日期时报出该行。规则库如实写明它的限度：它只比较两个日期的先后，不判断是否真的按期完成。无法解析的日期会单独报出，不会静默放过。 |
| `LG-004` 与 `LG-007` 从来没报过东西，是不是说明这两条已经通过了？ | 不是，这两条都把自己报进 `skipped`。`LG-004` 的 `threshold` 出厂为 `0`，表示未配置——请填上「差距多大就必须提措施」；`LG-007` 的状态取值出厂为空——请按本机构口径填入。配置之后，`LG-004` 只核对培养措施栏是否填写，`LG-007` 只核对状态取值是否在册，两者都不判断措施是否真的落实。 |

## 依据的标准

| 文件 | 文号 | 引用它的规则 |
|---|---|---|
| 《质量管理 能力管理和人员发展指南》 | GB/T 19025—2023（质量管理 能力管理和人员发展指南；2023-03-17 发布并实施；归口全国质量管理和质量保证标准化技术委员会；条号本次未取得） | LG-001, LG-002, LG-003, LG-005, LG-006 |
| 本机构培训与发展管理口径（本机构配置） | 无统一标准（本条依据为本机构配置的差距阈值） | LG-004 |
| 本机构培训与发展管理口径（本机构配置） | 无统一标准（本条依据为本机构配置的状态口径） | LG-007 |

**Boundary:** this plugin checks a **能力差距与培养计划台账** for arithmetic and closure — that each gap names its
position and competency, that the two level columns parse as numbers, that the gap equals required minus actual,
that a gap beyond your threshold carries a development action, that an action names an owner and a due date, that
the completion date is not later than the deadline, and that the action status comes from your vocabulary. It does
**not** decide whether an employee is competent, whether an assessment was objective, whether a development action
worked, or whether someone should be reassigned or dismissed.

> ### ⚠️ What this plugin deliberately leaves out
>
> **It ships no competency scale, and it assumes the levels are numbers.** `LG-002` and `LG-003` read three
> numeric columns and check the arithmetic between them. A register using letter grades (`A`/`B`/`C`) or words
> (`熟练`/`掌握`) is **reported as unparseable**, because comparing such levels is a modelling decision the
> plugin will not make for you. Convert the scale, or disable those rules.
>
> **It ships no threshold for "big enough to need action".** How much of a gap obliges a development action is
> the institution's talent-management call — some units require one for any shortfall, others tolerate a step —
> so `LG-004`'s threshold starts at `0` and the rule reports itself in `skipped` until you set it.
>
> **The status vocabulary ships empty** for the same reason. And the date rule checks only that the deadline
> does not precede the completion date, which is a data-entry property: **it does not judge whether the work was
> done late.**
>
> **Every `excerpt` in the rule pack says, in so many words, that the clause text was not obtained.** The regime
> lives in GB/T 19025 (identical to ISO 10015) and each institution's qualification and training rules. The
> verification pass could not retrieve verbatim clause text, so the pack states the gap in the `excerpt` field
> itself and keeps every rule at `warn` or `info`. **When the texts are in hand, replace each `excerpt` with the
> real clause and raise `kind` to `direct`.**

## Compatibility

| 项目 | 状态 |
|---|---|
| Harness | 对等版本范围 `>=0.1.2-rc.1 <0.2.0 \|\| >=0.2.0-0 <0.3.0` —— 已实测同时接受 `0.2.0-rc.2` 与 `0.2.1-alpha.1`。**刻意不声明 `engines.dsh`**：它没有任何读取者，也无法拒装任何宿主 |
| Node | `^22.19.0 || >=24.0.0` |
| 平台 | 全平台（纯 ESM；无原生代码、无联网、不调用模型） |
| 工具模式 | `native` / `ptc` / `both` 均可；批量校验整个目录时建议 `ptc`，schema 成本只付一次 |

## What it does

规则表、字段说明与行为细节见 [README.md](README.md#what-it-does)（英文主版本）。本插件只列出材料与所引条款之间的字面差异，并对无法执行的检查在 `skipped` 中逐项说明。

## Install

```sh
dsh plugin --profile <name> add dsh-learning-gap-check
dsh --profile <name> --dump-config | grep 'dsh-learning-gap-check'
```

## Configuration

全部可调参数都在 `src/config.ts` 的 Schemastery schema 中，只改 `cordis.yml` 即可生效，无需改代码；逐条阈值在 `rules/` 下的规则库文件里。

| 键 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `rulesFile` | string | `rules/learning-gap-check.yaml` | 规则库文件路径，相对插件包根目录 |
| `disabledRules` | string[] | `[]` | 要停用的规则 id 列表；每条都会出现在 `skipped` 中 |
| `onlyRules` | string[] | `[]` | 只执行这些规则 id；留空表示执行全部规则 |
| `skipNotes` | string | `""` | 附加到每条 `skipped` 说明后的备注 |
| `timeoutMs` | number | `120000` | 工具协作式超时预算（毫秒） |

## Material format

支持 JSON 与 YAML。完整字段示例见 [README.md](README.md#material-format)（英文主版本）。字段在读取层是可选的，由检查引擎校验，因此部分导出的材料会产生"缺项"类差异，而不是让程序崩溃。

## Rule sources

规则数据与代码分离，每条规则都带文件名、文号、按原文自身编号体系的条款号、逐字摘录与来源地址。加载期强制：摘录必须是真实引文且不少于八个字符；依据仅为原则性条款（`kind: derived-from-principle`，严重级上限 `warn`）或本机构配置（`kind: institutional-configuration`，上限 `info`）的检查不得标为 `error`。夸大依据的规则库会在加载期失败，而不会产出一份看起来很有底气的报告。

核验中确认的边界与"刻意没有作出的结论"见 [README.md](README.md#rule-sources)（英文主版本）与随包的 `rules/evidence/` 目录。

## Troubleshooting

- **插件装上了但工具不出现**：确认 `main` 指向 `lib/index.mjs` 且 `pnpm run build` 已生成该文件；`main` 写错会让加载器静默跳过该条目。
- **`dsh plugin add` 报版本不兼容**：peer 范围覆盖 `0.1.x` 与 `0.2.x`；若运行时在其之外，可显式豁免：`dsh plugin --profile <name> allow-version <包名@版本> --dsh-version <runtime> --accept-risk`
- **某条规则没有执行**：查看 `skipped` 数组，其中写明了规则 id 与原因。
- **`check` 报 `manifest-peers` 失败**：静态检查器比对的是一份早于 0.2 世代的硬编码 peer 范围；安装期的 peer 校验以运行时为准。这是 `dsh-plugin-dev` 的已知上游问题。
- **时间看起来偏移**：全部计算都是对输入字符串做墙上时钟运算，不做时区换算。

## Development

```sh
pnpm install
pnpm run typecheck
pnpm test
pnpm run build
node ../scripts/sync-shared.mjs dsh-learning-gap-check
```

第 4 项把 `../_shared` 的共享件同步进 `src/shared/`；每次改动共享件后都要重跑。

## License

[Apache License 2.0](LICENSE) © 2026 dsh-learning-gap-check contributors.

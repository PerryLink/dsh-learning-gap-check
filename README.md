# dsh-learning-gap-check — Competency gap and development plan register check

[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)

`dsh-learning-gap-check` reads one competency-gap and development-plan register — the employee header plus one row per competency — and checks that register's own arithmetic and closure: that each gap names its position and competency, that the recorded levels parse as numbers, that the gap equals the required level minus the actual level, that a gap beyond your configured threshold carries a development action, that an action names an owner and a due date, that the completion date is not later than the deadline, and that the action status comes from your own vocabulary.

## What it looks like

![Terminal demo of dsh-learning-gap-check: real output over its LG-002 fixture](https://raw.githubusercontent.com/PerryLink/dsh-learning-gap-check/main/docs/assets/dsh-learning-gap-check-demo.png)

Real output from this plugin over its own `LG-002` test fixture — not a mock-up. The rule pack ships no invented quotations, so a finding names both the clause it applied and the fact that the clause text was not obtained.

## What it answers

| You ask | What it answers |
|---|---|
| A row carries the competency but leaves the position blank. | `LG-001` reports a row only when `position` and `competency` are both empty; one of the two filled is enough. It checks that the row names a post and a competency, not whether the competency requirement for that post is reasonable or complete. |
| Our levels are written as words (`熟练`, `掌握`) or as letters (`A`/`B`/`C`) — what happens? | `LG-002` reads `actualLevel` and requires it to parse as a number, so a level written as a word or a letter is reported as unparseable. The plugin ships no competency scale: convert the register to a numeric scale, or disable `LG-002` together with `LG-003`. Parseability is all it checks — whether the assessment was objective or accurate is not judged. |
| The gap column says `3`, but required `4` minus actual `2` is `2` — does that get caught? | `LG-003` recomputes `requiredLevel − actualLevel` with a tolerance of `0` and reports the row whose stored `gapLevel` disagrees. It runs only when all three columns hold parseable numbers; if one is missing the rule goes to `skipped`. A negative gap is reported as it stands, because the columns may have been transposed, and the rule does not decide how large a gap counts as a problem. |
| A row records a development action but no owner and no due date. | `LG-005` requires `owner` and `dueAt` on every row whose `action` is filled, and reports the row missing either one. It checks that the two fields are recorded; it does not judge whether the action is effective or the deadline reasonable. |
| A row's completion date is later than its due date, or the two columns were filled in the wrong order. | `LG-006` compares `dueAt` with `completedAt` on every row and reports the row when the due date falls before the completion date. The pack states its limit in its own words: it compares only the order of the two dates and does not decide whether the work was really completed on schedule. A date it cannot parse is reported in its own right instead of being passed over. |
| `LG-004` and `LG-007` never report anything — does that mean my register passed them? | No: both rules report themselves in `skipped`. `LG-004` ships with `threshold: 0`, which means unconfigured — set the gap size at which a development action becomes mandatory. `LG-007` ships with an empty status vocabulary — fill it from your institution's own wording. Once configured, `LG-004` checks only that the action column is filled and `LG-007` only that the status value is in your vocabulary; neither judges whether the action was really carried out. |

## Standards it follows

| Document | Number | Cited by rules |
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

| Surface | Status |
|---|---|
| Harness | Peer range `>=0.1.2-rc.1 <0.2.0 \|\| >=0.2.0-0 <0.3.0` — verified to accept both `0.2.0-rc.2` and `0.2.1-alpha.1`. `engines.dsh` is deliberately not declared: it has no reader and cannot reject a host |
| Node | `^22.19.0 || >=24.0.0` |
| Platforms | All (plain ESM; no native code, no network, no model call) |
| Tool mode | Works in `native`, `ptc` and `both`; for a department's plan use `ptc` |

## What it does

Registers the `learning_gap_check` tool. It reads one gap-and-plan register — the employee header plus one row per
competency — applies a versioned rule pack, and returns a report.

| Rule | Check | Severity | Basis kind |
|---|---|---|---|
| `LG-001` | the position and competency are recorded | warn | principle |
| `LG-002` | the actual level parses as a number | warn | principle |
| `LG-003` | the gap equals required minus actual | warn | principle |
| `LG-004` | a gap beyond your threshold carries an action (off by default) | info | local |
| `LG-005` | an action names an owner and a due date | warn | principle |
| `LG-006` | the deadline does not precede the completion date | warn | principle |
| `LG-007` | the status comes from your vocabulary (off by default) | info | local |

## Install

```sh
dsh plugin --profile <name> add dsh-learning-gap-check
dsh --profile <name> --dump-config | grep 'dsh-learning-gap-check'
```

## Configuration

| Key | Type | Default | Description |
|---|---|---|---|
| `rulesFile` | string | `rules/learning-gap-check.yaml` | Rule-pack path, relative to the package root |
| `disabledRules` | string[] | `[]` | Rule ids to stop running; each appears in `skipped` |
| `onlyRules` | string[] | `[]` | Run only these rule ids; empty runs every rule |
| `skipNotes` | string | `""` | Note appended to every `skipped` reason |
| `timeoutMs` | number | `120000` | Cooperative tool timeout budget |

Rule-level parameters worth knowing:

- `LG-003` `resultField` / `expression` / `tolerance` — the gap arithmetic, `requiredLevel − actualLevel` by
  default with no tolerance. A negative result is reported as-is, since it may mean the columns were transposed.
- `LG-004` `triggerField` / `threshold` / `requiredField` — your rule for when an action becomes mandatory.
  A threshold of `0` means the rule does not run; `1` means a gap of one step or more.
- `LG-005` `conditionField` / `requiredFields` — what triggers the owner-and-deadline requirement.
- `LG-007` `values` — your status vocabulary, e.g. `[未开始, 进行中, 已完成, 已验收]`. Empty means no check.

## Material format

The tool accepts JSON or YAML:

```yaml
employee: 张工
department: 设备部
plan: 2026 年度能力提升计划
cycle: 2026 上半年
rows:
  - { 序号: '1', 岗位: 设备工程师, 能力项: 设备故障诊断, 要求等级: '4',
      现有等级: '2', 差距等级: '2', 评估方法: 实操考核 + 主管评价,
      评估日期: 2026-03-01, 培养措施: 安排为期三个月的现场带教与故障复盘,
      责任人: 李主管, 完成期限: 2026-06-30, 完成日期: 2026-06-20,
      状态: 进行中, 评估人: 王经理 }
```

Column names are matched case-insensitively and ignoring spaces, underscores and hyphens; the register's own
column names are kept, so a finding names the column it read.

## Rule sources

Rule data lives in `rules/learning-gap-check.yaml`. The pack's header states the citation gap in full, and each
rule's `note` repeats the part that matters for that rule. The load-time guard that normally enforces "an
excerpt must be a real quotation of at least eight characters" cannot tell a quotation from a description —
so this pack leans on the header, the per-rule notes and a test that asserts every `excerpt` admits the gap.

## Troubleshooting

- **`LG-002` fires on my `熟练` levels.** The plugin assumes numeric levels so it can check the arithmetic.
  Convert the scale, or disable `LG-002` and `LG-003`.
- **`LG-003` fires with a negative "should be".** The actual level exceeds the required one. Either the columns
  were transposed or the row records an over-qualified person; decide which and correct the data or disable the
  rule.
- **`LG-004` never runs.** Its threshold is `0`; set the gap size at which an action becomes mandatory.
- **`LG-006` fires although the work finished on time.** The rule compares the deadline against the completion
  date, so a completion *before* the deadline means the two columns are transposed. It makes no finding about
  lateness.
- **`LG-007` never runs.** Its vocabulary is empty; fill it with your statuses.
- **The plugin installs but the tool never appears.** Check that `main` resolves to `lib/index.mjs` and
  that `pnpm run build` produced it; a wrong `main` makes the loader skip the entry silently.
- **`dsh plugin add` refuses the package as incompatible.** The peer range covers `0.1.x` and `0.2.x`; if
  your runtime sits outside it, grant an explicit exemption:
  `dsh plugin --profile <name> allow-version dsh-learning-gap-check@0.1.0 --dsh-version <runtime> --accept-risk`
- **`check` reports `manifest-peers` as failed.** The static checker compares against a hard-coded peer
  range that predates the 0.2 line. The runtime enforces peer compatibility at install time, so the
  declared range is the correct one; this is a known upstream issue in `dsh-plugin-dev`.

## Development

```sh
pnpm install
pnpm run typecheck   # tsc --noEmit
pnpm test            # vitest, the shared table-plugin suite plus paired fixtures
pnpm run build       # tsdown -> lib/index.mjs + lib/index.d.mts
node ../scripts/sync-shared.mjs dsh-learning-gap-check   # refresh src/shared from ../_shared
```

The plugin is **data-only**: `src/model.ts` declares the table shape, the shared kit supplies the reader and
the check engine, and the rule pack declares every check.

## License

[Apache License 2.0](LICENSE) © 2026 dsh-learning-gap-check contributors.

# dsh-learning-gap-check — Registo de lacunas de competência e verificação do plano de desenvolvimento

[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)

`dsh-learning-gap-check` lê um registo de lacunas de competência e plano de desenvolvimento —o cabeçalho do colaborador mais uma linha por competência— e verifica a aritmética e o fecho desse próprio registo: que cada lacuna indique o seu posto e a sua competência, que os níveis registados sejam analisáveis como números, que a lacuna seja igual ao nível exigido menos o nível atual, que uma lacuna acima do limiar que configurar traga uma ação de desenvolvimento, que a ação indique responsável e prazo, que a data de conclusão não seja posterior ao prazo e que o estado da ação venha do seu próprio vocabulário.

## Como é a saída

![Terminal demo of dsh-learning-gap-check: real output over its LG-002 fixture](https://raw.githubusercontent.com/PerryLink/dsh-learning-gap-check/main/docs/assets/dsh-learning-gap-check-demo.png)

Saída real deste plugin sobre o seu próprio fixture de teste `LG-002` — não é uma simulação. O pacote de regras não inventa citações, por isso cada achado nomeia a cláusula aplicada e avisa que o seu texto não foi obtido.

## O que ele responde

| Você pergunta | O que ele responde |
|---|---|
| Uma linha traz a competência mas deixa o posto em branco. | `LG-001` só assinala uma linha quando `position` e `competency` estão ambas vazias; basta que uma delas esteja preenchida. Verifica que a linha indique o posto e a competência, não se a exigência de competência desse posto é razoável ou completa. |
| Os nossos níveis estão escritos com palavras («熟练», «掌握») ou com letras (A/B/C) — o que acontece? | `LG-002` lê `actualLevel` e exige que seja analisável como número, pelo que um nível em palavras ou letras é reportado como não analisável. O plugin não inclui qualquer escala de competência: converta o registo para uma escala numérica ou desative `LG-002` juntamente com `LG-003`. A analisabilidade é tudo o que verifica; não julga se a avaliação foi objetiva ou exata. |
| A coluna da lacuna diz `3`, mas `4` menos `2` dá `2` — isso é detetado? | Sim. `LG-003` recalcula `requiredLevel − actualLevel` com tolerância `0` e assinala a linha cujo `gapLevel` registado não coincide. Só corre quando as três colunas têm números analisáveis; se faltar uma, a regra passa a `skipped`. Um valor negativo é reportado tal como está, porque as colunas podem estar trocadas, e a regra não decide a partir de que dimensão a lacuna é um problema. |
| Uma linha regista uma ação de desenvolvimento, mas sem responsável nem prazo. | `LG-005` exige `owner` e `dueAt` em todas as linhas com `action` preenchida e assinala a linha à qual falta um dos dois. Verifica que os dois campos estejam registados; não julga se a ação é eficaz nem se o prazo é razoável. |
| A data de conclusão de uma linha é posterior ao seu prazo, ou as duas colunas estão trocadas. | `LG-006` compara `dueAt` com `completedAt` em cada linha e assinala a linha quando o prazo é anterior à data de conclusão. O pacote de regras declara o seu limite por palavras próprias: compara apenas a ordem das duas datas e não decide se o trabalho foi realmente concluído dentro do prazo. Uma data que não consegue analisar é reportada à parte em vez de ser ignorada. |
| `LG-004` e `LG-007` nunca reportam nada — significa que o meu registo passou nestas regras? | Não: ambas as regras se declaram em `skipped`. `LG-004` vem com `threshold: 0`, ou seja, por configurar: defina a partir de que lacuna a ação de desenvolvimento é obrigatória. `LG-007` vem com o vocabulário de estados vazio: preencha-o com a terminologia da sua instituição. Depois de configuradas, `LG-004` verifica apenas que a coluna da ação está preenchida e `LG-007` apenas que o valor do estado consta do seu vocabulário; nenhuma julga se a ação foi realmente executada. |

## Normas que segue

| Documento | Número | Regras que o citam |
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

| Superfície | Estado |
|---|---|
| Harness | Faixa de peers `>=0.1.2-rc.1 <0.2.0 \|\| >=0.2.0-0 <0.3.0` — verificada para aceitar tanto `0.2.0-rc.2` quanto `0.2.1-alpha.1`. **`engines.dsh` não é declarado**: não tem leitor e não pode recusar nenhum host |
| Node | `^22.19.0 || >=24.0.0` |
| Plataformas | Todas (ESM puro; sem código nativo, sem rede, sem chamada ao modelo) |
| Modo de ferramenta | Funciona em `native`, `ptc` e `both`; para um diretório inteiro use `ptc` |

## What it does

A tabela de regras, os campos e o comportamento detalhado estão em [README.md](README.md#what-it-does) (versão principal em inglês). O plugin apenas lista divergências literais frente às cláusulas citadas e indica em `skipped` cada verificação que não pôde ser executada.

## Install

```sh
dsh plugin --profile <name> add dsh-learning-gap-check
dsh --profile <name> --dump-config | grep 'dsh-learning-gap-check'
```

## Configuration

Todos os parâmetros ajustáveis ficam no esquema Schemastery de `src/config.ts`, portanto mudam pelo `cordis.yml` sem editar código; os limites por regra ficam no pacote de regras sob `rules/`.

| Chave | Tipo | Padrão | Descrição |
|---|---|---|---|
| `rulesFile` | string | `rules/learning-gap-check.yaml` | Caminho do pacote de regras, relativo à raiz do pacote |
| `disabledRules` | string[] | `[]` | Ids de regras a desativar; cada uma aparece em `skipped` |
| `onlyRules` | string[] | `[]` | Executar apenas estas regras; vazio executa todas |
| `skipNotes` | string | `""` | Nota acrescentada a cada motivo de `skipped` |
| `timeoutMs` | number | `120000` | Orçamento de tempo limite cooperativo da ferramenta |

## Material format

Aceita JSON ou YAML. O exemplo completo de campos está em [README.md](README.md#material-format) (versão principal em inglês). Os campos são opcionais na camada de leitura e validados pelo motor, de modo que uma exportação parcial gera achados sobre o que falta em vez de falhar.

## Rule sources

Os dados das regras ficam separados do código: cada regra traz documento, número, cláusula na numeração própria da fonte, trecho literal e URL de origem. O carregador impõe que o trecho seja citação real de pelo menos oito caracteres e que uma verificação baseada apenas em princípio geral (`kind: derived-from-principle`, teto `warn`) ou em política local (`kind: institutional-configuration`, teto `info`) nunca seja declarada `error`.

Os limites verificados e as conclusões deliberadamente **não** afirmadas estão em [README.md](README.md#rule-sources) (versão principal em inglês) e em `rules/evidence/`.

## Troubleshooting

- **O plugin instala mas a ferramenta não aparece**: confirme que `main` resolve para `lib/index.mjs` e que `pnpm run build` o gerou.
- **`dsh plugin add` recusa o pacote**: a faixa de peers cobre `0.1.x` e `0.2.x`; fora dela, conceda isenção explícita com `dsh plugin --profile <name> allow-version <pkg@ver> --dsh-version <runtime> --accept-risk`.
- **Uma regra não executou**: leia o arranjo `skipped`.
- **`check` informa `manifest-peers` como falha**: problema conhecido do `dsh-plugin-dev`; o runtime aplica a compatibilidade na instalação.
- **Os horários parecem deslocados**: toda a aritmética é de hora local sobre as cadeias fornecidas.

## Development

```sh
pnpm install
pnpm run typecheck
pnpm test
pnpm run build
node ../scripts/sync-shared.mjs dsh-learning-gap-check
```

O último comando copia o kit compartilhado de `../_shared` para `src/shared/`; execute-o novamente após cada alteração compartilhada.

## License

[Apache License 2.0](LICENSE) © 2026 dsh-learning-gap-check contributors.

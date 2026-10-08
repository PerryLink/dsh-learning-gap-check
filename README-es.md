# dsh-learning-gap-check — Registro de brechas de competencia y verificación del plan de desarrollo

`dsh-learning-gap-check` lee un registro de brechas de competencia y plan de desarrollo —la cabecera del empleado más una fila por competencia— y comprueba la aritmética y el cierre de ese propio registro: que cada brecha indique su puesto y su competencia, que los niveles registrados se analicen como números, que la brecha sea igual al nivel requerido menos el nivel actual, que una brecha superior a su umbral configurado lleve una acción de desarrollo, que la acción indique responsable y fecha límite, que la fecha de realización no sea posterior a la fecha límite y que el estado de la acción proceda de su propio vocabulario.

## Qué responde

| Usted pregunta | Qué responde |
|---|---|
| Una fila trae la competencia pero deja el puesto en blanco. | `LG-001` solo señala una fila cuando `position` y `competency` están los dos vacíos; basta con que uno de los dos esté relleno. Comprueba que la fila indique el puesto y la competencia, no si la exigencia de competencia de ese puesto es razonable o completa. |
| Nuestros niveles están escritos con palabras («熟练», «掌握») o con letras (A/B/C), ¿qué ocurre? | `LG-002` lee `actualLevel` y exige que se analice como número, así que un nivel escrito con palabras o letras se informa como no analizable. El plugin no incluye ninguna escala de competencia: convierta el registro a una escala numérica o desactive `LG-002` junto con `LG-003`. Lo único que comprueba es que se pueda analizar; no juzga si la evaluación fue objetiva o exacta. |
| La columna de brecha dice `3`, pero `4` menos `2` es `2`, ¿se detecta? | Sí. `LG-003` recalcula `requiredLevel − actualLevel` con tolerancia `0` y señala la fila cuyo `gapLevel` registrado no coincide. Solo se ejecuta cuando las tres columnas tienen números analizables; si falta una, la regla pasa a `skipped`. Un valor negativo se informa tal cual, porque puede que las columnas estén invertidas, y la regla no decide a partir de qué magnitud la brecha es un problema. |
| Una fila registra una acción de desarrollo, pero sin responsable ni fecha límite. | `LG-005` exige `owner` y `dueAt` en toda fila con `action` rellena, y señala la fila a la que le falta uno de los dos. Comprueba que ambos campos estén registrados; no juzga si la acción es eficaz ni si el plazo es razonable. |
| La fecha de realización de una fila es posterior a su fecha límite, o las dos columnas están invertidas. | `LG-006` compara `dueAt` con `completedAt` en cada fila y señala la fila cuando la fecha límite es anterior a la fecha de realización. El paquete de reglas declara su límite con sus propias palabras: solo compara el orden de las dos fechas y no decide si el trabajo se completó realmente en plazo. Una fecha que no puede analizar se informa aparte en lugar de pasarse por alto. |
| `LG-004` y `LG-007` no informan nunca de nada, ¿significa que mi registro las ha superado? | No: ambas reglas se declaran en `skipped`. `LG-004` viene con `threshold: 0`, es decir sin configurar: fije a partir de qué brecha la acción de desarrollo es obligatoria. `LG-007` viene con el vocabulario de estados vacío: rellénelo con la terminología de su institución. Una vez configuradas, `LG-004` solo comprueba que la columna de acción esté rellena y `LG-007` solo que el valor de estado figure en su vocabulario; ninguna juzga si la acción se llevó realmente a cabo. |

## Normas que sigue

| Documento | Número | Reglas que lo citan |
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

| Superficie | Estado |
|---|---|
| Harness | Rango de peers `>=0.1.2-rc.1 <0.2.0 \|\| >=0.2.0-0 <0.3.0` — verificado para aceptar tanto `0.2.0-rc.2` como `0.2.1-alpha.1`. **No se declara `engines.dsh`**: no tiene lector y no puede rechazar ningún host |
| Node | `^22.19.0 || >=24.0.0` |
| Plataformas | Todas (ESM puro; sin código nativo, sin red, sin llamada al modelo) |
| Modo de herramienta | Funciona en `native`, `ptc` y `both`; para un directorio completo use `ptc` |

## What it does

La tabla de reglas, los campos y el comportamiento detallado están en [README.md](README.md#what-it-does) (versión principal en inglés). El plugin sólo enumera divergencias literales frente a las cláusulas citadas e indica en `skipped` cada comprobación que no pudo ejecutarse.

## Install

```sh
dsh plugin --profile <name> add dsh-learning-gap-check
dsh --profile <name> --dump-config | grep 'dsh-learning-gap-check'
```

## Configuration

Todos los parámetros ajustables viven en el esquema Schemastery de `src/config.ts`, por lo que se cambian desde `cordis.yml` sin tocar el código; los umbrales por regla están en el paquete de reglas bajo `rules/`.

| Clave | Tipo | Predeterminado | Descripción |
|---|---|---|---|
| `rulesFile` | string | `rules/learning-gap-check.yaml` | Ruta del paquete de reglas, relativa a la raíz del paquete |
| `disabledRules` | string[] | `[]` | Ids de reglas que se dejan de ejecutar; cada una aparece en `skipped` |
| `onlyRules` | string[] | `[]` | Ejecutar solo estas reglas; vacío ejecuta todas |
| `skipNotes` | string | `""` | Nota añadida a cada motivo de `skipped` |
| `timeoutMs` | number | `120000` | Presupuesto de tiempo de espera cooperativo de la herramienta |

## Material format

Acepta JSON o YAML. El ejemplo completo de campos está en [README.md](README.md#material-format) (versión principal en inglés). Los campos son opcionales en la capa de lectura y los valida el motor, de modo que una exportación parcial produce hallazgos sobre lo que falta en lugar de un fallo.

## Rule sources

Los datos de las reglas están separados del código: cada regla lleva documento, número, cláusula en la numeración propia de la fuente, extracto literal y URL de origen. El cargador impone que el extracto sea una cita real de al menos ocho caracteres y que una comprobación basada sólo en un principio general (`kind: derived-from-principle`, tope `warn`) o en una política local (`kind: institutional-configuration`, tope `info`) nunca se declare `error`.

Los límites verificados y las conclusiones deliberadamente **no** afirmadas están en [README.md](README.md#rule-sources) (versión principal en inglés) y en `rules/evidence/`.

## Troubleshooting

- **El plugin se instala pero la herramienta no aparece**: compruebe que `main` resuelve a `lib/index.mjs` y que `pnpm run build` lo generó.
- **`dsh plugin add` rechaza el paquete**: la faixa de peers cubre `0.1.x` y `0.2.x`; fuera de ella, conceda una exención explícita con `dsh plugin --profile <name> allow-version <pkg@ver> --dsh-version <runtime> --accept-risk`.
- **Una regla no se ejecutó**: lea el arreglo `skipped`.
- **`check` informa `manifest-peers` como fallo**: es un problema conocido de `dsh-plugin-dev`; el runtime aplica la compatibilidad al instalar.
- **Los horarios parecen desplazados**: toda la aritmética es de hora local sobre las cadenas entregadas.

## Development

```sh
pnpm install
pnpm run typecheck
pnpm test
pnpm run build
node ../scripts/sync-shared.mjs dsh-learning-gap-check
```

El último comando copia el kit compartido de `../_shared` a `src/shared/`; vuelva a ejecutarlo tras cada cambio compartido.

## License

[Apache License 2.0](LICENSE) © 2026 dsh-learning-gap-check contributors.

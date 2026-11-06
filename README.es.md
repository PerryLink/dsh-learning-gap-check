<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-learning-gap-check-hero-en-dark.webp">
  <img src="docs/assets/dsh-learning-gap-check-hero-en-light.webp" width="100%" alt="Banner de dsh-learning-gap-check: a la izquierda, el nombre del plugin, dos líneas de valor y el pie; a la derecha, la fila 1 de un registro de brechas de competencia — puesto y competencia vacíos (LG-001), nivel requerido 4 menos nivel actual 2 da una brecha de 2 (LG-003), y un eje numérico de ejemplo marca el tramo de dos niveles; abajo, los cinco campos de cierre — acción, responsable, plazo, fecha de realización y estado — con el vocabulario de estados y el umbral de brecha sin configurar, por lo que ambos se informan en skipped; la nota inferior indica que una lista de diferencias vacía no es una aprobación">
</picture>

# dsh-learning-gap-check

**Cierra en una sola llamada la aritmética y el bucle de un registro de brechas de competencia y plan de desarrollo: solo diferencias, sin dictámenes.**

Un verificador de DeepSeek Harness para equipos de formación y recursos humanos: lee un registro JSON/YAML (cabecera del empleado más una fila por competencia), comprueba la aritmética de niveles, las acciones de desarrollo, los responsables y los plazos contra un paquete de reglas sustituible, y devuelve en qué fila, en qué columna y cuál es la diferencia.

[Instalar](#instalación-en-tres-pasos) · [Configuración](#configuración) · [FAQ](#faq) · [简体中文](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md)

[![License](https://img.shields.io/badge/license-Apache--2.0-3366CC?style=flat-square&labelColor=2B3245)](LICENSE)
[![DSH](https://img.shields.io/badge/DSH-%E2%89%A50.2.1%20%3C0.3.0-4B67B4?style=flat-square&labelColor=2B3245)](#compatibilidad)
[![npm](https://img.shields.io/npm/v/dsh-learning-gap-check?style=flat-square&labelColor=2B3245&color=CB3837)](https://www.npmjs.com/package/dsh-learning-gap-check)
[![CI](https://img.shields.io/github/actions/workflow/status/PerryLink/dsh-learning-gap-check/ci.yml?branch=main&label=CI&style=flat-square&labelColor=2B3245)](https://github.com/PerryLink/dsh-learning-gap-check/actions/workflows/ci.yml)
[![Node](https://img.shields.io/badge/node-%5E22.19%20%7C%7C%20%3E%3D24-339933?style=flat-square&labelColor=2B3245)](#compatibilidad)

[![Stars](https://img.shields.io/github/stars/PerryLink/dsh-learning-gap-check?style=flat-square&labelColor=2B3245)](https://github.com/PerryLink/dsh-learning-gap-check/stargazers)
[![npm downloads](https://img.shields.io/npm/dm/dsh-learning-gap-check?style=flat-square&labelColor=2B3245&color=CB3837)](https://www.npmjs.com/package/dsh-learning-gap-check)
[![dshfind](https://dshfind.com/api/badge/PerryLink/dsh-learning-gap-check?metric=downloads)](https://dshfind.com/plugins/PerryLink/dsh-learning-gap-check?ref=badge)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/PerryLink/dsh-learning-gap-check/badge)](https://securityscorecards.dev/viewer/?uri=github.com/PerryLink/dsh-learning-gap-check)
[![DSH Market](https://img.shields.io/badge/DSH_Market-listed-4B67B4?style=flat-square&labelColor=2B3245)](https://dsh.market/)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-C71D23?style=flat-square&labelColor=2B3245&logo=gitee)](https://gitee.com/perrylink/dsh-learning-gap-check)

```sh
dsh plugin --profile <name> add dsh-learning-gap-check
```

</div>

<sub>Plugin de la comunidad, no afiliado a DeepSeek. Repositorio canónico: <https://github.com/PerryLink/dsh-learning-gap-check> (Gitee es un espejo).</sub>

## Qué es

`dsh-learning-gap-check` lee un registro de brechas de competencia y plan de desarrollo —la cabecera del empleado más una fila por competencia— y comprueba la aritmética y el cierre de ese propio registro: que cada brecha indique su puesto y su competencia, que los niveles registrados se analicen como números, que la brecha sea igual al nivel requerido menos el nivel actual, que una brecha superior a su umbral configurado lleve una acción de desarrollo, que la acción indique responsable y fecha límite, que la fecha de realización no sea posterior a la fecha límite y que el estado de la acción proceda de su propio vocabulario.

Expone al modelo una sola herramienta, `learning_gap_check`, y mantiene las siete reglas como datos en `rules/learning-gap-check.yaml`: sustituir el paquete de reglas sustituye el conjunto de reglas sin tocar TypeScript. Solo enumera diferencias literales entre el material y las cláusulas que citan las reglas; **no** decide si un empleado es competente, si una evaluación fue objetiva, si una acción funcionó, ni sustituye al revisor.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-learning-gap-check-flow-v5-dark.svg">
  <img src="docs/assets/dsh-learning-gap-check-flow-v5-light.svg" width="100%" alt="Estructura de dsh-learning-gap-check: el registro de la izquierda (JSON/YAML, cabecera y diez campos de muestra) entra en un bucle de dos carriles en el centro; seis puntos de control comprueban de forma independiente campos y niveles (LG-001/LG-002), la aritmética de la brecha (LG-003), el disparo del umbral (LG-004), la acción con responsable y plazo (LG-005), el orden de las fechas (LG-006) y el vocabulario de estados (LG-007); el centro indica brecha = requerido menos actual; a la derecha, los resultados forman los canales issues[] y skipped[] (un warn, dos skipped), pasan por buildView() y terminan en la revisión humana">
</picture>

## Instalación en tres pasos

1. **Instala** (elige un canal):

   ```sh
   # canal git (último main; equivalente a git+https://github.com/PerryLink/dsh-learning-gap-check.git)
   dsh plugin --profile <name> add github:PerryLink/dsh-learning-gap-check
   # canal npm (versiones publicadas)
   dsh plugin --profile <name> add dsh-learning-gap-check
   # canal tarball: pnpm pack en este repo y luego
   dsh plugin --profile <name> add ./dsh-learning-gap-check-<version>.tgz
   ```

   No hay código nativo: `lib/index.mjs` y `rules/` son los artefactos publicados.

2. **Configuración mínima** (los valores por defecto ya funcionan; desactiva reglas o añade una nota si hace falta):

   ```yaml
   - insert:
       - id: dsh-learning-gap-check
         name: dsh-learning-gap-check
         config:
           disabledRules: []
           onlyRules: []
           skipNotes: Política de formación y desarrollo 2026 de la institución
   ```

3. **Verifica que se monta**:

   ```sh
   dsh --profile <name> --dump-config | grep 'dsh-learning-gap-check'
   ```

   El repo incluye un recorrido de un solo comando: ejecuta `pnpm run build` y luego el ejemplo.

   ```sh
   node samples/quickstart/run.mjs
   ```

   ```text
   $ node samples/quickstart/run.mjs
   learning_gap_check: 1 issue(s) — error 0, warn 1, info 0
   skipped: 2
   ```

   El ejemplo está en `samples/quickstart/input/LG-001-unsafe.json`; el resultado esperado, en `samples/quickstart/expected/result.json`.

**Desinstalar**: `dsh plugin --profile <name> remove dsh-learning-gap-check` (o elimina la fila del patch del perfil).

<details>
<summary>Instalar desde el mercado de DSH Desktop o mediante WorkBuddy / Coze</summary>

Todos los plugins de PerryLink pueden explorarse en el mercado integrado de DSH Desktop: **Market → Sources → add source → pegar** `https://perrylink-dsh-catalog.perrylink.workers.dev/catalog-source.json` **→ seleccionarlo**. La instalación sigue pasando por la verificación de identidad npm del mercado y tu confirmación.

Esta comprobación también se ofrece como un elemento de la «Teaching and Review Suite»: busca ese nombre en WorkBuddy / Coze (esta comprobación es una parte; disponibilidad según el catálogo).

</details>

## Capacidades clave

`dsh-learning-gap-check` completa todo el registro en **una sola llamada** y devuelve la lista de hallazgos y la de comprobaciones no ejecutadas:

- **Un registro de solo lectura** — acepta JSON o YAML con cabecera del empleado y una fila por competencia; el archivo de material solo se lee, el original nunca se modifica y la herramienta no escribe ningún archivo.
- **Alias de columna resueltos** — puesto, competencia, nivel requerido, nivel actual, nivel de brecha, método de evaluación, fecha de evaluación, acción de desarrollo, responsable, plazo, fecha de realización, estado y evaluador tienen alias en chino e inglés; la coincidencia ignora mayúsculas, espacios, guiones bajos y guiones.
- **Siete reglas, basadas en datos** — el paquete de reglas es YAML y declara por regla el tipo de comprobación, los parámetros, la base y la gravedad; apunta `rulesFile` a otro archivo para cambiar de versión del conjunto de reglas.
- **Aritmética y cierre** — recálculo de la fórmula de brecha, disparo por umbral, responsable y plazo, orden de fechas y vocabulario de estados, cada uno con su fila y su campo.
- **Las omisiones nunca son silenciosas** — una columna ausente, un parámetro ausente, una regla desactivada o un vocabulario vacío van a `skipped` con su motivo; una lista de hallazgos vacía no es un aprobado.
- **Sin dictámenes** — el informe renderizado pasa por un guardián de redacción que prohíbe términos de juicio («conforme», «no conforme», «rechazado») y siempre añade un descargo de responsabilidad.

### Reglas

| Regla | Qué comprueba | Gravedad | Tipo de base |
|---|---|---|---|
| `LG-001` | el puesto y la competencia están registrados (al menos uno) | warn | derived-from-principle |
| `LG-002` | el nivel actual (`actualLevel`) se analiza como número | warn | derived-from-principle |
| `LG-003` | el nivel de brecha es igual a requerido menos actual (tolerancia `0`) | warn | derived-from-principle |
| `LG-004` | una brecha superior al umbral lleva una acción (sin configurar de fábrica) | info | institutional-configuration |
| `LG-005` | una acción indica responsable y plazo | warn | derived-from-principle |
| `LG-006` | el plazo no es anterior a la fecha de realización | warn | derived-from-principle |
| `LG-007` | el estado procede de su vocabulario (sin configurar de fábrica) | info | institutional-configuration |

`derived-from-principle` limita la gravedad a `warn` y `institutional-configuration` a `info`; el límite se aplica al cargar, no por documentación.

### Ejemplos

Abajo hay un hallazgo real extraído de `reportJson`, producido con el fixture de prueba `LG-001`:

**Herramienta** `learning_gap_check`

**Entrada**

~~~json
{"employee":"张工","department":"设备部","rows":[{"岗位":"","能力项":"","要求等级":"4","现有等级":"2","差距等级":"2"}]}
~~~

**Salida**

~~~json
{
  "id": "dsh-learning-gap-check.LG-001.de09b5a6",
  "ruleId": "LG-001",
  "severity": "warn",
  "locator": {
    "row": 1,
    "field": "position"
  },
  "found": "第 1 行 position、competency 都为空",
  "expected": "position、competency 至少应填写一项"
}
~~~

*Observed from `tests/fixtures/LG-001/LG-001-unsafe.json`*

| Usted pregunta | Qué responde |
|---|---|
| Una fila trae la competencia pero deja el puesto en blanco. | `LG-001` solo señala una fila cuando `position` y `competency` están los dos vacíos; basta con que uno de los dos esté relleno. Comprueba que la fila indique el puesto y la competencia, no si la exigencia de competencia de ese puesto es razonable o completa. |
| Nuestros niveles están escritos con palabras (`proficient`, `mastered`) o con letras (A/B/C), ¿qué ocurre? | `LG-002` lee `actualLevel` y exige que se analice como número, así que un nivel escrito con palabras o letras se informa como no analizable. El plugin no incluye ninguna escala de competencia: convierta el registro a una escala numérica o desactive `LG-002` junto con `LG-003`. Lo único que comprueba es que se pueda analizar; no juzga si la evaluación fue objetiva o exacta. |
| La columna de brecha dice `3`, pero `4` menos `2` es `2`, ¿se detecta? | `LG-003` recalcula `requiredLevel − actualLevel` con tolerancia `0` y señala la fila cuyo `gapLevel` registrado no coincide. Solo se ejecuta fila por fila cuando las tres columnas están rellenas; una columna ausente o un campo vacío en toda la tabla envía la regla a `skipped`, mientras que una celda rellena pero no numérica se informa como no analizable por derecho propio. Un valor negativo se informa tal cual, porque puede que las columnas estén invertidas, y la regla no decide a partir de qué magnitud la brecha es un problema. |
| Una fila registra una acción de desarrollo, pero sin responsable ni fecha límite. | `LG-005` exige `owner` y `dueAt` en toda fila con `action` rellena, y señala la fila a la que le falta uno de los dos. Comprueba que ambos campos estén registrados; no juzga si la acción es eficaz ni si el plazo es razonable. |
| La fecha de realización de una fila es posterior a su fecha límite, o las dos columnas están invertidas. | `LG-006` compara `dueAt` con `completedAt` en cada fila y señala la fila cuando la fecha límite es anterior a la fecha de realización. El paquete de reglas declara su límite con sus propias palabras: solo compara el orden de las dos fechas y no decide si el trabajo se completó realmente en plazo. Una fecha que no puede analizar se informa aparte en lugar de pasarse por alto. |
| `LG-004` y `LG-007` no informan nunca de nada, ¿significa que mi registro las ha superado? | No: ambas reglas se declaran en `skipped`. `LG-004` viene con `threshold: 0`, es decir sin configurar: fije a partir de qué brecha la acción de desarrollo es obligatoria. `LG-007` viene con el vocabulario de estados vacío: rellénelo con la terminología de su institución. Una vez configuradas, `LG-004` solo comprueba que la columna de acción esté rellena y `LG-007` solo que el valor de estado figure en su vocabulario; ninguna juzga si la acción se llevó realmente a cabo. |

### Formato del material

Se aceptan JSON y YAML. Aquí hay un registro completo:

```yaml
employee: 张工
department: 设备部
plan: Plan de competencias 2026
cycle: 2026 H1
rows:
  - { 序号: '1', 岗位: 设备工程师, 能力项: 设备故障诊断, 要求等级: '4',
      现有等级: '2', 差距等级: '2', 评估方法: 实操考核 + 主管评价,
      评估日期: 2026-03-01, 培养措施: 安排为期三个月的现场带教与故障复盘,
      责任人: 李主管, 完成期限: 2026-06-30, 完成日期: 2026-06-20,
      状态: 进行中, 评估人: 王经理 }
```

- La lista de filas puede llamarse `rows`, `items`, `gaps` o `差距`; la cabecera puede llevar `employee`, `department`, `plan`, `cycle` y `checkedAt`.
- Los campos son opcionales en el lector y los valida el motor, de modo que una exportación parcial produce hallazgos de «campo ausente» en lugar de un fallo.
- Los alias se convierten en nombres de campo canónicos tras la lectura, así que un hallazgo localiza la celda por `position`, `competency` o `gapLevel`; el número de fila sale de la columna de secuencia del registro cuando existe (si no, del índice).
- Convierta Excel a JSON/YAML primero; un chat puede hacerlo donde la plataforma lo permita. Una llamada comprueba un registro; la fusión de varias hojas queda fuera de alcance.

### Normas que sigue

| Documento | Número | Reglas que lo citan |
|---|---|---|
| Quality management — Guidelines for competence management and people development | GB/T 19025—2023 (publicada y vigente desde 2023-03-17; a cargo del Comité Nacional Técnico de Gestión de la Calidad y Aseguramiento de la Calidad; número de cláusula no obtenido en esta pasada) | LG-001, LG-002, LG-003, LG-005, LG-006 |
| Política institucional de formación y desarrollo (configuración de la institución) | Sin norma unificada (esta regla se apoya en el umbral de brecha configurado por la institución) | LG-004 |
| Política institucional de formación y desarrollo (configuración de la institución) | Sin norma unificada (esta regla se apoya en el vocabulario de estados configurado por la institución) | LG-007 |

El régimen vive en GB/T 19025—2023 e ISO 10015:2019 (mismo título, vigente desde 2019-12-17). En esta pasada no se encontró campo de «estado de adopción» en la página nacional de normas, así que el paquete **no afirma ninguna relación de adopción** entre ambas. La edición de 2001 trataba de un sistema de gestión de la formación y la de 2023 trata de la gestión de competencias y el desarrollo de personas: no son revisiones del mismo tema; compruebe la portada y el prólogo de la norma vigente antes de citarla.

### Origen de las reglas

Los datos de las reglas están separados del código: cada regla lleva `document` / `number` / `clause` / `excerpt` / `kind` / `source`, y `excerpt` debe ser una cita literal de al menos ocho caracteres. El cargador impone esa disciplina de citación y limita la gravedad según el tipo de base; un paquete que infle su base falla al cargar en lugar de producir un informe que parezca sólido.

La trazabilidad de las citas la ejecuta a máquina `scripts/check-citations.mjs`: busca cada extracto en el registro de verificación, y `rules/citations-baseline.json` registra los segmentos aún no trazables (hoy vacío); la línea base solo puede reducirse. Esta pasada no pudo obtener el texto literal de las cláusulas, así que el paquete lo dice en el propio campo `excerpt` y mantiene cada regla en `warn` o `info`.

## Configuración

Todos los parámetros ajustables son campos Schemastery de `src/config.ts`, modificables desde `cordis.yml` sin tocar código; los umbrales por regla están en el paquete de reglas bajo `rules/`.

| Clave | Tipo | Predeterminado | Descripción |
|---|---|---|---|
| `rulesFile` | string | `rules/learning-gap-check.yaml` | Ruta del paquete de reglas, relativa a la raíz del paquete; cambiar el archivo cambia la versión del conjunto de reglas |
| `disabledRules` | string[] | `[]` | Ids de reglas que se dejan de ejecutar; cada una aparece en `skipped` |
| `onlyRules` | string[] | `[]` | Ejecutar solo estas reglas; vacío ejecuta todas |
| `skipNotes` | string | `""` | Nota añadida a cada motivo de `skipped`, p. ej. el nombre de las normas de aplicación de su institución |
| `timeoutMs` | number | `120000` | Presupuesto de tiempo de espera cooperativo de la herramienta, en milisegundos |

Los parámetros por regla viven en el paquete; los cuatro que conviene conocer:

- `LG-003` `resultField` / `expression` / `tolerance` — la aritmética de la brecha, `requiredLevel − actualLevel` por defecto y sin tolerancia. Un resultado negativo se informa tal cual, porque puede que las columnas estén invertidas.
- `LG-004` `triggerField` / `threshold` / `requiredField` — su regla para cuándo una acción pasa a ser obligatoria. Un umbral de `0` significa que la regla no se ejecuta; `1` significa una brecha de un escalón o más. La comparación es «igual o superior», así que un valor exactamente en el umbral dispara.
- `LG-005` `conditionField` / `requiredFields` — qué dispara la exigencia de responsable y plazo.
- `LG-007` `values` — su vocabulario de estados, p. ej. `[no iniciado, en curso, completado, aceptado]`. Vacío significa que no se comprueba.

Ejemplo de sobrescritura en su patch de perfil:

```yaml
- insert:
    - id: dsh-learning-gap-check
      name: dsh-learning-gap-check
      config:
        onlyRules: [LG-001, LG-002, LG-003, LG-005, LG-006]
        skipNotes: Según nuestra política de formación y desarrollo de 2026
```

## FAQ

<details>
<summary>¿Se sube el material o se escribe en disco?</summary>

No. El plugin no hace peticiones de red, no llama a ningún modelo y no almacena credenciales; lee el archivo local indicado en `file` o el texto en línea de `material` y lo comprueba en el proceso, sin escribir ningún archivo. El informe nombra el origen del material (una ruta absoluta o «(material en línea)»), y algunas comprobaciones citan la celda infractora (un nivel no analizable, un valor de estado, una fecha), así que esa ruta y esos valores sí entran en el registro de sesión junto con el resultado; el registro completo nunca se copia al informe.

</details>

<details>
<summary>¿Por qué todo está en verde si no se comprobó nada?</summary>

Lea `skipped`. `LG-004` viene con `threshold: 0` y `LG-007` con la lista `values` vacía, así que ambas quedan apagadas por defecto; una columna ausente o una regla desactivada mediante `disabledRules` también acaban ahí. Una lista de hallazgos vacía significa «las comprobaciones que se ejecutaron no encontraron diferencias», no «las que no se ejecutaron pasaron».

</details>

<details>
<summary>Nuestros niveles son palabras como «proficiente»: ¿podemos usarlos tal cual?</summary>

No. `LG-002` y `LG-003` suponen niveles numéricos: las palabras o letras se informan como no analizables. Convierta el registro a una escala numérica comparable o desactive `LG-002` y `LG-003`. El plugin no incluye escala porque asignar un número a «proficiente» es una decisión de modelado que debe tomar el usuario.

</details>

<details>
<summary>¿Compite con otros plugins por nombres de herramienta, servicios o rutas?</summary>

No. Registra una sola herramienta con espacio de nombres, `learning_gap_check`, no provee ninguna clave de servicio, no registra slots de cliente ni prefijos `webServer`, y no muta globales; el patch del bundle solo hace `insert` de su propia fila. El argumento punto por punto está en «Interoperabilidad con otros plugins DSH».

</details>

<details>
<summary>¿Cuánto coste de rendimiento supone?</summary>

Una llamada lee el material en memoria y cada regla hace comprobaciones de tiempo constante por fila, sin red ni llamadas al modelo; el número de reglas es fijo (siete), así que el coste crece linealmente con las filas. `timeoutMs` es un presupuesto cooperativo: la herramienta comprueba la señal de aborto antes y después de leer/analizar, y el host interrumpe al agotarse.

</details>

## Límites de seguridad

- **Material de solo lectura.** La herramienta lee el archivo de `file` (UTF-8) o usa el `material` en línea; no escribe archivos ni modifica originales. La declaración de demostración en `package.json` indica `writes: []` y `network: false`, y la única capacidad es `tools:register`.
- **Sin red, sin llamadas al modelo, sin credenciales.** La comprobación es cálculo puro en proceso; no hay ninguna vía que envíe el material fuera de la máquina.
- **Sin dictámenes.** El informe renderizado pasa por el guardián de redacción de `src/shared/wording.ts`, que prohíbe términos de juicio («conforme», «no conforme», «rechazado», «superó la aceptación»), y siempre se añade un descargo; un hallazgo describe la fila, la columna y lo que se esperaba.
- **Las citas no se inventan.** Un extracto debe ser una cita literal de al menos ocho caracteres; cuando la base es solo un principio (`derived-from-principle`) o configuración institucional (`institutional-configuration`), la gravedad se limita a `warn` e `info` respectivamente. Cuando no se obtuvo el texto, el campo `excerpt` lo dice.
- **Las omisiones nunca son silenciosas.** Toda comprobación que no pueda ejecutarse va a `skipped` con un motivo; una lista de hallazgos vacía nunca se presenta como «sin problemas».
- **Falla al cargar.** El paquete de reglas se valida al cargar: tipos de comprobación desconocidos, parámetros incompletos y expresiones regulares inválidas fallan en voz alta en lugar de ejecutarse con reglas rotas.
- **El registro es un efecto.** `ctx.tools.register` devuelve un disposer, así que la herramienta se retira cuando el plugin se descarga o se recarga en caliente.
- **Tiempo de espera cooperativo.** La señal de aborto se comprueba en los límites de lectura y análisis; un tiempo agotado no deja trabajo en segundo plano.

## Limitaciones conocidas

**Límite:** este plugin comprueba un **registro de brechas de competencia y plan de desarrollo** en su aritmética y su cierre — que cada brecha nombre su puesto y su competencia, que las dos columnas de nivel se analicen como números, que la brecha sea requerido menos actual, que una brecha superior a su umbral lleve una acción de desarrollo, que la acción nombre responsable y plazo, que la fecha de realización no sea posterior al plazo y que el estado de la acción proceda de su vocabulario. **No** decide si un empleado es competente, si una evaluación fue objetiva, si una acción de desarrollo funcionó, ni si alguien debería ser reasignado o despedido.

> ### ⚠️ Lo que este plugin deja fuera deliberadamente
>
> **No incluye ninguna escala de competencia y supone que los niveles son números.** `LG-002` y `LG-003` leen columnas numéricas y comprueban la aritmética entre ellas. Un registro con calificaciones por letras (`A`/`B`/`C`) o palabras (`proficient`/`mastered`) se **informa como no analizable**, porque comparar esos niveles es una decisión de modelado que el plugin no tomará por usted. Convierta la escala o desactive esas reglas.
>
> **No incluye un umbral para «bastante grande como para exigir acción».** Cuánta brecha obliga a una acción de desarrollo es una decisión de gestión del talento de la institución —algunas unidades la exigen para cualquier déficit, otras toleran un escalón—, así que el umbral de `LG-004` empieza en `0` y la regla se declara en `skipped` hasta que lo fije.
>
> **El vocabulario de estados también viene vacío** por la misma razón. Y la regla de fechas solo comprueba que el plazo no sea anterior a la fecha de realización, una propiedad de captura de datos: **no juzga si el trabajo se hizo tarde.**
>
> **Cada `excerpt` del paquete dice, con todas las letras, que el texto de la cláusula no se obtuvo.** El régimen vive en GB/T 19025 y en las normas de cualificación y formación de cada institución. La pasada de verificación no pudo recuperar el texto literal, así que el paquete declara la laguna en el propio campo `excerpt` y mantiene cada regla en `warn` o `info`. **Cuando tenga los textos, sustituya cada `excerpt` por la cláusula real y suba `kind` a `direct`.**

Otras limitaciones:

- **Las fechas solo se comparan por orden.** `LG-006` compara las partes de fecha de `dueAt` y `completedAt`, no convierte zonas horarias ni juzga retrasos; una fecha de realización anterior al plazo también se informa, porque suele significar que las columnas están invertidas. Los formatos admitidos son `2026-03-15` y `2026-03-15 09:30`.
- **La coincidencia de alias es literal.** Solo normaliza mayúsculas, espacios, guiones bajos y guiones; no infiere sinónimos ni hace coincidencia difusa. Un nombre de columna nuevo fuera de la tabla de alias de `src/model.ts` se trata como columna ausente hasta que lo añada.
- **Un registro por llamada.** La herramienta toma un solo archivo o un texto en línea; la consolidación de varias hojas, departamentos o ciclos debe dividirse o fusionarse antes.
- **Los números se extraen.** Las comprobaciones numéricas extraen un número del texto (toleran dígitos de ancho completo, separadores de miles y espacios); `nivel 3` se analiza como `3`, mientras que `nivel tres` no.
- **Tiempo de espera cooperativo.** `timeoutMs` depende de la señal de aborto del host; un registro muy grande debe dividirlo quien llama.
- **`check` puede informar `manifest-peers` como fallo.** El comprobador estático compara con un rango de peers codificado que precede a la línea 0.2; el runtime aplica la compatibilidad al instalar, así que el rango declarado es el correcto. Es un problema conocido de `dsh-plugin-dev`.
- **La herramienta no aparece tras instalar.** Compruebe que `main` resuelve a `lib/index.mjs` y que `pnpm run build` lo generó; un `main` incorrecto hace que el cargador omita la entrada en silencio.

## Interoperabilidad con otros plugins DSH

Este plugin ocupa un nombre de herramienta y no toca ningún evento compartido:

- **Un solo nombre de herramienta.** Solo registra `learning_gap_check`, con espacio de nombres; no toma ningún nombre desnudo de una herramienta incluida o de otro plugin.
- **Sin clave de servicio.** No provee ninguna clave de servicio, así que no puede colisionar en una.
- **Sin slot.** No registra ninguna clave de slot de cliente, así que no disputa un asiento `shadows-shipped-ui`.
- **Sin ruta HTTP.** No registra ningún prefijo `webServer`.
- **Sin listener de eventos.** Nunca llama a `ctx.on()`, así que no interactúa con la cadena `agent/pre-step` ni `tools/*` de ningún plugin y no puede cortocircuitar a otro listener.
- **Sin colisión en la capa de patch.** El patch del bundle solo hace `insert` de su propia fila; nunca sobrescribe el `config` de una fila incluida.
- **Sin mutación global.** No parchea prototipos, no reescribe `process.env` ni reemplaza el dispatcher global de fetch.
- **Dependencia explícita.** `inject: ['tools']`: sin el servicio tools el plugin no se carga (fail closed) en lugar de arrancar a medias y perder su función en silencio.

Evidencia estática: `src/index.ts:76-140` solo llama a `ctx.tools.register` y devuelve el disposer como efecto; `cordis.patch.yml:6-8` contiene un único `insert`; `package.json#dsh.capabilities` contiene solo `tools:register`.

## Compatibilidad

| Superficie | Estado |
|---|---|
| Harness | Rango de peers `>=0.1.2-rc.1 <0.2.0 \|\| >=0.2.0-0 <0.3.0` — verificado para aceptar tanto `0.2.0-rc.2` como `0.2.1-rc.2`. `engines.dsh` se declara como `>=0.2.1-0 <0.3.0` y el host lo aplica desde 0.2.1 |
| Node | `^22.19.0 \|\| >=24.0.0` |
| Plataformas | Todas (ESM puro; sin código nativo, sin red, sin llamada al modelo) |
| Modo de herramienta | Funciona en `native` y `ptc`; para llamadas repetidas en una sesión, `ptc` paga el coste del esquema una sola vez |

## Ecosistema y calidad

- [Espejo de Gitee](https://gitee.com/perrylink/dsh-learning-gap-check) (espejo sincronizado; GitHub es el canónico)
- [Página del plugin en dshfind](https://dshfind.com/plugins/PerryLink/dsh-learning-gap-check) (instalaciones y ranking)
- [Informe de OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/PerryLink/dsh-learning-gap-check) (impulsado por [.github/workflows/scorecard.yml](.github/workflows/scorecard.yml))
- [DSH Market](https://dsh.market/) (listado)
- [Elegir un verificador por material](https://perrylink.github.io/zh/checkers/choose/): este repositorio es uno de la familia de verificadores PerryLink
- [Base de conocimiento del ecosistema](https://perrylink.github.io/dsh-plugin-guide/): guía de desarrollo de plugins · datos de selección medidos · criterios de mantenimiento

## Desarrollo

```sh
pnpm install
pnpm run typecheck            # tsc --noEmit
pnpm test                     # vitest: suite compartida de plugins de tabla + fixtures emparejados por regla
pnpm run build                # tsdown -> lib/index.mjs + lib/index.d.mts
pnpm run verify:self-contained
pnpm run check:lockfile
pnpm run check:readmes        # consistencia de los README en cinco idiomas
pnpm run check:citations      # trazabilidad de extractos
pnpm pack
node ../scripts/sync-shared.mjs dsh-learning-gap-check   # refrescar src/shared
```

Estructura de directorios:

```text
src/index.ts        registro de la herramienta, resolución del paquete de reglas, lectura del material
src/config.ts       esquema de configuración Schemastery
src/model.ts        columnas del registro, alias y campos requeridos
src/check.ts        núcleo de comprobación puro (sin I/O, sin reloj, sin modelo)
src/parse.ts        lector JSON/YAML
src/view.ts         proyección del resultado para el modelo
src/shared/         motor de tablas compartido (copiado dentro, no dependencia externa)
rules/              el paquete de reglas (7 reglas) y la línea base de citas
tests/              vitest: suite compartida + fixtures emparejados por regla
samples/quickstart/ recorrido de un solo comando
scripts/            puertas de validación y generador de imágenes del README
```

El plugin es **basado en datos**: `src/model.ts` declara la forma de la tabla, el kit compartido aporta el lector y el motor, y el paquete de reglas declara cada comprobación. Las imágenes del README se generan con [`scripts/gen-readme-assets.py`](scripts/gen-readme-assets.py) (esqueleto Pillow, SVG escrito a mano) y se pueden reejecutar sin riesgo; sin UI ni datos de benchmark este repo solo produce el par de flujo claro/oscuro.

Topics: `deepseek-harness`, `dsh`, `dsh-plugin`, `cordis`, `learning`, `gap`

## Familia y agradecimientos

Este proyecto forma parte de la familia de plugins de DeepSeek Harness de [PerryLink](https://github.com/PerryLink) (todos Apache-2.0). Si te resulta útil, **una estrella ayuda a que la siguiente persona lo encuentre** — no hay nada bloqueado tras ella.

- [@PerryLink](https://github.com/PerryLink) — creador y mantenedor: el motor de comprobación de tablas, el paquete de reglas `LG-*` y la documentación en cinco idiomas.

<details>
<summary>Expandir todos los plugins</summary>

| Plugin | Estado |
|---|---|
| **[dsh-aqua-input-check](https://github.com/PerryLink/dsh-aqua-input-check)** |  |
| **[dsh-archive-check](https://github.com/PerryLink/dsh-archive-check)** |  |
| **[dsh-auto-review](https://github.com/PerryLink/dsh-auto-review)** |  |
| **[dsh-autotier](https://github.com/PerryLink/dsh-autotier)** | 🧊 CONGELADO — ver el README del repo |
| **[dsh-bid-ca-precheck](https://github.com/PerryLink/dsh-bid-ca-precheck)** |  |
| **[dsh-bid-qual-check](https://github.com/PerryLink/dsh-bid-qual-check)** |  |
| **[dsh-cert-mcp](https://github.com/PerryLink/dsh-cert-mcp)** | 🧊 CONGELADO — ver el README del repo |
| **[dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind)** |  |
| **[dsh-click](https://github.com/PerryLink/dsh-click)** |  |
| **[dsh-composer-history](https://github.com/PerryLink/dsh-composer-history)** |  |
| **[dsh-contract-stance](https://github.com/PerryLink/dsh-contract-stance)** |  |
| **[dsh-customs-doc-check](https://github.com/PerryLink/dsh-customs-doc-check)** |  |
| **[dsh-data-quality](https://github.com/PerryLink/dsh-data-quality)** |  |
| **[dsh-demurrage-ledger](https://github.com/PerryLink/dsh-demurrage-ledger)** |  |
| **[dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck)** |  |
| **[dsh-drill-script-check](https://github.com/PerryLink/dsh-drill-script-check)** |  |
| **[dsh-eia-guide-check](https://github.com/PerryLink/dsh-eia-guide-check)** |  |
| **[dsh-emergency-plan](https://github.com/PerryLink/dsh-emergency-plan)** |  |
| **[dsh-essay-rubric-check](https://github.com/PerryLink/dsh-essay-rubric-check)** |  |
| **[dsh-evidence-check](https://github.com/PerryLink/dsh-evidence-check)** |  |
| **[dsh-export-ctl-check](https://github.com/PerryLink/dsh-export-ctl-check)** |  |
| **[dsh-fast](https://github.com/PerryLink/dsh-fast)** |  |
| **[dsh-fmea-table-check](https://github.com/PerryLink/dsh-fmea-table-check)** |  |
| **[dsh-forecast-penalty](https://github.com/PerryLink/dsh-forecast-penalty)** |  |
| **[dsh-fund-research](https://github.com/PerryLink/dsh-fund-research)** |  |
| **[dsh-github](https://github.com/PerryLink/dsh-github)** |  |
| **[dsh-gongwen-flow-check](https://github.com/PerryLink/dsh-gongwen-flow-check)** |  |
| **[dsh-gongwen-word-check](https://github.com/PerryLink/dsh-gongwen-word-check)** |  |
| **[dsh-guard-plan-qc](https://github.com/PerryLink/dsh-guard-plan-qc)** |  |
| **[dsh-hazchem-check](https://github.com/PerryLink/dsh-hazchem-check)** |  |
| **[dsh-hazplan-check](https://github.com/PerryLink/dsh-hazplan-check)** |  |
| **[dsh-hidden-risk-map](https://github.com/PerryLink/dsh-hidden-risk-map)** |  |
| **[dsh-hs-classify](https://github.com/PerryLink/dsh-hs-classify)** |  |
| **[dsh-icd-rule-check](https://github.com/PerryLink/dsh-icd-rule-check)** |  |
| **[dsh-industry-research](https://github.com/PerryLink/dsh-industry-research)** |  |
| **[dsh-lawcite-adapter](https://github.com/PerryLink/dsh-lawcite-adapter)** |  |
| **[dsh-laya](https://github.com/PerryLink/dsh-laya)** |  |
| **[dsh-lc-doc-check](https://github.com/PerryLink/dsh-lc-doc-check)** |  |
| **[dsh-learning-gap-check](https://github.com/PerryLink/dsh-learning-gap-check)** |  |
| **[dsh-library](https://github.com/PerryLink/dsh-library)** |  |
| **[dsh-local-ai](https://github.com/PerryLink/dsh-local-ai)** |  |
| **[dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions)** |  |
| **[dsh-mask](https://github.com/PerryLink/dsh-mask)** |  |
| **[dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel)** |  |
| **[dsh-medrec-qc](https://github.com/PerryLink/dsh-medrec-qc)** |  |
| **[dsh-memento](https://github.com/PerryLink/dsh-memento)** |  |
| **[dsh-nsfc-form-check](https://github.com/PerryLink/dsh-nsfc-form-check)** |  |
| **[dsh-nurse-record-check](https://github.com/PerryLink/dsh-nurse-record-check)** |  |
| **[dsh-observe](https://github.com/PerryLink/dsh-observe)** |  |
| **[dsh-origin-rvc-check](https://github.com/PerryLink/dsh-origin-rvc-check)** |  |
| **[dsh-ota-review-check](https://github.com/PerryLink/dsh-ota-review-check)** |  |
| **[dsh-output-styles](https://github.com/PerryLink/dsh-output-styles)** |  |
| **[dsh-paper-doc-adapter](https://github.com/PerryLink/dsh-paper-doc-adapter)** |  |
| **[dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules)** |  |
| **[dsh-permit-report-check](https://github.com/PerryLink/dsh-permit-report-check)** |  |
| **[dsh-pipeline-check](https://github.com/PerryLink/dsh-pipeline-check)** |  |
| **[dsh-pleading-draft](https://github.com/PerryLink/dsh-pleading-draft)** |  |
| **[dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor)** | 🚫 RETIRADO (repo archivado) |
| **[dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide)** |  |
| **[dsh-plugin-kit](https://github.com/PerryLink/dsh-plugin-kit)** | 🚫 RETIRADO (repo archivado) |
| **[dsh-plugin-upgrade](https://github.com/PerryLink/dsh-plugin-upgrade)** | 🚫 RETIRADO (repo archivado) |
| **[dsh-policy-brief-draft](https://github.com/PerryLink/dsh-policy-brief-draft)** |  |
| **[dsh-power-loss-split](https://github.com/PerryLink/dsh-power-loss-split)** |  |
| **[dsh-power-ticket-check](https://github.com/PerryLink/dsh-power-ticket-check)** |  |
| **[dsh-ppap-check](https://github.com/PerryLink/dsh-ppap-check)** |  |
| **[dsh-protest-deadline](https://github.com/PerryLink/dsh-protest-deadline)** |  |
| **[dsh-railway-window](https://github.com/PerryLink/dsh-railway-window)** |  |
| **[dsh-repair-order-qc](https://github.com/PerryLink/dsh-repair-order-qc)** |  |
| **[dsh-research-report](https://github.com/PerryLink/dsh-research-report)** |  |
| **[dsh-review-reply-check](https://github.com/PerryLink/dsh-review-reply-check)** |  |
| **[dsh-rulefile-check](https://github.com/PerryLink/dsh-rulefile-check)** |  |
| **[dsh-safety-brief-check](https://github.com/PerryLink/dsh-safety-brief-check)** |  |
| **[dsh-score](https://github.com/PerryLink/dsh-score)** |  |
| **[dsh-session-sync](https://github.com/PerryLink/dsh-session-sync)** |  |
| **[dsh-site-log-check](https://github.com/PerryLink/dsh-site-log-check)** |  |
| **[dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security)** |  |
| **[dsh-soe-decision-check](https://github.com/PerryLink/dsh-soe-decision-check)** |  |
| **[dsh-soilwater-check](https://github.com/PerryLink/dsh-soilwater-check)** |  |
| **[dsh-sop-sync-check](https://github.com/PerryLink/dsh-sop-sync-check)** |  |
| **[dsh-spc-gbt-adapter](https://github.com/PerryLink/dsh-spc-gbt-adapter)** |  |
| **[dsh-talk](https://github.com/PerryLink/dsh-talk)** |  |
| **[dsh-tender-extract](https://github.com/PerryLink/dsh-tender-extract)** |  |
| **[dsh-tender-matrix](https://github.com/PerryLink/dsh-tender-matrix)** |  |
| **[dsh-test-drive](https://github.com/PerryLink/dsh-test-drive)** |  |
| **[dsh-ticktick](https://github.com/PerryLink/dsh-ticktick)** | 🚫 RETIRADO (repo archivado) |
| **[dsh-translate](https://github.com/PerryLink/dsh-translate)** |  |
| **[dsh-warranty-calc](https://github.com/PerryLink/dsh-warranty-calc)** |  |
| **[dsh-budget](https://github.com/PerryLink/dsh-budget)** | 🧊 CONGELADO — ver el README del repo |
| **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** | 🧊 CONGELADO — ver el README del repo |
| **[dsh-defend](https://github.com/PerryLink/dsh-defend)** | 🧊 CONGELADO — ver el README del repo |
| **[dsh-draw](https://github.com/PerryLink/dsh-draw)** | 🧊 CONGELADO — ver el README del repo |
| **[dsh-reach](https://github.com/PerryLink/dsh-reach)** | 🧊 CONGELADO — ver el README del repo |
| **[dsh-background-agents](https://github.com/PerryLink/dsh-background-agents)** | 🚫 RETIRADO (repo archivado) |
| **[dsh-session-pin](https://github.com/PerryLink/dsh-session-pin)** | 🚫 RETIRADO (repo archivado) |
| **[dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms)** | 🚫 RETIRADO (repo archivado) |

</details>

## Licencia

[LICENSE](LICENSE) (Apache License 2.0) © 2026 dsh-learning-gap-check contributors

<p align="center"><sub>Apache-2.0 · Plugin de la comunidad, no afiliado a DeepSeek.</sub></p>

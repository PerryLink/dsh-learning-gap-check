# dsh-learning-gap-check — क्षमता अंतराल और विकास योजना रजिस्टर की जाँच

[![DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)

`dsh-learning-gap-check` एक क्षमता-अंतराल और विकास-योजना रजिस्टर पढ़ता है — कर्मचारी हेडर और प्रत्येक क्षमता की एक पंक्ति — और उसी रजिस्टर की अपनी गणना तथा शृंखला-पूर्णता की जाँच करता है: क्या प्रत्येक अंतराल में पद और क्षमता लिखी है, क्या दर्ज स्तर संख्याओं के रूप में पढ़े जा सकते हैं, क्या अंतराल आवश्यक स्तर में से वर्तमान स्तर घटाने के बराबर है, क्या आपके तय सीमांक से अधिक अंतराल पर विकास उपाय दर्ज है, क्या उपाय में ज़िम्मेदार व्यक्ति और पूर्णता तिथि दर्ज है, क्या पूर्णता तिथि समय-सीमा से बाद की नहीं है, और क्या उपाय की स्थिति आपकी ही शब्दावली से ली गई है।

## आउटपुट कैसा दिखता है

![Terminal demo of dsh-learning-gap-check: real output over its LG-002 fixture](https://raw.githubusercontent.com/PerryLink/dsh-learning-gap-check/main/docs/assets/dsh-learning-gap-check-demo.png)

इस प्लगइन का अपने ही `LG-002` टेस्ट फ़िक्स्चर पर वास्तविक आउटपुट — कोई नकली चित्र नहीं। नियम-पैक उद्धरण नहीं गढ़ता, इसलिए हर निष्कर्ष लागू किए गए खंड का नाम और यह भी बताता है कि उसका मूल पाठ इस बार प्राप्त नहीं हुआ।

## यह किन सवालों का जवाब देता है

| आपका सवाल | इसका जवाब |
|---|---|
| किसी पंक्ति में क्षमता दर्ज है, पर पद का कॉलम खाली है। | `LG-001` उस पंक्ति को तभी दर्ज करता है जब `position` और `competency` दोनों खाली हों; दोनों में से एक भरा होना ही पर्याप्त है। यह देखता है कि पंक्ति में पद और क्षमता लिखे हैं या नहीं, यह नहीं कि उस पद की क्षमता-अपेक्षा उचित या पूर्ण है। |
| हमारे रजिस्टर में स्तर शब्दों में («熟练», «掌握») या अक्षरों में (A/B/C) लिखे हैं — तब क्या होगा? | `LG-002` `actualLevel` पढ़ता है और अपेक्षा करता है कि वह संख्या के रूप में पढ़ा जा सके, इसलिए शब्दों या अक्षरों में लिखा स्तर «न पढ़ा जा सकने वाला» दर्ज होता है। प्लगइन कोई क्षमता-स्तर मापक साथ नहीं लाता: रजिस्टर को संख्यात्मक मापक में बदलें, या `LG-002` के साथ `LG-003` भी बंद कर दें। यह केवल पढ़े जा सकने की जाँच करता है; मूल्यांकन वस्तुनिष्ठ या सटीक था या नहीं, यह नहीं आँकता। |
| अंतराल कॉलम में `3` लिखा है, पर आवश्यक `4` में से वर्तमान `2` घटाने पर `2` बनता है — क्या यह पकड़ में आता है? | हाँ। `LG-003` `requiredLevel − actualLevel` को सहनशीलता `0` के साथ दोबारा जोड़ता है और जिस पंक्ति का दर्ज `gapLevel` मेल नहीं खाता उसे दर्ज करता है। यह तभी चलता है जब तीनों कॉलमों में पढ़ी जा सकने वाली संख्याएँ हों; एक भी छूटे तो यह `skipped` में चला जाता है। ऋणात्मक मान जैसा है वैसा दर्ज होता है, क्योंकि कॉलम उलटे भरे हो सकते हैं; और अंतराल कितना बड़ा हो तो समस्या मानी जाए, यह नियम तय नहीं करता। |
| किसी पंक्ति में विकास उपाय दर्ज है, पर ज़िम्मेदार व्यक्ति और पूर्णता तिथि दोनों नहीं। | `LG-005` हर उस पंक्ति में `owner` और `dueAt` की अपेक्षा करता है जिसमें `action` भरा है, और जिसमें इनमें से एक भी न हो उसे दर्ज करता है। यह देखता है कि दोनों कॉलम दर्ज हैं या नहीं; उपाय कारगर है या समय-सीमा उचित है, यह नहीं आँकता। |
| किसी पंक्ति की पूर्णता तिथि उसकी समय-सीमा के बाद की है, या दोनों कॉलम उलटे भर गए हैं। | `LG-006` हर पंक्ति में `dueAt` की तुलना `completedAt` से करता है और तब उस पंक्ति को दर्ज करता है जब समय-सीमा पूर्णता तिथि से पहले की हो। नियम-पैक अपनी सीमा अपने शब्दों में लिखता है: यह केवल दोनों तिथियों का क्रम देखता है, यह नहीं तय करता कि काम वास्तव में समय पर पूरा हुआ। जो तिथि पढ़ी न जा सके वह अलग से दर्ज होती है, चुपचाप छोड़ी नहीं जाती। |
| `LG-004` और `LG-007` कभी कुछ दर्ज ही नहीं करते — क्या इसका अर्थ है कि मेरा रजिस्टर इनमें पास हो गया? | नहीं: दोनों नियम स्वयं को `skipped` में दर्ज करते हैं। `LG-004` में `threshold: 0` है, यानी अनकॉन्फ़िगर — तय करें कि कितने अंतराल पर विकास उपाय अनिवार्य होगा। `LG-007` की स्थिति-शब्दावली ख़ाली है — उसमें अपनी संस्था की शब्दावली भरें। कॉन्फ़िगर होने के बाद `LG-004` केवल यह देखता है कि उपाय का कॉलम भरा है और `LG-007` केवल यह कि स्थिति का मान आपकी सूची में है; कोई भी यह नहीं आँकता कि उपाय वास्तव में लागू हुआ या नहीं। |

## यह किन मानकों पर आधारित है

| दस्तावेज़ | संख्यांक | इन्हें उद्धृत करने वाले नियम |
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

| सतह | स्थिति |
|---|---|
| Harness | peer रेंज `>=0.1.2-rc.1 <0.2.0 \|\| >=0.2.0-0 <0.3.0` — `0.2.0-rc.2` और `0.2.1-alpha.1` दोनों को स्वीकार करने के लिए सत्यापित। **`engines.dsh` जानबूझकर घोषित नहीं**: इसका कोई पाठक नहीं और यह किसी होस्ट को अस्वीकार नहीं कर सकता |
| Node | `^22.19.0 || >=24.0.0` |
| प्लेटफ़ॉर्म | सभी (शुद्ध ESM; कोई नेटिव कोड नहीं, कोई नेटवर्क नहीं, कोई मॉडल कॉल नहीं) |
| टूल मोड | `native`, `ptc` और `both` में काम करता है; पूरे फ़ोल्डर के लिए `ptc` चुनें |

## What it does

नियम-सूची, फ़ील्ड और विस्तृत व्यवहार [README.md](README.md#what-it-does) (अंग्रेज़ी मुख्य संस्करण) में हैं। यह प्लगइन केवल उद्धृत धाराओं के सामने शाब्दिक अंतर सूचीबद्ध करता है और हर न चल पाई जाँच को `skipped` में बताता है।

## Install

```sh
dsh plugin --profile <name> add dsh-learning-gap-check
dsh --profile <name> --dump-config | grep 'dsh-learning-gap-check'
```

## Configuration

सभी समायोज्य पैरामीटर `src/config.ts` की Schemastery स्कीमा में हैं, इसलिए कोड बदले बिना `cordis.yml` से बदले जा सकते हैं; प्रति-नियम सीमाएँ `rules/` के नियम-पैक में हैं।

| कुंजी | प्रकार | डिफ़ॉल्ट | विवरण |
|---|---|---|---|
| `rulesFile` | string | `rules/learning-gap-check.yaml` | नियम-पैक का पथ, पैकेज रूट के सापेक्ष |
| `disabledRules` | string[] | `[]` | बंद करने वाले नियम id; प्रत्येक `skipped` में दिखता है |
| `onlyRules` | string[] | `[]` | केवल ये नियम चलाएँ; खाली होने पर सभी नियम चलते हैं |
| `skipNotes` | string | `""` | हर `skipped` कारण के आगे जोड़ी जाने वाली टिप्पणी |
| `timeoutMs` | number | `120000` | उपकरण का सहकारी समय-सीमा बजट |

## Material format

JSON या YAML स्वीकार्य है। पूरा फ़ील्ड उदाहरण [README.md](README.md#material-format) (अंग्रेज़ी मुख्य संस्करण) में है। पढ़ने की परत में फ़ील्ड वैकल्पिक हैं और जाँच इंजन उन्हें सत्यापित करता है, इसलिए आंशिक निर्यात पर क्रैश के बजाय "अनुपस्थित" श्रेणी के निष्कर्ष मिलते हैं।

## Rule sources

नियम-डेटा कोड से अलग है: प्रत्येक नियम में दस्तावेज़, संख्या, स्रोत की अपनी क्रमांकन-प्रणाली के अनुसार धारा, शब्दशः उद्धरण और स्रोत URL होता है। लोडर लागू करता है कि उद्धरण कम से कम आठ अक्षरों का वास्तविक उद्धरण हो, और जिस जाँच का आधार केवल सामान्य सिद्धांत (`kind: derived-from-principle`, अधिकतम `warn`) या स्थानीय नीति (`kind: institutional-configuration`, अधिकतम `info`) हो, उसे कभी `error` घोषित न किया जाए।

सत्यापित सीमाएँ और जान-बूझकर **न** कहे गए निष्कर्ष [README.md](README.md#rule-sources) (अंग्रेज़ी मुख्य संस्करण) और `rules/evidence/` में हैं।

## Troubleshooting

- **प्लगइन इंस्टॉल हो गया पर टूल दिखता नहीं**: जाँचें कि `main` `lib/index.mjs` पर जाता है और `pnpm run build` ने उसे बनाया है।
- **`dsh plugin add` असंगत बताकर मना करता है**: peer range `0.1.x` और `0.2.x` दोनों को कवर करती है; बाहर होने पर स्पष्ट छूट दें: `dsh plugin --profile <name> allow-version <pkg@ver> --dsh-version <runtime> --accept-risk`।
- **कोई नियम नहीं चला**: `skipped` सरणी देखें।
- **`check` में `manifest-peers` विफल दिखता है**: यह `dsh-plugin-dev` की ज्ञात अपस्ट्रीम समस्या है; रनटाइम इंस्टॉल के समय अनुकूलता लागू करता है।
- **समय खिसका हुआ लगता है**: सारी गणना दिए गए स्ट्रिंग पर वॉल-क्लॉक है।

## Development

```sh
pnpm install
pnpm run typecheck
pnpm test
pnpm run build
node ../scripts/sync-shared.mjs dsh-learning-gap-check
```

अंतिम कमांड `../_shared` का साझा किट `src/shared/` में कॉपी करता है; हर साझा बदलाव के बाद इसे दोबारा चलाएँ।

## License

[Apache License 2.0](LICENSE) © 2026 dsh-learning-gap-check contributors.

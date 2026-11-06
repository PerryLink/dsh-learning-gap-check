<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-learning-gap-check-hero-en-dark.webp">
  <img src="docs/assets/dsh-learning-gap-check-hero-en-light.webp" width="100%" alt="dsh-learning-gap-check बैनर: बाईं ओर प्लगइन का नाम, मूल्य की दो पंक्तियाँ और फ़ुटर; दाईं ओर क्षमता-अंतराल रजिस्टर की पंक्ति 1 — पद और क्षमता खाली (LG-001), आवश्यक स्तर 4 में से वर्तमान स्तर 2 घटाने पर अंतराल 2 (LG-003), और एक नमूना संख्या-अक्ष दो-स्तरीय फैलाव दिखाता है; नीचे पाँच शृंखला-फ़ील्ड — उपाय, ज़िम्मेदार व्यक्ति, समय-सीमा, पूर्णता तिथि और स्थिति — जिनमें स्थिति शब्दावली और अंतराल सीमा कॉन्फ़िगर नहीं हैं, इसलिए दोनों skipped में दर्ज हैं; नीचे की टिप्पणी कहती है कि खाली issues सूची उत्तीर्णता नहीं है">
</picture>

# dsh-learning-gap-check

**एक ही कॉल में क्षमता-अंतराल और विकास-योजना रजिस्टर की गणना और शृंखला पूरी जाँचें — केवल अंतर, कोई निर्णय नहीं।**

प्रशिक्षण और मानव संसाधन टीमों के लिए DeepSeek Harness जाँचकर्ता: JSON/YAML रजिस्टर (कर्मचारी हेडर और प्रत्येक क्षमता की एक पंक्ति) पढ़ता है, बदले जा सकने वाले नियम-पैक के अनुसार स्तरों की गणना, विकास उपाय, ज़िम्मेदार व्यक्ति और समय-सीमा जाँचता है, और बताता है कि कौन-सी पंक्ति, कौन-सा कॉलम और क्या अंतर है।

[इंस्टॉल](#तीन-चरणों-में-शुरुआत) · [कॉन्फ़िगरेशन](#कॉन्फ़िगरेशन) · [FAQ](#faq) · [简体中文](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md)

[![License](https://img.shields.io/badge/license-Apache--2.0-3366CC?style=flat-square&labelColor=2B3245)](LICENSE)
[![DSH](https://img.shields.io/badge/DSH-%E2%89%A50.2.1%20%3C0.3.0-4B67B4?style=flat-square&labelColor=2B3245)](#संगतता)
[![npm](https://img.shields.io/npm/v/dsh-learning-gap-check?style=flat-square&labelColor=2B3245&color=CB3837)](https://www.npmjs.com/package/dsh-learning-gap-check)
[![CI](https://img.shields.io/github/actions/workflow/status/PerryLink/dsh-learning-gap-check/ci.yml?branch=main&label=CI&style=flat-square&labelColor=2B3245)](https://github.com/PerryLink/dsh-learning-gap-check/actions/workflows/ci.yml)
[![Node](https://img.shields.io/badge/node-%5E22.19%20%7C%7C%20%3E%3D24-339933?style=flat-square&labelColor=2B3245)](#संगतता)

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

<sub>सामुदायिक प्लगइन, DeepSeek से असंबद्ध। कैनोनिकल रिपॉज़िटरी: <https://github.com/PerryLink/dsh-learning-gap-check> (Gitee एक मिरर है)।</sub>

## यह क्या है

`dsh-learning-gap-check` एक क्षमता-अंतराल और विकास-योजना रजिस्टर पढ़ता है — कर्मचारी हेडर और प्रत्येक क्षमता की एक पंक्ति — और उसी रजिस्टर की अपनी गणना तथा शृंखला-पूर्णता की जाँच करता है: क्या प्रत्येक अंतराल में पद और क्षमता लिखी है, क्या दर्ज स्तर संख्याओं के रूप में पढ़े जा सकते हैं, क्या अंतराल आवश्यक स्तर में से वर्तमान स्तर घटाने के बराबर है, क्या आपके तय सीमांक से अधिक अंतराल पर विकास उपाय दर्ज है, क्या उपाय में ज़िम्मेदार व्यक्ति और पूर्णता तिथि दर्ज है, क्या पूर्णता तिथि समय-सीमा से बाद की नहीं है, और क्या उपाय की स्थिति आपकी ही शब्दावली से ली गई है।

यह मॉडल के सामने एक ही उपकरण रखता है, `learning_gap_check`, और सातों नियम `rules/learning-gap-check.yaml` में डेटा के रूप में रखता है: नियम-पैक बदलने से नियम-समुच्चय बदल जाता है, TypeScript छूने की ज़रूरत नहीं। यह केवल सामग्री और नियमों द्वारा उद्धृत धाराओं के बीच शाब्दिक अंतर बताता है; यह **तय नहीं करता** कि कोई कर्मचारी सक्षम है या नहीं, मूल्यांकन वस्तुनिष्ठ था या नहीं, उपाय कारगर हुआ या नहीं, और न ही समीक्षक का स्थान लेता है।

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-learning-gap-check-flow-v5-dark.svg">
  <img src="docs/assets/dsh-learning-gap-check-flow-v5-light.svg" width="100%" alt="dsh-learning-gap-check संरचना: बाईं ओर का रजिस्टर (JSON/YAML, हेडर और दस नमूना फ़ील्ड) केंद्र में दो-लेन लूप में प्रवेश करता है; छह जाँच-बिंदु स्वतंत्र रूप से फ़ील्ड और स्तर (LG-001/LG-002), अंतराल गणना (LG-003), सीमा-ट्रिगर (LG-004), उपाय के साथ ज़िम्मेदार व्यक्ति और समय-सीमा (LG-005), तिथि-क्रम (LG-006) और स्थिति शब्दावली (LG-007) की जाँच करते हैं; केंद्र में अंतराल = आवश्यक घटा वर्तमान लिखा है; दाईं ओर परिणाम issues[] और skipped[] चैनल बनाते हैं (एक warn, दो skipped), buildView() से गुज़रते हैं और मानव समीक्षा पर रुकते हैं">
</picture>

## तीन चरणों में शुरुआत

1. **इंस्टॉल करें** (एक चैनल चुनें):

   ```sh
   # git चैनल (नवीनतम main; git+https://github.com/PerryLink/dsh-learning-gap-check.git के बराबर)
   dsh plugin --profile <name> add github:PerryLink/dsh-learning-gap-check
   # npm चैनल (प्रकाशित रिलीज़)
   dsh plugin --profile <name> add dsh-learning-gap-check
   # tarball चैनल: इस रेपो में pnpm pack करके
   dsh plugin --profile <name> add ./dsh-learning-gap-check-<version>.tgz
   ```

   कोई नेटिव कोड नहीं: `lib/index.mjs` और `rules/` ही भेजे गए आर्टिफ़ैक्ट हैं।

2. **न्यूनतम कॉन्फ़िग** (डिफ़ॉल्ट से ही चलता है; ज़रूरत हो तो नियम बंद करें या टिप्पणी जोड़ें):

   ```yaml
   - insert:
       - id: dsh-learning-gap-check
         name: dsh-learning-gap-check
         config:
           disabledRules: []
           onlyRules: []
           skipNotes: संस्था की प्रशिक्षण और विकास नीति 2026
   ```

3. **माउंट सत्यापित करें**:

   ```sh
   dsh --profile <name> --dump-config | grep 'dsh-learning-gap-check'
   ```

   रेपो में एक-कमांड वॉकथ्रू है: `pnpm run build` चलाएँ, फिर नमूना।

   ```sh
   node samples/quickstart/run.mjs
   ```

   ```text
   $ node samples/quickstart/run.mjs
   learning_gap_check: 1 issue(s) — error 0, warn 1, info 0
   skipped: 2
   ```

   नमूना `samples/quickstart/input/LG-001-unsafe.json` में है; अपेक्षित परिणाम `samples/quickstart/expected/result.json` में।

**अनइंस्टॉल**: `dsh plugin --profile <name> remove dsh-learning-gap-check` (या प्रोफ़ाइल पैच से वह पंक्ति हटाएँ)।

<details>
<summary>DSH Desktop मार्केट या WorkBuddy / Coze से इंस्टॉल करें</summary>

सभी PerryLink प्लगइन DSH Desktop के अंतर्निहित मार्केट में ब्राउज़ किए जा सकते हैं: **Market → Sources → Add source → पेस्ट करें** `https://perrylink-dsh-catalog.perrylink.workers.dev/catalog-source.json` **→ चुनें**। इंस्टॉलेशन के लिए मार्केट की npm पहचान जाँच और आपकी पुष्टि आवश्यक रहती है।

यह जाँच «Teaching and Review Suite» के एक मद के रूप में भी उपलब्ध है: WorkBuddy / Coze में वह नाम खोजें (यह जाँच उसका एक भाग है; उपलब्धता कैटलॉग के अनुसार)।

</details>

## मुख्य क्षमताएँ

`dsh-learning-gap-check` पूरा रजिस्टर **एक ही उपकरण कॉल** में पूरा करता है और निष्कर्ष-सूची तथा न-चली-जाँच-सूची लौटाता है:

- **एक ही रीड-ओनली रजिस्टर** — कर्मचारी हेडर और प्रत्येक क्षमता की एक पंक्ति वाला JSON या YAML स्वीकार करता है; सामग्री फ़ाइल केवल पढ़ी जाती है, मूल कभी नहीं बदला जाता, और उपकरण कोई फ़ाइल नहीं लिखता।
- **कॉलम उपनाम हल होते हैं** — पद, क्षमता, आवश्यक स्तर, वर्तमान स्तर, अंतराल स्तर, मूल्यांकन विधि, मूल्यांकन तिथि, विकास उपाय, ज़िम्मेदार व्यक्ति, समय-सीमा, पूर्णता तिथि, स्थिति और मूल्यांकनकर्ता के चीनी और अंग्रेज़ी उपनाम हैं; मिलान में केस, रिक्त स्थान, अंडरस्कोर और हाइफ़न अनदेखे होते हैं।
- **सात नियम, डेटा-चालित** — नियम-पैक YAML है और प्रत्येक नियम के लिए जाँच प्रकार, पैरामीटर, आधार और गंभीरता घोषित करता है; नियम-समुच्चय का संस्करण बदलने के लिए `rulesFile` दूसरी फ़ाइल पर इंगित करें।
- **गणना और शृंखला** — अंतराल सूत्र का पुनर्गणना, सीमांक पर प्रतिक्रिया, ज़िम्मेदार व्यक्ति और समय-सीमा, तिथियों का क्रम और स्थिति-शब्दावली, हर एक अपनी पंक्ति और फ़ील्ड के साथ।
- **छूट कभी चुप नहीं** — गायब कॉलम, गायब पैरामीटर, बंद किया गया नियम या खाली शब्दावली, सब कारण के साथ `skipped` में जाते हैं; खाली निष्कर्ष-सूची का अर्थ उत्तीर्ण नहीं है।
- **कोई निर्णय नहीं** — प्रस्तुत रिपोर्ट एक शब्द-संरक्षक से गुज़रती है जो «अनुपालन», «अनुपालन-हीन», «अस्वीकृत» जैसे निर्णायक शब्द रोकता है, और अंत में अस्वीकरण हमेशा जोड़ा जाता है।

### नियम

| नियम | क्या जाँचता है | गंभीरता | आधार प्रकार |
|---|---|---|---|
| `LG-001` | पद और क्षमता दर्ज हैं (कम से कम एक) | warn | derived-from-principle |
| `LG-002` | वर्तमान स्तर (`actualLevel`) संख्या के रूप में पढ़ा जा सकता है | warn | derived-from-principle |
| `LG-003` | अंतराल स्तर = आवश्यक में से वर्तमान (सहनशीलता `0`) | warn | derived-from-principle |
| `LG-004` | सीमांक से अधिक अंतराल पर उपाय दर्ज हो (फ़ैक्टरी में अनकॉन्फ़िगर) | info | institutional-configuration |
| `LG-005` | उपाय में ज़िम्मेदार व्यक्ति और समय-सीमा दर्ज हो | warn | derived-from-principle |
| `LG-006` | समय-सीमा पूर्णता तिथि से पहले की न हो | warn | derived-from-principle |
| `LG-007` | स्थिति आपकी शब्दावली से हो (फ़ैक्टरी में अनकॉन्फ़िगर) | info | institutional-configuration |

`derived-from-principle` गंभीरता को `warn` पर और `institutional-configuration` उसे `info` पर सीमित करता है; यह सीमा लोड के समय लागू होती है, दस्तावेज़ीकरण से नहीं।

### उदाहरण

नीचे `reportJson` से निकाला गया एक वास्तविक निष्कर्ष है, जो `LG-001` टेस्ट फ़िक्स्चर से बना है:

**उपकरण** `learning_gap_check`

**इनपुट**

~~~json
{"employee":"张工","department":"设备部","rows":[{"岗位":"","能力项":"","要求等级":"4","现有等级":"2","差距等级":"2"}]}
~~~

**आउटपुट**

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

| आपका सवाल | इसका जवाब |
|---|---|
| किसी पंक्ति में क्षमता दर्ज है, पर पद का कॉलम खाली है। | `LG-001` उस पंक्ति को तभी दर्ज करता है जब `position` और `competency` दोनों खाली हों; दोनों में से एक भरा होना ही पर्याप्त है। यह देखता है कि पंक्ति में पद और क्षमता लिखे हैं या नहीं, यह नहीं कि उस पद की क्षमता-अपेक्षा उचित या पूर्ण है। |
| हमारे रजिस्टर में स्तर शब्दों में (`proficient`, `mastered`) या अक्षरों में (A/B/C) लिखे हैं — तब क्या होगा? | `LG-002` `actualLevel` पढ़ता है और अपेक्षा करता है कि वह संख्या के रूप में पढ़ा जा सके, इसलिए शब्दों या अक्षरों में लिखा स्तर «न पढ़ा जा सकने वाला» दर्ज होता है। प्लगइन कोई क्षमता-स्तर मापक साथ नहीं लाता: रजिस्टर को संख्यात्मक मापक में बदलें, या `LG-002` के साथ `LG-003` भी बंद कर दें। यह केवल पढ़े जा सकने की जाँच करता है; मूल्यांकन वस्तुनिष्ठ या सटीक था या नहीं, यह नहीं आँकता। |
| अंतराल कॉलम में `3` लिखा है, पर आवश्यक `4` में से वर्तमान `2` घटाने पर `2` बनता है — क्या यह पकड़ में आता है? | हाँ। `LG-003` `requiredLevel − actualLevel` को सहनशीलता `0` के साथ दोबारा जोड़ता है और जिस पंक्ति का दर्ज `gapLevel` मेल नहीं खाता उसे दर्ज करता है। यह पंक्ति-दर-पंक्ति तभी चलता है जब तीनों कॉलम भरे हों; कॉलम गायब हो या पूरी तालिका में फ़ील्ड खाली हो तो नियम `skipped` में चला जाता है, जबकि भरा हुआ पर संख्या न हो ऐसा सेल अलग से «न पढ़ा जा सकने वाला» दर्ज होता है। ऋणात्मक मान जैसा है वैसा दर्ज होता है, क्योंकि कॉलम उलटे भरे हो सकते हैं; और अंतराल कितना बड़ा हो तो समस्या मानी जाए, यह नियम तय नहीं करता। |
| किसी पंक्ति में विकास उपाय दर्ज है, पर ज़िम्मेदार व्यक्ति और पूर्णता तिथि दोनों नहीं। | `LG-005` हर उस पंक्ति में `owner` और `dueAt` की अपेक्षा करता है जिसमें `action` भरा है, और जिसमें इनमें से एक भी न हो उसे दर्ज करता है। यह देखता है कि दोनों कॉलम दर्ज हैं या नहीं; उपाय कारगर है या समय-सीमा उचित है, यह नहीं आँकता। |
| किसी पंक्ति की पूर्णता तिथि उसकी समय-सीमा के बाद की है, या दोनों कॉलम उलटे भर गए हैं। | `LG-006` हर पंक्ति में `dueAt` की तुलना `completedAt` से करता है और तब उस पंक्ति को दर्ज करता है जब समय-सीमा पूर्णता तिथि से पहले की हो। नियम-पैक अपनी सीमा अपने शब्दों में लिखता है: यह केवल दोनों तिथियों का क्रम देखता है, यह नहीं तय करता कि काम वास्तव में समय पर पूरा हुआ। जो तिथि पढ़ी न जा सके वह अलग से दर्ज होती है, चुपचाप छोड़ी नहीं जाती। |
| `LG-004` और `LG-007` कभी कुछ दर्ज ही नहीं करते — क्या इसका अर्थ है कि मेरा रजिस्टर इनमें पास हो गया? | नहीं: दोनों नियम स्वयं को `skipped` में दर्ज करते हैं। `LG-004` में `threshold: 0` है, यानी अनकॉन्फ़िगर — तय करें कि कितने अंतराल पर विकास उपाय अनिवार्य होगा। `LG-007` की स्थिति-शब्दावली ख़ाली है — उसमें अपनी संस्था की शब्दावली भरें। कॉन्फ़िगर होने के बाद `LG-004` केवल यह देखता है कि उपाय का कॉलम भरा है और `LG-007` केवल यह कि स्थिति का मान आपकी सूची में है; कोई भी यह नहीं आँकता कि उपाय वास्तव में लागू हुआ या नहीं। |

### सामग्री का प्रारूप

JSON और YAML दोनों स्वीकार्य हैं। यहाँ एक पूरा रजिस्टर है:

```yaml
employee: 张工
department: 设备部
plan: 2026 वार्षिक क्षमता योजना
cycle: 2026 H1
rows:
  - { 序号: '1', 岗位: 设备工程师, 能力项: 设备故障诊断, 要求等级: '4',
      现有等级: '2', 差距等级: '2', 评估方法: 实操考核 + 主管评价,
      评估日期: 2026-03-01, 培养措施: 安排为期三个月的现场带教与故障复盘,
      责任人: 李主管, 完成期限: 2026-06-30, 完成日期: 2026-06-20,
      状态: 进行中, 评估人: 王经理 }
```

- पंक्ति-सूची का नाम `rows`, `items`, `gaps` या `差距` हो सकता है; हेडर में `employee`, `department`, `plan`, `cycle` और `checkedAt` हो सकते हैं।
- फ़ील्ड पढ़ने की परत में वैकल्पिक हैं और जाँच इंजन उन्हें सत्यापित करता है, इसलिए आंशिक निर्यात पर क्रैश के बजाय «फ़ील्ड अनुपस्थित» श्रेणी के निष्कर्ष मिलते हैं।
- पढ़ने के बाद उपनाम मानक फ़ील्ड नामों में बदल जाते हैं, इसलिए निष्कर्ष कोशिका को `position`, `competency` या `gapLevel` से पहचानता है; पंक्ति संख्या रजिस्टर के क्रम-कॉलम से आती है (न हो तो सूचकांक से)।
- पहले Excel को JSON/YAML में बदलें; जहाँ प्लेटफ़ॉर्म समर्थन दे वहाँ चैट यह कर सकती है। एक कॉल एक रजिस्टर जाँचती है; कई शीटों का विलय दायरे से बाहर है।

### किन मानकों पर आधारित

| दस्तावेज़ | संख्यांक | इन्हें उद्धृत करने वाले नियम |
|---|---|---|
| Quality management — Guidelines for competence management and people development | GB/T 19025—2023 (2023-03-17 को जारी और प्रभावी; राष्ट्रीय गुणवत्ता प्रबंधन और गुणवत्ता आश्वासन तकनीकी समिति के अधीन; धारा संख्या इस बार प्राप्त नहीं हुई) | LG-001, LG-002, LG-003, LG-005, LG-006 |
| संस्था की प्रशिक्षण और विकास नीति (संस्था कॉन्फ़िगरेशन) | कोई एकीकृत मानक नहीं (यह नियम संस्था द्वारा कॉन्फ़िगर किए गए अंतराल सीमांक पर आधारित है) | LG-004 |
| संस्था की प्रशिक्षण और विकास नीति (संस्था कॉन्फ़िगरेशन) | कोई एकीकृत मानक नहीं (यह नियम संस्था द्वारा कॉन्फ़िगर की गई स्थिति-शब्दावली पर आधारित है) | LG-007 |

यह व्यवस्था GB/T 19025—2023 और ISO 10015:2019 में निहित है (एक ही शीर्षक, 2019-12-17 से प्रभावी)। इस बार राष्ट्रीय मानक पृष्ठ पर «अंगीकरण स्थिति» का कोई फ़ील्ड नहीं मिला, इसलिए नियम-पैक दोनों के बीच **किसी अंगीकरण संबंध का दावा नहीं करता**। 2001 संस्करण प्रशिक्षण-प्रबंधन प्रणाली पर था और 2023 संस्करण क्षमता प्रबंधन तथा व्यक्ति विकास पर: ये एक ही विषय के संशोधन नहीं हैं; उद्धृत करने से पहले वर्तमान मानक का आवरण और प्राक्कथन स्वयं जाँचें।

### नियमों का स्रोत

नियम-डेटा कोड से अलग है: प्रत्येक नियम में `document` / `number` / `clause` / `excerpt` / `kind` / `source` होते हैं, और `excerpt` कम से कम आठ अक्षरों का शब्दशः उद्धरण होना चाहिए। लोडर यह उद्धरण-अनुशासन लागू करता है और आधार प्रकार के अनुसार गंभीरता सीमित करता है; अपने आधार को बढ़ा-चढ़ाकर दिखाने वाला पैक लोड के समय विफल होता है, ठोस दिखने वाली रिपोर्ट नहीं बनाता।

उद्धरण-निश्चितता `scripts/check-citations.mjs` मशीन से लागू करता है: यह हर अंश को सत्यापन-रिकॉर्ड में खोजता है, और `rules/citations-baseline.json` उन खंडों को दर्ज करता है जो अभी अनुरेखणीय नहीं हैं (आज खाली); आधार-रेखा केवल घट सकती है। इस बार धाराओं का शब्दशः पाठ प्राप्त नहीं हो सका, इसलिए पैक यह बात `excerpt` फ़ील्ड में ही लिखता है और हर नियम को `warn` या `info` पर रखता है।

## कॉन्फ़िगरेशन

सभी समायोज्य पैरामीटर `src/config.ts` की Schemastery स्कीमा में हैं, इसलिए कोड बदले बिना `cordis.yml` से बदले जा सकते हैं; प्रति-नियम सीमाएँ `rules/` के नियम-पैक में हैं।

| कुंजी | प्रकार | डिफ़ॉल्ट | विवरण |
|---|---|---|---|
| `rulesFile` | string | `rules/learning-gap-check.yaml` | नियम-पैक का पथ, पैकेज रूट के सापेक्ष; फ़ाइल बदलने से नियम-समुच्चय का संस्करण बदलता है |
| `disabledRules` | string[] | `[]` | बंद करने वाले नियम id; प्रत्येक `skipped` में दिखता है |
| `onlyRules` | string[] | `[]` | केवल ये नियम चलाएँ; खाली होने पर सभी नियम चलते हैं |
| `skipNotes` | string | `""` | हर `skipped` कारण के आगे जोड़ी जाने वाली टिप्पणी, जैसे संस्था के कार्यान्वयन नियमों का नाम |
| `timeoutMs` | number | `120000` | उपकरण का सहकारी समय-सीमा बजट, मिलीसेकंड में |

प्रति-नियम पैरामीटर पैक में रहते हैं; चार जिन्हें जानना उपयोगी है:

- `LG-003` `resultField` / `expression` / `tolerance` — अंतराल की गणना, डिफ़ॉल्ट `requiredLevel − actualLevel` और बिना सहनशीलता। ऋणात्मक परिणाम जैसा है वैसा दर्ज होता है, क्योंकि इसका अर्थ कॉलम उलटे भरे होना हो सकता है।
- `LG-004` `triggerField` / `threshold` / `requiredField` — आपका नियम कि कब उपाय अनिवार्य होता है। `threshold: 0` का अर्थ है नियम नहीं चलता; `1` का अर्थ एक स्तर या अधिक का अंतराल। तुलना «बराबर या अधिक» है, इसलिए ठीक सीमांक पर भी प्रतिक्रिया होती है।
- `LG-005` `conditionField` / `requiredFields` — कौन-सी शर्त ज़िम्मेदार व्यक्ति और समय-सीमा की अपेक्षा जगाती है।
- `LG-007` `values` — आपकी स्थिति-शब्दावली, जैसे `[शुरू नहीं, जारी, पूर्ण, स्वीकृत]`। खाली का अर्थ है कोई जाँच नहीं।

प्रोफ़ाइल पैच में ओवरराइड का उदाहरण:

```yaml
- insert:
    - id: dsh-learning-gap-check
      name: dsh-learning-gap-check
      config:
        onlyRules: [LG-001, LG-002, LG-003, LG-005, LG-006]
        skipNotes: हमारी 2026 प्रशिक्षण और विकास नीति के अनुसार
```

## FAQ

<details>
<summary>सामग्री अपलोड होती है या डिस्क पर लिखी जाती है?</summary>

नहीं। प्लगइन कोई नेटवर्क अनुरोध नहीं करता, किसी मॉडल को नहीं बुलाता और कोई क्रेडेंशियल संग्रहीत नहीं करता; यह `file` में दी गई स्थानीय फ़ाइल या `material` के इनलाइन पाठ को पढ़ता है और प्रक्रिया के भीतर जाँचता है, कोई फ़ाइल नहीं लिखता। रिपोर्ट सामग्री का स्रोत (निरपेक्ष फ़ाइल पथ या «(इनलाइन सामग्री)») बताती है, और कुछ जाँचें दोषी कोशिका का मान भी बताती हैं (जैसे न पढ़ा जा सकने वाला स्तर, स्थिति का मान, तिथि), इसलिए वह पथ और वे मान परिणाम के साथ सत्र-रिकॉर्ड में जाते हैं; पूरा रजिस्टर कभी रिपोर्ट में कॉपी नहीं होता।

</details>

<details>
<summary>सब हरा है पर कुछ जाँचा ही नहीं गया — क्यों?</summary>

`skipped` देखें। `LG-004` में `threshold: 0` और `LG-007` में खाली `values` सूची है, इसलिए दोनों डिफ़ॉल्ट रूप से बंद रहते हैं; गायब कॉलम या `disabledRules` से बंद किया गया नियम भी वहीं जाता है। खाली निष्कर्ष-सूची का अर्थ है «जो जाँचें चलीं उनमें अंतर नहीं मिला», न कि «जो नहीं चलीं वे पास हो गईं»।

</details>

<details>
<summary>हमारे स्तर «proficient» जैसे शब्दों में हैं — क्या वैसे ही इस्तेमाल कर सकते हैं?</summary>

नहीं। `LG-002` और `LG-003` संख्यात्मक स्तर मानते हैं: शब्द या अक्षर «न पढ़े जा सकने वाले» के रूप में दर्ज होते हैं। रजिस्टर को तुलनीय संख्यात्मक मापक में बदलें, या `LG-002` और `LG-003` बंद करें। प्लगइन कोई मापक नहीं देता, क्योंकि «proficient» को संख्या में बदलना एक मॉडलिंग निर्णय है जो उपयोगकर्ता को लेना है।

</details>

<details>
<summary>क्या यह अन्य प्लगइनों से उपकरण नाम, सेवा या रूट पर टकराता है?</summary>

नहीं। यह नेमस्पेस वाला एक ही उपकरण `learning_gap_check` पंजीकृत करता है, कोई सेवा कुंजी नहीं देता, कोई क्लाइंट स्लॉट या `webServer` उपसर्ग पंजीकृत नहीं करता, और कोई ग्लोबल नहीं बदलता; बंडल पैच केवल अपनी पंक्ति `insert` करता है। बिंदु-दर-बिंदु तर्क «अन्य DSH प्लगइनों के साथ इंटरऑपरेबिलिटी» में है।

</details>

<details>
<summary>प्रदर्शन पर कितना खर्च है?</summary>

एक कॉल सामग्री को मेमोरी में पढ़ती है और हर नियम प्रति पंक्ति स्थिर-समय जाँच करता है, कोई नेटवर्क या मॉडल कॉल नहीं; नियमों की संख्या निश्चित सात है, इसलिए खर्च पंक्तियों के साथ रैखिक बढ़ता है। `timeoutMs` सहकारी बजट है: उपकरण पढ़ने/पढ़ाई से पहले और बाद में रद्दीकरण संकेत जाँचता है, और समय समाप्त होने पर होस्ट बाधित करता है।

</details>

## सुरक्षा सीमाएँ

- **केवल पढ़ने योग्य सामग्री।** उपकरण `file` की फ़ाइल (UTF-8) पढ़ता है या इनलाइन `material` इस्तेमाल करता है; कोई फ़ाइल नहीं लिखता और मूल नहीं बदलता। `package.json` में डेमो घोषणा `writes: []` और `network: false` कहती है, और एकमात्र क्षमता `tools:register` है।
- **कोई नेटवर्क नहीं, कोई मॉडल कॉल नहीं, कोई क्रेडेंशियल नहीं।** जाँच शुद्ध इन-प्रोसेस गणना है; सामग्री को मशीन से बाहर भेजने का कोई रास्ता नहीं है।
- **कोई निर्णय नहीं।** प्रस्तुत रिपोर्ट `src/shared/wording.ts` के शब्द-संरक्षक से गुज़रती है, जो «अनुपालन», «अनुपालन-हीन», «अस्वीकृत», «स्वीकृति पार» जैसे निर्णायक शब्द रोकता है, और अस्वीकरण हमेशा जोड़ा जाता है; निष्कर्ष केवल पंक्ति, कॉलम और अपेक्षा बताता है।
- **उद्धरण गढ़े नहीं जाते।** अंश कम से कम आठ अक्षरों का शब्दशः उद्धरण होना चाहिए; जब आधार केवल सिद्धांत (`derived-from-principle`) या संस्था कॉन्फ़िगरेशन (`institutional-configuration`) हो, तो गंभीरता क्रमशः `warn` और `info` पर सीमित होती है। जब पाठ प्राप्त नहीं हुआ, तो `excerpt` फ़ील्ड यह बताता है।
- **छूट कभी चुप नहीं।** जो भी जाँच नहीं चल सकती वह कारण के साथ `skipped` में जाती है; खाली निष्कर्ष-सूची कभी «कोई समस्या नहीं» के रूप में प्रस्तुत नहीं होती।
- **लोड पर विफल।** नियम-पैक लोड के समय सत्यापित होता है: अज्ञात जाँच प्रकार, अपूर्ण पैरामीटर और अमान्य रेगुलर एक्सप्रेशन ज़ोर से विफल होते हैं, टूटे नियमों के साथ नहीं चलते।
- **पंजीकरण एक इफ़ेक्ट है।** `ctx.tools.register` डिस्पोज़र लौटाता है, इसलिए प्लगइन अनलोड या हॉट-रीलोड पर उपकरण हट जाता है।
- **सहकारी समय-सीमा।** रद्दीकरण संकेत पढ़ने और पढ़ाई की सीमाओं पर जाँचा जाता है; समय समाप्त होने पर पृष्ठभूमि कार्य नहीं बचता।

## ज्ञात सीमाएँ

**सीमा:** यह प्लगइन एक **क्षमता-अंतराल और विकास-योजना रजिस्टर** की गणना और शृंखला जाँचता है — कि हर अंतराल अपना पद और क्षमता बताता है, कि दोनों स्तर-कॉलम संख्याओं के रूप में पढ़े जाते हैं, कि अंतराल आवश्यक में से वर्तमान के बराबर है, कि आपके सीमांक से अधिक अंतराल पर विकास उपाय है, कि उपाय ज़िम्मेदार व्यक्ति और समय-सीमा बताता है, कि पूर्णता तिथि समय-सीमा से बाद की नहीं है, और कि उपाय की स्थिति आपकी शब्दावली से है। यह **तय नहीं करता** कि कोई कर्मचारी सक्षम है, मूल्यांकन वस्तुनिष्ठ था, विकास उपाय कारगर हुआ, या किसी को स्थानांतरित/हटाया जाना चाहिए।

> ### ⚠️ यह प्लगइन जो जान-बूझकर शामिल नहीं करता
>
> **इसमें कोई क्षमता-स्तर मापक नहीं है, और यह मानता है कि स्तर संख्याएँ हैं।** `LG-002` और `LG-003` संख्यात्मक कॉलम पढ़ते हैं और उनके बीच की गणना जाँचते हैं। अक्षर-श्रेणी (`A`/`B`/`C`) या शब्दों (`proficient`/`mastered`) वाला रजिस्टर **न पढ़े जा सकने वाला** दर्ज होता है, क्योंकि ऐसे स्तरों की तुलना एक मॉडलिंग निर्णय है जो प्लगइन आपके लिए नहीं लेगा। मापक बदलें, या वे नियम बंद करें।
>
> **«कार्रवाई ज़रूरी होने जितना बड़ा» के लिए कोई सीमांक नहीं है।** कितना अंतराल विकास उपाय अनिवार्य करता है, यह संस्था के प्रतिभा-प्रबंधन का निर्णय है — कुछ इकाइयाँ हर कमी पर उपाय माँगती हैं, कुछ एक स्तर तक सहन करती हैं — इसलिए `LG-004` का सीमांक `0` से शुरू होता है और जब तक आप उसे तय नहीं करते, नियम स्वयं को `skipped` में दर्ज करता है।
>
> **स्थिति-शब्दावली भी इसी कारण खाली है।** और तिथि नियम केवल यह जाँचता है कि समय-सीमा पूर्णता तिथि से पहले की न हो, जो डेटा-प्रविष्टि का गुण है: **यह नहीं आँकता कि काम देर से हुआ।**
>
> **नियम-पैक का हर `excerpt` स्पष्ट कहता है कि धारा का पाठ इस बार प्राप्त नहीं हुआ।** यह व्यवस्था GB/T 19025 और हर संस्था के योग्यता तथा प्रशिक्षण नियमों में निहित है। सत्यापन चरण शब्दशः पाठ नहीं ला सका, इसलिए पैक यह कमी `excerpt` फ़ील्ड में ही बताता है और हर नियम को `warn` या `info` पर रखता है। **पाठ मिलने पर हर `excerpt` को वास्तविक धारा से बदलें और `kind` को `direct` तक उठाएँ।**

अन्य सीमाएँ:

- **तिथियाँ केवल क्रम से तुलना होती हैं।** `LG-006` `dueAt` और `completedAt` के तिथि-भाग की तुलना करता है, समय-क्षेत्र नहीं बदलता और देरी नहीं आँकता; पूर्णता तिथि समय-सीमा से पहले की हो तो भी दर्ज होती है, क्योंकि इसका अर्थ आमतौर पर कॉलम उलटे भरे होना है। समर्थित रूप `2026-03-15` और `2026-03-15 09:30` हैं।
- **उपनाम मिलान शाब्दिक है।** यह केवल केस, रिक्त स्थान, अंडरस्कोर और हाइफ़न सामान्य करता है; समानार्थी नहीं निकालता और फ़ज़ी मिलान नहीं करता। `src/model.ts` की उपनाम-तालिका से बाहर का नया कॉलम नाम तब तक गायब कॉलम माना जाता है जब तक आप उसे न जोड़ें।
- **एक कॉल, एक रजिस्टर।** उपकरण एक ही फ़ाइल या एक इनलाइन पाठ लेता है; कई शीट, विभाग या चक्रों का समेकन पहले विभाजित या विलय करना होगा।
- **संख्याएँ निकाली जाती हैं।** संख्यात्मक जाँच पाठ से संख्या निकालती है (पूर्ण-चौड़ाई अंक, हज़ार विभाजक और रिक्त स्थान सहन करती है); `स्तर 3` का `3` बनता है, जबकि `स्तर तीन` नहीं बनता।
- **सहकारी समय-सीमा।** `timeoutMs` होस्ट के रद्दीकरण संकेत पर निर्भर है; बहुत बड़ा रजिस्टर कॉल करने वाले को बाँटना चाहिए।
- **`check` में `manifest-peers` विफल दिख सकता है।** स्थिर जाँचकर्ता 0.2 पंक्ति से पहले की हार्डकोडेड peer रेंज से तुलना करता है; रनटाइम इंस्टॉल के समय peer अनुकूलता लागू करता है, इसलिए घोषित रेंज सही है। यह `dsh-plugin-dev` की ज्ञात अपस्ट्रीम समस्या है।
- **इंस्टॉल के बाद उपकरण नहीं दिखता।** जाँचें कि `main` `lib/index.mjs` पर जाता है और `pnpm run build` ने उसे बनाया है; गलत `main` पर लोडर प्रविष्टि चुपचाप छोड़ देता है।

## अन्य DSH प्लगइनों के साथ इंटरऑपरेबिलिटी

यह प्लगइन एक उपकरण नाम लेता है और किसी साझा ईवेंट को नहीं छूता:

- **एक ही उपकरण नाम।** यह केवल `learning_gap_check` पंजीकृत करता है, नेमस्पेस के साथ; अंतर्निहित उपकरण या किसी अन्य प्लगइन का कोई नंगा नाम नहीं लेता।
- **कोई सेवा कुंजी नहीं।** कोई सेवा कुंजी नहीं देता, इसलिए उस पर टकराव असंभव है।
- **कोई स्लॉट नहीं।** कोई क्लाइंट स्लॉट कुंजी पंजीकृत नहीं करता, इसलिए `shadows-shipped-ui` सीट के लिए प्रतिस्पर्धा नहीं करता।
- **कोई HTTP रूट नहीं।** कोई `webServer` उपसर्ग पंजीकृत नहीं करता।
- **कोई ईवेंट लिसनर नहीं।** कभी `ctx.on()` नहीं बुलाता, इसलिए किसी प्लगइन की `agent/pre-step` या `tools/*` शृंखला से नहीं जुड़ता और किसी अन्य लिसनर को शॉर्ट-सर्किट नहीं कर सकता।
- **पैच-परत टकराव नहीं।** बंडल पैच केवल अपनी पंक्ति `insert` करता है; अंतर्निहित पंक्ति का `config` कभी नहीं बदलता।
- **कोई ग्लोबल बदलाव नहीं।** प्रोटोटाइप नहीं बदलता, `process.env` नहीं लिखता, वैश्विक fetch डिस्पैचर नहीं बदलता।
- **स्पष्ट निर्भरता।** `inject: ['tools']`: tools सेवा न हो तो प्लगइन लोड ही नहीं होता (fail closed), आधा चालू होकर चुपचाप कार्य खोता नहीं।

स्थिर प्रमाण: `src/index.ts:76-140` केवल `ctx.tools.register` कहता है और डिस्पोज़र को इफ़ेक्ट के रूप में लौटाता है; `cordis.patch.yml:6-8` में एक ही `insert` है; `package.json#dsh.capabilities` में केवल `tools:register` है।

## संगतता

| सतह | स्थिति |
|---|---|
| Harness | peer रेंज `>=0.1.2-rc.1 <0.2.0 \|\| >=0.2.0-0 <0.3.0` — `0.2.0-rc.2` और `0.2.1-rc.2` दोनों को स्वीकार करने के लिए सत्यापित। `engines.dsh` `>=0.2.1-0 <0.3.0` के रूप में घोषित है और 0.2.1 से होस्ट इसे लागू करता है |
| Node | `^22.19.0 \|\| >=24.0.0` |
| प्लेटफ़ॉर्म | सभी (शुद्ध ESM; कोई नेटिव कोड नहीं, कोई नेटवर्क नहीं, कोई मॉडल कॉल नहीं) |
| टूल मोड | `native` और `ptc` में काम करता है; एक सत्र में बार-बार कॉल के लिए `ptc` स्कीमा लागत एक ही बार चुकाता है |

## इकोसिस्टम और गुणवत्ता

- [Gitee मिरर](https://gitee.com/perrylink/dsh-learning-gap-check) (सिंक मिरर; GitHub कैनोनिकल है)
- [dshfind प्लगइन पृष्ठ](https://dshfind.com/plugins/PerryLink/dsh-learning-gap-check) (इंस्टॉल और रैंकिंग)
- [OpenSSF Scorecard रिपोर्ट](https://securityscorecards.dev/viewer/?uri=github.com/PerryLink/dsh-learning-gap-check) ([.github/workflows/scorecard.yml](.github/workflows/scorecard.yml) से संचालित)
- [DSH Market](https://dsh.market/) (सूचीबद्ध)
- [सामग्री के अनुसार जाँचकर्ता चुनें](https://perrylink.github.io/zh/checkers/choose/): यह रेपो PerryLink जाँचकर्ता परिवार का एक सदस्य है
- [इकोसिस्टम ज्ञान-आधार](https://perrylink.github.io/dsh-plugin-guide/): प्लगइन विकास गाइड · मापे गए चयन आँकड़े · रखरखाव के मानदंड

## डेवलपमेंट

```sh
pnpm install
pnpm run typecheck            # tsc --noEmit
pnpm test                     # vitest: साझा टेबल-प्लगइन सूट + प्रति नियम जोड़ी फ़िक्स्चर
pnpm run build                # tsdown -> lib/index.mjs + lib/index.d.mts
pnpm run verify:self-contained
pnpm run check:lockfile
pnpm run check:readmes        # पाँच भाषाओं के README की संगति
pnpm run check:citations      # उद्धरण-नुरेखणीयता
pnpm pack
node ../scripts/sync-shared.mjs dsh-learning-gap-check   # src/shared ताज़ा करें
```

निर्देशिका संरचना:

```text
src/index.ts        उपकरण पंजीकरण, नियम-पैक का पता लगाना, सामग्री पढ़ना
src/config.ts       Schemastery कॉन्फ़िग स्कीमा
src/model.ts        रजिस्टर कॉलम, उपनाम और अपेक्षित फ़ील्ड
src/check.ts        शुद्ध जाँच कोर (कोई I/O, कोई घड़ी, कोई मॉडल नहीं)
src/parse.ts        JSON/YAML पाठक
src/view.ts         मॉडल के लिए परिणाम प्रक्षेपण
src/shared/         साझा टेबल इंजन (अंदर कॉपी, बाहरी निर्भरता नहीं)
rules/              नियम-पैक (7 नियम) और उद्धरण आधार-रेखा
tests/              vitest: साझा सूट + प्रति नियम जोड़ी फ़िक्स्चर
samples/quickstart/ एक-कमांड वॉकथ्रू
scripts/            गेट और README चित्र जनरेटर
```

प्लगइन **डेटा-चालित** है: `src/model.ts` तालिका का आकार घोषित करता है, साझा किट पाठक और जाँच इंजन देता है, और नियम-पैक हर जाँच घोषित करता है। README चित्र [`scripts/gen-readme-assets.py`](scripts/gen-readme-assets.py) से उत्पन्न होते हैं (Pillow ढाँचा, हस्तलिखित SVG) और सुरक्षित रूप से दोबारा चलाए जा सकते हैं; UI और बेंचमार्क डेटा न होने से यह रेपो केवल हल्का/गहरा फ़्लो जोड़ा बनाता है।

Topics: `deepseek-harness`, `dsh`, `dsh-plugin`, `cordis`, `learning`, `gap`

## परिवार और आभार

यह परियोजना [PerryLink](https://github.com/PerryLink) के DeepSeek Harness प्लगइन परिवार का हिस्सा है (सभी Apache-2.0)। अगर यह उपयोगी लगे, तो **एक स्टार अगले व्यक्ति को इसे खोजने में मदद करता है** — इसके पीछे कोई सुविधा बंद नहीं है।

- [@PerryLink](https://github.com/PerryLink) — निर्माता और अनुरक्षक: टेबल जाँच इंजन, `LG-*` नियम-पैक और पाँच भाषाओं का दस्तावेज़।

<details>
<summary>सभी प्लगइन देखें</summary>

| प्लगइन | स्थिति |
|---|---|
| **[dsh-aqua-input-check](https://github.com/PerryLink/dsh-aqua-input-check)** |  |
| **[dsh-archive-check](https://github.com/PerryLink/dsh-archive-check)** |  |
| **[dsh-auto-review](https://github.com/PerryLink/dsh-auto-review)** |  |
| **[dsh-autotier](https://github.com/PerryLink/dsh-autotier)** | 🧊 फ़्रोज़न — रेपो README देखें |
| **[dsh-bid-ca-precheck](https://github.com/PerryLink/dsh-bid-ca-precheck)** |  |
| **[dsh-bid-qual-check](https://github.com/PerryLink/dsh-bid-qual-check)** |  |
| **[dsh-cert-mcp](https://github.com/PerryLink/dsh-cert-mcp)** | 🧊 फ़्रोज़न — रेपो README देखें |
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
| **[dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor)** | 🚫 रिटायर्ड (रेपो संग्रहीत) |
| **[dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide)** |  |
| **[dsh-plugin-kit](https://github.com/PerryLink/dsh-plugin-kit)** | 🚫 रिटायर्ड (रेपो संग्रहीत) |
| **[dsh-plugin-upgrade](https://github.com/PerryLink/dsh-plugin-upgrade)** | 🚫 रिटायर्ड (रेपो संग्रहीत) |
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
| **[dsh-ticktick](https://github.com/PerryLink/dsh-ticktick)** | 🚫 रिटायर्ड (रेपो संग्रहीत) |
| **[dsh-translate](https://github.com/PerryLink/dsh-translate)** |  |
| **[dsh-warranty-calc](https://github.com/PerryLink/dsh-warranty-calc)** |  |
| **[dsh-budget](https://github.com/PerryLink/dsh-budget)** | 🧊 फ़्रोज़न — रेपो README देखें |
| **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** | 🧊 फ़्रोज़न — रेपो README देखें |
| **[dsh-defend](https://github.com/PerryLink/dsh-defend)** | 🧊 फ़्रोज़न — रेपो README देखें |
| **[dsh-draw](https://github.com/PerryLink/dsh-draw)** | 🧊 फ़्रोज़न — रेपो README देखें |
| **[dsh-reach](https://github.com/PerryLink/dsh-reach)** | 🧊 फ़्रोज़न — रेपो README देखें |
| **[dsh-background-agents](https://github.com/PerryLink/dsh-background-agents)** | 🚫 रिटायर्ड (रेपो संग्रहीत) |
| **[dsh-session-pin](https://github.com/PerryLink/dsh-session-pin)** | 🚫 रिटायर्ड (रेपो संग्रहीत) |
| **[dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms)** | 🚫 रिटायर्ड (रेपो संग्रहीत) |

</details>

## लाइसेंस

[LICENSE](LICENSE) (Apache License 2.0) © 2026 dsh-learning-gap-check contributors

<p align="center"><sub>Apache-2.0 · सामुदायिक प्लगइन, DeepSeek से असंबद्ध।</sub></p>

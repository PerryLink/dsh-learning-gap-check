#!/usr/bin/env python3
"""README visuals for dsh-learning-gap-check — drawn from this plugin's real run.

Two figures, both read off the shipped source and rule pack:

  hero 1440x576 (Pillow, four files: zh/en x light/dark)
      One row of the capability-gap register, excerpted. The row is 张工 /
      设备部 / 2026 上半年. Its 岗位 and 能力项 cells are empty, which is the
      one real finding of samples/quickstart (LG-001, warn, row 1). The
      arithmetic block shows 4 - 2 = 2 for 要求等级 / 现有等级 / 差距等级
      (LG-003; the shipped tolerance is 0). The level scale marks 2 and 4 and
      brackets the two-level gap. The closure strip carries the values the
      register actually stores: 措施 已填, 责任人 李主管, 期限 06-30,
      完成 06-20, 状态 进行中. LG-004 (threshold 0) and LG-007 (values []) ship
      unconfigured, so both are reported in skipped, not passed. Footer counts
      are the quickstart output: issues 1, warn 1, skipped 2.

  flow 1100x660 (hand-written SVG, two files: light/dark)
      A two-lane closed loop, not a row of arrowed boxes. The register on the
      left (JSON/YAML, header + ten fields) enters the loop. Six checkpoints sit
      on the two lanes: fields and levels (LG-001/LG-002), gap arithmetic
      (LG-003), threshold trigger (LG-004), action with owner and due date
      (LG-005), date order (LG-006), status vocabulary (LG-007). The lanes are
      the development-cycle the register records; the centre says, in the
      plugin's own terms, that the rules are checked per row and independently,
      not in execution order. The loop's results leave down a collector rail
      into two channels, issues[] and skipped[], then buildView() projects
      markdown / reportJson / summary and stops at human review. LG-004 and
      LG-007 are drawn dashed because the shipped pack leaves them
      unconfigured; the quickstart report is warn 1 and skipped 2.

Every value in both figures was produced by running this repository's own
lib/index.mjs over samples/quickstart/input/LG-001-unsafe.json. No invented
data: the one issue is "第 1 行 position、competency 都为空", and the two
skipped reasons are the shipped threshold / values messages.

Run:  python scripts/gen-readme-assets.py [all|hero|flow]
Needs: Pillow and the Windows faces msyh.ttc / msyhbd.ttc / consola.ttf /
       consolab.ttf. A missing face aborts instead of shipping tofu boxes.
"""
from __future__ import annotations

import math
import os
import sys
from pathlib import Path
from xml.etree import ElementTree
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets"
NAME = "dsh-learning-gap-check"

FONT_FILES = {
    "cjk": r"C:\Windows\Fonts\msyh.ttc",
    "cjk_bold": r"C:\Windows\Fonts\msyhbd.ttc",
    "mono": r"C:\Windows\Fonts\consola.ttf",
    "mono_bold": r"C:\Windows\Fonts\consolab.ttf",
}
for _kind, _path in FONT_FILES.items():
    if not os.path.exists(_path):
        raise SystemExit(f"FATAL: font missing for {_kind}: {_path}")

# Family palette: accent #4B67B4 (dark #8496f5), light page #f9f6fd -> #e4eaf8,
# dark page #131a2a -> #0c1016. The two skins share every role name.
SKIN = {
    "light": dict(
        bg_from="#f9f6fd", bg_to="#e4eaf8",
        card="#ffffff", edge="#e6e2ef",
        text="#141419", sub="#4d5261", faint="#8b90a0",
        accent="#4B67B4", accent_soft="#ece7f9",
        mark="#b45309", mark_bg="#fdf3e9", mark_edge="#e8b483",
        ok="#15803d", ok_bg="#e8f5ec", ok_edge="#9dcdb0",
        band="#f5f2fb", band_alt="#faf8fe", grid="#e3dfee",
        shadow=(34, 27, 70), glow="#7a68c9",
    ),
    "dark": dict(
        bg_from="#131a2a", bg_to="#0c1016",
        card="#1b2231", edge="#2e374b",
        text="#f0f3f9", sub="#a8b1c4", faint="#7c8497",
        accent="#8496f5", accent_soft="#242d42",
        mark="#e0a44e", mark_bg="#2a2216", mark_edge="#7a5a24",
        ok="#4bc46c", ok_bg="#16281d", ok_edge="#2f6b41",
        band="#202839", band_alt="#1e2534", grid="#2b3348",
        shadow=(0, 0, 0), glow="#8496f5",
    ),
}

_SCRATCH = ImageDraw.Draw(Image.new("RGB", (8, 8)))
_FONTS: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}


def font(size: float, kind: str = "cjk") -> ImageFont.FreeTypeFont:
    key = (kind, int(round(size)))
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype(FONT_FILES[kind], int(round(size)))
    return _FONTS[key]


def hx(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def rgb(value) -> tuple[int, int, int]:
    return value if isinstance(value, tuple) else hx(value)


def mix(first, second, t: float):
    a, b = rgb(first), rgb(second)
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def tw(text: str, size: float, kind: str = "cjk") -> float:
    return _SCRATCH.textlength(text, font=font(size, kind))


def need(text: str, size: float, kind: str, max_w: float, what: str) -> None:
    width = tw(text, size, kind)
    if width > max_w + 0.5:
        raise SystemExit(f"FATAL: {what} overflows: {text!r} needs {width:.1f}px "
                         f"> {max_w:.0f}px")


def put(draw: ImageDraw.ImageDraw, x: float, y: float, text: str, size: float,
        color, kind: str = "cjk", anchor: str = "ls",
        max_w: float | None = None, what: str = "text") -> float:
    width = tw(text, size, kind)
    if max_w is not None and width > max_w + 0.5:
        raise SystemExit(f"FATAL: {what} overflows: {text!r} needs {width:.1f}px "
                         f"> {max_w:.0f}px")
    draw.text((x, y), text, font=font(size, kind), fill=rgb(color), anchor=anchor)
    return width


def gradient(width: int, height: int, c1: str, c2: str) -> Image.Image:
    base = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(base)
    a, b = hx(c1), hx(c2)
    for y in range(height):
        t = 0.12 * (y / height) + 0.88 * (y / height) ** 1.25
        draw.line([(0, y), (width, y)],
                  fill=tuple(int(round(p + (q - p) * t)) for p, q in zip(a, b)))
    return base


def glow(img: Image.Image, cx: int, cy: int, radius: int, color, alpha: int) -> Image.Image:
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                 fill=rgb(color) + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(radius * 0.55))
    return Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")


def card(img: Image.Image, box: tuple, s: dict, radius: int = 20,
         fill: str = "card", edge: str = "edge", width: int = 2,
         blur: int = 16, dy: int = 9, alpha: int = 40) -> Image.Image:
    x0, y0, x1, y1 = box
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle([x0, y0 + dy, x1, y1 + dy], radius=radius,
                           fill=s["shadow"] + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(box, radius=radius, fill=hx(s[fill]),
                           outline=hx(s[edge]), width=width)
    return img


def dashed_line(draw: ImageDraw.ImageDraw, a: tuple, b: tuple, color,
                width: int = 2, dash: int = 6, gap: int = 5) -> None:
    length = math.hypot(b[0] - a[0], b[1] - a[1])
    if length == 0:
        return
    step = dash + gap
    count = int(length // step) + 1
    for i in range(count):
        t0 = i * step / length
        t1 = min((i * step + dash) / length, 1.0)
        if t0 >= 1:
            break
        draw.line([(a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0),
                   (a[0] + (b[0] - a[0]) * t1, a[1] + (b[1] - a[1]) * t1)],
                  fill=rgb(color), width=width)


def dashed_rect(draw: ImageDraw.ImageDraw, box: tuple, color,
                width: int = 2) -> None:
    x0, y0, x1, y1 = box
    dashed_line(draw, (x0 + 10, y0), (x1 - 10, y0), color, width)
    dashed_line(draw, (x0 + 10, y1), (x1 - 10, y1), color, width)
    dashed_line(draw, (x0, y0 + 10), (x0, y1 - 10), color, width)
    dashed_line(draw, (x1, y0 + 10), (x1, y1 - 10), color, width)


def pill(img: Image.Image, x: float, y: float, text: str, size: float,
         fg, bg, kind: str = "cjk_bold", pad: int = 14,
         height: int | None = None, anchor: str = "left") -> tuple[float, int]:
    draw = ImageDraw.Draw(img)
    width = tw(text, size, kind)
    h = height or int(round(size * 1.85))
    box_w = width + pad * 2
    x0 = x - box_w if anchor == "right" else x
    draw.rounded_rectangle([x0, y, x0 + box_w, y + h], radius=h // 2,
                           fill=hx(bg))
    draw.text((x0 + pad, y + h / 2), text, font=font(size, kind),
              fill=hx(fg), anchor="lm")
    return box_w, h


def mini_chip(draw: ImageDraw.ImageDraw, x: float, y: float, text: str,
              size: float, fg, bg, kind: str = "mono_bold", pad: int = 8,
              height: int = 20, anchor: str = "left") -> float:
    width = tw(text, size, kind)
    box_w = width + pad * 2
    x0 = x - box_w if anchor == "right" else x
    draw.rounded_rectangle([x0, y, x0 + box_w, y + height], radius=height // 2,
                           fill=hx(bg))
    draw.text((x0 + pad, y + height / 2), text, font=font(size, kind),
              fill=hx(fg), anchor="lm")
    return box_w


def check_dot(img: Image.Image, cx: float, cy: float, radius: float, s: dict,
              fg: str = "ok", bg: str = "ok_bg", edge: str = "ok_edge") -> None:
    """A tick drawn as two strokes: no font in the family has to carry U+2713."""
    draw = ImageDraw.Draw(img)
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                 fill=hx(s[bg]), outline=hx(s[edge]), width=2)
    draw.line([(cx - radius * 0.45, cy + radius * 0.02),
               (cx - radius * 0.10, cy + radius * 0.38),
               (cx + radius * 0.50, cy - radius * 0.34)],
              fill=hx(s[fg]), width=max(2, int(radius * 0.26)),
              joint="curve")


# ---------------------------------------------------------------------------
# Hero copy — every value traced to samples/quickstart and the shipped config.
# ---------------------------------------------------------------------------
HERO = {
    "zh": dict(
        kicker="DeepSeek Harness 插件 · 能力台账核对",
        title1="dsh-learning-", title2="gap-check",
        value=["七条规则逐行核对一份能力台账，", "差在哪一格、为什么，一次列清。"],
        sub="只列台账内的算术与闭环差异；结论仍由审核人作出。",
        meta="LG-001…LG-007 · warn 1 · skipped 2 · 空 issues ≠ 通过",
        foot="Apache-2.0 · 只读 · 不联网 · 不调用模型 · 不写文件",
        row_title="台账 · 第 1 行",
        row_chip="JSON · 1 行",
        person="张工 · 设备部 · 2026 上半年",
        sec1="算术 · LG-003",
        eq_labels=["要求", "现有", "差距"],
        tolerance="容差 0",
        scale="示例数值轴 1–4",
        gap="差距 2 级",
        sec2="闭环 · LG-004…LG-007",
        closure=[("措施", "已填", "ok"), ("责任人", "李主管", "ok"),
                 ("期限", "06-30", "ok"), ("完成", "06-20", "ok"),
                 ("状态", "进行中", "warn")],
        skip_note="LG-004 threshold 0 · LG-007 values [] → skipped",
        issue="LG-001 × 第 1 行 岗位、能力项都为空",
        counts="issues 1 · warn 1 · skipped 2",
        notpass="空 issues ≠ 通过",
    ),
    "en": dict(
        kicker="DeepSeek Harness plugin · capability ledger",
        title1="dsh-learning-", title2="gap-check",
        value=["Seven rules audit one capability ledger,",
               "cell by cell — the gap and its reason."],
        sub="Arithmetic and closure only — the reviewer still decides.",
        meta="LG-001…LG-007 · warn 1 · skipped 2 · empty issues ≠ a pass",
        foot="Apache-2.0 · read-only · no network · no model · no writes",
        row_title="Ledger · row 1",
        row_chip="JSON · 1 row",
        person="Zhang · Equipment · H1 2026",
        sec1="Arithmetic · LG-003",
        eq_labels=["Required", "Actual", "Gap"],
        tolerance="tolerance 0",
        scale="sample number axis 1–4",
        gap="gap 2 levels",
        sec2="Closure · LG-004…LG-007",
        closure=[("Action", "set", "ok"), ("Owner", "Li", "ok"),
                 ("Due", "06-30", "ok"), ("Done", "06-20", "ok"),
                 ("Status", "active", "warn")],
        skip_note="LG-004 threshold 0 · LG-007 values [] → skipped",
        issue="LG-001 × row 1: position and competency both empty",
        counts="issues 1 · warn 1 · skipped 2",
        notpass="empty issues ≠ a pass",
    ),
}


def render_hero(lang: str, skin: str) -> Image.Image:
    t = HERO[lang]
    s = SKIN[skin]
    img = gradient(1440, 576, s["bg_from"], s["bg_to"])
    img = glow(img, 1160, 120, 330, s["glow"], 24)
    img = glow(img, 120, 540, 260, s["glow"], 14)
    draw = ImageDraw.Draw(img)
    draw.line([(832, 60), (832, 520)], fill=mix(s["edge"], s["bg_from"], 0.45), width=1)

    img = card(img, (868, 60, 1376, 520), s, radius=22)
    draw = ImageDraw.Draw(img)

    # ---- left column -----------------------------------------------------
    pill(img, 64, 54, t["kicker"], 18, s["accent"], s["accent_soft"],
         "cjk_bold", pad=15, height=36)
    need(t["title1"], 88, "mono_bold", 776, "hero title line 1")
    need(t["title2"], 88, "mono_bold", 776, "hero title line 2")
    put(draw, 64, 168, t["title1"], 88, s["text"], "mono_bold", what="hero title 1")
    put(draw, 64, 262, t["title2"], 88, s["accent"], "mono_bold", what="hero title 2")

    for i, line in enumerate(t["value"]):
        need(line, 33, "cjk_bold", 776, f"hero value line {i + 1}")
        put(draw, 64, 340 + i * 48, line, 33, s["text"], "cjk_bold",
            what=f"hero value {i + 1}")
    need(t["sub"], 25, "cjk", 776, "hero sub")
    put(draw, 64, 438, t["sub"], 25, s["sub"], "cjk", what="hero sub")
    need(t["meta"], 20, "cjk", 776, "hero meta")
    put(draw, 64, 488, t["meta"], 20, s["faint"], "cjk", what="hero meta")
    need(t["foot"], 20, "cjk", 776, "hero footer")
    put(draw, 64, 540, t["foot"], 20, s["faint"], "cjk", what="hero footer")

    # ---- right card: header ---------------------------------------------
    put(draw, 890, 98, t["row_title"], 15, s["text"], "cjk_bold",
        what="hero row title")
    mini_chip(draw, 1354, 80, t["row_chip"], 11, s["accent"], s["accent_soft"],
              "cjk_bold", anchor="right", height=21)
    put(draw, 890, 122, t["person"], 12.5, s["faint"], "cjk",
        what="hero person")
    draw.line([(890, 136), (1354, 136)], fill=hx(s["grid"]), width=1)

    # ---- arithmetic block ------------------------------------------------
    put(draw, 890, 160, t["sec1"], 11.5, s["accent"], "cjk_bold",
        what="hero arithmetic label")

    eq_size = 46
    tokens = [("4", "num", "text"), (" − ", "op", "sub"),
              ("2", "num", "text"), (" = ", "op", "sub"),
              ("2", "num", "accent")]
    widths = [tw(tok, eq_size, "mono_bold") for tok, _, _ in tokens]
    total = sum(widths)
    x = 898.0
    num_centers: list[float] = []
    for (tok, role, col), width in zip(tokens, widths):
        if role == "num":
            num_centers.append(x + width / 2)
        draw.text((x, 238), tok, font=font(eq_size, "mono_bold"),
                  fill=hx(s[col]), anchor="ls")
        x += width
    eq_end = x
    label_colors = [s["sub"], s["sub"], s["mark"]]
    for cx, label, col in zip(num_centers, t["eq_labels"], label_colors):
        put(draw, cx, 186, label, 11.5, col, "cjk_bold", anchor="ms",
            what="hero equation label")
    check_dot(img, eq_end + 22, 222, 12, s)
    draw = ImageDraw.Draw(img)
    mini_chip(draw, 1354, 210, t["tolerance"], 11, s["sub"], s["band"],
              "cjk", anchor="right", height=22)

    # ---- level scale -----------------------------------------------------
    lx0, lx1 = 898.0, 1354.0
    gap = 8.0
    cell_w = (lx1 - lx0 - 3 * gap) / 4
    centers: list[float] = []
    for level in (1, 2, 3, 4):
        x0 = lx0 + (level - 1) * (cell_w + gap)
        x1 = x0 + cell_w
        centers.append((x0 + x1) / 2)
        if level == 4:
            fill, edge, fg = s["accent"], s["accent"], "#ffffff"
        elif level == 2:
            fill, edge, fg = s["accent_soft"], s["accent"], s["accent"]
        else:
            fill, edge, fg = s["band"], s["grid"], s["faint"]
        draw.rounded_rectangle([x0, 266, x1, 296], radius=10, fill=hx(fill),
                               outline=hx(edge), width=2)
        put(draw, (x0 + x1) / 2, 289, str(level), 11.5, fg, "mono_bold",
            anchor="ms", what="hero level tick")

    # the two-level span between actual 2 and required 4
    span_a, span_b = centers[1], centers[3]
    span_y = 303
    draw.line([(span_a, span_y), (span_b, span_y)], fill=hx(s["mark"]), width=2)
    for x_tip, direction in ((span_a, -1), (span_b, 1)):
        draw.polygon([(x_tip, span_y), (x_tip + direction * 7, span_y - 4),
                      (x_tip + direction * 7, span_y + 4)], fill=hx(s["mark"]))
    put(draw, 898, 316, t["scale"], 11, s["faint"], "cjk", what="hero scale")
    put(draw, (span_a + span_b) / 2, 316, t["gap"], 11, s["mark"], "cjk_bold",
        anchor="ms", what="hero gap label")
    draw.line([(890, 330), (1354, 330)], fill=hx(s["grid"]), width=1)

    # ---- closure strip ---------------------------------------------------
    put(draw, 890, 352, t["sec2"], 11.5, s["accent"], "cjk_bold",
        what="hero closure label")
    chip_gap = 6.0
    chip_w = (1354 - 898 - 4 * chip_gap) / 5
    for i, (label, value, tone) in enumerate(t["closure"]):
        x0 = 898 + i * (chip_w + chip_gap)
        x1 = x0 + chip_w
        if tone == "warn":
            fill, edge, value_color = s["mark_bg"], s["mark_edge"], s["mark"]
        else:
            fill, edge, value_color = s["ok_bg"], s["ok_edge"], s["ok"]
        draw.rounded_rectangle([x0, 366, x1, 412], radius=12, fill=hx(fill))
        if tone == "warn":
            dashed_rect(draw, (x0, 366, x1, 412), s["mark_edge"], width=2)
        else:
            draw.rounded_rectangle([x0, 366, x1, 412], radius=12,
                                   outline=hx(edge), width=2)
        put(draw, x0 + chip_w / 2, 385, label, 11, s["sub"], "cjk_bold",
            anchor="ms", what="hero closure field")
        put(draw, x0 + chip_w / 2, 404, value, 12.5, value_color, "cjk_bold",
            anchor="ms", what="hero closure value")

    put(draw, 890, 432, t["skip_note"], 11, s["mark"], "cjk",
        max_w=464, what="hero skipped note")
    draw.line([(890, 444), (1354, 444)], fill=hx(s["grid"]), width=1)

    # ---- finding + counts ------------------------------------------------
    put(draw, 890, 466, t["issue"], 11.5, s["mark"], "cjk",
        max_w=464, what="hero issue")
    put(draw, 890, 490, t["counts"], 11.5, s["sub"], "cjk",
        max_w=300, what="hero counts")
    put(draw, 1354, 490, t["notpass"], 11, s["mark"], "cjk_bold", anchor="rs",
        what="hero not-a-pass")

    return img


# ---------------------------------------------------------------------------
# Flow SVG — 1100 x 660. A two-lane loop with six checkpoints, two exits.
# ---------------------------------------------------------------------------
FLOW = dict(
    title="dsh-learning-gap-check",
    subtitle="结构图 · 一份能力台账的一次核对",
    kicker="台账 → 别名归一 → 七条规则逐行核对 → issues[] / skipped[] → buildView()",
    rules="rules/learning-gap-check.yaml · v2026.1 · 7 条",
    counts="error 0 · warn 1 · info 0 · 空 issues ≠ 通过",
    input_title="台账",
    input_chip="JSON · YAML",
    input_person="张工 · 设备部",
    input_meta="2026 上半年 · 1 行",
    input_rows=[("岗位", "（空）", "warn"), ("能力项", "（空）", "warn"),
                ("要求等级", "4", "plain"), ("现有等级", "2", "plain"),
                ("差距等级", "2", "plain"), ("培养措施", "已填", "plain"),
                ("责任人", "李主管", "plain"), ("完成期限", "06-30", "plain"),
                ("完成日期", "06-20", "plain"), ("状态", "进行中", "plain")],
    input_notes=[("列名中英文都认", "faint"), ("忽略大小写 / 空格 / _ / -", "faint"),
                 ("缺 rows → MaterialError", "mark"),
                 ("缺某一列 → 逐条 skipped", "mark"),
                 ("文件或内联 · 只读", "faint")],
    loop_caption="七条规则 · 逐行独立核对",
    loop_sub="轨道 = 台账记录的培养闭环，不是执行顺序",
    loop_note="每条规则各读一处；跑不了就进 skipped",
    issues_title="issues[]",
    issues_chip="1 条",
    issues_rows=[("LG-001 · 第 1 行", "warn"),
                 ("position、competency 都为空", "text"),
                 ("expected：至少填写一项", "faint"),
                 ("kind：derived-from-principle", "faint")],
    issues_counts="1 warn · 0 error · 0 info",
    issues_note="空 issues ≠ 通过",
    skipped_title="skipped[]",
    skipped_chip="2 条",
    skipped_rows=[("LG-004 · threshold 0 未配置", "mark"),
                  ("LG-007 · values [] 未配置", "mark")],
    skipped_note="未执行 ≠ 通过",
    skipped_sub="每条都写明原因",
    review_title="人工复核",
    review_sub="不判胜任 · 不判措施有效",
    build_title="buildView()",
    build_sub="markdown · reportJson",
    build_summary="summary{error 0 · warn 1 · info 0}",
    build_counts="issueCount 1 · skippedCount 2",
    build_note="reportJson 保留 locator / basis / fix",
    build_notpass="空 issues ≠ 通过",
    footer_left="只读材料 · 不联网 · 不调用模型 · 不写文件",
    footer_right="规则包即数据：rules/learning-gap-check.yaml · 7 条 · Apache-2.0",
)

STATIONS = [
    # x, y, rule id, title, detail, state; the cards sit on the loop's two lanes
    (272, 118, "LG-001 · LG-002", "字段与等级", "岗位/能力项空 × · 2 √", "warn"),
    (448, 118, "LG-003", "差距算术", "4 − 2 = 2 √ · 容差 0", "ok"),
    (624, 118, "LG-004", "阈值触发", "threshold 0 未配置", "skip"),
    (624, 492, "LG-005", "措施 · 人 · 期限", "owner · dueAt 已填 √", "ok"),
    (448, 492, "LG-006", "日期先后", "06-20 ≤ 06-30 √", "ok"),
    (272, 492, "LG-007", "状态词表", "values [] → skipped", "skip"),
]

CJK_FONT = ("'Microsoft YaHei','PingFang SC','Noto Sans CJK SC',"
            "'Source Han Sans SC',sans-serif")
MONO_FONT = "'Consolas','SFMono-Regular','Menlo',ui-monospace,monospace"


class Figure:
    def __init__(self, skin: str):
        self.s = SKIN[skin]
        self.parts: list[str] = []

    def add(self, line: str) -> None:
        self.parts.append(line)

    def text(self, x: float, y: float, body: str, size: float, color: str,
             *, kind: str = "cjk", weight: int = 400, anchor: str = "start",
             max_w: float | None = None, what: str = "text",
             spacing: float | None = None, opacity: float | None = None) -> None:
        if max_w is not None:
            width = tw(body, size, kind)
            if width > max_w + 0.5:
                raise SystemExit(f"FATAL: {what} overflows: {body!r} needs "
                                 f"{width:.1f}px > {max_w:.0f}px")
        family = MONO_FONT if kind.startswith("mono") else CJK_FONT
        attrs = [f'x="{x:.1f}"', f'y="{y:.1f}"', f'fill="{color}"',
                 f'font-family="{family}"', f'font-size="{size:g}"']
        if weight != 400:
            attrs.append(f'font-weight="{weight}"')
        if anchor != "start":
            attrs.append(f'text-anchor="{anchor}"')
        if spacing is not None:
            attrs.append(f'letter-spacing="{spacing:g}"')
        if opacity is not None:
            attrs.append(f'opacity="{opacity:g}"')
        self.add(f'<text {" ".join(attrs)}>{escape(body)}</text>')

    def rect(self, x: float, y: float, w: float, h: float, r: float,
             fill: str, stroke: str | None = None, sw: float = 1,
             *, shadow: bool = False, dash: str | None = None,
             opacity: float | None = None) -> None:
        attrs = [f'x="{x:.1f}"', f'y="{y:.1f}"', f'width="{w:.1f}"',
                 f'height="{h:.1f}"', f'rx="{r:.1f}"', f'fill="{fill}"']
        if stroke is not None:
            attrs += [f'stroke="{stroke}"', f'stroke-width="{sw:g}"']
        if dash is not None:
            attrs.append(f'stroke-dasharray="{dash}"')
        if shadow:
            attrs.append('filter="url(#soft)"')
        if opacity is not None:
            attrs.append(f'opacity="{opacity:g}"')
        self.add(f'<rect {" ".join(attrs)}/>')

    def line(self, x1: float, y1: float, x2: float, y2: float, color: str,
             width: float = 1, *, dash: str | None = None,
             marker: bool = False, opacity: float | None = None) -> None:
        attrs = [f'x1="{x1:.1f}"', f'y1="{y1:.1f}"', f'x2="{x2:.1f}"',
                 f'y2="{y2:.1f}"', f'stroke="{color}"',
                 f'stroke-width="{width:g}"', 'stroke-linecap="round"']
        if dash is not None:
            attrs.append(f'stroke-dasharray="{dash}"')
        if marker:
            attrs.append('marker-end="url(#arr)"')
        if opacity is not None:
            attrs.append(f'opacity="{opacity:g}"')
        self.add(f'<line {" ".join(attrs)}/>')

    def path(self, d: str, color: str, width: float = 2,
             *, fill: str = "none", marker: bool = False,
             opacity: float | None = None) -> None:
        attrs = [f'd="{d}"', f'fill="{fill}"', f'stroke="{color}"',
                 f'stroke-width="{width:g}"', 'stroke-linecap="round"',
                 'stroke-linejoin="round"']
        if marker:
            attrs.append('marker-end="url(#arr)"')
        if opacity is not None:
            attrs.append(f'opacity="{opacity:g}"')
        self.add(f'<path {" ".join(attrs)}/>')

    def chip(self, x: float, y: float, body: str, size: float, fg: str,
             bg: str, *, kind: str = "mono_bold", pad: float = 8,
             height: float = 20, anchor: str = "left") -> float:
        w = tw(body, size, kind) + pad * 2
        x0 = x - w if anchor == "right" else x
        self.rect(x0, y, w, height, height / 2, bg)
        self.text(x0 + pad, y + height / 2 + size * 0.36, body, size, fg,
                  kind=kind, weight=700)
        return w

    def render(self) -> str:
        return "\n".join(self.parts) + "\n"


def station_card(fig: Figure, x: int, y: int, rule: str, title: str,
                 detail: str, state: str) -> None:
    s = fig.s
    w, h = 160, 58
    fill = s["band"] if state == "skip" else s["card"]
    edge = s["mark_edge"] if state == "warn" else (
        s["grid"] if state == "skip" else s["edge"])
    fig.rect(x, y, w, h, 18, fill, edge, 1.5, shadow=True,
             dash="5 4" if state == "skip" else None)
    if state == "warn":
        fig.rect(x, y + 10, 3, h - 20, 1.5, s["mark"])
    id_color = s["faint"] if state == "skip" else s["accent"]
    fig.text(x + 14, y + 18, rule, 11, id_color, kind="mono_bold",
             weight=700, max_w=132, what=f"station id {rule}")
    mark = {"ok": ("√", s["ok"]), "warn": ("×", s["mark"]),
            "skip": ("–", s["faint"])}[state]
    fig.text(x + 146, y + 19, mark[0], 14, mark[1], weight=700, anchor="end")
    fig.text(x + 14, y + 37, title, 13, s["text"], kind="cjk", weight=700,
             max_w=132, what=f"station title {rule}")
    detail_color = {"ok": s["ok"], "warn": s["mark"], "skip": s["mark"]}[state]
    fig.text(x + 14, y + 54, detail, 11, detail_color, kind="cjk",
             max_w=132, what=f"station detail {rule}")


def render_flow(skin: str) -> str:
    s = SKIN[skin]
    f = Figure(skin)
    f.add(f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="660" '
          f'viewBox="0 0 1100 660" role="img" aria-label="{NAME} 结构图：'
          f'台账经别名归一进入双车道闭环，环上六个检位分别核对字段与等级、'
          f'差距算术、阈值触发、措施责任人期限、日期先后、状态词表；'
          f'两条结果通道 issues[] 与 skipped[] 汇入 buildView()，结论交人工复核">')
    f.add(f'<title>{NAME} — 双车道闭环结构图</title>')
    f.add('<defs>')
    f.add(f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
          f'<stop offset="0" stop-color="{s["bg_from"]}"/>'
          f'<stop offset="1" stop-color="{s["bg_to"]}"/></linearGradient>')
    f.add('<filter id="soft" x="-20%" y="-20%" width="140%" height="150%">'
          '<feDropShadow dx="0" dy="6" stdDeviation="9" flood-color="#3a2c66" '
          'flood-opacity="0.10"/></filter>')
    f.add(f'<marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" '
          f'markerWidth="6" markerHeight="6" orient="auto">'
          f'<path d="M1 1 L9 5 L1 9 z" fill="{s["accent"]}"/></marker>')
    f.add(f'<radialGradient id="glow" cx="50%" cy="50%" r="50%">'
          f'<stop offset="0" stop-color="{s["glow"]}" stop-opacity="0.14"/>'
          f'<stop offset="1" stop-color="{s["glow"]}" stop-opacity="0"/>'
          f'</radialGradient>')
    f.add('</defs>')
    f.add(f'<rect width="1100" height="660" rx="22" fill="url(#bg)"/>')
    f.add('<ellipse cx="980" cy="110" rx="330" ry="240" fill="url(#glow)"/>')
    f.add('<ellipse cx="120" cy="600" rx="260" ry="200" fill="url(#glow)"/>')

    # ---- header ----------------------------------------------------------
    f.text(44, 54, FLOW["title"], 24, s["text"], kind="mono_bold",
           weight=700, max_w=290, what="flow title")
    f.text(380, 52, FLOW["subtitle"], 15, s["text"], weight=700,
           max_w=300, what="flow subtitle")
    f.text(1056, 48, FLOW["rules"], 11, s["sub"], kind="cjk", anchor="end",
           max_w=380, what="flow rules")
    f.text(1056, 68, FLOW["counts"], 11, s["faint"], kind="cjk", anchor="end",
           max_w=380, what="flow counts")
    f.text(44, 74, FLOW["kicker"], 11.5, s["faint"], kind="cjk",
           max_w=640, what="flow kicker")
    f.line(44, 88, 1056, 88, s["grid"], 1)

    # ---- input card ------------------------------------------------------
    f.rect(44, 104, 206, 436, 18, s["card"], s["edge"], 1.5, shadow=True)
    f.rect(60, 118, 3, 14, 1.5, s["accent"])
    f.text(72, 130, FLOW["input_title"], 13, s["text"], weight=700)
    f.chip(234, 116, FLOW["input_chip"], 11, s["accent"], s["accent_soft"],
           anchor="right", height=20)
    f.text(60, 154, FLOW["input_person"], 11.5, s["sub"], max_w=174,
           what="input person")
    f.text(60, 173, FLOW["input_meta"], 11, s["faint"], max_w=174,
           what="input meta")
    f.line(60, 187, 234, 187, s["grid"], 1)
    for index, (key, value, tone) in enumerate(FLOW["input_rows"]):
        y = 208 + index * 21
        f.text(60, y, key, 11, s["sub"], max_w=80, what=f"input key {key}")
        color = s["mark"] if tone == "warn" else (
            s["faint"] if value == "（空）" else s["text"])
        f.text(150, y, value, 11, color, kind="mono" if value.isascii() else "cjk",
               max_w=84, what=f"input value {key}")
    for index, (note, tone) in enumerate(FLOW["input_notes"]):
        f.text(60, 448 + index * 18, note, 11,
               s["mark"] if tone == "mark" else s["faint"], kind="cjk",
               max_w=174, what=f"input note {index}")

    # ---- stations first, then the lane they sit on ------------------------
    for x, y, rule, title, detail, state in STATIONS:
        station_card(f, x, y, rule, title, detail, state)

    # ---- loop track ------------------------------------------------------
    # The stations are drawn above / below the lane, then the lane is painted
    # over their inner edge, so the loop reads as one continuous line.
    f.rect(272, 176, 520, 318, 52, "none", s["accent"], 2.4, opacity=0.6)
    # short arrow segments sit in the gaps between station cards
    f.line(433, 176, 447, 176, s["accent"], 2, marker=True)
    f.line(609, 176, 623, 176, s["accent"], 2, marker=True)
    f.line(792, 315, 792, 335, s["accent"], 2, marker=True)
    f.line(623, 494, 609, 494, s["accent"], 2, marker=True)
    f.line(447, 494, 433, 494, s["accent"], 2, marker=True)
    f.line(272, 438, 272, 418, s["accent"], 2, marker=True)
    # input hand-off and the return label
    f.line(250, 340, 271, 340, s["accent"], 2, marker=True)
    f.text(278, 326, "输入", 11, s["accent"], kind="cjk", weight=700)
    f.text(280, 462, "下一周期", 11, s["faint"], kind="cjk")

    # ---- centre ----------------------------------------------------------
    f.text(532, 224, FLOW["loop_caption"], 12, s["accent"], kind="cjk",
           weight=700, anchor="middle", max_w=400, what="loop caption")
    eq_size = 40
    eq_gap = 12
    tokens = [("4", "num", s["text"]), ("−", "op", s["sub"]),
              ("2", "num", s["text"]), ("=", "op", s["sub"]),
              ("2", "num", s["accent"])]
    widths = [tw(tok, eq_size, "mono_bold") for tok, _, _ in tokens]
    total = sum(widths) + eq_gap * (len(tokens) - 1)
    x = 532 - total / 2
    num_centers: list[float] = []
    for (tok, role, color), width in zip(tokens, widths):
        if role == "num":
            num_centers.append(x + width / 2)
        f.text(x, 312, tok, eq_size, color, kind="mono_bold", weight=700)
        x += width + eq_gap
    for cx, label, color in zip(num_centers, ["要求", "现有", "差距"],
                                [s["sub"], s["sub"], s["mark"]]):
        f.text(cx, 268, label, 11.5, color, kind="cjk", weight=700,
               anchor="middle", what="equation label")
    f.text(532, 344, "差距 = 要求 − 现有 · 容差 0", 11.5, s["sub"], kind="cjk",
           anchor="middle", max_w=420, what="equation caption")
    f.text(532, 368, FLOW["loop_sub"], 11, s["faint"], kind="cjk",
           anchor="middle", max_w=420, what="loop sub")
    # two small evidence chips in the loop centre
    chip_y = 392
    chip_specs = [("warn 1", s["mark"], s["mark_bg"]),
                  ("skipped 2", s["sub"], s["band"]),
                  ("error 0", s["faint"], s["band"])]
    chip_widths = [tw(body, 11, "mono_bold") + 20 for body, _, _ in chip_specs]
    chip_x = 532 - (sum(chip_widths) + 12) / 2
    for (body, fg, bg), cw in zip(chip_specs, chip_widths):
        f.chip(chip_x, chip_y, body, 11, fg, bg, height=20)
        chip_x += cw + 6
    f.text(532, 438, FLOW["loop_note"], 11, s["faint"], kind="cjk",
           anchor="middle", max_w=420, what="loop note")

    # ---- output channels -------------------------------------------------
    # collector rail from the loop's right edge into both channels
    f.line(792, 335, 807, 335, s["accent"], 1.4, dash="3 4")
    f.line(807, 198, 807, 380, s["accent"], 1.4, dash="3 4")
    f.line(807, 198, 819, 198, s["accent"], 1.4, marker=True)
    f.line(807, 380, 819, 380, s["accent"], 1.4, marker=True)

    # issues
    f.rect(820, 104, 236, 188, 18, s["card"], s["edge"], 1.5, shadow=True)
    f.text(836, 128, FLOW["issues_title"], 14, s["accent"], kind="mono_bold",
           weight=700)
    f.chip(1040, 116, FLOW["issues_chip"], 11, s["accent"], s["accent_soft"],
           anchor="right", height=20)
    f.line(836, 142, 1040, 142, s["grid"], 1)
    for index, (body, tone) in enumerate(FLOW["issues_rows"]):
        color = {"warn": s["mark"], "text": s["text"],
                 "faint": s["faint"]}[tone]
        f.text(836, 164 + index * 20, body, 11,
               color, kind="mono" if index in (2, 3) else "cjk",
               max_w=188, what=f"issues row {index}")
    f.line(836, 240, 1040, 240, s["grid"], 1)
    f.text(836, 260, FLOW["issues_counts"], 11, s["sub"], kind="cjk",
           max_w=188, what="issues counts")
    f.text(836, 278, FLOW["issues_note"], 11, s["mark"], kind="cjk",
           weight=700, max_w=188, what="issues note")

    # skipped
    f.rect(820, 308, 236, 144, 18, s["card"], s["edge"], 1.5, shadow=True)
    f.text(836, 332, FLOW["skipped_title"], 14, s["sub"], kind="mono_bold",
           weight=700)
    f.chip(1040, 320, FLOW["skipped_chip"], 11, s["sub"], s["band"],
           anchor="right", height=20)
    f.line(836, 346, 1040, 346, s["grid"], 1)
    for index, (body, _tone) in enumerate(FLOW["skipped_rows"]):
        f.text(836, 368 + index * 22, body, 11, s["mark"], kind="cjk",
               max_w=188, what=f"skipped row {index}")
    f.text(836, 416, FLOW["skipped_note"], 11, s["mark"], kind="cjk",
           weight=700, max_w=188, what="skipped note")
    f.text(836, 436, FLOW["skipped_sub"], 11, s["faint"], kind="cjk",
           max_w=188, what="skipped sub")

    # human review
    f.rect(820, 468, 236, 72, 18, s["card"], s["edge"], 1.5, shadow=True)
    f.rect(836, 482, 3, 14, 1.5, s["ok"])
    f.text(848, 494, FLOW["review_title"], 12, s["text"], weight=700)
    f.text(836, 516, FLOW["review_sub"], 11, s["faint"], kind="cjk",
           max_w=204, what="review sub")

    # ---- buildView bar ---------------------------------------------------
    f.rect(44, 556, 1012, 58, 18, s["band"], s["grid"], 1.2)
    f.text(60, 580, FLOW["build_title"], 14, s["accent"], kind="mono_bold",
           weight=700)
    f.text(60, 600, FLOW["build_sub"], 11, s["sub"], kind="mono")
    f.line(300, 570, 300, 600, s["grid"], 1)
    f.text(318, 580, FLOW["build_summary"], 11, s["sub"], kind="cjk",
           max_w=300, what="build summary")
    f.text(318, 600, FLOW["build_note"], 11, s["faint"], kind="cjk",
           max_w=300, what="build note")
    f.text(636, 580, FLOW["build_counts"], 11, s["sub"], kind="cjk",
           max_w=300, what="build counts")
    f.text(636, 600, "报告只列差异 · 结论留给审核人", 11, s["faint"],
           kind="cjk", max_w=300, what="build human note")
    f.chip(1040, 576, FLOW["build_notpass"], 11, s["mark"], s["mark_bg"],
           anchor="right", height=22)

    # ---- footer ----------------------------------------------------------
    f.text(44, 640, FLOW["footer_left"], 11, s["faint"], kind="cjk",
           max_w=460, what="footer left")
    f.text(1056, 640, FLOW["footer_right"], 11, s["faint"], kind="cjk",
           anchor="end", max_w=520, what="footer right")

    f.add('</svg>')
    return f.render()


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode not in ("all", "hero", "flow"):
        raise SystemExit("usage: gen-readme-assets.py [all|hero|flow]")
    OUT.mkdir(parents=True, exist_ok=True)

    if mode in ("all", "hero"):
        for lang in ("zh", "en"):
            for skin in ("light", "dark"):
                img = render_hero(lang, skin)
                path = OUT / f"{NAME}-hero-{lang}-{skin}.webp"
                img.save(path, "WEBP", quality=92, method=6)
                print(f"wrote {path.relative_to(ROOT)}")

    if mode in ("all", "flow"):
        for skin in ("light", "dark"):
            svg = render_flow(skin)
            ElementTree.fromstring(svg.encode("utf-8"))  # well-formedness gate
            path = OUT / f"{NAME}-flow-v5-{skin}.svg"
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(svg)
            print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

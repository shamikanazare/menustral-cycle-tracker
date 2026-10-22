import os
import math
from PIL import Image, ImageDraw, ImageFont

# A4 Dimensions at 200 DPI (crisp and high resolution, perfect for print & screen)
WIDTH = 1654
HEIGHT = 2339

img = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# Helper function to create vertical/linear gradients
def create_linear_gradient(width, height, start_color, end_color):
    base = Image.new("RGBA", (width, height), start_color)
    top = Image.new("RGBA", (width, height), end_color)
    mask = Image.new("L", (width, height))
    mask_data = []
    for y in range(height):
        alpha = int(255 * (y / height))
        mask_data.extend([alpha] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

# Background: subtle luxury soft pink/lavender gradient
bg = create_linear_gradient(WIDTH, HEIGHT, (255, 240, 248, 255), (245, 235, 255, 255))
img.paste(bg, (0, 0))

# Decorative ambient circles
def draw_glow_circle(im, center, radius, color):
    overlay = Image.new("RGBA", (radius * 2, radius * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -2):
        alpha = int(color[3] * (1 - (r / radius) ** 1.5))
        d.ellipse([radius - r, radius - r, radius + r, radius + r], fill=(color[0], color[1], color[2], alpha))
    im.paste(overlay, (center[0] - radius, center[1] - radius), overlay)

draw_glow_circle(img, (WIDTH - 100, 100), 450, (255, 180, 215, 60))
draw_glow_circle(img, (150, HEIGHT - 200), 500, (216, 180, 254, 55))
draw_glow_circle(img, (WIDTH // 2, HEIGHT // 2), 400, (255, 220, 240, 40))

# Load fonts
def get_font(name, size):
    fonts_dir = "C:\\Windows\\Fonts"
    path = os.path.join(fonts_dir, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

font_title = get_font("segoeuib.ttf", 46)
font_subtitle = get_font("segoeui.ttf", 22)
font_h1 = get_font("segoeuib.ttf", 26)
font_h2 = get_font("segoeuib.ttf", 21)
font_bold = get_font("segoeuib.ttf", 17)
font_body = get_font("segoeui.ttf", 16)
font_small = get_font("segoeui.ttf", 14)
font_mono = get_font("consola.ttf", 15)
font_mono_bold = get_font("consolab.ttf", 16)
font_big_num = get_font("segoeuib.ttf", 36)

# Colors
C_TEXT_DARK = (46, 21, 40, 255)
C_TEXT_MUTED = (130, 92, 118, 255)
C_ROSE_DEEP = (184, 43, 107, 255)
C_PURPLE = (126, 34, 206, 255)
C_BORDER = (245, 215, 233, 255)
C_CARD_BG = (255, 255, 255, 235)

def draw_rounded_card(im, xy, fill_color, border_color, radius=18, border_width=2):
    x1, y1, x2, y2 = xy
    card = Image.new("RGBA", (x2 - x1, y2 - y1), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, x2 - x1 - 1, y2 - y1 - 1], radius=radius, fill=fill_color, outline=border_color, width=border_width)
    im.paste(card, (x1, y1), card)

# ================= 1. HEADER =================
draw_rounded_card(img, [50, 50, WIDTH - 50, 210], (255, 255, 255, 245), (248, 195, 222, 255), radius=22, border_width=3)

# Logo Icon Box
icon_box = Image.new("RGBA", (110, 110), (0, 0, 0, 0))
ib_draw = ImageDraw.Draw(icon_box)
ib_draw.rounded_rectangle([0, 0, 109, 109], radius=24, fill=(236, 72, 153, 255))
img.paste(icon_box, (80, 75), icon_box)

# Logo letter / flower inside icon box
draw.text((108, 92), "🌸", font=get_font("seguiemj.ttf", 52) if os.path.exists("C:\\Windows\\Fonts\\seguiemj.ttf") else font_title, fill=(255, 255, 255, 255))

# Header Titles
draw.text((215, 76), "SAKHI: Menstrual Cycle & Fertility Planner", font=font_title, fill=(92, 35, 75, 255))
draw.text((215, 134), "Algorithm-Driven Cycle Tracking, Ovulation Forecasting & Conception Mode for Married Women", font=font_subtitle, fill=C_ROSE_DEEP)
draw.text((215, 168), "Pure Client-Side Biomedical Data Intelligence · 100% Privacy Preserving", font=font_small, fill=C_TEXT_MUTED)

# Header Tag Badges on Right
def draw_badge(im, xy, text, bg_col, text_col):
    bx1, by1, bx2, by2 = xy
    b = Image.new("RGBA", (bx2 - bx1, by2 - by1), (0, 0, 0, 0))
    bd = ImageDraw.Draw(b)
    bd.rounded_rectangle([0, 0, bx2 - bx1 - 1, by2 - by1 - 1], radius=14, fill=bg_col)
    im.paste(b, (bx1, by1), b)
    bbox = bd.textbbox((0, 0), text, font=font_small)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((bx1 + (bx2 - bx1 - tw) // 2, by1 + (by2 - by1 - th) // 2 - 2), text, font=font_small, fill=text_col)

draw_badge(img, [WIDTH - 300, 80, WIDTH - 80, 120], "AOA UNIVERSITY PROJECT", (255, 224, 240, 255), (168, 39, 101, 255))
draw_badge(img, [WIDTH - 300, 135, WIDTH - 80, 175], "SEMESTER V · 2026", (243, 232, 255, 255), (107, 33, 168, 255))

# ================= 2. AUTHORS & METADATA BAR =================
draw_rounded_card(img, [50, 226, WIDTH - 50, 276], (255, 255, 255, 240), C_BORDER, radius=12, border_width=1)
draw.text((80, 239), "Project Authors: Shamika Nazare & Kadam Madhushree", font=font_bold, fill=(142, 43, 92, 255))
draw.text((WIDTH // 2 - 80, 239), "Course: Analysis of Algorithms (AOA)", font=font_bold, fill=(92, 35, 75, 255))
draw.text((WIDTH - 420, 239), "Architecture: HTML5 · CSS3 · Vanilla ES6", font=font_bold, fill=C_PURPLE)

# Layout: 2 Columns
COL_W = 745
COL1_X = 50
COL2_X = 855

# ================= LEFT COLUMN =================
curr_y = 295

# CARD 1: CLINICAL MOTIVATION & PROBLEM
draw_rounded_card(img, [COL1_X, curr_y, COL1_X + COL_W, curr_y + 240], C_CARD_BG, C_BORDER)
draw.text((COL1_X + 25, curr_y + 18), "🎯 Problem Statement & Clinical Motivation", font=font_h1, fill=(112, 38, 82, 255))
draw.line([COL1_X + 25, curr_y + 55, COL1_X + COL_W - 25, curr_y + 55], fill=(245, 220, 235, 255), width=1)

text_p1 = (
    "• Menstrual cycles naturally vary due to stress, physiological shifts, and conditions such as PCOD / PCOS.\n"
    "• For married couples trying to conceive, timing is vital: human oocytes remain viable for only 12–24 hours,\n"
    "  while sperm survives up to 5 days in fertile cervical mucus, defining a strict 6-day fertile stage.\n"
    "• Most commercial apps upload deeply personal reproductive telemetry to external cloud servers.\n"
    "• Sakhi provides an algorithm-powered client-side architecture delivering predictive accuracy with 100% privacy."
)
draw.text((COL1_X + 25, curr_y + 70), text_p1, font=font_body, fill=C_TEXT_DARK, spacing=8)
curr_y += 256

# CARD 2: ALGORITHMIC ARCHITECTURE (AOA CORE)
draw_rounded_card(img, [COL1_X, curr_y, COL1_X + COL_W, curr_y + 560], (255, 252, 255, 245), (233, 195, 247, 255), border_width=2)
draw.text((COL1_X + 25, curr_y + 18), "⚡ Core Algorithmic Architecture (AOA)", font=font_h1, fill=(126, 34, 206, 255))
draw.line([COL1_X + 25, curr_y + 55, COL1_X + COL_W - 25, curr_y + 55], fill=(245, 220, 235, 255), width=1)

# Algorithm Grid (2x2)
algos = [
    ("Merge Sort", "O(n log n)", "Divide-and-conquer sorting over chronological period intervals. Calculates Min, Median, and Maximum cycle distributions efficiently."),
    ("KMP String Search", "O(n + m)", "Precomputes Longest Prefix Suffix (LPS) table to resolve health inquiries in Health Assistant with zero redundant backtrack comparisons."),
    ("Moving Average", "O(n)", "Sliding window model (k = 3 intervals) adjusting cycle forecasts dynamically against physiological variations without server lag."),
    ("Binary Search", "O(log n)", "Logarithmic queries over sorted cycle duration frequencies to pinpoint statistical pattern shifts compared to O(n) linear scanning.")
]

for idx, (a_name, a_cpx, a_desc) in enumerate(algos):
    ax = COL1_X + 25 + (idx % 2) * (COL_W // 2 - 15)
    ay = curr_y + 70 + (idx // 2) * 155
    aw = (COL_W // 2 - 30)
    ah = 140
    draw_rounded_card(img, [ax, ay, ax + aw, ay + ah], (255, 255, 255, 255), (245, 220, 235, 255), radius=12, border_width=1)
    draw.text((ax + 14, ay + 12), a_name, font=font_h2, fill=(92, 32, 69, 255))
    
    # Complexity badge
    draw_badge(img, [ax + aw - 110, ay + 12, ax + aw - 12, ay + 38], a_cpx, (253, 242, 248, 255), C_ROSE_DEEP)
    
    # Description lines
    words = a_desc.split(" ")
    lines = []
    cur_line = []
    for w in words:
        if len(" ".join(cur_line + [w])) > 32:
            lines.append(" ".join(cur_line))
            cur_line = [w]
        else:
            cur_line.append(w)
    if cur_line:
        lines.append(" ".join(cur_line))
    draw.text((ax + 14, ay + 50), "\n".join(lines), font=font_small, fill=C_TEXT_MUTED, spacing=4)

# Benchmark Race Box
ry = curr_y + 400
rw = COL_W - 50
rx = COL1_X + 25
draw_rounded_card(img, [rx, ry, rx + rw, ry + 130], (253, 247, 255, 255), (244, 184, 215, 255), radius=14, border_width=2)
draw.text((rx + 20, ry + 12), "Empirical Sorting Race Benchmark (3,000 iterations over recorded cycle lengths):", font=font_bold, fill=(112, 38, 82, 255))

# Race comparison split
draw.text((rx + 45, ry + 48), "Bubble Sort [O(n²)]", font=font_body, fill=(197, 48, 48, 255))
draw.text((rx + 45, ry + 75), "184.2 ms (Slow, redundant swaps)", font=font_mono_bold, fill=(197, 48, 48, 255))

draw.text((rx + rw // 2 - 25, ry + 60), "VS", font=font_h1, fill=(192, 123, 160, 255))

draw_rounded_card(img, [rx + rw // 2 + 30, ry + 40, rx + rw - 20, ry + 115], (230, 249, 240, 255), (154, 230, 180, 255), radius=10, border_width=1)
draw.text((rx + rw // 2 + 45, ry + 48), "Merge Sort [O(n log n)] ⚡", font=font_bold, fill=(39, 103, 73, 255))
draw.text((rx + rw // 2 + 45, ry + 75), "26.8 ms  (6.8x Faster Execution)", font=font_mono_bold, fill=(39, 103, 73, 255))
curr_y += 576

# CARD 3: CLIENT-SIDE SECURITY & INTEGRITY
draw_rounded_card(img, [COL1_X, curr_y, COL1_X + COL_W, curr_y + 220], C_CARD_BG, C_BORDER)
draw.text((COL1_X + 25, curr_y + 18), "🔒 Biomedical Privacy & Client-Side Execution", font=font_h1, fill=(112, 38, 82, 255))
draw.line([COL1_X + 25, curr_y + 55, COL1_X + COL_W - 25, curr_y + 55], fill=(245, 220, 235, 255), width=1)

text_p3 = (
    "• Zero Cloud Vulnerability: Period dates, symptoms, intimacy logs, and BBT data are stored\n"
    "  strictly in browser-native LocalStorage with encrypted object serialization.\n"
    "• Autonomous Client Runtime: Prediction engines and KMP matching run with zero API delays.\n"
    "• Total User Autonomy: Granular data purging controls allow clearing history or complete factory resets."
)
draw.text((COL1_X + 25, curr_y + 72), text_p3, font=font_body, fill=C_TEXT_DARK, spacing=7)


# ================= RIGHT COLUMN =================
curr_y = 295

# CARD 4: CONCEPTION & MARRIED WOMEN SPECIALIZED MODE
draw_rounded_card(img, [COL2_X, curr_y, COL2_X + COL_W, curr_y + 550], (255, 252, 255, 245), (220, 181, 245, 255), border_width=2)
draw.text((COL2_X + 25, curr_y + 18), "👶 Conception & Married Women Mode (TTC)", font=font_h1, fill=C_PURPLE)
draw_badge(img, [COL2_X + COL_W - 170, curr_y + 16, COL2_X + COL_W - 25, curr_y + 46], "SPECIALIZED MODE", (243, 232, 255, 255), (126, 34, 206, 255))
draw.line([COL2_X + 25, curr_y + 55, COL2_X + COL_W - 25, curr_y + 55], fill=(245, 220, 235, 255), width=1)

draw.text((COL2_X + 25, curr_y + 68), "Daily Conception Probability Model (Calculated from Ovulation Offset):", font=font_bold, fill=(92, 35, 75, 255))

# 4 Conception Meters
meters = [
    ("Peak (33%)", "Ovulation Day", (245, 230, 255, 255), (201, 136, 239, 255), (107, 33, 168, 255)),
    ("Very High (31%)", "1 Day Prior", (255, 230, 242, 255), (249, 168, 204, 255), (168, 39, 101, 255)),
    ("High (27%)", "2 Days Prior", (255, 242, 250, 255), (247, 210, 233, 255), (142, 43, 92, 255)),
    ("Low (< 2%)", "Non-Fertile", (248, 249, 250, 255), (226, 232, 240, 255), (100, 116, 139, 255)),
]

mw = (COL_W - 50 - 30) // 4
for midx, (m_val, m_lbl, m_bg, m_border, m_txt) in enumerate(meters):
    mx = COL2_X + 25 + midx * (mw + 10)
    my = curr_y + 98
    draw_rounded_card(img, [mx, my, mx + mw, my + 78], m_bg, m_border, radius=12, border_width=2)
    draw.text((mx + 12, my + 14), m_val, font=font_bold, fill=m_txt)
    draw.text((mx + 12, my + 44), m_lbl, font=font_small, fill=m_txt)

# TTC Core Features Grid
ttc_feats = [
    ("🌸 6-Day Fertile Window", "Calculates exact start and end dates based on sperm survival (up to 5 days) and egg release viability."),
    ("🍼 Estimated Due Date Calculator", "Uses Naegele's rule (Ovulation + 266 days) to predict estimated delivery date if pregnancy occurs this cycle."),
    ("🌡️ Basal Body Temp & Cervical Fluid", "Calendar logging for egg-white slippery fluid and post-ovulatory sustained 0.5°F thermal shift."),
    ("👶 Intercourse / Conceive Logging", "Interactive calendar markers displaying baby icons on dates with logged intimacy during fertile days.")
]

for fidx, (f_title, f_desc) in enumerate(ttc_feats):
    fx = COL2_X + 25 + (fidx % 2) * (COL_W // 2 - 15)
    fy = curr_y + 195 + (fidx // 2) * 160
    fw = (COL_W // 2 - 30)
    fh = 145
    draw_rounded_card(img, [fx, fy, fx + fw, fy + fh], (255, 255, 255, 255), (245, 220, 235, 255), radius=12, border_width=1)
    draw.text((fx + 14, fy + 12), f_title, font=font_h2, fill=(126, 34, 206, 255))
    
    words = f_desc.split(" ")
    lines = []
    cur_line = []
    for w in words:
        if len(" ".join(cur_line + [w])) > 30:
            lines.append(" ".join(cur_line))
            cur_line = [w]
        else:
            cur_line.append(w)
    if cur_line:
        lines.append(" ".join(cur_line))
    draw.text((fx + 14, fy + 52), "\n".join(lines), font=font_small, fill=C_TEXT_DARK, spacing=4)
curr_y += 566

# CARD 5: SYSTEM MODULES SHOWCASE
draw_rounded_card(img, [COL2_X, curr_y, COL2_X + COL_W, curr_y + 260], C_CARD_BG, C_BORDER)
draw.text((COL2_X + 25, curr_y + 18), "📱 Integrated System Architecture", font=font_h1, fill=(112, 38, 82, 255))
draw.line([COL2_X + 25, curr_y + 55, COL2_X + COL_W - 25, curr_y + 55], fill=(245, 220, 235, 255), width=1)

modules = [
    ("📊 Live Dashboard", "Dynamic SVG cycle ring, next period countdown, ovulation badge, and 4 phase-adaptive wellness tips."),
    ("📅 Smart Calendar", "Month-view grid with period interval merging, ovulation star badges (✨), and symptom/mood logging."),
    ("💬 Health Assistant", "KMP-powered educational chatbot answering PCOS, PCOD, pre-pregnancy, and folic acid queries."),
    ("⚙️ Profile & Settings", "Custom cycle lengths, condition selection (Normal/PCOD/PCOS), and instant TTC mode toggle.")
]

for midx, (m_title, m_desc) in enumerate(modules):
    mx = COL2_X + 25 + (midx % 2) * (COL_W // 2 - 15)
    my = curr_y + 70 + (midx // 2) * 85
    mw = (COL_W // 2 - 30)
    mh = 72
    draw_rounded_card(img, [mx, my, mx + mw, my + mh], (255, 255, 255, 255), (245, 225, 238, 255), radius=10, border_width=1)
    draw.text((mx + 12, my + 10), m_title, font=font_bold, fill=(92, 35, 75, 255))
    draw.text((mx + 12, my + 34), m_desc, font=font_small, fill=C_TEXT_MUTED)
curr_y += 276

# CARD 6: EMPIRICAL RESULTS & LATENCY
draw_rounded_card(img, [COL2_X, curr_y, COL2_X + COL_W, curr_y + 188], (255, 255, 255, 240), C_BORDER)
draw.text((COL2_X + 25, curr_y + 16), "📈 Empirical Results & System Verification", font=font_h1, fill=(112, 38, 82, 255))

stat_cards = [
    ("< 5 ms", "Query Latency (KMP)", C_ROSE_DEEP),
    ("6.8x", "Sorting Speedup", (39, 103, 73, 255)),
    ("100%", "Client Data Privacy", C_PURPLE),
]

sc_w = (COL_W - 50 - 24) // 3
for sc_idx, (sc_val, sc_lbl, sc_col) in enumerate(stat_cards):
    scx = COL2_X + 25 + sc_idx * (sc_w + 12)
    scy = curr_y + 55
    draw_rounded_card(img, [scx, scy, scx + sc_w, scy + 110], (253, 247, 255, 255), (242, 215, 235, 255), radius=12)
    draw.text((scx + 20, scy + 18), sc_val, font=font_big_num, fill=sc_col)
    draw.text((scx + 20, scy + 68), sc_lbl, font=font_bold, fill=C_TEXT_MUTED)

# ================= FOOTER =================
draw_rounded_card(img, [50, HEIGHT - 85, WIDTH - 50, HEIGHT - 35], (255, 255, 255, 245), C_BORDER, radius=12)
draw.text((75, HEIGHT - 67), "🌸 Sakhi: Menstrual Cycle Tracker & Conception Planner", font=font_bold, fill=(112, 38, 82, 255))
draw.text((WIDTH // 2 - 120, HEIGHT - 67), "University Capstone Project · Academic Year 2026", font=font_body, fill=C_TEXT_MUTED)
draw.text((WIDTH - 440, HEIGHT - 67), "HTML5 / ES6 / CSS3 · Algorithms: Merge Sort, KMP, Binary Search", font=font_bold, fill=C_ROSE_DEEP)

# Save as high-resolution PNG
output_path = "C:\\Users\\shami\\Desktop\\SEM V\\AOA\\AOA Project\\menustral-cycle-tracker\\poster.png"
img.save(output_path, "PNG", dpi=(200, 200))
print(f"Poster successfully saved at: {output_path}")

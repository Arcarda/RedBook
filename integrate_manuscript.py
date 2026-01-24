# Red Book Manuscript Integration Script
# This script integrates all artifacts into the main manuscript

import re
import os

ARTIFACTS_DIR = r"O:\Antigravity\Workspaces\Writing\RedBook\Artifacts"
MANUSCRIPT = r"O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Manu.md"
OUTPUT = r"O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Manu_FINAL.md"

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def fix_encoding(text):
    """Fix common encoding issues"""
    replacements = {
        'â€"': '—',
        'â€™': "'",
        'â€œ': '"',
        'â€': '"',
        '\r\n': '\n',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Read the operators orders
operators_orders = {}
orders_content = read_file(os.path.join(ARTIFACTS_DIR, "operators_orders_0-8.md"))

# Parse each chapter's orders (they are between ```markdown and ```)
pattern = r'\*\*OPERATOR\'S ORDERS — CHAPTER (\d+)\*\*\n\n(.*?)```'
matches = re.findall(pattern, orders_content, re.DOTALL)
for chapter_num, orders_text in matches:
    # Clean up the orders text
    orders = orders_text.strip()
    operators_orders[int(chapter_num)] = f"\n**OPERATOR'S ORDERS — CHAPTER {chapter_num}**\n\n{orders}\n"

# Read main manuscript
manuscript = read_file(MANUSCRIPT)
manuscript = fix_encoding(manuscript)

# Insert operators orders before each chapter divider
# Chapter 0 ends before "## CHAPTER 1"
# Chapter 1 ends before "## CHAPTER 2", etc.

chapter_markers = [
    ("## CHAPTER 1:", 0),
    ("## CHAPTER 2:", 1),
    ("## CHAPTER 3:", 2),
    ("## CHAPTER 4:", 3),
    ("## CHAPTER 5:", 4),
    ("## CHAPTER 6:", 5),
    ("## CHAPTER 7:", 6),
    ("## CHAPTER 8:", 7),
]

# Insert in reverse order to preserve line positions
for marker, chapter_num in reversed(chapter_markers):
    if chapter_num in operators_orders:
        # Find the --- before the marker
        idx = manuscript.find(marker)
        if idx > 0:
            # Find the --- before this marker
            prev_divider = manuscript.rfind("---", 0, idx)
            if prev_divider > 0:
                # Insert orders before the ---
                manuscript = manuscript[:prev_divider] + operators_orders[chapter_num] + "\n" + manuscript[prev_divider:]

# Add Chapter 8's orders at the end (before any final content)
if 8 in operators_orders:
    # Find end of Chapter 8 content
    if "# SECTION II:" in manuscript:
        idx = manuscript.find("# SECTION II:")
        prev_divider = manuscript.rfind("---", 0, idx)
        if prev_divider > 0:
            manuscript = manuscript[:prev_divider] + operators_orders[8] + "\n" + manuscript[prev_divider:]

# Now append chapters 9-19
chapter_files = [
    "chapter_09_bridge.md",
    "chapter_10_signal.md",
    "chapter_11_logistics.md",
    "chapter_12_fleet.md",
    "chapter_13_cocaptain.md",
    "chapter_14_grief.md",
    "chapter_15_forgiveness.md",
    "chapter_16_relapse.md",
    "chapter_17_crisis.md",
    "chapter_18_trauma.md",
    "chapter_19_maintenance.md",
]

for chapter_file in chapter_files:
    chapter_path = os.path.join(ARTIFACTS_DIR, chapter_file)
    if os.path.exists(chapter_path):
        chapter_content = read_file(chapter_path)
        chapter_content = fix_encoding(chapter_content)
        manuscript += "\n\n---\n\n" + chapter_content

# Append appendices
appendix_files = [
    "appendix_intelligence.md",
    "appendix_drydock.md",
    "appendix_medevac.md",
    "appendix_sources.md",
    "appendix_glossary.md",
    "appendix_fieldnotes.md",
]

manuscript += "\n\n---\n\n# APPENDICES\n"

for appendix_file in appendix_files:
    appendix_path = os.path.join(ARTIFACTS_DIR, appendix_file)
    if os.path.exists(appendix_path):
        appendix_content = read_file(appendix_path)
        appendix_content = fix_encoding(appendix_content)
        manuscript += "\n\n---\n\n" + appendix_content

# Write output
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(manuscript)

print(f"Created integrated manuscript: {OUTPUT}")
print(f"Line count: {len(manuscript.splitlines())}")

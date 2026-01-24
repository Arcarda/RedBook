# The Red Book — Affinity 3.0.3 (Unified App) Layout Guide

## Step-by-Step Setup Instructions (2026 Unified Workflow)

This guide is optimized for the **Affinity Unified App (v3.0.3)**. You no longer need to switch between Photo, Designer, and Publisher; use the **Studio** picker in the top-left corner.

---

## Phase 1: Create Your Unified Document

### New Document Settings

1. **File → New**
2. Select **Print** from the category list (if "Press Ready" is missing, use standard "Print").
3. Configure **manually** as follows:

| Setting | Value |
|---------|-------|
| Page Width | 5 in |
| Page Height | 7 in (Re-eval: 29k words requires smaller trim) |
| DPI | 300 |
| Pages | ~160-180 (estimated) |
| Facing Pages | ✓ Checked |
| Start On | Right |
| Color Format | CMYK/8 |
| Color Profile | US Web Coated (SWOP) v2 (or Gracol 2006) |

1. Click **"Margins"** tab:

| Setting | Value |
|---------|-------|
| Inside | 0.75 in |
| Outside | 0.5 in |
| Top | 0.5 in |
| Bottom | 0.625 in |

1. Click **"Bleed"** tab:
   - All sides: 0.125 in

2. Click **Create**

### Studio Switcher (Top Left)

In 3.0.2, use the **Studio Picker** to change tools without switching apps:

- **Layout Studio:** Primary tool for the book interior (Text, ToC, Sections).
- **Vector Studio:** For the cover design and ornaments.
- **Pixel Studio:** For photo editing and textures.

---

## Phase 2: Set Up Unified Text Styles

1. Open **Text Styles** panel.
2. Click **"+"** → **Paragraph Style**.
3. Create these core styles:

#### Body Style

- Font: EB Garamond (or your chosen font)
- Size: 11pt
- Leading: 14.85pt (1.35×)
- Alignment: Left Justified, last line left
- First Line Indent: 0.25 in
- Hyphenation: On

#### Body-First Style

- Based on: Body
- First Line Indent: 0 in
- Use after headings

#### H1-Chapter Style

- Font: EB Garamond Bold
- Size: 28pt
- Leading: 32pt
- Space Before: 0pt
- Space After: 24pt
- Keep with next paragraph

#### H2-Section Style

- Font: EB Garamond Bold
- Size: 14pt
- Space Before: 18pt
- Space After: 9pt

#### Operators-Orders-Title Style

- Font: EB Garamond Bold Small Caps
- Size: 11pt
- Space Before: 12pt
- Space After: 6pt

---

## Phase 3: Create Master Pages

### Access Master Pages

1. **Pages** panel → Click **"Master Pages"** at top
2. You'll see A-Master (default)

### Create Master Pages

#### A-Master: Standard Text Pages

1. Double-click A-Master to edit
2. Add **Running Header:**
   - Draw text frame at top of page, inside margins
   - Left page (verso): Insert → Fields → Document → Title
   - Right page (recto): Chapter title (will update manually or via Section Manager)
   - Style: 8pt, Small Caps

3. Add **Page Numbers:**
   - Draw text frame in footer area
   - Insert → Fields → Page Number
   - Left page: Align left
   - Right page: Align right
   - Style: 9pt

#### B-Master: Chapter Opener

1. Right-click A-Master → **Add Master**
2. Name it "B-Chapter Opener"
3. Remove running header
4. Remove page number
5. This page will be blank — chapter content added per-page

#### C-Master: Section Title

1. Add another master page
2. Centered layout for "SECTION I: THE COMMAND" style
3. No headers/footers

---

## Phase 4: Import Your Manuscript

### Prepare the Manuscript

Before importing, optionally convert `Red_Book_Manu_FINAL.md` to RTF or DOCX:

- This preserves some formatting (bold, italic)
- Use Pandoc: `pandoc Red_Book_Manu_FINAL.md -o Red_Book_Manu.docx`

### Unified Import Process

1. Go to page 1.
2. **File → Place**
3. Select `Red_Book_Manu_FINAL.docx`.
4. **HOLD SHIFT** and click once in the top-left margin corner.
   - **Result:** Affinity 3.0.3 will auto-generate all pages and link the flow immediately.

---

## Phase 5: Advanced 3.0.3 Features

### Canva AI Integration (For Cover/Art)

If you have Canva Pro connected, use the **AI Studio** panel for:

- Generative Fill for cover textures.
- Super Resolution for upscaling low-res assets.

### ePub Export

1. **File → Export**
2. Select **ePub** (New in V3).
3. Use for digital proofing alongside your Print PDF.

### Apply Master Pages

1. In Pages panel, select the page
2. Right-click → **Apply Master → B-Chapter Opener**
3. Apply to all chapter start pages

---

## Phase 5: Style Your Content

### Find & Replace Styling

Use **Edit → Find & Replace** to batch-apply styles:

1. Search for `## CHAPTER` (regex if needed)
2. Replace with same text, apply H1-Chapter style

### Manual Styling Checklist

For each chapter:

- [ ] Apply B-Master to opener page
- [ ] Style chapter title as H1-Chapter
- [ ] Remove first-line indent from first paragraph
- [ ] Style all "OPERATOR'S ORDERS" boxes
- [ ] Check for widows/orphans

---

## Phase 6: Create Operator's Orders Boxes

### Build the Box

1. Draw a **Rectangle** tool shape
2. Fill: 5% Black (very light gray)
3. Stroke: 0.5pt, 40% Black
4. Corner radius: 2pt (optional)

5. Draw a **Text Frame** inside the rectangle
6. Style the header: Operators-Orders-Title
7. Style list items: Body style with numbering

8. **Group** the rectangle and text frame (Ctrl+G)
9. Copy this group and paste for each chapter's box

---

## Phase 7: Section Breaks

### Create Ornament

For `---` section breaks in the manuscript:

**Option A: Simple Rule**

1. Draw a line (1.5-2 inches wide)
2. Stroke: 0.5pt, 50% Black
3. Center on page

**Option B: Symbol**

1. Type: • • • or ⚓ or ※
2. Center, style at 10pt
3. Space before/after: 12pt

---

## Phase 8: Front Matter Setup

### Page Order

| Page | Content | Master |
|------|---------|--------|
| i | Title Page | D-FrontMatter |
| ii | Copyright | D-FrontMatter |
| iii | Dedication | D-FrontMatter |
| iv | Blank | None |
| v-viii | Table of Contents | D-FrontMatter |
| ix-x | Preface | A-Master |
| 1 | Chapter 0 begins | B-Chapter Opener |

### Section Manager

1. **View → Studio → Sections**
2. Right-click page 1 (Chapter 0) → **Start Section**
3. Set numbering to start at 1
4. Previous pages will use lowercase Roman numerals

---

## Phase 9: Export for Print

### Before Exporting

- [ ] Check all images are placed (if any)
- [ ] View → Show Bleed to verify bleeds
- [ ] Look for overset text (red + icons)
- [ ] Spell check: Edit → Spelling

### Export Settings

1. **File → Export**
2. Choose **PDF** format
3. Select preset: **PDF/X-1a:2003**

| Setting | Value |
|---------|-------|
| Area | All Pages |
| Include Bleed | ✓ Checked |
| Include Marks | ☐ Unchecked |
| Embed Fonts | ✓ Automatic |

1. Click **Export**

---

## Quick Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Place/Import | Ctrl+Shift+P |
| Text Frame Tool | T |
| Apply Paragraph Style | Click in Styles panel |
| Group Objects | Ctrl+G |
| Show Pages Panel | View → Studio → Pages |
| Show Layers | View → Studio → Layers |
| Toggle Guides | Ctrl+; |
| Preview Mode | W |

---

## Troubleshooting

### Text Not Flowing

- Check that text frames are linked (blue arrows should connect)
- Click overflow indicator and draw new frame on next page

### Styles Not Applying

- Ensure cursor is in the paragraph
- Check for overrides (lightning bolt icon in Styles panel)

### Export Issues

- Ensure all fonts are installed system-wide
- Check for RGB images (convert to grayscale/CMYK)

---

*Layout guide for The Red Book - A Field Manual for Self-Command*

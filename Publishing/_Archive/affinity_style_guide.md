# The Red Book — Affinity Publisher Style Guide

## Document Setup

### Trim Size

- **Main Book:** 5" × 7" (Selected for the 29k-word manuscript)
- **Field Journal:** 5" × 7" (Standardized to match the main book for bundling)
- **Bleed:** 0.125" on all sides

### Margins (for 6" × 9")

| Edge | Measurement |
|------|-------------|
| Inside (Gutter) | 0.75" |
| Outside | 0.5" |
| Top | 0.5" |
| Bottom | 0.625" |

> **Note:** The inside margin is larger to accommodate binding — text won't disappear into the spine.

### Bleed Settings

- **Bleed:** 0.125" on all sides
- Required for any elements that extend to the page edge (chapter openers, decorative rules)
- Enable "Include Bleed" when exporting

### Color Mode

- **Interior:** Grayscale or Black (most POD printers)
- **Cover:** CMYK
- Color Profile: US Web Coated (SWOP) v2 or similar

### Resolution

- All images: **300 DPI minimum** (effective PPI after scaling)

---

## Typography

### Font Palette (Limit to 2-3 fonts)

| Role | Font | Style | Size |
|------|------|-------|------|
| **Body Text** | Garamond Premier Pro, EB Garamond, or Libre Baskerville | Regular | 11pt |
| **Headings (Chapter)** | Same as body or contrasting sans | Bold/Small Caps | 24-36pt |
| **Headings (Section)** | Same as body | Bold | 14-16pt |
| **Subheadings** | Same as body | Bold Italic or Small Caps | 12-13pt |
| **Block Quotes** | Same as body | Italic | 10-11pt |
| **Operator's Orders Boxes** | Secondary font (optional) | Bold | 10-11pt |
| **Running Headers** | Same as body | Small Caps | 8-9pt |
| **Page Numbers** | Same as body | Regular | 9pt |

### Image Trace & Assets (New in 3.0.2)

- Use the **Image Trace** feature (Vector Studio) to convert any sketch or scan into a vector ornament.
- **Canva Assets:** You can now drag-and-drop elements directly from the Canva library into your layout if connected.

### Free/Open-Source Alternatives

- **Body:** EB Garamond, Crimson Pro, Libre Baskerville (Google Fonts)
- **Headers:** Outfit, Lora Bold, or keep consistent with body

### Line Spacing (Leading)

- **Body text:** 1.35× font size (14.85pt for 11pt text)
- **Headings:** 1.2× or tighter

### Paragraph Settings

- **First-line indent:** 0.25" (do NOT indent first paragraph after heading)
- **Paragraph spacing:** 0pt between paragraphs (use indents only)
- **Alignment:** Left-justified with last line left (avoid rivers)
- **Hyphenation:** Enabled, with conservative settings

### Character Count Per Line

- Target: **55-70 characters** per line (optimal readability)

---

## Master Pages

Create the following master pages in Affinity Publisher:

### 1. A-Master: Standard Text Pages

- Running header (book title on verso, chapter title on recto)
- Page numbers in footer (outside corners)
- Standard margins applied

### 2. B-Master: Chapter Opener

- No running header or page number
- Generous top margin (drop ~2.5-3 inches from top)
- Chapter number and title placement
- Optional decorative rule or icon

### 3. C-Master: Section Title Pages

- "SECTION I: THE COMMAND" style
- Centered layout, minimal decoration
- Optional section description

### 4. D-Master: Front/Back Matter

- For title page, copyright, dedication, TOC
- No running headers/footers
- Custom layouts per page

### 5. E-Master: Appendix Pages

- Similar to A-Master but with "APPENDIX" in running header

---

## Paragraph Styles to Create

Set these up in Affinity Publisher's Text Styles panel:

### Body Styles

| Style Name | Based On | Description |
|------------|----------|-------------|
| `Body` | None | Standard paragraph text |
| `Body-First` | Body | No first-line indent (after headings) |
| `Body-Quote` | Body | Indented block quote, italic |
| `Body-List` | Body | Bulleted/numbered list items |

### Heading Styles

| Style Name | Description |
|------------|-------------|
| `H1-Chapter` | Chapter titles (Day Zero, Who Is Steering?, etc.) |
| `H2-Section` | Major sections within chapters |
| `H3-Subsection` | Smaller divisions |
| `H1-Section-Title` | Section dividers (SECTION I: THE COMMAND) |

### Special Styles

| Style Name | Description |
|------------|-------------|
| `Operators-Orders-Title` | "OPERATOR'S ORDERS — CHAPTER X" header |
| `Operators-Orders-Item` | Numbered items in summary boxes |
| `Case-Brief-Title` | "CASE BRIEF:" headers |
| `Scientific-Citation` | In-text research references |
| `Emphasis-Key-Term` | First use of key terms (bold) |

### Field Journal Specific Styles

| Style Name | Description |
|------------|-------------|
| `Journal-Day-Title` | Large "DAY X" header |
| `Journal-Phase-Header` | "MORNING WATCH" / "EVENING DEBRIEF" subheaders |
| `Journal-Prompt-Label` | Bold labels (e.g., "1. Primary Objective:") |
| `Journal-Entry-Line` | Styling for the horizontal response lines |

---

## Character Styles

| Style Name | Formatting | Usage |
|------------|------------|-------|
| `Emphasis` | Italic | Standard emphasis |
| `Strong` | Bold | Key takeaways, critical points |
| `Key-Term` | Bold + Small Caps | First definition of framework terms |
| `Ship-Voice` | Italic | The Passenger's internal dialogue |
| `Blockquote-Source` | Small Caps | Attribution for quotes |

---

## Design Elements

### Operator's Orders Boxes

```
┌─────────────────────────────────────────┐
│ OPERATOR'S ORDERS — CHAPTER X          │
│                                         │
│ 1. First key takeaway                   │
│ 2. Second key takeaway                  │
│ ...                                     │
└─────────────────────────────────────────┘
```

- Light gray background (#F5F5F5) or thin border
- Slight padding (0.15" internal)
- Placed at end of each chapter

### Section Dividers

- Triple dashes (`---`) in manuscript = horizontal rule
- Use subtle typographic ornament or simple line (0.5pt weight)

### Chapter Opener Design

- Chapter number: Large, possibly with nautical/military styling
- Chapter title: Bold, prominent
- Subtitle in parentheses: Smaller, beneath title
- Drop cap (optional): First letter of first paragraph

### Pull Quotes (Optional)

- For key insights, consider pull quotes in margins or between paragraphs
- Example: *"Motion creates emotion, not the other way around."*

---

## Page Numbering Scheme

| Section | Style | Start |
|---------|-------|-------|
| Front Matter (Title, Copyright, Dedication) | Lower Roman (i, ii, iii) | i |
| Preface, TOC | Lower Roman (continues) | — |
| Main Content (Chapter 0 onward) | Arabic (1, 2, 3) | Reset to 1 |
| Appendices | Arabic (continues) | — |

---

## Export Settings for Print

### PDF/X-1a:2003 Export

1. **Preset:** PDF/X-1a:2003
2. **Include Bleed:** ✓ Checked
3. **Marks:** None (printer adds their own)
4. **Compression:** High Quality (no JPEG compression for text)
5. **Compatibility:** PDF 1.4

### Proofing Checklist Before Export

- [ ] All images are 300 DPI effective
- [ ] No overset text (red plus icons in text frames)
- [ ] All fonts embedded or converted to curves
- [ ] Bleeds extend to bleed line
- [ ] No widows/orphans on critical pages
- [ ] Page count is even (or matches printer requirements)

---

## File Organization

Recommended folder structure:

```
RedBook_Publishing/
├── 01_Manuscript/
│   └── Red_Book_Manu_FINAL.md
├── 02_Affinity_Files/
│   ├── RedBook_Interior.afpub
│   └── RedBook_Cover.afpub
├── 03_Assets/
│   ├── Cover/
│   ├── Icons/
│   ├── Ornaments/
│   └── Fonts/
├── 04_Export/
│   ├── Print_Ready/
│   └── Proofs/
└── 05_Resources/
    ├── affinity_style_guide.md (this file)
    └── asset_specifications.md
```

---

## Quick Reference: The Red Book Elements

| Manuscript Element | Affinity Treatment |
|--------------------|-------------------|
| `# CHAPTER X: TITLE` | H1-Chapter style + B-Master page |
| `## SECTION TITLE` | H2-Section style |
| `**(SUBTITLE)**` | Character style: Small caps or italic |
| `**Bold text**` | Strong character style |
| `*Italic text*` | Emphasis character style |
| `> Quote block` | Body-Quote paragraph style |
| `- List item` | Body-List style |
| `---` | Section break ornament or horizontal rule |
| `**OPERATOR'S ORDERS**` | Operators-Orders box (grouped frame) |

---

*Created for The Red Book - A Field Manual for Self-Command*

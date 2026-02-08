# The Red Book — Asset Specifications

## Cover Assets

### Front Cover

- **Dimensions:** 5" × 7" + 0.125" bleed on all sides = **5.25" × 7.25"**
- **Resolution:** 300 DPI minimum
- **Color Mode:** CMYK
- **File Format:** .afphoto (Affinity Photo) or high-res PNG/TIFF

#### Design Requirements

| Element | Specification |
|---------|---------------|
| Title | "THE RED BOOK" — prominent, impactful |
| Subtitle | "A Field Manual for Self-Command" — below title |
| Author Name | Your name — bottom third |
| Imagery | Abstract, nautical/command theme, or minimalist |
| Safety Zone | Keep critical text 0.25" from trim edge |

### Back Cover

- **Dimensions:** Same as front (5.25" × 7.25" with bleed)
- **Elements:**
  - Book description/blurb (150-200 words)
  - Author bio (optional)
  - Barcode placement area (2" × 1.2" in bottom right)
  - Category/genre line
  - Pull quote or endorsement (if available)

### Spine

- **Width:** Calculate based on page count and paper stock
  - Formula: `Spine Width = (Page Count ÷ 2) × Paper Caliper`
  - **The Red Book (~170 pages):** ~0.34" (50lb Cream)
  - **Field Journal (90 Days / ~200 pages):** ~0.40" (60lb White recommended for journaling)

### Full Cover Wrap (for print)

- **Total Width:** Back + Spine + Front + Bleeds
- **The Red Book:** 5.25" + 0.34" + 5.25" = **10.84"**
- **Field Journal:** 5.25" + 0.40" + 5.25" = **10.90"**

---

## Interior Assets

### Chapter Opener Icons (Optional)

- **Size:** 0.5" × 0.5" to 1" × 1"
- **Format:** Vector (SVG preferred) or 300 DPI PNG with transparency
- **Style:** Simple, single-color (works in grayscale)
- **Themes:** Nautical/maritime imagery to match "Operator/Ship" metaphor

#### Suggested Icon Set

| Chapter | Icon Suggestion |
|---------|-----------------|
| 0-4 (The Command) | Anchor, Ship wheel, Compass |
| 5-8 (The Systems) | Gear, Reactor symbol, Radar |
| 9-11 (The Environment) | Bridge/helm, Radio waves, Briefcase |
| 12-15 (The Fleet) | Fleet ships, Handshake, Anchor (chain) |
| 16-19 (The Storms) | Storm clouds, Lifeboat, Lighthouse |
| **Field Journal** | Logbook, Quill, Pilot's wings |

### Section Ornaments

- **Purpose:** Visual breaks between sections (`---` in manuscript)
- **Options:**
  - Simple horizontal rule (0.5pt, 2" wide, centered)
  - Triple dots (• • •)
  - Nautical symbol (⚓ or ⎈)
  - Custom typographic ornament
- **Size:** Small, subtle — should not distract from text

### Operator's Orders Box Styling

- **Background:** Light gray (#F0F0F0 to #F5F5F5) or white with border
- **Border:** 0.5pt black or dark gray, rounded corners (optional)
- **Padding:** 0.15" on all sides
- **Width:** Full text column width minus 0.25" each side

### Pull Quote Styling (Optional)

- **Format:** Indented block with decorative quotation marks
- **Font:** Same as body, italic, larger size (13-14pt)
- **Background:** None or very subtle shade
- **Example quotes to highlight:**
  - *"Motion creates emotion, not the other way around."*
  - *"You are not the enemy. You are the patient and the physician."*
  - *"The goal is not to kill the Passenger; it is to give it a better role."*

---

## Font Assets

### Primary Fonts (Choose one set)

#### Option A: Classic & Authoritative

| Role | Font | Source |
|------|------|--------|
| Body | Garamond Premier Pro | Adobe Fonts / Purchase |
| Headings | Garamond Premier Pro Bold | Same |
| Accent | — | — |

#### Option B: Open Source / Free

| Role | Font | Source |
|------|------|--------|
| Body | EB Garamond | Google Fonts (free) |
| Headings | EB Garamond Bold / Lora Bold | Google Fonts (free) |
| Accent (optional) | Outfit | Google Fonts (free) |

#### Option C: Modern Professional

| Role | Font | Source |
|------|------|--------|
| Body | Crimson Pro | Google Fonts (free) |
| Headings | Outfit or Montserrat | Google Fonts (free) |

### Font Installation

1. Download font files (.ttf or .otf)
2. Install to Windows: Right-click → Install for all users
3. Fonts will be available in Affinity Publisher

---

## Color Palette

### Interior (Grayscale)

| Use | Value |
|-----|-------|
| Body Text | 100% Black |
| Headings | 100% Black |
| Box Backgrounds | 5-10% Black |
| Rules/Lines | 40-60% Black |

### Cover (CMYK)

| Color | CMYK Values | Use |
|-------|-------------|-----|
| Deep Red | C:15 M:100 Y:90 K:10 | Title, accents |
| Black | C:0 M:0 Y:0 K:100 | Text, outlines |
| Cream/Off-White | C:0 M:2 Y:8 K:0 | Background |
| Navy Blue | C:100 M:80 Y:30 K:20 | Optional accent |

> **Note:** "Red Book" lends itself to a striking red and black cover design. Consider a predominantly dark cover with red title text.

---

## Image Requirements

### If Including Any Images

- **Resolution:** 300 DPI at final printed size
- **Format:** TIFF (preferred) or high-quality PNG
- **Color Mode:** Grayscale for interior, CMYK for cover
- **Compression:** None or lossless

### Stock Image Resources (if needed)

- Unsplash (free, high-quality)
- Pexels (free)
- Adobe Stock (paid, high-quality)
- Shutterstock (paid)

---

## Printer-Specific Templates

### Amazon KDP

- [Cover Calculator](https://kdp.amazon.com/cover-calculator)
- Interior: PDF/X-1a, no crop marks
- Cover: PDF, include bleed
- Spine width calculated automatically

### IngramSpark

- [Template Generator](https://myaccount.ingramspark.com/Portal/Tools/CoverTemplateGenerator)
- More trim size options
- Requires exact spine width calculation

### Barnes & Noble Press

- Similar to KDP requirements
- Download templates from their dashboard

---

## Checklist: Assets to Create/Gather

### Cover

- [ ] Front cover design (6.25" × 9.25" with bleed)
- [ ] Back cover design with barcode space
- [ ] Spine design (calculate width after finalizing page count)
- [ ] Full wraparound cover file for printer

### Interior

- [ ] Chapter opener icon(s) — optional
- [ ] Section break ornament — optional
- [ ] Font files installed

### Files

- [ ] Style guide document (this file)
- [ ] Manuscript (.md or .docx for import)
- [ ] ISBN barcode image (if self-publishing with your own ISBN)

---

## Asset Delivery Folder Structure

```
RedBook_Publishing/
├── 03_Assets/
│   ├── Cover/
│   │   ├── front_cover_final.afphoto
│   │   ├── back_cover_final.afphoto
│   │   ├── full_cover_wrap.afphoto
│   │   └── barcode.png
│   ├── Icons/
│   │   ├── anchor.svg
│   │   ├── compass.svg
│   │   ├── ship_wheel.svg
│   │   └── ...
│   ├── Ornaments/
│   │   └── section_break.svg
│   └── Fonts/
│       ├── EBGaramond-Regular.ttf
│       ├── EBGaramond-Bold.ttf
│       └── EBGaramond-Italic.ttf
```

---

*Asset specifications for The Red Book - A Field Manual for Self-Command*

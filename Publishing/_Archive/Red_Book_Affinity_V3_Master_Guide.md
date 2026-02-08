# The Red Book: Master Assembly Guide (Affinity V3)

> **Software Version:** Affinity Publisher 3.0.3.4027 (by Canva)
> **Date:** January 27, 2026
> **Scope:** The Red Book (Main) & Official Field Journal

---

## 1. Project Specifications (Unified)

Both books share the same physical footprint for consistent bundling.

| Spec | The Red Book (Main) | Field Journal |
| :--- | :--- | :--- |
| **Trim Size** | 5" x 7" | 5" x 7" |
| **Bleed** | 0.125" (All sides) | 0.125" (All sides) |
| **Margins** | Inner: 0.75" / Outer: 0.5" <br> Top: 0.5" / Bottom: 0.625" | Same |
| **Color** | Grayscale (Black Only) | Grayscale (Black Only) |
| **Resolution** | 300 DPI | 300 DPI |
| **Est. Pages** | ~170 | ~200 |

---

## 2. Phase I: Document Setup (Do this first)

### Step 1: Create New Document

1. Launch **Affinity Publisher**.
2. **File > New** (Cmd+N / Ctrl+N).
3. Select **Print (Press Ready)**.
4. Entering Settings:
   - **Page Width:** `5 in`
   - **Page Height:** `7 in`
   - **DPI:** `300`
   - **Facing Pages:** [x] Checked (Horizontal)
   - **Arrange:** Left-to-Right
   - **Start on:** Right
5. **Margins Tab:**
   - Inner: `0.75` | Outer: `0.5` | Top: `0.5` | Bottom: `0.625`
6. **Bleed Tab:**
   - Inner/Outer/Top/Bottom: `0.125 in`
7. Click **Create**.

### Step 2: Master Page Setup

Go to the **Window > Pages** panel. Select the **Master Pages** tab.

**A-Master (Main Body):**

- Draw text frames for headers (Top) and page numbers (Bottom).
- *Tip:* Use `Text > Insert > Fields > Page Number`.

**B-Master (Chapter Opener):**

- Create a new Master based on "None".
- Leave header/footer blank.
- Add a top margin guide at `2.0 in` (Drop starts here).

**J-Master (Journal Only):**

- **Left Page:** Header "MORNING WATCH". 3 text blocks with lines.
- **Right Page:** Header "EVENING DEBRIEF". 3 text blocks with lines.

---

## 3. Phase II: Content Import & Tag Mapping

This is the critical step where we convert "Word/Markdown" formatting into "Affinity Styles".

### Step 1: Prepare the Source

Ensure your `Red_Book_Manu_FINAL_Import.docx` uses standard Word styles:

- **Heading 1:** Chapter Titles
- **Heading 2:** Section Headers
- **Normal:** Body Text
- **Quote:** Blockquotes

### Step 2: The Place Command

1. Go to **Page 1 (Right)**.
2. **File > Place...**
3. Select `Red_Book_Manu_FINAL_Import.docx`.
4. **CRITICAL:** Scroll down in the Place dialog to **"Show Import Options"** (if available) OR check the settings in the sidebar.
   - *Note:* In V3, this often happens *after* you select the file but before you click to place. Look for the context toolbar.

### Step 3: Style Mapping (The "Tags")

When content flows in, Affinity imports the Word Styles. You will see them in the **Text Styles** panel (Window > Text > Text Styles).

**Strategy: Rename & Merge**
Don't create new styles; repurpose the imported ones to match our naming convention.

| Imported Word Style | Target Affinity Style | Action |
| :--- | :--- | :--- |
| `Heading 1` | `H1-Chapter` | Right-click `Heading 1` > **Rename Style** to `H1-Chapter`. Update visual settings (Font: Garamond 24pt). |
| `Heading 2` | `H2-Section` | Rename to `H2-Section`. Update (Font: Garamond 14pt, Bold). |
| `Normal` | `Body` | Rename to `Body`. Update (Font: Garamond 11pt, Justified). |
| `Quote` | `Body-Quote` | Rename to `Body-Quote`. Update (Italic, Indented). |
| `Strong` / `Bold` | `Strong` | Keep as character style. |
| `Emphasis` / `Italic` | `Emphasis` | Keep as character style. |

### Step 4: Auto-Flow

1. Your cursor will look like a loaded text icon.
2. Hold **SHIFT** and click the top-left margin of Page 1.
3. Affinity will automatically create as many pages as needed to fit the text.

---

## 4. Phase III: Layout & Typography

### Find & Replace Cleanup

Use **Ctrl+F / Cmd+F** (Find and Replace) to fix common issues:

- **Double Spaces:** Find `  ` -> Replace ` ` (single space).
- **Section Breaks:** Find `---` -> Change Paragraph Style to `Section-Break-Graphic` (or replace with centered `* * *`).

### "Operator's Orders" Boxes

Affinity 3.0 allows "Pinning" objects to text.

1. Create your gray box group (Rectangle + Text Frame).
2. Cut (Ctrl+X).
3. Place cursor at the end of the chapter text.
4. Paste (Ctrl+V).
5. Use the **Float** or **Inline** pin settings to ensure it moves if text reflows.

---

## 5. Phase IV: Field Journal Specifics

The Field Journal is 90% repetition. Use **Data Merge** or **Master Pages**.

**The Master Page Method (Recommended):**

1. Design the "Morning Watch / Evening Debrief" spread on **J-Master**.
2. In the Pages panel, add 90 pages (Pages 1-90).
3. Select all pages -> Right Click -> **Apply Master** -> `J-Master`.
4. Manually update the "Day 1", "Day 2" headers *OR* use a Section Manager trick:
   - *Advanced:* Use "Section Name" field on the master page, and start a new section for every page named "Day X". (Tedious).
   - *Better:* Just type "DAY #" on the master, and manually unlock/edit the number on each page (Ctrl+Shift+Click object to unlock from master).

---

## 6. Phase V: Export for Print

**File > Export** settings for KDP/IngramSpark:

- **Preset:** PDF/X-1a:2003 (Industry Standard).
- **Raster DPI:** 300.
- **Include Bleed:** [x] **YES** (Vital for background colors/images).
- **Preview Export:** Always check the PDF before uploading. Look for:
  - Missing fonts (text turns into dots or generic serif).
  - Images touching the edge (ensure they go PAST the trim line into bleed).

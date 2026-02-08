# PRODUCTION GUIDE: The Red Book & Field Journal

**Objective:** Assemble the print-ready files for "The Red Book" (Manual) and its companion "Field Journal" using Affinity Publisher.

---

## 1. THE STRATEGY

You are producing **two distinct books** that share the same DNA (Size, Fonts, Styles).

| Spec | Book I: The Manual | Book II: The Field Journal |
| :--- | :--- | :--- |
| **Purpose** | Reading (Text Heavy) | Writing (Interactive) |
| **Page Size** | 5" x 7" | 5" x 7" |
| **Margins** | 0.75" Inner / 0.5" Outer | 0.75" Inner / 0.5" Outer |
| **Primary Master** | **Master A** (Text Frames) | **Master C** (SVG Forms) |
| **Content File** | `Red_Book_Manu_Import_Perfect.docx` | `Field_Journal_Import_Perfect.docx` |

---

## 2. THE ASSET KIT

Ensure these files are ready in your workspace:

### Content (Text)
*   `Red_Book_Manu_Import_Perfect.docx` (The main manuscript, styled)
*   `Field_Journal_Import_Perfect.docx` (Intro, SITREPs, Prompts)

### Layout (Visuals)
*   `Affinity_Asset_Master_A_Frame.svg` (Standard Text Frame)
*   `Affinity_Asset_Master_B_Divider.svg` (Chapter Divider)
*   `Affinity_Asset_Master_C_Left.svg` (Morning Watch layout)
*   `Affinity_Asset_Master_C_Right.svg` (Evening Debrief layout)

---

## 3. PHASE I: THE RED BOOK (MANUAL)

**Goal:** Create the text-heavy reading book.

### Step 1: Document Setup
1.  **New Document:**
    *   **Size:** 5 in x 7 in.
    *   **DPI:** 300.
    *   **Facing Pages:** Checked.
    *   **Margins:** Inner 0.75", Outer 0.5", Top 0.5", Bottom 0.625".
    *   **Bleed:** 0.125" (All sides).

### Step 2: Master Pages
1.  **Create "Master A" (Standard Body):**
    *   **Drag & Drop** `Affinity_Asset_Master_A_Left.svg` onto the LEFT spread. Center it.
    *   **Drag & Drop** `Affinity_Asset_Master_A_Right.svg` onto the RIGHT spread. Center it.
    *   **Draw Text Frames (Crucial for Flow):**
        *   Draw a Text Frame on the **Left Page**, snapping to margins.
        *   Draw a Text Frame on the **Right Page**, snapping to margins.
        *   **LINK THEM:** Click the triangle "Link" icon on the bottom-right of the Left frame, then click the Right frame. This ensures text flows Left -> Right.
    *   **Running Header (Frame):** Draw a small text box *above* the top black line on **both pages**.
        *   **Position:** X: Snap to Margin, Y ≈ 0.3".
        *   **Size:** W: 3.75", H: 0.25".
        *   **Style:** `Header - Running`.
    *   **Page Number (Frame):** Draw a small text box *below* the bottom footer bracket on **both pages**.
        *   **Position:** X: Snap to Margin, Y ≈ 6.75".
        *   **Size:** W: 3.75", H: 0.25".
        *   **Style:** `Folio`.
2.  **Create "Master B" (Chapter Breaks):**
    *   **Drag & Drop** `Affinity_Asset_Master_B_Divider.svg` onto the Right Page.
    *   Remove headers/footers for this Master.
    *   This provides the "Anchor" icon and Divider line automatically.

### Step 3: Content Import
1.  Go to Page 1. Apply **Master B** (Title Page).
2.  Go to Page 3 (First content). Apply **Master A**.
3.  **File > Place...** -> Select `Red_Book_Manu_Import_Perfect.docx`.
4.  Click inside the text frame.
5.  **Shift + Click** the "Text Flow" triangle (bottom right) to auto-generate pages for the whole book.

### Step 4: Styling
1.  Open the **Text Styles** panel.
2.  Use **Find and Replace** to map styles if needed (Word "Heading 1" usually maps automatically to Affinity "Heading 1").
3.  *Tip:* Style the `OperatorsOrder` paragraphs with a box/border to make them stand out.

---

## 4. PHASE II: THE FIELD JOURNAL

**Goal:** Create the interactive notebook.

### Step 1: Document Setup
*   *Same settings as The Red Book (5x7).*

### Step 2: Master Pages (The Secret Sauce)
1.  **Create "Master C" (The Daily Spread):**
    *   **Left Page:** Drag & Drop `Affinity_Asset_Master_C_Left.svg`. Center it.
    *   **Right Page:** Drag & Drop `Affinity_Asset_Master_C_Right.svg`. Center it.
    *   *Note:* These SVGs are the "Lines" you write on. They are now part of the page structure.

### Step 3: Layout Construction
1.  **Intro Section (Pages 1-10):**
    *   Apply **Master A** (Text).
    *   Place `Field_Journal_Import_Perfect.docx` (The "Logbook Philosophy" section).
2.  **The Deployment (Pages 11-100):**
    *   Insert 90 pages.
    *   Apply **Master C** to all of them.
    *   *Result:* You now have 90 days of "Morning/Evening" spreads ready to print.
3.  **Weekly Reviews:**
    *   Every 7 days, insert a spread with **Master A**.
    *   Paste the "Weekly S.I.T.R.E.P." text from the DOCX file here.

---

## 5. ART DIRECTION (Next Steps)

Once the text and layout are locked:

1.  Leave **Empty Frames** where visuals should go.
2.  Refer to `Art_Direction_Plan.md` for the "Shot List" (Diagrams, Atmospheric Plates).
3.  We will generate these assets later and drop them into the empty frames.

**Ready to Build.**

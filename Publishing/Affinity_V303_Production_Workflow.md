# Production Workflow: The Red Book & Field Journal

**Ref: Master Guide**

This document details the step-by-step execution plan to build "The Red Book" and "Official Field Journal" in Affinity Publisher v3.0.3.

---

## Phase 1: Document Initialization

### 1.1 Create New Document

1. Launch Affinity Publisher.
2. **File > New**.
3. **Layout**:
    * **Page Width**: 5 in
    * **Page Height**: 7 in
    * **DPI**: 300
    * **Facing Pages**: [x] Checked
    * **Arrangement**: Horizontal
    * **Start on**: Right
4. **Margins** (Ref: Master Guide):
    * **Inner**: 0.75 in
    * **Outer**: 0.5 in
    * **Top**: 0.5 in
    * **Bottom**: 0.625 in
5. **Bleed**:
    * Set all sides (Inner, Outer, Top, Bottom) to **0.125 in**.
6. Click **Create**.

### 1.2 Baseline Grid Setup

1. Go to **View > Baseline Grid Manager**.
2. Check **Use Baseline Grid**.
3. **Start Position**: 0.5 in (Matches Top Margin).
4. **Grid Spacing**: 14.85 pt (Matches Body Text Leading).
5. **Display Threshold**: < 100%.
6. Click **Close**.

---

## Phase 2: Master Page Construction

### 2.1 Master A: Standard Text

1. Open **Pages Panel**. Double-click **Master A**.
2. **Text Frames**:
    * Draw a text frame that snaps exactly to the blue margin guides on the Left Page.
    * Draw another on the Right Page.
    * **Link**: Click the "Flow" triangle on the Left frame, then click the Right frame to link them.
3. **Running Header**:
    * Draw a small text box above the Top Margin (centered).
    * Type `<Running Header>`.
    * Go to **Text > Insert > Fields > Section Name**.
4. **Folio (Page Numbers)**:
    * Draw a small text box below the Bottom Margin.
    * Type `#`.
    * Go to **Text > Insert > Fields > Page Number**.
    * *Tip*: Align Left Page number to Left Margin, Right Page number to Right Margin.

### 2.2 Master B: Section Divider

1. Click **Add Master** icon (top of Pages panel). Name: "Master B - Section".
2. **No Text Frames**: Leave the main area clear.
3. **Title Block**:
    * Draw a text frame in the visual center.
    * Set placeholder text: "PART TITLE".
4. **Anchor**:
    * Draw a simple horizontal line or place a small logo at the bottom center.

### 2.3 Master C: Field Journal

1. Click **Add Master**. Name: "Master C - Journal".
2. **Grid Layer**:
    * Open **Layers Panel**. Create a New Layer named "Guides".
    * **File > Place**. Select `journal_lines_7mm.svg` (or dots).
    * Drag it to cover the writing area.
    * **Lock** the "Guides" layer so you don't select it later.
3. **Headers**:
    * Add text box "Morning Watch" (Left Page top).
    * Add text box "Evening Brief" (Right Page top).

---

## Phase 3: Style Definition & Mapping

**CRITICAL STEP**: Do this *before* importing your content.

1. **Open Text Styles Panel** (View > Studio > Text Styles).
2. **Delete** all default styles (optional, keeps it clean).
3. **Create "Body" Style**:
    * Click "Create Paragraph Style". Name: `Body Text`.
    * **Font**: Garamond (or chosen font), 11pt.
    * **Paragraph > Alignment**: Left (Justified optional).
    * **Spacing > Leading**: Exactly 14.85pt.
4. **Create "Heading 1" Style**:
    * Name: `Part Title`.
    * **Font**: Bold / Display, 24pt.
    * **Next Style**: `Body Text`.
5. **Create "Heading 2" Style**:
    * Name: `Section Header`.
    * **Font**: Bold, 14pt.

*(Repeat for all styles listed in Master Guide Table 1.1)*

---

## Phase 4: Import & Layout

### 4.1 Placing the Manuscript

1. Go to Page 1 of your document.
2. **File > Place**. Select your Word Document (`.docx`).
3. **Import Options**:
    * [x] "Use Styles"
    * [ ] "Preserve Text Styles" (Uncheck this to force mapping if names match exactly).
    * *Better Method*: Import, then use **Find and Replace**.
4. Click the first text frame. The text will flow.
5. **Auto-Flow**: Shift-Click the "Flow" triangle on the bottom right of the text frame. Affinity will automatically create new pages until all text is placed.

### 4.2 Cleaning & Mapping

1. **Find and Replace Panel** (Ctrl/Cmd + F).
2. **Scope**: Document.
3. **Find**: (Format) Paragraph Style: `Normal` (from Word).
4. **Replace**: (Format) Paragraph Style: `Body Text` (Affinity).
5. Click **Replace All**.
6. *Repeat for Headings -> Part Titles, etc.*

### 4.3 Applying Masters

1. Right-click a Chapter Title page in the Pages panel.
2. **Apply Master**.
3. Select **Master B - Section**.
4. Ensure "Replace Existing" is checked.
5. Click OK.

---

## Phase 5: Export for Production

1. **File > Export**.
2. **Format**: PDF.
3. **Preset**: PDF/X-1a:2003 (Standard for print).
4. **Area**: All Pages.
5. **Include Bleed**: [x] Checked.
6. Click **Export**.

---
*Created by Antigravity*

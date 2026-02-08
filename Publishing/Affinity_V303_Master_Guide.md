# Affinity Publisher Master Guide: Red Book & Field Journal

This comprehensive guide covers the setup, import, and layout workflow for "The Red Book" and "Official Field Journal" using Affinity Publisher v3.0.3.

## 1. Import Mapping Structure (Word to Affinity)

When importing text from Microsoft Word, ensure your source document uses Styles, not manual formatting. Map the incoming styles to your Affinity Publisher Styles as follows:

| Word Style Name | Affinity Publisher Style | Function / Purpose |
| :--- | :--- | :--- |
| **Normal** | `Body Text` | Standard paragraph text. 10/12pt font. |
| **Heading 1** | `Part Title` | Major section dividers (use with Master B). |
| **Heading 2** | `Section Header` | In-chapter subheadings. |
| **Heading 3** | `Subsection Header` | Minor content breaks. |
| **Quote** | `Blockquote` | Indented text for citations or flavor text. |
| **Emphasis** | `Body Text (Italic)` | *Character Style* for emphasis. |
| **Strong** | `Body Text (Bold)` | *Character Style* for importance. |
| **Date/Time** | `Journal Timestamp` | For "Morning Watch" / "Evening Brief" entries. |
| **List Bullet** | `Bullet List` | Standard bulleted lists. |
| **List Number** | `Numbered List` | Procedural steps. |

> [!TIP]
> **Pro Tip**: Use the **"Find and Replace"** panel with formatting constraints to quickly clean up local formatting overrides after import.

## 2. Master Page Specifications

Based on the design review, here are the specifications for the three primary Master Pages.

### Master A: Standard Text

* **Usage**: General body content, rules, lore.
* **Elements**:
  * **Running Header**: Centered at top. Style: `Header - Running` (Small Caps).
  * **Folio (Page Number)**: Centered at bottom. Style: `Folio`.
  * **Margins**: Inner (Gutter) 20mm, Outer 15mm, Top 25mm, Bottom 20mm.
* **Design Note**: Avoid heavy borders on headers; let the typography define the space.

### Master B: Section Divider

* **Usage**: Chapter starts, Part dividers.
* **Elements**:
  * **Title Block**: Visually centered (optical center). Style: `Display Title`.
  * **Anchor Element**: A small graphic or dividing line at the bottom center to ground the page.

### Master C: Field Journal Spread (Morning/Evening)

* **Usage**: Daily tracking sheets.
* **Left Page (Verso)**: "Morning Watch"
* **Right Page (Recto)**: "Evening Brief"
* **Utility Layer**:
  * Create a layer named "Guides" on this Master.
  * Add a **Dot Grid** (5mm spacing) or **Lines** (7mm spacing) in non-photo blue (C:10 M:0 Y:0 K:0) or 10% Black.
  * *Lock this layer* so it doesn't get accidentally moved during content entry.

## 3. Persona & Studio Workflow

Affinity Publisher's unique advantage is the efficient switching between Personas.

### Publisher Persona (Default)

* **Focus**: Layout, page ordering, text flow.
* **Key Panels**: `Pages`, `Layers`, `Text Styles`, `Table of Contents`.
* **Task**: Import Word docs here. Apply Master Pages to spreads. Flow text from frame to frame.

### Designer Persona

* **Focus**: Vector assets, logos, complex headers.
* **Access**: Click the distinct "Designer" icon in the top toolbar (Blue curve).
* **Keys**:
  * Edit the "Red Book" logo vector directly on the cover page without leaving the application.
  * Create custom vector swooshes for the `Section Divider` master.

### Photo Persona

* **Focus**: Image correction, texturing.
* **Access**: Click the "Photo" icon (Purple camera).
* **Keys**:
  * If you place a paper texture background, switch to Photo Persona to apply **Levels**, **Curves**, or **HSL** adjustments directly to the texture layer within the layout.
  * Use "Live Filters" (e.g., Gaussian Blur on background elements) for non-destructive editing.

## 4. Best Practices Checklist

* [ ] **Global Layers**: Use the "Section Manager" to handle page numbering resetting if needed for different "Books".
* [ ] **Baseline Grid**: Go to `View > Baseline Grid Manager` and enable it. Set start to `Top Margin`. Ensure `Body Text` style has "Align to Baseline Grid" enabled. This ensures text lines up perfectly across the spread.
* [ ] **Pre-Flight**: Before export, look for the "Preflight" traffic light in the top toolbar. Resolve all "Overflowing Text" and "Missing Resource" errors.

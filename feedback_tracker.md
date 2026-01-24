# The Red Book - Reader Feedback Tracker

## Status Legend

- 🔴 **Open** - Not yet addressed
- 🟡 **In Progress** - Being worked on
- 🟢 **Resolved** - Implemented/addressed
- ⚪ **Deferred** - Will address later / low priority

---

## Feedback Session 1 — 2026-01-14 (External Reader)

### FB-001: Naming Confusion — "Red Book" Terminology  

**Status:** 🟢 Resolved  
**Type:** Clarity/UX  
**Priority:** High

**Issue:** The term "Red Book" is overloaded:

1. The **manual title** is "The Red Book"
2. The **personal notebook** is called "Red Book" (Chapter 0, line 135)
3. **Logbook entries** at chapter ends may confuse readers about whether these are the same

**Reader Quote:**
> "Referring to the personal notebook as a Red Book might be confusing since the title of the manual is also the Red Book... I thought they might be the same, but the intro also mentions making sure you have a red book before Chapter 6"

**Author Clarification:**

- The main Red Book **includes** logging sections with extra padding at the end
- A **separate, optional renewable logbook** will be available for purchase
- Proceeds support mental health charities

**Proposed Solution:**

- Rename personal notebook to **"Field Journal"** or **"Captain's Log"**
- Keep Logbook Entries as internal prompts within the manual
- Clarify the relationship in the preface and Chapter 0/6

---

### FB-002: Mixed List Types in Operator's Orders  

**Status:** 🟢 Resolved  
**Type:** Structure/UX  
**Priority:** Medium

**Issue:** "Operator's Orders" sections contain both:

- **Information items** (facts/concepts)
- **Action items** (things to do)

**Reader Quote:**
> "When listing the Operator's Orders at the end of each chapter, the list has a mix of information items and action items... I'd consider maybe splitting it into two lists"

**Proposed Solution:**

- Split into **"Operator's Notes"** (key takeaways/concepts)
- Keep **"Operator's Orders"** for action items only
- OR: Use visual markers (e.g., ▸ for actions, • for notes)

---

### FB-003: Missing Hyperlinks for Self-References  

**Status:** 🟢 Resolved  
**Type:** Navigation/UX  
**Priority:** Medium

**Issue:** Internal references to chapters/sections lack hyperlinks, making navigation difficult.

**Reader Quote:**
> "Adding hyperlinks to all the self-references throughout the book to chapters and sections would be really useful... Especially in the intro where you reference medevac for crises"

**Example Locations:**

- Line 34: "see Chapter 17 and Appendix MEDEVAC"
- Various chapter cross-references throughout

**Proposed Solution:**

- Add markdown anchor links for HTML/EPUB versions
- Format: `[Chapter 17](#chapter-17-protocol-mayday)`

---

## Future Feedback Sessions

_Space for additional external feedback to be logged here_

---

## Feedback Integration Notes

### Business Model Context

- **Built-in logging sections:** The main manual has logging pages at the end
- **Optional Logbook:** Separate purchasable journal with:
  - Renewable/reorderable format
  - Proceeds support author/community
  - Donations to mental health charities

### Terminology Decision Matrix

| Current Term | Proposed Alternative | Rationale |
|--------------|---------------------|-----------|
| Red Book (notebook) | Field Journal | Avoids conflict with manual title |
| Red Book (manual) | The Red Book (capitalized) | Keep as-is, it's the brand |
| Logbook Entry | Field Journal Entry | Aligns with renamed notebook |
| Official Red Book | Official Field Journal | For purchasable product |

# Fix script for Red Book manuscript
import re

MANUSCRIPT = r"O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Manu_FINAL.md"

with open(MANUSCRIPT, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Remove misplaced Chapter 8 Operator's Orders (between "Let us begin." and "# TABLE OF CONTENTS")
# This block was incorrectly inserted after the preface
pattern = r'(Let us begin\.\s*)\n\n\*\*OPERATOR\'S ORDERS — CHAPTER 8\*\*.*?(?=\n---\n\n# TABLE OF CONTENTS)'
content = re.sub(pattern, r'\1', content, flags=re.DOTALL)

# Fix 2: Replace all instances of "" (double quotes used as em-dash placeholder) with actual em-dash
content = content.replace('""', '—')

# Fix 3: Also replace the pattern \" " with em-dash if any remain
content = content.replace('" "', '—')

# Fix 4: Fix TOC entries that may have wrong em-dash representation
content = content.replace('" —', '—')
content = content.replace('— "', '—')

with open(MANUSCRIPT, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(MANUSCRIPT, 'r', encoding='utf-8') as f:
    new_content = f.read()
    
lines = new_content.split('\n')
print(f"Total lines: {len(lines)}")
print(f"Contains misplaced Ch8 Orders: {'CHAPTER 8' in new_content[:3000]}")
print(f"Contains double-quote artifacts: {'\"\"' in new_content}")

# Show lines 45-70 to verify
print("\nLines 45-70:")
for i, line in enumerate(lines[44:70], start=45):
    print(f"{i}: {line[:80]}")

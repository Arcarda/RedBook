import re
import collections

def scan_manuscript():
    path = r'O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Manu_FINAL.md'
    
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    report = []
    
    # 1. Repeated Words (e.g., "the the")
    report.append("### 1. REPEATED WORDS")
    repeated_pattern = re.compile(r'\b(\w+)\s+\1\b', re.IGNORECASE)
    found_repeats = False
    for i, line in enumerate(lines):
        matches = repeated_pattern.findall(line)
        for match in matches:
            report.append(f"Line {i+1}: '{match} {match}'")
            found_repeats = True
    if not found_repeats:
        report.append("None found.")
    report.append("")

    # 2. Capitalization Consistency (Operator / Passenger)
    report.append("### 2. CAPITALIZATION CONSISTENCY")
    terms = ["Operator", "Passenger", "Red Book", "Field Journal"]
    for term in terms:
        lower_term = term.lower()
        # Find instances where it is lowercase but likely shouldn't be
        # We look for the word (case insensitive) and check if it exactly matches the title case
        pattern = re.compile(r'\b' + re.escape(lower_term) + r'\b', re.IGNORECASE)
        for i, line in enumerate(lines):
            for match in pattern.finditer(line):
                word = match.group()
                if word != term and word != term.upper() and i > 50: # Skip front matter
                    # Ignore common false positives if necessary
                    report.append(f"Line {i+1}: Found '{word}' instead of '{term}'")
    report.append("")
    
    # 3. Common Weasel Words
    report.append("### 3. WEASEL WORDS (Overused qualifiers)")
    weasels = ["very", "really", "literally", "just", "perhaps"]
    for w in weasels:
        count = len(re.findall(r'\b' + w + r'\b', text, re.IGNORECASE))
        report.append(f"'{w}': {count} occurrences")
        
    # Write Report
    report_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Publishing\proofing_report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(report))
        
    print(f"Proofing report generated at: {report_path}")

if __name__ == '__main__':
    scan_manuscript()

import os

def generate_field_journal():
    output_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Field_Journal_Interior.md'
    
    content = []
    
    # Front Matter
    content.append("# OFFICIAL FIELD JOURNAL\n")
    content.append("*Companion to The Red Book*\n")
    content.append("\\newpage\n\n")

    # Property Of
    content.append("## PROPERTY OF:\n\n")
    content.append("______________________________________\n\n")
    content.append("______________________________________\n\n")
    content.append("If found, please return to the above address.\n")
    content.append("\\newpage\n\n")

    # Standing Orders
    content.append("# STANDING ORDERS\n\n")
    content.append("Draft your non-negotiable principles here. Refer to Chapter 4 of The Red Book.\n\n")
    for i in range(1, 11):
        content.append(f"**ORDER {i}:** ___________________________________________________________________\n\n")
        content.append("_____________________________________________________________________________\n\n")
    content.append("\\newpage\n\n")

    # Daily Logs (90 Days)
    for day in range(1, 91):
        content.append(f"# DAY {day}\n\n")
        
        # Morning Watch
        content.append("### MORNING WATCH\n\n")
        content.append("**1. Primary Objective:**\n\n")
        content.append("_____________________________________________________________________________\n\n")
        content.append("**2. Anticipated Friction:**\n\n")
        content.append("_____________________________________________________________________________\n\n")
        content.append("**3. The Protocol:**\n\n")
        content.append("_____________________________________________________________________________\n\n")
        
        content.append("---\n\n")
        
        # Evening Debrief
        content.append("### EVENING DEBRIEF\n\n")
        content.append("**1. The Win:**\n\n")
        content.append("_____________________________________________________________________________\n\n")
        content.append("**2. The Drift (Where did I lose the wheel?):**\n\n")
        content.append("_____________________________________________________________________________\n\n")
        content.append("**3. Final Score (1-10):** ______\n\n")
        
        content.append("\\newpage\n\n")

    # Damage Reports (10 Pages)
    content.append("# DAMAGE REPORTS\n\n")
    content.append("*Use these pages when a mutiny occurs. Protocol: Label it. Analyze it. Reset.*")
    content.append("\\newpage\n\n")
    
    for i in range(1, 11):
        content.append(f"## INCIDENT REPORT #{i}\n\n")
        content.append("**Date/Time:** _________________\n\n")
        content.append("**Trigger (H.A.L.T.?):** _____________________________________________________________\n\n")
        content.append("**The Mutiny Script Used:** ________________________________________________________\n\n")
        content.append("**Corrective Action Taken:** _______________________________________________________\n\n")
        content.append("_____________________________________________________________________________\n\n")
        content.append("_____________________________________________________________________________\n\n")
        content.append("\\newpage\n\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(content))
    
    print(f"Field Journal Markdown created at: {output_path}")

if __name__ == '__main__':
    generate_field_journal()

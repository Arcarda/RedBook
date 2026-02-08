import markdown
import os
import re

def create_field_journal_layout():
    css_path = 'layout.css'
    output_path = 'Field_Journal_App.html'
    
    # Static content defined here for control, or could read from file and parse
    # For structure, defining the templates in code allows loop generation easier
    
    morning_template = """
<div class="morning-watch">
    <h2>Morning Watch</h2>
    <p><strong>Day:</strong> <span class="form-line short"></span> &nbsp;&nbsp;&nbsp; <strong>Date:</strong> <span class="form-line short"></span></p>
    
    <p><strong>H.A.L.T. Check:</strong> <span class="checkbox"></span>Hungry <span class="checkbox"></span>Angry <span class="checkbox"></span>Lonely <span class="checkbox"></span>Tired</p>
    
    <h3>1. Primary Objective</h3>
    <p>What is the ONE thing that makes today successful?</p>
    <span class="form-line"></span>
    <span class="form-line"></span>
    
    <h3>2. Threat Assessment</h3>
    <p>Where are the traps? (Calendar, events, triggers)</p>
    <span class="form-line"></span>
    <span class="form-line"></span>
    
    <h3>3. Passenger Alert</h3>
    <p>What is the resistance telling you right now?</p>
    <span class="form-line"></span>
    <span class="form-line"></span>
    
    <div style="flex-grow:1;"></div>
    <p style="text-align:center; font-style:italic;">"Motion creates emotion."</p>
</div>
"""

    evening_template = """
<div class="evening-debrief">
    <h2>Evening Debrief</h2>
    
    <h3>1. The Win</h3>
    <p>One thing I did well today.</p>
    <span class="form-line"></span>
    <span class="form-line"></span>
    
    <h3>2. The Variance</h3>
    <p>Where did I drift? Why?</p>
    <span class="form-line"></span>
    <span class="form-line"></span>
    
    <h3>3. Tomorrow's Anchor</h3>
    <p>One commitment for tomorrow to sharpen the line.</p>
    <span class="form-line"></span>
    <span class="form-line"></span>

    <div style="flex-grow:1;"></div>
    <div class="operators-order" style="margin-bottom:0;">
        <h3>Daily Rating</h3>
        <p>Sleep: ___ / Fuel: ___ / Move: ___</p>
    </div>
</div>
"""

    sitrep_template = """
<div class="sitrep">
    <h2>Weekly S.I.T.R.E.P.</h2>
    <p><strong>Week of:</strong> <span class="form-line"></span></p>
    
    <h3>Wins This Week</h3>
    <span class="form-line"></span>
    <span class="form-line"></span>
    <span class="form-line"></span>
    
    <h3>The Drift</h3>
    <p>Where did the ship lose speed or course this week?</p>
    <span class="form-line"></span>
    <span class="form-line"></span>
    
    <h3>Pattern Spotted</h3>
    <p>What script did the Passenger use most?</p>
    <span class="form-line"></span>
    
    <h3>Next Week Focus</h3>
    <span class="form-line"></span>
</div>
<div class="page-break" style="page-break-before: always;"></div>
<div class="notes-page">
    <h2>Field Notes</h2>
    <!-- Ruled lines -->
    <div style="background-image: repeating-linear-gradient(white 0px, white 29px, black 30px); height: 100%; width: 100%;"></div>
</div>
"""

    # Intro content (simplified for now)
    intro_html = """
    <div class="intro">
        <h1>The Field Journal</h1>
        <p>This is your operational log. It is not a diary. It is a tool for self-command.</p>
        <div class="page-break" style="page-break-before: always;"></div>
    </div>
    """

    # Generate the Sequence
    print("Generating 90-day sequence...")
    journal_body = intro_html
    
    days = 90
    for day in range(1, days + 1):
        journal_body += f'<!-- Day {day} -->\n'
        journal_body += morning_template
        journal_body += evening_template
        
        # Every 7 days, add SITREP
        if day % 7 == 0:
            journal_body += sitrep_template

    # CSS Reading
    css_content = ""
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()

    # Assemble Full HTML
    full_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>The Field Journal</title>
        <style>
            {css_content}
            /* Specific overrides for visuals */
            .page-break {{ page-break-after: always; }}
        </style>
    </head>
    <body>
        {journal_body}
    </body>
    </html>
    '''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Field Journal HTML created at: {output_path}")

if __name__ == '__main__':
    create_field_journal_layout()

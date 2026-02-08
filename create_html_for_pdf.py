import markdown
import os
import re

def create_html_for_pdf():
    manuscript_path = 'Red_Book_Manu_FINAL.md'
    css_path = 'layout.css'
    output_path = 'Red_Book_Manu_App.html'
    
    # Read Manuscript
    with open(manuscript_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Read CSS
    css_content = ""
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
    else:
        print(f"Warning: {css_path} not found.")

    # ---------------------------------------------------------
    # Pre-processing: Wrap specific sections in DIVs
    # ---------------------------------------------------------
    
    # 1. Wrap Operator's Orders
    # Pattern: Look for **OPERATOR'S ORDERS...** followed by a list, ending at double newline or next header
    # We use a pattern that captures the header and the list following it
    order_pattern = re.compile(r'(\*\*OPERATOR\'S ORDERS — CHAPTER.*?\*\*\n\n(?:(?:\d+\.|-).*?\n)+)', re.DOTALL)
    
    def wrap_order(match):
        content = match.group(1)
        # Convert the bold header to an h3 inside the div for better styling control
        content = re.sub(r'\*\*(OPERATOR\'S ORDERS — CHAPTER.*?)\*\*', r'<h3>\1</h3>', content)
        return f'<div class="operators-order">\n{content}\n</div>'

    text = order_pattern.sub(wrap_order, text)

    # 2. Wrap Operator's Notes (Optional, if we want them distinct)
    # Using similar pattern if needed. For now, let's treat them similarly or just let them be.
    # Let's wrap them in a similar box but maybe a different class if we define one later.
    # For now reusing operators-order style or just leaving as is? 
    # The CSS had .operators-order. Let's make a Notes one too if needed, 
    # but the prompt specifically mentioned "Operator's Orders".
    # I'll wrap Notes too for consistency but maybe give it a generic "box" or same class if appropriate.
    # Actually, let's stick to the specific request first.

    # ---------------------------------------------------------
    # HTML Conversion
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    # HTML Conversion
    # ---------------------------------------------------------
    html_body = markdown.markdown(text, extensions=['extra', 'toc', 'smarty'])

    # Application of "Class Mapping" for Affinity Import Simulation
    # We add classes that match our CSS / Affinity Styles
    html_body = html_body.replace('<p>', '<p class="body-text">')
    html_body = html_body.replace('<h1>', '<h1 class="part-title">')
    html_body = html_body.replace('<h2>', '<h2 class="section-header">')
    html_body = html_body.replace('<h3>', '<h3 class="subsection-header">')
    html_body = html_body.replace('<blockquote>', '<blockquote class="blockquote">')

    # Assemble Full HTML
    full_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>The Red Book: Field Manual</title>
        <style>
            {css_content}
        </style>
    </head>
    <body>
        <div class="book-container">
            {html_body}
        </div>
    </body>
    </html>
    '''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"HTML created at: {output_path}")

if __name__ == '__main__':
    create_html_for_pdf()

import markdown
import os

def create_html_for_pdf():
    manuscript_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Manu_FINAL.md'
    output_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Field_Manual.html'
    
    with open(manuscript_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Convert to HTML
    html_content = markdown.markdown(text, extensions=['extra', 'toc'])

    # Application of "Field Manual" Styling
    full_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>The Red Book: Field Manual</title>
        <style>
            @page {{
                size: A5;
                margin: 20mm;
            }}
            body {{
                font-family: "Georgia", serif;
                line-height: 1.5;
                color: #1a1a1a;
                font-size: 11pt;
            }}
            h1, h2, h3 {{
                font-family: "Arial", sans-serif;
                color: #8B0000; /* Dark Red */
                page-break-after: avoid;
            }}
            h1 {{
                text-align: center;
                text-transform: uppercase;
                border-bottom: 2px solid #8B0000;
                padding-bottom: 10px;
                margin-top: 2em;
                page-break-before: always;
            }}
            h2 {{
                border-bottom: 1px solid #ccc;
                padding-bottom: 5px;
                margin-top: 1.5em;
            }}
            blockquote {{
                font-style: italic;
                border-left: 4px solid #8B0000;
                margin: 1.5em 2em;
                padding-left: 1em;
                background-color: #f9f9f9;
                padding: 10px;
            }}
            code, pre {{
                background-color: #f0f0f0;
                font-family: "Consolas", monospace;
                padding: 2px 4px;
                border-radius: 3px;
            }}
            hr {{
                border: 0;
                height: 1px;
                background: #8B0000;
                margin: 2em 0;
            }}
            p {{
                margin-bottom: 1em;
                text-align: justify;
            }}
            /* Specific formatting for the Logbook entries */
            strong {{
                color: #000;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    '''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"HTML created at: {output_path}")

if __name__ == '__main__':
    create_html_for_pdf()

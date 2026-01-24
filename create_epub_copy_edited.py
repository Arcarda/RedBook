import os
import re
import markdown
from ebooklib import epub


def apply_copy_edits(text: str) -> str:
    """
    Applies copy editing fixes to the manuscript text.
    Fixes encoding issues, punctuation, and minor orthographic errors.
    """
    # Fix corrupted em-dashes (common encoding issue from copy/paste)
    # These appear as various corrupted sequences
    text = text.replace('""', '—')
    text = text.replace('"—"', '—')
    text = text.replace('â€"', '—')
    
    # Fix any leftover mojibake patterns for em-dashes
    text = re.sub(r'â€"', '—', text)
    
    # Fix curly quotes that may have encoding issues
    text = text.replace(''', "'")
    text = text.replace(''', "'")
    text = text.replace('"', '"')
    text = text.replace('"', '"')
    
    # Fix ellipses that may have encoding issues
    text = text.replace('â€¦', '…')
    
    # Normalize multiple spaces (but not indentation)
    text = re.sub(r'([^\n]) {2,}', r'\1 ', text)
    
    # Normalize line endings
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')
    
    return text


def create_copy_edited_epub():
    """
    Creates a Kindle-optimized EPUB from the Red Book manuscript,
    applying copy editing fixes during conversion.
    """
    book = epub.EpubBook()

    # Set metadata
    book.set_identifier('redbook-fieldmanual-002')
    book.set_title('The Red Book')
    book.set_language('en')
    book.add_author('Manual of Self-Command')
    book.add_metadata('DC', 'description', 
                      'A Field Manual for Self-Command. A comprehensive guide to understanding the internal conflict between the Passenger (limbic system) and the Operator (prefrontal cortex), with protocols for building self-mastery.')

    # Read manuscript
    manuscript_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Manu_FINAL.md'
    with open(manuscript_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Apply copy edits
    print("Applying copy edits...")
    text = apply_copy_edits(text)
    print(f"  - Fixed encoding issues")
    print(f"  - Normalized spacing and line endings")

    # Convert Markdown to HTML
    # Using extensions for better formatting
    print("Converting Markdown to HTML...")
    html_content = markdown.markdown(
        text, 
        extensions=[
            'extra',       # Fenced code blocks, tables, etc.
            'toc',         # Table of contents
            'smarty',      # Smart quotes and dashes
            'sane_lists',  # Better list handling
        ]
    )

    # Create enhanced stylesheet for Kindle
    style = '''
        @namespace epub "http://www.idpf.org/2007/ops";
        
        body { 
            font-family: "Georgia", "Times New Roman", serif; 
            margin: 5%; 
            text-align: justify;
            line-height: 1.6;
        }
        
        h1 { 
            text-align: center; 
            text-transform: uppercase; 
            color: #1a1a1a; 
            margin-top: 2em;
            margin-bottom: 1em;
            font-size: 1.8em;
            border-bottom: 2px solid #333;
            padding-bottom: 0.5em;
        }
        
        h2 { 
            color: #333;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-size: 1.4em;
        }
        
        h3 {
            color: #444;
            margin-top: 1.2em;
            font-size: 1.2em;
        }
        
        h4 {
            color: #555;
            font-size: 1em;
            font-style: italic;
        }
        
        p {
            text-indent: 1.5em;
            margin: 0.5em 0;
        }
        
        p:first-of-type,
        h1 + p,
        h2 + p,
        h3 + p {
            text-indent: 0;
        }
        
        blockquote { 
            font-style: italic; 
            margin: 1em 2em; 
            border-left: 4px solid #666; 
            padding-left: 1em;
            color: #444;
        }
        
        ul, ol {
            margin: 1em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.3em 0;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
            font-size: 0.9em;
        }
        
        th, td {
            border: 1px solid #ccc;
            padding: 0.5em;
            text-align: left;
        }
        
        th {
            background-color: #f5f5f5;
            font-weight: bold;
        }
        
        code {
            font-family: "Courier New", monospace;
            background-color: #f5f5f5;
            padding: 0.1em 0.3em;
            font-size: 0.9em;
        }
        
        pre {
            background-color: #f5f5f5;
            padding: 1em;
            overflow-x: auto;
            font-size: 0.85em;
            line-height: 1.4;
        }
        
        hr {
            border: none;
            border-top: 1px solid #ccc;
            margin: 2em 0;
        }
        
        strong {
            font-weight: bold;
        }
        
        em {
            font-style: italic;
        }
        
        /* Operator's Orders sections */
        p strong:first-child {
            color: #333;
        }
        
        .toc { 
            list-style-type: none; 
        }
    '''
    nav_css = epub.EpubItem(
        uid="style_nav", 
        file_name="style/nav.css", 
        media_type="text/css", 
        content=style
    )
    book.add_item(nav_css)

    # Create the main chapter
    c1 = epub.EpubHtml(title='The Red Book', file_name='manuscript.xhtml', lang='en')
    c1.content = f'<html><head><link rel="stylesheet" type="text/css" href="style/nav.css" /></head><body>{html_content}</body></html>'
    book.add_item(c1)

    # Add Cover
    cover_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Publishing\cover_minimal_2_black.png'
    if os.path.exists(cover_path):
        print("Adding cover image...")
        with open(cover_path, 'rb') as f:
            book.set_cover("cover.png", f.read())
    else:
        print(f"Warning: Cover not found at {cover_path}")

    # Define Table of Contents
    book.toc = (
        epub.Link('manuscript.xhtml', 'The Red Book', 'main'),
    )

    # Add default NCX and Nav pages
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define Spine (reading order)
    book.spine = ['nav', c1]

    # Write EPUB
    output_path = r'O:\Antigravity\Workspaces\Writing\RedBook\The_Red_Book_CopyEdited.epub'
    print(f"Writing EPUB to: {output_path}")
    epub.write_epub(output_path, book, {})
    
    print("\n" + "="*60)
    print("EPUB created successfully!")
    print(f"File: {output_path}")
    print("="*60)
    
    # Verify file size
    if os.path.exists(output_path):
        size_kb = os.path.getsize(output_path) / 1024
        print(f"File size: {size_kb:.1f} KB")


if __name__ == '__main__':
    create_copy_edited_epub()

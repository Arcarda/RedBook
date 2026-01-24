import os
import markdown
import ebooklib
from ebooklib import epub

def create_epub():
    book = epub.EpubBook()

    # Set metadata
    book.set_identifier('redbook-fieldmanual-001')
    book.set_title('The Red Book')
    book.set_language('en')
    book.add_author('Manual of Self-Command')

    # Read manuscript
    manuscript_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Manu_FINAL.md'
    with open(manuscript_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Convert Markdown to HTML
    # We use some extensions for better Kindle compatibility
    html_content = markdown.markdown(text, extensions=['extra', 'toc'])

    # Add stylesheet
    style = '''
        @namespace epub "http://www.idpf.org/2007/ops";
        body { font-family: "Georgia", serif; margin: 5%; text-align: justify; }
        h1 { text-align: center; text-transform: uppercase; color: #333; margin-top: 2em; }
        h2 { border-bottom: 2px solid #333; padding-bottom: 5px; margin-top: 1.5em; }
        blockquote { font-style: italic; margin: 1em 2em; border-left: 4px solid #333; padding-left: 1em; }
        .toc { list-style-type: none; }
    '''
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # Create Chapter
    c1 = epub.EpubHtml(title='The Red Book', file_name='manuscript.xhtml', lang='en')
    c1.content = f'<html><head><link rel="stylesheet" type="text/css" href="style/nav.css" /></head><body>{html_content}</body></html>'
    book.add_item(c1)

    # Add Cover
    cover_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Publishing\cover_minimal_2_black.png'
    if os.path.exists(cover_path):
        with open(cover_path, 'rb') as f:
            book.set_cover("cover.png", f.read())
    else:
        print(f"Warning: Cover not found at {cover_path}")

    # Define Table of Contents
    book.toc = (epub.Link('manuscript.xhtml', 'Introduction', 'intro'),
                (epub.Section('The Manual'),
                 (epub.Link('manuscript.xhtml', 'Contents', 'toc'),))
               )

    # Add default NCX and Nav pages
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define Spine
    book.spine = ['nav', c1]

    # Write EPUB
    output_path = r'O:\Antigravity\Workspaces\Writing\RedBook\Red_Book_Field_Manual.epub'
    epub.write_epub(output_path, book, {})
    print(f"EPUB created successfully at: {output_path}")

if __name__ == '__main__':
    create_epub()

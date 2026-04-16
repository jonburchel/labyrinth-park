"""
Convert provisional patent application from Markdown to a clean,
print-ready HTML file suitable for Print-to-PDF for USPTO filing.
Also generates password-protected PDF for confidential sharing.
"""

import markdown
import os
import glob
import sys

PATENT_DIR = os.path.join(os.path.dirname(__file__))
MD_FILE = os.path.join(PATENT_DIR, 'provisional-application.md')
HTML_FILE = os.path.join(PATENT_DIR, 'provisional-application.html')
PDF_FILE = os.path.join(PATENT_DIR, 'provisional-application.pdf')
PDF_PROTECTED = os.path.join(PATENT_DIR, 'provisional-application-CONFIDENTIAL.pdf')
DRAWINGS_DIR = os.path.join(PATENT_DIR, 'drawings')

# Read markdown
with open(MD_FILE, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Strip the filing instructions section (not part of the patent itself)
cut_marker = '## FILING INSTRUCTIONS'
if cut_marker in md_content:
    md_content = md_content[:md_content.index(cut_marker)]

# Convert to HTML
html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

# Build image references for drawings
drawing_files = sorted(glob.glob(os.path.join(DRAWINGS_DIR, '*.png')))
drawings_html = '<div class="drawings-section"><h2>DRAWINGS</h2>\n'
for img_path in drawing_files:
    fname = os.path.basename(img_path)
    drawings_html += f'<div class="drawing"><img src="drawings/{fname}" alt="{fname}"><p class="caption">{fname.replace(".png","").replace("_"," ").title()}</p></div>\n'
drawings_html += '</div>'

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Provisional Patent Application - Autonomously Reconfigurable Living Landscape Maze System</title>
<style>
  @page {{
    size: letter;
    margin: 1in;
  }}
  body {{
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #000;
    max-width: 7.5in;
    margin: 0 auto;
    padding: 0.5in;
  }}
  h1 {{
    font-size: 16pt;
    text-align: center;
    border-bottom: 2px solid #000;
    padding-bottom: 10pt;
    margin-top: 0;
  }}
  h2 {{
    font-size: 14pt;
    margin-top: 24pt;
    border-bottom: 1px solid #666;
    padding-bottom: 4pt;
    page-break-after: avoid;
  }}
  h3 {{
    font-size: 12pt;
    margin-top: 18pt;
    page-break-after: avoid;
  }}
  p {{
    text-align: justify;
    margin: 6pt 0;
  }}
  ul, ol {{
    margin: 6pt 0 6pt 24pt;
  }}
  li {{
    margin: 3pt 0;
  }}
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 12pt 0;
    font-size: 11pt;
  }}
  th, td {{
    border: 1px solid #000;
    padding: 4pt 8pt;
    text-align: left;
  }}
  th {{
    background: #eee;
    font-weight: bold;
  }}
  hr {{
    border: none;
    border-top: 1px solid #999;
    margin: 18pt 0;
  }}
  strong {{
    font-weight: bold;
  }}
  .drawings-section {{
    page-break-before: always;
  }}
  .drawing {{
    page-break-inside: avoid;
    text-align: center;
    margin: 24pt 0;
  }}
  .drawing img {{
    max-width: 100%;
    max-height: 8in;
    border: 1px solid #ccc;
  }}
  .caption {{
    font-style: italic;
    font-size: 10pt;
    margin-top: 4pt;
  }}
  @media print {{
    body {{
      padding: 0;
    }}
    .no-print {{
      display: none;
    }}
  }}
</style>
</head>
<body>

<div class="no-print" style="background:#ffffcc; border:2px solid #cc0; padding:12px; margin-bottom:24px; font-family:sans-serif; font-size:10pt;">
  <strong>FILING INSTRUCTIONS:</strong> Open this file in Chrome or Edge. Press Ctrl+P.
  Set destination to "Save as PDF". Set margins to "Default". Ensure "Background graphics" is checked.
  Save the PDF. Upload to <a href="https://patentcenter.uspto.gov">USPTO Patent Center</a> as your provisional application.
</div>

{html_body}

{drawings_html}

</body>
</html>
"""

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Created {HTML_FILE}")

# Generate PDF using playwright
password = None
if len(sys.argv) > 1:
    password = sys.argv[1]

try:
    from playwright.sync_api import sync_playwright
    print("Generating PDF...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f'file:///{os.path.abspath(HTML_FILE).replace(chr(92), "/")}')
        page.wait_for_load_state('networkidle')
        # Hide the no-print banner
        page.evaluate('document.querySelectorAll(".no-print").forEach(e => e.style.display = "none")')
        page.pdf(
            path=PDF_FILE,
            format='Letter',
            margin={'top': '0.75in', 'right': '0.75in', 'bottom': '0.75in', 'left': '0.75in'},
            print_background=True
        )
        browser.close()
    print(f"Created {PDF_FILE}")

    # Create password-protected version
    if password:
        from pypdf import PdfReader, PdfWriter
        reader = PdfReader(PDF_FILE)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        # Add confidential watermark-style metadata
        writer.add_metadata({
            '/Title': 'CONFIDENTIAL - Provisional Patent Application',
            '/Subject': 'Autonomously Reconfigurable Living Landscape Maze System',
            '/Creator': 'Labyrinth Park LLC',
            '/Keywords': 'CONFIDENTIAL, PATENT PENDING, DO NOT DISTRIBUTE'
        })
        writer.encrypt(user_password=password, owner_password=password,
                      permissions_flag=0b0000)  # no permissions (no copy, no print without password)
        with open(PDF_PROTECTED, 'wb') as f:
            writer.write(f)
        print(f"Created {PDF_PROTECTED}")
        print(f"  Password: {password}")
        print(f"  Encrypted, no-copy, no-print without password")
    else:
        print(f"  (Run with password argument to create encrypted version:")
        print(f"   python build_pdf.py YourPassword123)")

except ImportError as e:
    print(f"  PDF generation requires playwright and pypdf: {e}")
    print(f"  Fallback: Open {HTML_FILE} in Chrome -> Ctrl+P -> Save as PDF")

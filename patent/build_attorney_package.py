"""
Convert patent-package markdown files to professional HTML + PDF.
Uses the same Playwright-based approach as build_pdf.py.
"""

import markdown
import os
import sys

PATENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Files to convert (filename stem -> title)
TARGETS = {
    "attorney-cover-letter": "Attorney Briefing: Universal Modular Landscape Infrastructure Platform",
    "expert-review-wave1": "Expert Review Wave 1: Collated Findings",
    "expert-review-wave2": "Expert Review Wave 2: Collated Results",
    "expert-review-round2": "Expert Review Round 2: Compiled Results",
}

CSS = """
@page {
    size: letter;
    margin: 1in;
}
body {
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #000;
    max-width: 7.5in;
    margin: 0 auto;
    padding: 0.5in;
}
.confidential-header {
    text-align: center;
    font-size: 10pt;
    font-weight: bold;
    color: #990000;
    border-bottom: 2px solid #990000;
    padding-bottom: 6pt;
    margin-bottom: 24pt;
    letter-spacing: 2pt;
}
h1 {
    font-size: 16pt;
    text-align: center;
    border-bottom: 2px solid #000;
    padding-bottom: 10pt;
    margin-top: 0;
}
h2 {
    font-size: 14pt;
    margin-top: 24pt;
    border-bottom: 1px solid #666;
    padding-bottom: 4pt;
    page-break-after: avoid;
}
h3 {
    font-size: 12pt;
    margin-top: 18pt;
    page-break-after: avoid;
}
h4 {
    font-size: 11pt;
    margin-top: 14pt;
    page-break-after: avoid;
}
p {
    text-align: justify;
    margin: 6pt 0;
}
ul, ol {
    margin: 6pt 0 6pt 24pt;
}
li {
    margin: 3pt 0;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12pt 0;
    font-size: 10pt;
}
th, td {
    border: 1px solid #000;
    padding: 4pt 8pt;
    text-align: left;
}
th {
    background: #eee;
    font-weight: bold;
}
hr {
    border: none;
    border-top: 1px solid #999;
    margin: 18pt 0;
}
strong {
    font-weight: bold;
}
code {
    font-family: 'Courier New', monospace;
    font-size: 10pt;
    background: #f4f4f4;
    padding: 1pt 4pt;
}
blockquote {
    margin: 12pt 24pt;
    padding: 6pt 12pt;
    border-left: 3pt solid #ccc;
    font-style: italic;
}
@media print {
    body {
        padding: 0;
    }
}
"""


def build_html(stem, title):
    md_path = os.path.join(PATENT_DIR, f"{stem}.md")
    html_path = os.path.join(PATENT_DIR, f"{stem}.html")

    if not os.path.exists(md_path):
        print(f"  SKIP {md_path} (not found)")
        return None

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(
        md_content, extensions=["tables", "fenced_code"]
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="confidential-header">
CONFIDENTIAL &mdash; Labyrinth Park LLC
</div>

{html_body}

</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  HTML -> {html_path}")
    return html_path


def build_pdfs(html_files):
    """Generate PDFs from HTML files using Playwright."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for html_path in html_files:
            pdf_path = html_path.replace(".html", ".pdf")
            page = browser.new_page()
            file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
            page.goto(file_url)
            page.wait_for_load_state("networkidle")
            page.pdf(
                path=pdf_path,
                format="Letter",
                margin={
                    "top": "0.75in",
                    "right": "0.75in",
                    "bottom": "0.75in",
                    "left": "0.75in",
                },
                print_background=True,
            )
            page.close()
            print(f"  PDF  -> {pdf_path}")

        browser.close()


def main():
    print("Building attorney package...\n")

    html_files = []
    for stem, title in TARGETS.items():
        result = build_html(stem, title)
        if result:
            html_files.append(result)

    if not html_files:
        print("\nNo HTML files generated. Nothing to convert to PDF.")
        return

    print(f"\nGenerating {len(html_files)} PDFs...")
    try:
        build_pdfs(html_files)
    except ImportError as e:
        print(f"\n  PDF generation requires playwright: {e}")
        print("  Install with: pip install playwright && python -m playwright install chromium")
        return

    print(f"\nDone. {len(html_files)} HTML + PDF pairs created.")


if __name__ == "__main__":
    main()

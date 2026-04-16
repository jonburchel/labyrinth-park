import markdown
import os

with open("legal/nda-template.md", "r") as f:
    md = f.read()

body = markdown.markdown(md, extensions=["tables"])

html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<title>Non-Disclosure Agreement - Labyrinth Park LLC</title>
<style>
@page {{ size: letter; margin: 1in; }}
body {{ font-family: 'Times New Roman', serif; font-size: 12pt; line-height: 1.5;
       max-width: 7in; margin: 0 auto; padding: 0.5in; color: #000; }}
h1 {{ font-size: 16pt; text-align: center; margin-top: 0; }}
h2 {{ font-size: 13pt; margin-top: 18pt; }}
p {{ text-align: justify; }}
strong {{ font-weight: bold; }}
hr {{ border: none; border-top: 2px solid #000; margin: 24pt 0; }}
</style></head><body>{body}</body></html>"""

with open("legal/nda-template.html", "w") as f:
    f.write(html)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{os.path.abspath('legal/nda-template.html').replace(chr(92), '/')}")
    page.wait_for_load_state("networkidle")
    page.pdf(path="legal/nda-template.pdf", format="Letter",
             margin=dict(top="1in", right="1in", bottom="1in", left="1in"))
    browser.close()

print("Created legal/nda-template.html")
print("Created legal/nda-template.pdf")
print("Ready for DocuSign upload")

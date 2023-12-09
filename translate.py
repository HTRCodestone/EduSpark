import subprocess
import os
import markdownify
from bs4 import BeautifulSoup
import re

def process_html(input_html, output_html):
    # Open and read the HTML file
    with open(input_html, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove all image tags
    for img in soup.find_all('img'):
        img.decompose()

    # Convert bolded text to headers (h2)
    for bold_tag in soup.find_all(['b', 'strong']):
        bold_tag.name = 'h2'

    # Replace non-ASCII characters wiith whitespace
    processed_html = re.sub(r'[^\x00-\x7F]+', ' ', str(soup))

    # Write the processed HTML to a new file
    with open(output_html, 'w', encoding='utf-8') as file:
        file.write(processed_html)


def convert_pdf_to_html(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = ['pdftohtml', '-s', pdf_path, os.path.join(output_dir, 'output.html')]
    subprocess.run(command)

def fast_down(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    markdown = markdownify.markdownify(html)
    return markdown

def process_markdown(input_md, output_md):
    with open(input_md, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Fixing hyphenated line breaks
    md_content = re.sub(r'(\w)-\n(\w)', r'\1\2', md_content)

    # Correcting headers: Assuming headers are in the style '*Header Name:*'
    md_content = re.sub(r'\*(.+):\*', r'## \1', md_content)

    # Fixing list formatting: Assuming lists are in the style '* list item'
    md_content = re.sub(r'\n\* ', r'\n- ', md_content)

    # Combine separated header letters into a single line
    md_content = re.sub(r'(\b[A-Za-z]\b)\n-+\n\n\n(\b[A-Za-z]\b)', r'\1\2', md_content)

    # Write the processed Markdown to a new file
    with open(output_md, 'w', encoding='utf-8') as file:
        file.write(md_content)

pdf_path = 'test.pdf'  # Replace with your PDF file path
output_dir = r'C:\Users\egeke\Desktop\Development Files\Project\test'    # Replace with your desired output directory
input_html = r'C:\Users\egeke\Desktop\Development Files\Project\test\output-html.html'
output_html = 'output-html.html'

convert_pdf_to_html(pdf_path, output_dir)
process_html(input_html, output_html)
input_markdown = fast_down('output-html.html')


#save markdown to file
with open('test.md', 'w') as f:
    f.write(input_markdown)

input_md = 'test.md'
output_md = 'output-md.md'
process_markdown(input_md, output_md)
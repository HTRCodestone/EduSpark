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

    # Remove all HTML comments
    md_content = re.sub(r'<!--.*?-->', '', md_content, flags=re.DOTALL)

    # Reduce multiple new lines to two
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)

    # Remove a specific string
    specific_string = 'C:\\Users\\egeke\\Desktop\\Development Files\\Project\\test\\output-html.html'
    md_content = md_content.replace(specific_string, '')

    # Combine fragmented header lines
    md_content = re.sub(r'((?:\b[A-Za-z]+\b\n-+\n\n\n)+)([A-Za-z ]+)\n-+', lambda m: " ".join(m.group(0).split()) + '\n', md_content)

    # Replace text
    md_content = replace_text(md_content)

    # Write the processed Markdown to a new file
    with open(output_md, 'w', encoding='utf-8') as file:
        file.write(md_content)

def replace_text(original_text):
    # Define the first text to be replaced and its replacement
    text_to_replace_1 = '''THE ONT
-------

A
-

RIO CURRICUL
------------

UM,
---

GR
--

ADES 9 AND 10
-------------'''
    replacement_text_1 = '''THE ONTARIO CURRICULUM,GRADES 9 AND 10
--------------------------------------'''

    # Define the second text to be replaced and its replacement
    text_to_replace_2 = '''THE PROGR
---------

A
-

M IN ENGLISH
------------'''
    replacement_text_2 = '''THE PROGRAM IN ENGLISH
----------------------'''

    # Replace the texts
    modified_text = original_text.replace(text_to_replace_1, replacement_text_1)
    modified_text = modified_text.replace(text_to_replace_2, replacement_text_2)

    return modified_text

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
import subprocess
import os
import markdownify

def convert_pdf_to_html(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = ['pdftohtml', '-s', pdf_path, os.path.join(output_dir, 'output.html')]
    subprocess.run(command)

def markdownify(path):
    with open(path, 'r') as f:
        html = f.read()
    markdown = markdownify.markdownify(html)
    return markdown

pdf_path = 'test.pdf'  # Replace with your PDF file path
output_dir = r'C:\Users\egeke\Desktop\Development Files\python-codestone\test'    # Replace with your desired output directory



convert_pdf_to_html(pdf_path, output_dir)
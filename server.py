from flask import Flask, send_file, request, rebder_template, abort
import os
import urllib.request
from pymongo import MongoClient
import bleach
import os
import urllib.request

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb_uri')  # Replace 'mongodb_uri' with your MongoDB URI
db = client['your_database']  # Replace 'your_database' with your database name
tasks_collection = db['tasks']

absence_data = {}

@app.route('/absences')
def index():
    return render_template('index.html')

@app.route('/report_absence', methods=['POST'])
def report_absence():
    student_name = request.form.get('student_name')
    absence_reason = request.form.get('absence_reason')

    absence_data[student_name] = absence_reason

    return render_template('absence_recorded.html', student_name=student_name, absence_reason=absence_reason)

@app.route('/view_absences')
def view_absences():
    return render_template('view_absences.html', absence_data=absence_data)

@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()

    # Sanitize inputs
    date = bleach.clean(data.get('date'))
    time = bleach.clean(data.get('time'))
    objective = bleach.clean(data.get('objective'))
    tags = [bleach.clean(tag) for tag in data.get('tags', [])]

    # Construct the task document
    task_document = {
        "taskname": {
            "task date/time": f"{date} {time}",
            "task flags": tags,
            "task objectives": objective
        }
    }

    # Save the task document in MongoDB
    tasks_collection.insert_one(task_document)

    return 'Task created successfully'

@app.route('/download_curriculum', methods=['GET'])
def download_curriculum_endpoint():
    subject = request.args.get('subject')
    grade = request.args.get('grade')

    # Convert grade to integer if possible
    try:
        grade = int(grade)
    except ValueError:
        abort(400, description="Invalid grade. Grade must be an integer.")

    # Call the download_curriculum function
    file_path = download_curriculum(subject, grade)

    if file_path:
        return send_file(file_path, as_attachment=True)
    else:
        abort(400, description="Invalid request parameters.")

def download_curriculum(subject, grade):
    def generate_curriculum_url(sub, grd):
        if sub.lower() == "computer studies":
            return "https://www.edu.gov.on.ca/eng/curriculum/secondary/computer10to12_2008.pdf"

        if sub.lower() == "english":
            return f"https://www.edu.gov.on.ca/eng/curriculum/secondary/english{grd}currb.pdf"

        if sub.lower() == "mathematics":
            return f"https://www.edu.gov.on.ca/eng/curriculum/secondary/math{grd}curr.pdf"

        if sub.lower() == "science":
            if grd in [9, 10]:
                return "https://www.edu.gov.on.ca/eng/curriculum/secondary/science910_2008.pdf"
            elif grd in [11, 12]:
                return "https://www.edu.gov.on.ca/eng/curriculum/secondary/2009science11_12.pdf"

        grade_str = '910' if grd in [9, 10] else str(grd)
        return f"https://www.edu.gov.on.ca/eng/curriculum/secondary/{sub.lower()}{grade_str}curr.pdf"

    def download_file(url, destination):
        urllib.request.urlretrieve(url, destination)

    # Check if the grade is valid (9, 10, 11, or 12)
    if grade not in [9, 10, 11, 12]:
        print("Invalid grade. Please enter a valid grade (9, 10, 11, or 12).")
        return None

    # Generate the URL
    url = generate_curriculum_url(subject, grade)

    # Download the file
    destination = f"{subject.lower()}_grade{grade}_curriculum.pdf"
    download_file(url, destination)

    # Return the path
    return os.path.abspath(destination)

## helper functions

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

if __name__ == '__main__':
    app.run(debug=True)

import os
import urllib.request

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

downloaded_file_path = download_curriculum(subject_input, grade_input) # returns path to the file

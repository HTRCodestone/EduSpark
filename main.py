import urllib.request

def generate_curriculum_url(subject, grade):
    # Special cases for specific subjects
    if subject.lower() == "computer studies":
        return "https://www.edu.gov.on.ca/eng/curriculum/secondary/computer10to12_2008.pdf"

    if subject.lower() == "english":
        # Use <grade>currb.pdf for English
        return f"https://www.edu.gov.on.ca/eng/curriculum/secondary/english{grade}currb.pdf"

    if subject.lower() == "mathematics":
        # Use math<grade>curr.pdf for Mathematics
        return f"https://www.edu.gov.on.ca/eng/curriculum/secondary/math{grade}curr.pdf"

    if subject.lower() == "science":
        # Use specific links for Science based on the grade
        if grade in [9, 10]:
            return "https://www.edu.gov.on.ca/eng/curriculum/secondary/science910_2008.pdf"
        elif grade in [11, 12]:
            return "https://www.edu.gov.on.ca/eng/curriculum/secondary/2009science11_12.pdf"

    # Default case for other subjects
    grade_str = '910' if grade in [9, 10] else str(grade)
    return f"https://www.edu.gov.on.ca/eng/curriculum/secondary/{subject.lower()}{grade_str}curr.pdf"

def download_file(url, destination):
    urllib.request.urlretrieve(url, destination)

def main():
    # Get subject and grade from the user
    subject = input("Enter the subject: ")
    grade = int(input("Enter the grade (9, 10, 11, or 12): "))

    # Check if the grade is valid (9, 10, 11, or 12)
    if grade not in [9, 10, 11, 12]:
        print("Invalid grade. Please enter a valid grade (9, 10, 11, or 12).")
        return

    # Generate the URL
    url = generate_curriculum_url(subject, grade)

    # Download the file
    destination = f"{subject.lower()}_grade{grade}_curriculum.pdf"
    download_file(url, destination)

    # Print the success message
    print(f"File downloaded successfully to {destination}")

if __name__ == "__main__":
    main()

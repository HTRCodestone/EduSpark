import fitz  # PyMuPDF

def extract_text_from_page(page):
    # Extract text from the page
    return page.get_text()

def pdf_to_text_with_structure(pdf_path, text_file_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Create a text file for writing
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        # Iterate through each page in the PDF
        for page_number in range(pdf_document.page_count):
            # Get the page
            page = pdf_document[page_number]

            # Extract text from the page
            page_text = extract_text_from_page(page)

            # Identify headers and subheaders based on font size
            lines = page_text.split('\n')
            for line in lines:
                font_size = line.split(" ")[0]
                if font_size.isdigit() and int(font_size) > 10:
                    text_file.write(f"\n\n=== Header ===\n{line}\n")
                elif font_size.isdigit() and int(font_size) > 8:
                    text_file.write(f"\n--- Subheader ---\n{line}\n")
                else:
                    text_file.write(line + '\n')

    # Close the PDF document
    pdf_document.close()


# Example usage:
pdf_path = "secret_report-card.pdf"
text_file_path = "out.txt"

pdf_to_text_with_structure(pdf_path, text_file_path)
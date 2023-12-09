def format_text_with_headers_and_underlines(input_text):
    """
    This function formats the provided text input into a cleaner format,
    keeping underlines and not conglomerating underscored text with normal text.
    """
    # Split the text into lines
    lines = input_text.split('\n')

    formatted_lines = []
    current_header = []
    is_underline = False

    for line in lines:
        stripped_line = line.strip()

        if not stripped_line:  # If the line is empty
            # Add the current header if there is one
            if current_header:
                formatted_lines.append("".join(current_header))
                current_header = []
            formatted_lines.append(line)
        elif set(stripped_line) == {'-'}:  # Check if the line is an underline
            # Add the current header if there is one
            if current_header:
                formatted_lines.append("".join(current_header))
                current_header = []
            formatted_lines.append(line)
            is_underline = True
        elif is_underline:  # If the previous line was an underline
            formatted_lines.append(stripped_line)
            is_underline = False
        else:  # If it's a normal line
            # Append the line to the current header
            current_header.append(stripped_line)

    # Add the remaining header if there is one
    if current_header:
        formatted_lines.append("".join(current_header))

    return '\n'.join(formatted_lines)

formatted_text = format_text_with_headers_and_underlines("\nTHE ONT\n-------\n\nA\n-\n\nRIO CURRICUL\n------------\n\nUM,\n---\n\nGR\n--\n\nADES 9 AND 10\n-------------\n\nthis is a demonstration\n\nheader\n---------\n\nsome more text")
print(formatted_text)
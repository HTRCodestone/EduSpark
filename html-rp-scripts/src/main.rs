use scraper::{Html, ElementRef};
use regex::Regex;
use std::fs;
use std::io::{self};

fn replace_text(original_text: &str) -> String {
    // Define the first text to be replaced and its replacement
    let text_to_replace_1 = "THE ONT\n-------\n\nA\n-\n\nRIO CURRICUL\n------------\n\nUM,\n---\n\nGR\n--\n\nADES 9 AND 10\n-------------";
    let replacement_text_1 = "THE ONTARIO CURRICULUM,GRADES 9 AND 10\n--------------------------------------";

    // Define the second text to be replaced and its replacement
    let text_to_replace_2 = "THE PROGR\n---------\n\nA\n-\n\nM IN ENGLISH\n------------";
    let replacement_text_2 = "THE PROGRAM IN ENGLISH\n----------------------";

    // Replace the texts
    let mut modified_text = original_text.replace(text_to_replace_1, replacement_text_1);
    modified_text = modified_text.replace(text_to_replace_2, replacement_text_2);

    modified_text
}

fn process_html(input_html: &str, output_html: &str) -> io::Result<()> {
    // Read the HTML file
    let html_content = fs::read_to_string(input_html)?;

    // Parse the HTML
    let document = Html::parse_document(&html_content);

    // Initialize a new String to store the modified HTML
    let mut new_html = String::new();

    // Iterate over elements in the document
    for element in document.root_element().descendants() {
        if let Some(element_ref) = ElementRef::wrap(element) {
            let tag_name = element_ref.value().name();

            // Skip image tags
            if tag_name == "img" {
                continue;
            }

            // Replace <b> and <strong> tags with <h2>
            if tag_name == "b" || tag_name == "strong" {
                new_html.push_str(&format!("<h2>{}</h2>", element_ref.inner_html()));
            } else {
                // For other elements, simply use their HTML representation
                new_html.push_str(&element_ref.html());
            }
        }
    }

    // Replace non-ASCII characters with whitespace
    let re = Regex::new(r"[^\x00-\x7F]+").unwrap();
    new_html = re.replace_all(&new_html, " ").to_string();

    // Write the new HTML to the output file
    fs::write(output_html, new_html)?;

    Ok(())
}

// command line arguments: program.exe --replace input.html output.html or program.exe --process input.html output.html
fn main() {
    // Get the command line arguments
    let args: Vec<String> = std::env::args().collect();

    // Check if the correct number of arguments were provided
    if args.len() != 4 {
        println!("Usage: program.exe --replace input.html output.html or program.exe --process input.html output.html");
        return;
    }

    // Check if the first argument is --replace or --process
    if args[1] == "--replace" {
        // Replace the text in the HTML file
        let input_html = &args[2];
        let output_html = &args[3];
        let html_content = fs::read_to_string(input_html).expect("Unable to read file");
        let modified_text = replace_text(&html_content);
        fs::write(output_html, modified_text).expect("Unable to write file");
    } else if args[1] == "--process" {
        // Process the HTML file
        let input_html = &args[2];
        let output_html = &args[3];
        process_html(input_html, output_html).expect("Unable to process HTML");
    } else {
        println!("Usage: program.exe --replace input.html output.html or program.exe --process input.html output.html");
        return;
    }
}
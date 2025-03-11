import fitz  # PyMuPDF

def wrap_text(text, max_length=100):
    """Splits text into lines that fit within the max_length."""
    lines = []
    while len(text) > max_length:
        break_point = text.rfind(' ', 0, max_length)
        if break_point == -1:
            break_point = max_length
        lines.append(text[:break_point].strip())
        text = text[break_point:].strip()
    lines.append(text)  # Append the last chunk of text
    return lines

def format_syllabus_content(syllabus):
    """Formats the syllabus content into a structured text string for the PDF."""
    text = f"{syllabus['course_code']} - {syllabus['program']} ({syllabus['year']})\n\n"
    text += "Course Content:\n\n"
    
    for index, (unit, details) in enumerate(syllabus["syllabus"].items(), 1):
        unit_title = details["title"]
        topics = ", ".join(details["topics"])
        experiential_learning = ", ".join(details["experiential_learning"])

        text += f"Unit {index}: {unit_title}\n\n"
        wrapped_topics = wrap_text(topics)
        for line in wrapped_topics:
            text += f"{line}\n"
        
        text += "\nExperiential Learning:\n\n"
        wrapped_experiential_learning = wrap_text(experiential_learning)
        for line in wrapped_experiential_learning:
            text += f"{line}\n"
        
        text += "\n"  # Extra newline after each unit
    
    return text

def add_text_to_pdf_page(pdf, text, fontsize=10, position=(50, 50)):
    """Adds formatted text to a new PDF page."""
    page = pdf.new_page()
    page.insert_text(position, text, fontsize=fontsize)

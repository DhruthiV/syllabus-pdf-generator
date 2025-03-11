import fitz  # PyMuPDF
from .syllabus_format import format_syllabus_content

def combine_syllabi_pdfs(syllabi):
    """
    Combines multiple syllabi into a single PDF.
    :param syllabi: List of syllabus dictionaries.
    :return: Bytes of the combined PDF.
    """
    pdf = fitz.open()
    
    for syllabus in syllabi:
        page = pdf.new_page()
        text = format_syllabus_content(syllabus)
        page.insert_text((50, 50), text, fontsize=10)
    
    pdf_bytes = pdf.write()
    pdf.close()
    
    return pdf_bytes
import fitz  # PyMuPDF
from .syllabus_format import format_syllabus_content

def generate_syllabus_pdf(syllabus):
    """
    Generates a PDF for a given syllabus dictionary.
    :param syllabus: Dictionary containing syllabus details.
    :return: Bytes of the generated PDF.
    """
    pdf = fitz.open()
    page = pdf.new_page()
    
    text = format_syllabus_content(syllabus)
    page.insert_text((50, 50), text, fontsize=10)
    
    pdf_bytes = pdf.write()
    pdf.close()
    
    return pdf_bytes

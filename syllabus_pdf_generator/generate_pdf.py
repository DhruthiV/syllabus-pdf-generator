from .imports import SimpleDocTemplate, Paragraph, Spacer, BytesIO, A4
from .syllabus_format import format_syllabus_content

def generate_syllabus_pdf(syllabus):
    """
    Generates a PDF for a given syllabus dictionary.
    :param syllabus: Dictionary containing syllabus details.
    :return: Bytes of the generated PDF.
    """
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=A4)

    formatted_content = format_syllabus_content(syllabus)
    pdf.build(formatted_content)

    buffer.seek(0)
    return buffer.getvalue()
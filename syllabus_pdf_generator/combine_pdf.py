from .imports import SimpleDocTemplate, Paragraph, Spacer, BytesIO, A4
from .syllabus_format import format_syllabus_content


def combine_syllabi_pdfs(syllabi):
    """
    Combines multiple syllabi into a single PDF.
    :param syllabi: List of syllabus dictionaries.
    :return: Bytes of the combined PDF.
    """
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    for syllabus in syllabi:
        elements.extend(format_syllabus_content(syllabus))
        elements.append(Spacer(1, 24))  # Space between syllabi

    pdf.build(elements)
    buffer.seek(0)
    return buffer.getvalue()

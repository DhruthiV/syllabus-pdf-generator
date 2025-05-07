from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def format_syllabus_content(syllabus):
    """
    Formats syllabus content into a structured list of ReportLab elements.
    :param syllabus: Dictionary containing syllabus details.
    :return: List of formatted ReportLab elements.
    """
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph(f"<b>{syllabus['course_code']} - {syllabus['program']} ({syllabus['year']})</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Course Content
    elements.append(Paragraph("<b>Course Content:</b>", styles["Heading2"]))

    for index, (unit, details) in enumerate(syllabus["syllabus"].items(), 1):
        unit_title = details["title"]
        topics = ", ".join(details["topics"])
        experiential_learning = ", ".join(details["experiential_learning"])

        elements.append(Paragraph(f"<b>Unit {index}: {unit_title}</b>", styles["Heading3"]))
        elements.append(Paragraph(f"{topics}", styles["Normal"]))
        elements.append(Spacer(1, 6))

        elements.append(Paragraph("<b>Experiential Learning:</b>", styles["Heading3"]))
        elements.append(Paragraph(f"{experiential_learning}", styles["Normal"]))
        elements.append(Spacer(1, 12))

    return elements

def generate_syllabus_pdf(syllabus):
    """
    Generates a PDF for a given syllabus dictionary.
    :param syllabus: Dictionary containing syllabus details.
    :return: Bytes of the generated PDF.
    """
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    formatted_content = format_syllabus_content(syllabus)
    pdf.build(formatted_content)

    buffer.seek(0)
    return buffer.getvalue()

def combine_syllabi_pdfs(syllabi):
    """
    Combines multiple syllabi into a single PDF.
    :param syllabi: List of syllabus dictionaries.
    :return: Bytes of the combined PDF.
    """
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    for syllabus in syllabi:
        elements.extend(format_syllabus_content(syllabus))
        elements.append(Spacer(1, 24))  # Space between syllabi

    pdf.build(elements)
    buffer.seek(0)
    return buffer.getvalue()

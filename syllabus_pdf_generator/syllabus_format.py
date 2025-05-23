from .imports import SimpleDocTemplate, Paragraph, Spacer, BytesIO,getSampleStyleSheet


def format_syllabus_content(syllabus):
    """
    Formats syllabus content into a structured list of ReportLab elements.
    :param syllabus: Dictionary containing syllabus details.
    :return: List of formatted ReportLab elements.
    """
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph(f"<b>{syllabus['course_code']} - {syllabus['program']} ({syllabus['course_credits']})</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Course Content
    elements.append(Paragraph("<b>Course Content:</b>", styles["Heading2"]))

    for index, (unit, details) in enumerate(syllabus["course_content"].items(), 1):
        unit_title = details["title"]
        topics = ", ".join(details["topics"])
        experiential_learning = ", ".join(details["experiential_learning"])
        no_of_hours = " ".join(details["no_of_hours"])

        elements.append(Paragraph(f"<b>Unit {index}: {unit_title}</b>", styles["Heading3"]))
        elements.append(Paragraph(f"{topics}", styles["Normal"]))
        elements.append(Spacer(1, 6))

        elements.append(Paragraph("<b>Experiential Learning:</b>", styles["Heading3"]))
        elements.append(Paragraph(f"{experiential_learning}", styles["Normal"]))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph("<b>No of Hours :</b>", styles["Heading3"]))
        elements.append(Paragraph(f"{no_of_hours}", styles["Normal"]))
        elements.append(Spacer(1, 12))


    return elements

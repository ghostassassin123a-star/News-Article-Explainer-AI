from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth

from datetime import datetime


def create_pdf(result, filename="AI_News_Analysis.pdf"):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER
    title_style.textColor = HexColor("#2563EB")

    heading_style = styles["Heading2"]
    heading_style.textColor = HexColor("#2563EB")

    normal_style = styles["BodyText"]
    normal_style.leading = 20

    story = []

    # ----------------------------
    # Title
    # ----------------------------

    story.append(
        Paragraph(
            "AI News Analysis Report",
            title_style,
        )
    )

    story.append(Spacer(1, 20))

    # ----------------------------
    # Date
    # ----------------------------

    story.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now().strftime('%d %B %Y %I:%M %p')}",
            normal_style,
        )
    )

    story.append(Spacer(1, 20))

    # ----------------------------
    # AI Used
    # ----------------------------

    story.append(
        Paragraph(
            "<b>Generated using Google Gemini AI</b>",
            normal_style,
        )
    )

    story.append(Spacer(1, 25))

    # ----------------------------
    # Result
    # ----------------------------

    for line in result.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):

            heading = line.replace("#", "").strip()

            story.append(
                Paragraph(
                    heading,
                    heading_style,
                )
            )

            story.append(Spacer(1, 10))

        else:

            story.append(
                Paragraph(
                    line,
                    normal_style,
                )
            )

            story.append(Spacer(1, 8))

    doc.build(
        story,
        onFirstPage=add_footer,
        onLaterPages=add_footer,
    )

    return filename


def add_footer(canvas, doc):

    canvas.saveState()

    canvas.setFont("Helvetica", 9)

    canvas.setFillColor(HexColor("#6B7280"))

    page = canvas.getPageNumber()

    footer = f"AI News Article Explainer | Page {page}"

    width = stringWidth(
        footer,
        "Helvetica",
        9,
    )

    canvas.drawString(
        (595 - width) / 2,
        20,
        footer,
    )

    canvas.restoreState()
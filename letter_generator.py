import io
from datetime import datetime

import streamlit as st
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

INSTITUTION_NAME = "Symbiosis Institute of Media and Communication"
FROM_NAME = "Sushobhan Patankar"
FROM_TITLE = "Professor and Deputy Director"
ADDRESS = "Symbiosis International University"
ADDRESS2 = "Post: Lavale, Tal: Mulshi, District: Pune"

st.set_page_config(
    page_title="SIMC Internship Letter Generator",
    page_icon="📄",
    layout="centered",
)

st.markdown(
    """
    <style>
    .block-container { max-width: 700px; padding-top: 2rem; }
    .letter-note {
        padding: 12px 16px; border-radius: 8px;
        background: #f4f4f4; margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def pronouns(gender):
    if gender == "Male":
        return "He", "His", "Mr."
    if gender == "Female":
        return "She", "Her", "Ms."
    return "They", "Their", "Mr./Ms."


def build_pdf(student_name, prn, gender):
    pronoun, possessive, title = pronouns(gender)
    date = datetime.now().strftime("%d %B %Y")

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=22 * mm,
        leftMargin=22 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        title=f"Internship Letter - {student_name}",
        author=FROM_NAME,
    )

    styles = getSampleStyleSheet()
    normal = ParagraphStyle(
        "LetterBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=18,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
    )
    small = ParagraphStyle(
        "Small",
        parent=normal,
        fontSize=10,
        leading=14,
        alignment=0,
    )
    right = ParagraphStyle(
        "Right",
        parent=small,
        alignment=2,
    )

    story = [
        Paragraph(
            f"<b>From</b><br/>{FROM_NAME}<br/>{FROM_TITLE}<br/>"
            f"{INSTITUTION_NAME}<br/>{ADDRESS}<br/>{ADDRESS2}",
            small,
        ),
        Paragraph(f"<b>Date</b><br/>{date}", right),
        Spacer(1, 12),
        Paragraph("To whomsoever, it may concern", normal),
        Paragraph(f"{'Dear Sir' if gender == 'Male' else 'Dear Madam' if gender == 'Female' else 'Dear Sir/Madam'},", normal),
        Paragraph(
            f"This is to certify that <b>{student_name}</b> (PRN: {prn}) is a "
            f"bonafide student of Symbiosis Institute of Media and Communication, Pune. "
            f"{pronoun} is pursuing MA (Journalism and Media Industries).",
            normal,
        ),
        Paragraph(
            f"As a part of the curriculum, students are expected to do an internship "
            f"training at a media organisation. The institute has no objection to "
            f"{possessive.lower()} internship training at your prestigious news organization.",
            normal,
        ),
        Paragraph("Thank You", normal),
        Spacer(1, 30),
        Paragraph(f"<b>{FROM_NAME}</b><br/>{FROM_TITLE}<br/>{INSTITUTION_NAME}", small),
    ]

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


st.title("📄 Internship Letter Generator")
st.caption("Symbiosis Institute of Media and Communication")

st.markdown(
    '<div class="letter-note">Enter your details below. Your internship letter will be generated as a PDF for immediate download.</div>',
    unsafe_allow_html=True,
)

with st.form("letter_form"):
    student_name = st.text_input(
        "Student Full Name",
        placeholder="Enter your full name",
    )
    prn = st.text_input(
        "PRN",
        placeholder="Enter your PRN",
    )
    gender = st.selectbox(
        "Gender",
        ["-- Select Gender --", "Male", "Female", "Other"],
    )
    submitted = st.form_submit_button("Generate Letter", use_container_width=True)

if submitted:
    student_name = student_name.strip()
    prn = prn.strip()

    if not student_name or not prn or gender == "-- Select Gender --":
        st.error("Please fill in all the fields.")
    else:
        pdf = build_pdf(student_name, prn, gender)
        filename = f"Internship_Letter_{prn.replace(' ', '_')}.pdf"

        st.success("Your internship letter has been generated successfully.")
        st.download_button(
            "⬇️ Download Internship Letter (PDF)",
            data=pdf,
            file_name=filename,
            mime="application/pdf",
            use_container_width=True,
        )

        with st.expander("Preview details"):
            st.write(f"**Student:** {student_name}")
            st.write(f"**PRN:** {prn}")
            st.write(f"**Gender:** {gender}")

st.caption("Please check the details carefully before downloading the letter.")

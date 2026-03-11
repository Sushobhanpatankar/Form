import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import datetime

# Gmail configuration
GMAIL_ADDRESS = "sushobhan.patankar@simc.edu"
GMAIL_PASSWORD = "uwmh unpe sota efdg"
RECIPIENT_EMAIL = "sushobhan.patankar@simc.edu"

# Institution details
INSTITUTION_NAME = "Symbiosis Institute of Media and Communication"
FROM_NAME = "Sushobhan Patankar"
FROM_TITLE = "Professor and Deputy Director"
ADDRESS = "Symbiosis International University"
ADDRESS2 = "Post: Lavale, Tal: Mulshi, District: Pune"

# Page config
st.set_page_config(
    page_title="Internship Letter Generator",
    page_icon="📄",
    layout="centered"
)

# Custom CSS for a clean, professional look
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Source+Sans+3:wght@300;400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Source Sans 3', sans-serif;
        }
        .main {
            background-color: #f8f6f1;
        }
        .block-container {
            padding-top: 2rem;
            max-width: 680px;
        }
        h1 {
            font-family: 'Playfair Display', serif !important;
            color: #1a1a2e !important;
            font-size: 2rem !important;
        }
        .subtitle {
            color: #666;
            font-size: 0.95rem;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .stTextInput > label, .stSelectbox > label {
            font-weight: 600;
            color: #333;
        }
        .success-box {
            background: #e8f5e9;
            border-left: 4px solid #2e7d32;
            padding: 16px 20px;
            border-radius: 6px;
            color: #1b5e20;
            font-weight: 500;
        }
        .error-box {
            background: #ffebee;
            border-left: 4px solid #c62828;
            padding: 16px 20px;
            border-radius: 6px;
            color: #b71c1c;
            font-weight: 500;
        }
        .letter-preview {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 32px;
            font-family: 'Source Sans 3', sans-serif;
            font-size: 13.5px;
            line-height: 1.8;
            color: #222;
            box-shadow: 0 2px 12px rgba(0,0,0,0.07);
        }
        .stButton > button {
            background-color: #1a1a2e;
            color: white;
            border: none;
            padding: 0.6rem 2rem;
            font-size: 1rem;
            border-radius: 6px;
            font-family: 'Source Sans 3', sans-serif;
            font-weight: 600;
            width: 100%;
            transition: background 0.2s;
        }
        .stButton > button:hover {
            background-color: #2d2d5e;
            color: white;
        }
        .divider {
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 24px 0;
        }
    </style>
""", unsafe_allow_html=True)


def get_pronouns(gender):
    if gender == "Male":
        return {"pronoun": "He", "possessive": "His", "salutation": "Dear Sir", "title": "Mr."}
    elif gender == "Female":
        return {"pronoun": "She", "possessive": "Her", "salutation": "Dear Madam", "title": "Ms."}
    else:
        return {"pronoun": "They", "possessive": "Their", "salutation": "Dear Sir/Madam", "title": "Mr./Ms."}


def generate_html_letter(student_name, roll_number, gender):
    pronouns = get_pronouns(gender)
    current_date = datetime.now().strftime("%d %B %Y")

    html_content = f"""
    <html><head><style>
        body {{ font-family: Calibri, Arial, sans-serif; line-height: 1.6; padding: 20px; color: #333; }}
        .header-section {{ display: flex; justify-content: space-between; margin-bottom: 30px; font-size: 13px; }}
        .from-section {{ width: 60%; }}
        .date-section {{ width: 35%; text-align: right; }}
        .letter-body {{ font-size: 13px; line-height: 1.8; text-align: justify; }}
        .letter-body p {{ margin: 15px 0; }}
        .signature {{ margin-top: 40px; font-size: 13px; }}
        .signature-name {{ margin-top: 40px; font-weight: bold; }}
    </style></head>
    <body>
        <div class="header-section">
            <div class="from-section">
                <strong>From</strong><br>
                {FROM_NAME}<br>{FROM_TITLE}<br>{INSTITUTION_NAME}<br>{ADDRESS}<br>{ADDRESS2}
            </div>
            <div class="date-section">
                <strong>Date</strong><br>{current_date}
            </div>
        </div>
        <p>To whomsoever, it may concern</p>
        <div class="letter-body">
            <p>{pronouns['salutation']},</p>
            <p>This is to certify that <strong>{student_name}</strong> (Roll No: {roll_number}) is a bonafide student of Symbiosis Institute of Media and Communication, Pune. {pronouns['pronoun']} is pursuing MA (Journalism and Media Industries).</p>
            <p>As a part of the curriculum, students are expected to do an internship training at a media organisation. The institute has no objection to {pronouns['possessive'].lower()} internship training at your prestigious news organization.</p>
            <p>Thank You</p>
        </div>
        <div class="signature">
            <div class="signature-name">{FROM_NAME}</div>
            <div>{FROM_TITLE}</div>
            <div style="color:#555;font-size:12px;">{INSTITUTION_NAME}</div>
        </div>
    </body></html>
    """
    return html_content


def send_email(student_name, roll_number, gender):
    try:
        pronouns = get_pronouns(gender)
        msg = MIMEMultipart('alternative')
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = f"Internship Letter for {student_name} (Roll No: {roll_number})"

        plain_text = f"""Dear Sir/Madam,

Internship letter request for {pronouns['title']} {student_name} (Roll No: {roll_number}).

Please find the letter below and issue it to the student mentioned.

Best regards,
Symbiosis Institute of Media and Communication"""

        html_letter = generate_html_letter(student_name, roll_number, gender)
        msg.attach(MIMEText(plain_text, 'plain'))
        msg.attach(MIMEText(html_letter, 'html'))

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True, "Email sent successfully!"
    except Exception as e:
        return False, f"Error sending email: {str(e)}"


# ── UI ──────────────────────────────────────────────────────────────────────

st.markdown("# 📄 Internship Letter Generator")
st.markdown('<p class="subtitle">Symbiosis Institute of Media and Communication</p>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

with st.form("letter_form"):
    student_name = st.text_input("Student Full Name", placeholder="e.g. Rahul Sharma")
    roll_number  = st.text_input("Roll Number", placeholder="e.g. SIMC2024001")
    gender       = st.selectbox("Gender", ["-- Select Gender --", "Male", "Female", "Other"])

    submitted = st.form_submit_button("Generate & Send Letter")

if submitted:
    if not student_name.strip() or not roll_number.strip() or gender == "-- Select Gender --":
        st.markdown('<div class="error-box">⚠️ Please fill in all fields before submitting.</div>', unsafe_allow_html=True)
    else:
        with st.spinner("Generating and sending your letter..."):
            success, message = send_email(student_name.strip(), roll_number.strip(), gender)

        if success:
            st.markdown(
                f'<div class="success-box">✅ Your request has been submitted successfully!<br><br>'
                f'Your internship letter will be ready for collection from the institute <strong>tomorrow or the next working day</strong>. '
                f'Please visit the office during working hours to collect it.</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(f'<div class="error-box">❌ {message}</div>', unsafe_allow_html=True)

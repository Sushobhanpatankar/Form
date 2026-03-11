from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import datetime

app = Flask(__name__)

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

def get_pronouns(gender):
    """Return pronouns and salutation based on gender"""
    if gender.lower() == "male":
        return {
            "pronoun": "He",
            "possessive": "His",
            "salutation": "Dear Sir",
            "title": "Mr."
        }
    elif gender.lower() == "female":
        return {
            "pronoun": "She",
            "possessive": "Her",
            "salutation": "Dear Madam",
            "title": "Ms."
        }
    else:
        return {
            "pronoun": "They",
            "possessive": "Their",
            "salutation": "Dear Sir/Madam",
            "title": "Mr./Ms."
        }

def generate_html_letter(student_name, roll_number, gender):
    """Generate HTML letter with personalized content"""
    pronouns = get_pronouns(gender)
    current_date = datetime.now().strftime("%d %B %Y")

    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Calibri', 'Arial', sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                color: #333;
            }}
            .letter-container {{
                max-width: 8.5in;
                height: 11in;
                margin: 0 auto;
                padding: 40px;
                background: white;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            .header-section {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 30px;
                font-size: 13px;
            }}
            .from-section {{
                width: 60%;
            }}
            .date-section {{
                width: 35%;
                text-align: right;
            }}
            .from-section strong,
            .date-section strong {{
                font-weight: bold;
                display: block;
                margin-bottom: 5px;
            }}
            .greeting {{
                margin-top: 30px;
                margin-bottom: 20px;
                font-size: 13px;
            }}
            .letter-body {{
                font-size: 13px;
                line-height: 1.8;
                margin-bottom: 20px;
                text-align: justify;
            }}
            .letter-body p {{
                margin: 15px 0;
            }}
            .signature {{
                margin-top: 40px;
                font-size: 13px;
            }}
            .signature-name {{
                margin-top: 40px;
                font-weight: bold;
            }}
            .signature-title {{
                margin-top: 3px;
            }}
            .institution {{
                margin-top: 5px;
                font-size: 12px;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <div class="letter-container">
            <div class="header-section">
                <div class="from-section">
                    <strong>From</strong>
                    {FROM_NAME}<br>
                    {FROM_TITLE}<br>
                    {INSTITUTION_NAME}<br>
                    {ADDRESS}<br>
                    {ADDRESS2}
                </div>
                <div class="date-section">
                    <strong>Date</strong>
                    {current_date}
                </div>
            </div>

            <div class="greeting">
                To whomsoever, it may concern
            </div>

            <div class="letter-body">
                <p>{pronouns['salutation']},</p>

                <p>This is to certify that <strong>{student_name}</strong> (Roll No: {roll_number}) is a bonafide student of Symbiosis Institute of Media and Communication, Pune. {pronouns['pronoun']} is pursuing MA (Journalism and Media Industries).</p>

                <p>As a part of the curriculum, students are expected to do an internship training at a media organisation. The institute has no objection to {pronouns['possessive'].lower()} internship training at your prestigious news organization.</p>

                <p>Thank You</p>
            </div>

            <div class="signature">
                <div class="signature-name">{FROM_NAME}</div>
                <div class="signature-title">{FROM_TITLE}</div>
                <div class="institution">{INSTITUTION_NAME}</div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

def send_email(student_name, roll_number, gender):
    """Send email with HTML letter"""
    try:
        pronouns = get_pronouns(gender)

        # Create email
        msg = MIMEMultipart('alternative')
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = f"Internship Letter for {student_name} (Roll No: {roll_number})"

        # Email body - notification to recipient
        plain_text = f"""Dear Sir/Madam,

Internship letter request for {pronouns['title']} {student_name} (Roll No: {roll_number}).

Please find the letter below and issue it to the student mentioned.

Best regards,
Symbiosis Institute of Media and Communication"""

        # Generate HTML letter
        html_letter = generate_html_letter(student_name, roll_number, gender)

        # Attach email body
        msg.attach(MIMEText(plain_text, 'plain'))
        msg.attach(MIMEText(html_letter, 'html'))

        # Send email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        return True, "Email sent successfully!"
    except Exception as e:
        return False, f"Error sending email: {str(e)}"

@app.route('/')
def index():
    """Render the form"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Handle form submission"""
    try:
        data = request.get_json()
        student_name = data.get('student_name', '').strip()
        roll_number = data.get('roll_number', '').strip()
        gender = data.get('gender', '').strip()

        # Validation
        if not student_name or not roll_number or not gender:
            return jsonify({
                'success': False,
                'message': 'Please fill in all fields'
            }), 400

        # Send email with HTML letter
        success, message = send_email(student_name, roll_number, gender)

        if success:
            return jsonify({
                'success': True,
                'message': f'Letter sent successfully to {RECIPIENT_EMAIL}!'
            })
        else:
            return jsonify({
                'success': False,
                'message': message
            }), 500

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

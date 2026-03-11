# Internship Letter Generator

A web-based application to generate and send personalized internship letters with gender-specific salutations and pronouns. Students can use the form without any installation required!

## Features

✅ **Web Form Interface** - Easy-to-use HTML form accessible via browser
✅ **Gender-Specific Content** - Automatically adjusts salutations and pronouns based on gender
✅ **HTML Email Letters** - Professional formatted emails that print beautifully
✅ **Email Integration** - Automatically sends letters via Gmail
✅ **Student Information** - Captures name, roll number, and gender
✅ **No Installation Needed** - Students just open a URL in their browser

## Installation

### 1. Install Required Package

```bash
pip install flask
```

Or add to your existing requirements.txt and install:
```bash
pip install -r requirements.txt
```

### 2. Project Structure

```
D:\Insta_py\python 3.14\
├── letter_generator.py          # Main Flask application
├── templates/
│   └── index.html               # Web form
└── LETTER_GENERATOR_README.md   # This file
```

## Configuration

The application is already configured with:
- **Gmail Account**: sushobhan.patankar@simc.edu
- **App Password**: uwmh unpe sota efdg
- **Recipient Email**: sushobhan.patankar@simc.edu
- **Institution**: Symbiosis Institute of Media and Communication

### How to Share with Students

The app runs on `http://127.0.0.1:5000` locally. To let students access it:

**Option 1: Local Network** (Students on same WiFi)
- Find your computer's IP: `ipconfig` (Windows) or `hostname -I` (Mac/Linux)
- Share URL like: `http://192.168.x.x:5000`

**Option 2: Deploy Online** (Recommended for remote access)
- Deploy to free services like Heroku, Railway, or Render
- Share the public URL with students

**Option 3: Just send them the form**
- Students fill form → Click send → Letter automatically emailed to recipient

### To Change Configuration

Edit `letter_generator.py` and modify these variables:

```python
GMAIL_ADDRESS = "your-email@gmail.com"
GMAIL_PASSWORD = "your-app-password"
RECIPIENT_EMAIL = "recipient@example.com"
```

## Running the Application

### Option 1: From Command Line (Bash/PowerShell)

```bash
cd D:/Insta_py/python\ 3.14
python letter_generator.py
```

### Option 2: From PowerShell with Virtual Environment

```powershell
cd "D:\Insta_py\python 3.14"
.\.venv\Scripts\Activate.ps1
python letter_generator.py
```

### Access the Application

Once running, open your browser and go to:
```
http://127.0.0.1:5000
```

## How to Use

1. **Open the web form** at `http://127.0.0.1:5000`
2. **Enter student details**:
   - Student Name (e.g., "Raj Kumar")
   - Roll Number (e.g., "MA2024001")
   - Gender (Male, Female, or Other)
3. **Click "Send Letter to Recipient"**
4. The application will:
   - Generate a personalized HTML letter
   - Automatically send it to the configured recipient email
   - Show a success message
   - The email is beautifully formatted and prints perfectly

## Gender-Specific Customization

The letter automatically adjusts based on selected gender:

| Gender | Salutation | Pronoun | Possessive |
|--------|-----------|---------|-----------|
| Male | Dear Sir | He | His |
| Female | Dear Madam | She | Her |
| Other | Dear Sir/Madam | They | Their |

## Email Details

### Subject Line
```
Internship Letter for [Student Name] (Roll No: [Roll Number])
```

### Letter Content

The HTML email includes:
- **From**: Sushobhan Patankar, Professor and Deputy Director
- **Institution**: Symbiosis Institute of Media and Communication
- **Address**: Post: Lavale, Tal: Mulshi, District: Pune
- **Date**: Current date automatically added
- **Personalized salutation** (Dear Sir/Madam) based on gender
- **Personalized pronouns** (He/She) throughout the letter
- **Student details**: Name and Roll Number
- **Professional formatting**: Designed to print beautifully without any overflow
- **Signature**: Name and designation properly formatted at the end

## Troubleshooting

### Email Not Sending?

1. **Check Gmail credentials**:
   - Make sure you have the correct Gmail address
   - Verify the App Password is correct (not your regular Gmail password)
   - If using 2-step verification, generate a new App Password

2. **Gmail Settings**:
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Generate a new 16-character password

3. **Port Issues**:
   - The app uses Gmail's SMTP over SSL (port 465)
   - Make sure your firewall allows this connection

### Port Already in Use?

If port 5000 is already in use, modify `letter_generator.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)  # Change to 5001
```

Then access: `http://127.0.0.1:5001`

### Email Not Displaying Correctly?

If the letter doesn't format properly in email:
1. Make sure your email client supports HTML emails
2. Try viewing in a web browser or different email client
3. The letter prints perfectly from any email client's print function

## Security Notes

⚠️ **Important**:
- Never commit email credentials to version control
- The app password is specific to Gmail and not your actual password
- Consider moving credentials to environment variables for production use

## Future Enhancements

- [ ] Database to store generated letters
- [ ] Download letter as PDF option
- [ ] Email templates customization
- [ ] Bulk letter generation from CSV
- [ ] Letter history/archive
- [ ] Custom letterhead upload
- [ ] Multi-language support
- [ ] Student email confirmation feature

## Support

For issues or questions, contact the development team.

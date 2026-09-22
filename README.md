# SIMC Internship Letter Generator

A simple student-facing web form for generating internship letters as PDF files.

## Student workflow

1. Open the web app.
2. Enter full name and PRN.
3. Select gender.
4. Click **Generate Letter**.
5. Download the generated PDF.

## Deploy with Streamlit Community Cloud

1. Sign in to Streamlit Community Cloud with GitHub.
2. Create a new app from this repository.
3. Select branch `main`.
4. Set the main file to `letter_generator.py`.
5. Deploy.

The app does not require Gmail credentials or an email server. The PDF is generated in the student's browser session.

## Important

The previous version of this project contained a Gmail app password in source code. That credential should be revoked and replaced if it is still active. No email credentials are required by the current version.

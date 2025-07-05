import smtplib
from flask import Flask, render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def send_email(body, email_list):
    sender_email = "uharsh12348@gmail.com"
    password = "dkzwnmurfdngstji"
    subject = "hello"
    
    
    for receiver_email in email_list:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print(f"Sent to {receiver_email} successfully")
        except Exception as e:
            print(f"Failed to send to {receiver_email}", e)
        finally:
            server.quit()

@app.route('/send', methods=['POST'])
def send_mail_sytem():
    body = request.form['body']
    file = request.files['excel_file']
    if not file:
        return "No file uploaded", 400
    df = pd.read_excel(file)
    # Try to find the email column (case-insensitive)
    email_col = None
    for col in df.columns:
        if 'email' in col.lower():
            email_col = col
            break
    if not email_col:
        return "No email column found in the uploaded file.", 400
    email_list = df[email_col].dropna().astype(str).tolist()
    send_email(body, email_list)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

import smtplib
from flask import Flask, render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def send_email(body):
    sender_email = "uharsh12348@gmail.com"
    receiver_email = "harshtiwariii01032004@gmail.com"
    password = "dkzwnmurfdngstji"
    subject = "hello"
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
        print(" successfully")
        
    except Exception as e:
        print("nothing", e)

    finally:
        server.quit()
    
@app.route('/send', methods=['POST'])
def send_mail_sytem():
    body = request.form['body']
    send_email(body)
    return redirect(url_for('index'))
       
root=tk.Tk()
root.title("send mail")
root.geometry("300x200")

label=tk.Label(root,text="abcde")
label.pack(pady=20)
send_button = tk.Button(root,text="abc",command=send_email)
send_button.pack(pady=10)

root.mainloop()



if __name__ == '__main__':
    app.run(debug=True)

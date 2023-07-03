from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Change the server and port based on your email provider
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        return True
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sender_email = request.form['sender_email']
        sender_password = request.form['sender_password']
        recipient_email = request.form['recipient_email']
        subject = request.form['subject']
        body = request.form['body']

        if send_email(sender_email, sender_password, recipient_email, subject, body):
            return "Email sent successfully!"
        else:
            return "An error occurred while sending the email."

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

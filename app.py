
from flask import Flask
# we import the Twilio client from the dependency we just installed
from flask import request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app = Flask(__name__)
@app.route('/',methods=['GET'])
def hello_world():

     return 'Hello, World!'
@app.route('/sendmail', methods=['POST'])
def send_mail():
    # Python code to illustratdde Sending mail from
    # your Gmail account
    print(request.json)
    data=request.json
    name=data['name']
    phone_no=data['phone_no']
    email = data['email']
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = "justolearnpune@gmail.com"
    message['Subject'] = 'Inquery Justolearn.'  # The subject line
    # The body and the attachments for the mail
    mail_content = "Recived Enquire from  " + " name: " + name + " email: " + email + "phone_no" + phone_no
    message.attach(MIMEText(mail_content, 'plain'))
    import smtplib

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login("justolearnpune@gmail.com", "justo.007")

    # message to be sent
    text = message.as_string()
    # sending the mail
    s.sendmail(email, "justolearnpune@gmail.com", text)

    # terminating the session
    s.quit()
    return  "mail sent"

if __name__ == '__main__':
    app.run()



from email.message import EmailMessage
import smtplib
import requests

def sendAnEmail(title,subject,message, email_receiver, path=None):
    print("Attempting to send an email")
    print(email_receiver)
    print(type(email_receiver))

    email_sender = 'pay@prestoghana.com'
    email_password = 'Babebabe123$'

    recievers = ['prestoghana@gmail.com', 'onikosiadewale18@gmail.com']

    for r in email_receiver:
        recievers.append(r)
    print("recievers")
    print(recievers)

    
    # email_receiver = recipient

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        @font-face {{
            font-family: 'Plus Jakarta';
            src: url('PlusJakartaSans-VariableFont_wght.woff2') format('woff2-variations'),
                url('PlusJakartaSans-Italic-VariableFont_wght.woff2') format('woff2-variations');
            font-weight: 100 500; /* Adjust font weights based on available weights */
            font-style: normal;
        }}

        body {{
            font-family: 'Plus Jakarta', sans-serif;
            color:black;
            margin: auto 10px;
        }}

        div{{
            font-family: 'Plus Jakarta', sans-serif;
            font-weight:200;
        }}

        </style>

    </head>
    <body style="margin:auto 10px; color:black; font-family: 'Plus Jakarta', sans-serif;">
        {message}
        <h6 style="font-weight:200">This email is powered by <a href='https://prestoghana.com'>PrestoGhana</a></h6>
    </body>
    </html>
    """

    em = EmailMessage()
    em["From"] = f"{title} <{email_sender}>"
    em['To'] = email_receiver
    em['Subject'] = subject

    em.set_content('')  
    em.add_alternative(html_content, subtype='html')

    print(em)

    if path != None:
        em.add_attachment(open(path, 'rb').read(), maintype='application', subtype='pdf', filename=title)

    smtp_server = 'mail.privateemail.com'
    port = 465


    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, em.as_string())
    server.quit()
    return "Done!"
    


def sendNaloSms(phone, message):
    url = "https://sms.nalosolutions.com/smsbackend/clientapi/Resl_Nalo/send-message/?username=johndoe&password=some_password&type=0&destination=233XXXXXXXXX&dlr=1&source=NALO&message=This+is+a+test+from+Mars"

    payload={
    "msisdn": phone,
    "message": message,
    "sender_id": "CentralUni",
    "username":"prestoghana",
    "password":"Babebabe123$"
    }
    headers = {}

    response = requests.post(url, headers=headers, data=payload)

    print(response)
    print(response.status_code)
    print(response.headers)
    print(response.text)
    return {"response":response.text,"code":response.status_code}

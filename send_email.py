import smtplib, ssl 


def send_email(message):
    host="smtp.gmail.com"
    # port = 465

    user = "chinmays117@gmail.com"
    password ="kivedzrempstlpib"

    context = ssl.create_default_context()

    receiver = "chinmays117@gmail.com"

    with smtplib.SMTP_SSL(host,smtplib.SMTP_SSL_PORT,context=context) as server:
        server.login(user,password)
        server.sendmail(user,receiver,message)
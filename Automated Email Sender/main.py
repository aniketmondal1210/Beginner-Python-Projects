import smtplib

sender_mail = "xyz@gmail.com" # Enter sender mail here
sender_password = "suwk jfrv ueri wnei" # Enter sender password here, not gmail password, you have to generate app password for this from your google account settings in security section

receiver_mail = ["abc@gmail.com","bcd@gmail.com"] # List of receiver mails

subject = "Test Mail"
body = "This is a test mail sent using python"

email_message = f"Subject: {subject}\n{body}"

with smtplib.SMTP("smtp.gmail.com",587) as server:
    server.starttls() #tls is a protocol that encrypts and delivers mail securely
    server.login(sender_mail,sender_password)
    for receiver in receiver_mail:
        server.sendmail(sender_mail,receiver,email_message)

print("Mail sent successfully")

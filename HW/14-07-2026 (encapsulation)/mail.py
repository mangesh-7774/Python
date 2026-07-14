import smtplib
from email.message import EmailMessage

def send_email(receiver_email,otp) :
  sender_email = "bhaleraom737@gmail.com"
  password = "qtuj ljte jasb vegr"

  msg = EmailMessage()
  msg["Subject"] = "Your Login OTP"
  msg["From"] = sender_email
  msg["To"] = receiver_email

  msg.set_content(f"Your OTP is {otp}")

  with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(sender_email,password)
    smtp.send_message(msg)
  print("OTP sent successfully")

def send_success(receiver_email) :
  sender_email = "bhaleraom737@gmail.com"
  password = "qtuj ljte jasb vegr"

  msg = EmailMessage()
  msg["Subject"] = "Success Message"
  msg["From"] = sender_email
  msg["To"] = receiver_email

  msg.set_content(f"User Logedin Successfully...!")

  with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(sender_email,password)
    smtp.send_message(msg)
  print("Success message sent successfully")

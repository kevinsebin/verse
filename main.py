import json
import requests
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import pytz

now = datetime.datetime.now()
month = now.strftime('%B')
month = month.lower()
print(month)

now = datetime.datetime.now()
date = str(now.date())
new = date.split('-')
date_num = int(new[2])

d2 = now.strftime("%B %d, %Y")


def send_data(month, date_num):
  url = f'https://day-manage-default-rtdb.firebaseio.com/months/{month}.json'
  req = requests.get(url = url)
  data = json.loads(req.content.decode())
  day_message = data[date_num - 1]

  # me == my email address
  # you == recipient's email address
  me = "kevinsebinranger@gmail.com"
  you = "kevinsebinkk@gmail.com"

  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Message"
  msg['From'] = me
  msg['To'] = you

  text = 'Message from Jesus'
  html = f"""\
  <!DOCTYPE html>
  <html>
    <body style="background-color:#FF6F61;">
      <h1 style="font-size:300%; color:white; padding:40px">Jesus loves you!</h1>
      <p style="font-size:160%; color:white; padding:40px">{day_message}</p>
      <br>
      <br>
      <br>
    </body>
  </html>
  """

  # Record the MIME types of both parts - text/plain and text/html.
  part1 = MIMEText(text, 'plain')
  part2 = MIMEText(html, 'html')

  # Attach parts into message container.
  # According to RFC 2046, the last part of a multipart message, in this case
  # the HTML message, is best and preferred.
  msg.attach(part1)
  msg.attach(part2)
  # Send the message via local SMTP server.
  mail = smtplib.SMTP('smtp.gmail.com', 587)

  mail.ehlo()

  mail.starttls()

  mail.login('kevinsebinranger@gmail.com', 'ikjjulzjxxgdiqfe')
  UTC = pytz.utc
  IST = pytz.timezone('Asia/Kolkata')
    
  datetime_ist = datetime.datetime.now(IST)
  hour = int(datetime_ist.strftime('%H'))
  minute = int(datetime_ist.strftime('%M'))
  if hour == 12 and minute == 0:
    print('true')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()
  else:
    print('message yet to send')

send_data(month, date_num)

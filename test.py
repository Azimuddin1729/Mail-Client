import smtplib 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart 
from email import encoders

server=smtplib.SMTP('smtp.gmail.com',587) # 
server.starttls() 


with open ('app_password.txt','r') as f:
    password=f.read().strip()

try:
    server.login("temp118234@gmail.com", password)
except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication failed: {e}")
    server.quit()
    exit()

message=MIMEMultipart()

message['From']="temp118234@gmail.com"
message['To']="temp117824@gmail.com"

message['Subject']="Learning Network Programming"

with open('msg.txt','r') as f:
    msgtobesent=f.read()

message.attach(MIMEText(msgtobesent,'plain'))

with open ('gojo_hello.jpg','rb') as f:
    image=f.read()

img=MIMEBase('application','octet-stream')

img.set_payload(image)
encoders.encode_base64(img)
filename='gojo_hello.jpg'
img.add_header('Content-Disposition',f'attachment; filename={filename}')

message.attach(img)

stufftobesend=message.as_string()
try:
    server.sendmail("temp118234@gmail.com", "temp117824@gmail.com", stufftobesend)  
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

server.quit()

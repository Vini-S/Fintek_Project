'''import os
print(os.name)
print(os.getcwd())
filename = 'name.txt'
f = open(filename, 'w')
f.write("hello world")
f.close()
file = open(filename, 'r')
text = file.read()
print(text)
file = os.popen(filename, 'w')
file.write("hello")

'''
'''
#program to create an entry box which accepts only the numeric value.
from tkinter import Tk, Entry
top = Tk()

def correct(inp):
    if inp.isdigit():
        return True
    else:
        return False

e = Entry(top)
e.place(x=50, y=50)

reg = top.register(correct)
e.config(validate="key",validatecommand=(reg, '%p'))

top.mainloop()
'''
#webscraping
'''
import requests
import bs4
#res = requests.get("http://www.internshala.com")
res = requests.get("http://www.howstat.com/cricket/Statistics/Players/PlayerList.asp?Group=A")
print(type(res))
#print(res.text)        #prints the html code of webpage
soup = bs4.BeautifulSoup(res.text,"lxml")
print(type(soup))
hi = soup.select('table')
print(hi)
print(hi[0])
print(hi[0].getText())
'''
'''
#code to 
q = list(input().rstrip("A").rstrip("B"))
while("A" in q or "B" in q):
    if "A" in q:
        a = q.index("A")
        q[a+1] = str(int(q[a+1])+1)
        del(q[a])
    if "B" in q:
        b = q.index("B")
        q[b+1] = str(int(q[b+1])-1) if int(q[b+1])>0 else ""
        del(q[b])
print(''.join(q))
        

'''

'''

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "vinitasharma13061999@gmail.com"
receiver_email = "fintekschedule@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
<head>
<title></title>
</head>
<body style="background-color: #f4f4f4;">

<table cellpadding="0" cellspacing="0" width="100%">
    <!-- LOGO -->
    <tr>
        <td bgcolor="#7c72dc" align="center"  style="padding: 50px 10px 40px 10px;">    
        </td>
    </tr>
    <!-- HERO -->
    <tr>
        <td bgcolor="#7c72dc" align="center" style="padding: 0px 10px 0px 10px;">
            <table border="0" cellpadding="0" cellspacing="0" width="480" >
                <tr>
                    <td bgcolor="#ffffff" align="center" valign="top" style="padding: 20px 20px 20px 20px; color: #111111; font-family:Arial; font-size: 48px; font-weight: 400; letter-spacing: 4px;">
                      <h1 style="font-size: 32px; font-weight: 400; margin: 0;">Forgot password ?</h1>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <!-- COPY BLOCK -->
    <tr>
        <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
            <table border="0" cellpadding="0" cellspacing="0" width="480" >
              <!-- COPY -->
              <tr>
                <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family:Arial; font-size: 18px; line-height: 25px;" >
                  <p>You're receiving this email because you requested a password reset for your user account at Fintek Schedule.</p>
                  <p>Follow the link bellow to reset your password.</p>
                </td>
              </tr>
              <!-- BULLETPROOF BUTTON -->
              <tr>
                <td bgcolor="#ffffff" align="left">
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td bgcolor="#ffffff" align="center" style="padding: 20px 30px 60px 30px;">
                        <table border="0" cellspacing="0" cellpadding="0">
                          <tr>
                              <td align="center" style="border-radius: 3px;" bgcolor="#7c72dc"><a href="https://litmus.com" target="_blank" style="font-size: 20px; font-family:Arial; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #7c72dc; display: inline-block;">Reset Password</a></td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
        </td>
    </tr>
    <!-- COPY CALLOUT -->
    <tr>
        <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
            <table border="0" cellpadding="0" cellspacing="0" width="480" >
                <!-- HEADLINE -->
                <tr>
                  <td bgcolor="#111111" align="center" style="padding: 40px 30px 20px 30px; color: #ffffff; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;" >
                    <h2 style="font-size: 24px; font-weight: 400; margin: 0;">Thank you for using our site.</h2>
                  </td>
                </tr>
                
        </table>
        </td>
    </tr>   
</table>
</body>
</html>


"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.


'''

import re
import PyPDF2

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("^The.*Spain$", txt)
print(y)
if (x):
  print("YES! We have a match!")
else:
  print("No match")


























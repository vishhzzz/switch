'''
Process of Mail
1. User logs into mail provider
2. Writes the mail, send to other person
3. vishal's gmail mail is sent to kumar's gmail server.
4. Gmail server holds/stores the mail for kumar.
5. When kumar logs into server, that mail is downloaded and shown to him.

to do this, it relies on 1 protocol: SMTP - Simple Mail Transfer Protocol.
SMTP: has all the rules that determine -
      how an email is received by mail servers,
      passed on to next mail servers and
      how email is sent around the internet.

In Python we have module which does all this for us <--- smtplib
      
'''
import smtplib

my_email = "arjun.codes2402@gmail.com"
password = 'jrdl vtmh vegd tiwz'

connection = smtplib.SMTP('smtp.gmail.com') # we need to specify the location of email provider's SMTP server. Its diff for every email provider.

# starttls starts TLS - Transport Layer Security.
# way of securing our connection to our email server.
connection.starttls()

# once it is secure, we now login to the service.
connection.login(user=my_email, password=password)

# sending email
# connection.sendmail(from_addr=my_email, to_addrs='vishal.kr5202@gmail.com', msg="Hello Vishal!!!") This very much looks like SPAM becoz there is not Subject.
connection.sendmail(from_addr=my_email, to_addrs='vishal.kr5202@gmail.com', msg="Subject:Hello Vishal!!!\n\nThis is my mail body.!!!")

connection.close()

# we can ommit this close the same way, we did with file opening - with as.
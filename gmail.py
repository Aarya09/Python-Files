import smtplib
import getpass

myemail=input("your email id :")
password=getpass.getpass()
recemail=input("reciever's email id : ")

#create smtp session
s = smtplib.SMTP('SMTP.GMAIL.COM',587)

#start tls for security
s.starttls()
#authentication
s.login(myemail,password)

#message to be sent 
message="need to be send "

#sending the mail 
s.sendmail(myemail,recemail,message)

#terminating the session
s.quit()
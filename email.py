#import smtplib
import getpass

password=input("What is your password")

print(password)

password=getpass.getpass("Password Please")


# smtp_object=smtplib.SMTP("smtp.gmail.com",587)

# smtp_object.ehlo()
# print(smtp_object)

# smtp_object.starttls()
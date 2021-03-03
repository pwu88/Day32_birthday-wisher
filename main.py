# import smtplib
#
# my_email = "peijia.wu@yahoo.com"
# password = "vbjcryebymxdztxr"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email, password =password)
#     connection.sendmail(
#         from_addr= my_email,
#         to_addrs="peijiawu888@gmail.com",
#         msg = "Subject: Hello\n\nTHis is the body of my email")
# date_of_birth = dt.datetime(year = 2021, month = 2, day= 2)
import datetime as dt
import random
import smtplib

#randomly select quote if its a Tuesday
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 1:
    print("today is Tuesday")
    choice = random.randint(0,101)
    with open ("quotes.txt", 'r') as file:
        quotes = file.readlines()
        chosen_quote(quotes[choice])

#send email to self

my_email = "peijiawu888@gmail.com"
password = "Ky0shusama3"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password =password)
    connection.sendmail(
        from_addr= my_email,
        to_addrs="peijia.wu@yahoo.com",
        msg = "Subject: Hello\n\nTHis is the body of my email")


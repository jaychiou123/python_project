##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas

my_mail = "jay912145@gmail.com"
password = "prniebnwidnvddeu"
receive = "jay912145@gmail.com"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
dict = {(row["month"], row["day"]):row for (index, row) in data.iterrows()}
month_lists = data["month"].to_list()

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
context = []
if month in month_lists and int(data[data.month == month].day) == day:
    letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    with open("./letter_templates/" + random.choice(letter_list), "r") as letter:
        context = letter.read()
        context = context.replace("[NAME]", data[data.month == month].name.to_string(index=False))




# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connect:
    connect.starttls()
    connect.login(user=my_mail, password=password)
    connect.sendmail(from_addr=my_mail, to_addrs=receive, msg=f"Subject:Happy birthday\n\n{context}")




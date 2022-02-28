import datetime as dt
import smtplib
import pandas
import random

my_email = "*************" #Enter your email id
my_password = "*********"  #Enter your password
today = (dt.datetime.now().month, dt.datetime.now().day)
#print(today)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birth_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#print(birth_dict)

if today in birth_dict:
    birth_person = birth_dict[today]
    #print(birth_person["name"])
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birth_person["name"])
        #print(contents)


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birth_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")

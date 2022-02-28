import smtplib
import random
import datetime as dt

my_email = "vanditmehta2205@gmail.com"
my_password = "Darshini@2502"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="vanditmehta.18.ce@iite.indusuni.ac.in",
                        msg=f"Subject:Motivation time\n\n{quote}")
    connection.close()

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email="****************" # Enter email id
my_password="***************" # Enter password
headers = {'Accept-Language' : "en-US", 'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0"}
response = requests.get(url="https://www.amazon.com/Acer-A515-46-R3UB-Display-Quad-Core-Processor/dp/B09HVC79PC/ref=sr_1_3?crid=21WY3H0GVRCPZ&keywords=laptops&qid=1649322945&sprefix=laptop%2Caps%2C276&sr=8-3", headers=headers)
#print(response.text)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_in_digit = price.split("$")[1]
#print(price_in_digit)

if float(price_in_digit)<370.000:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        #print("in")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mehtavandit303@gmail.com",
                            msg=f"Subject:It time to do some shoping\n\n The prices of your laptop has come down")
        #print("sent")

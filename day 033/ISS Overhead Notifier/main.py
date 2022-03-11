import requests
import datetime as dt
import time
import smtplib

MY_EMAIL = "*******************"
MY_PASSWORD = "*************"
MY_LAT = 37.7550636464
MY_LONG = 14.995246019


def get_iss_location():
    """Gets the current location of the ISS, returns it as a TUPLE."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_location = response.json()
    return float(iss_location["iss_position"]["latitude"]), float(iss_location["iss_position"]["longitude"])


def is_iss_nearby(pos):
    """Takes a location as a TUPLE and returns TRUE if it's near the defined position."""
    iss_lat, iss_long = pos
    if abs(MY_LAT - iss_lat) < 5 and abs(MY_LONG - iss_long) < 5:
        return True
    return False


def is_nighttime():
    """Returns TRUE if it's nighttime at the defined location."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    daytime = response.json()
    sunset = int(daytime["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(daytime["results"]["sunrise"].split("T")[1].split(":")[0])
    now = dt.datetime.utcnow().hour
    if now >= sunset or now <= sunrise:
        return True
    return False


while True:
    if is_iss_nearby(get_iss_location()) and is_nighttime():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_PASSWORD, msg=f"Subject\n\nLook up!The ISS is above you "
                                                                          f"in the sky.")
    time.sleep(60)

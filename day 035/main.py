import requests
from twilio.rest import Client
api_key="fc2e6d471e102746b4dd9f5b951b5bbe"
parameters={
    "lat": 69.970978,
    "lon": -26.500824 ,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

account_sid = "ACcc2aaf1f80c0cc0a5afc3d538e4976f0"
auth_token = "80471ca14afc086c0b90df254104d143"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
#print(response.json())
weather_data = response.json()["hourly"]
#print(len(weather_data))

will_rain = False
for i in range(0,12):
    if weather_data[i]["weather"][0]["id"] < 800:
        will_rain = True

if will_rain==True:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today, take you umbrella with you",
        from_='+17755425759',
        to='*************'
    )
    print(message.status)

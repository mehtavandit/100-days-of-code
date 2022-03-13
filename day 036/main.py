import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_FOR_STOCK = "2HCA7DNJLCNWYTFR"
API_KEY_FOR_NEWS = "04f0f0ade15c4a8ebc6cea7852138898"
account_sid = "ACcc2aaf1f80c0cc0a5afc3d538e4976f0"
auth_token = "a0d9b1ee5d0bdcfc64d37667e9b4ed7d"


stock_params={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_FOR_STOCK
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response=response.json()["Time Series (Daily)"]
response_list = [value for (key, value) in response.items()]
yesterday_closing_price = float(response_list[0]["4. close"])
#print(type(yesterday_closing_price))

day_before_yesterday_closing_price = float(response_list[1]["4. close"])
#print(type(day_before_yesterday_closing_price))

difference = abs(yesterday_closing_price-day_before_yesterday_closing_price)
#print(difference)

percentage_difference = (difference/yesterday_closing_price)*100
#print(percentage_difference)

if percentage_difference > 5:
    news_params = {
        "apiKey": API_KEY_FOR_NEWS,
        "q": COMPANY_NAME

    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    #print(news_response.json())
    news_articles = news_response.json()["articles"]
    first_three_articles = news_articles[:3]
    news_list = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in first_three_articles]
    client = Client(account_sid, auth_token)
    #print(news_list)
    for article in news_list:
        message = client.messages \
            .create(
            body=article,
            from_='************' # Enter your twilio phone number,
            to='*************'   # Enter your mobile number
        )
    #print("sent")

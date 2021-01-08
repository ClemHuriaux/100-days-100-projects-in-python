import os
import requests
import datetime as dt
import dateutil.parser as parse_date
from twilio.rest import Client
import math

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ["ALPHAVANTAGE_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API"]
TWILIO_API_KEY = os.environ["TWILIO_API_KEY"]
KEY_TO_DICT_VALUE = "4. close"
ACCOUNT_SID_TWILIO = "AC339ce8a07c8d1b1b410af0861d7e734e"
STOCK_API_PARAMETERS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

NEWS_API_PARAMETERS = {
    "language": "en",
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}


def calculate_percentage(a, b):
    return ((b - a) / a) * 100


def format_sms(single_new, name, percentage_stock):
    triangle_way = "🔺" if percentage_stock > 0 else "🔻"
    string = f"{name}: {triangle_way}{round(percentage_stock, 0)}% \n" \
             f"Headline: {single_new['title']} \n" \
             f"Brief: {single_new['description']}"
    return string


today = dt.datetime.today()
date = dt.datetime(year=today.year, month=today.month, day=today.day, hour=5)
yesterday_and_before = [date - dt.timedelta(days=i) for i in range(1, 3)]
response = requests.get(STOCK_API_URL, params=STOCK_API_PARAMETERS)
response.raise_for_status()
stock_data = response.json()['Time Series (60min)']
two_prices = [float(value[KEY_TO_DICT_VALUE]) for key, value in stock_data.items()
              if parse_date.parse(key) in yesterday_and_before]
percentage = calculate_percentage(two_prices[0], two_prices[1])
if abs(percentage) > 5:
    print("Get News")

    news = requests.get(NEWS_API_URL, params=NEWS_API_PARAMETERS)
    news.raise_for_status()
    news = news.json()["articles"][:3]
    for new in news:
        client = Client(ACCOUNT_SID_TWILIO, TWILIO_API_KEY)
        message = client.messages.create(
            to="",  # The num you want
            from_="+14158516224",
            body=format_sms(new, STOCK, percentage))



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


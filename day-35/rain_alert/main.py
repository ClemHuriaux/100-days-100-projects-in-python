import requests
from twilio.rest import Client
import os

API_URL = "https://api.openweathermap.org/data/2.5/onecall"

API_KEY = os.environ['OPEN_WEATHER_API_KEY']
LAT_LONG = (48.847801, 2.552770)
PARAMETERS = {
    "lat": LAT_LONG[0],
    "lon": LAT_LONG[1],
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
NUMBER_OF_HOURS_WANTED = 12

account_sid = "AC339ce8a07c8d1b1b410af0861d7e734e"
auth_token = os.environ["TWILIO_AUTH_KEY"]


def generate_statements(json, number):
    return json["hourly"][int(number)]["weather"][0]["id"]


will_rain = False
response = requests.get(API_URL, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
next_hours_code = [generate_statements(weather_data, i) for i in range(12)]
if any(i >= 700 for i in next_hours_code):
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="",  # The num you want
        from_="+14158516224",
        body="It's gonna rain ! Take your ☂️!")



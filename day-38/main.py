import os
import requests
from datetime import datetime

GENRE = "male"
WEIGHT = 85
HEIGHT = 178
AGE = 23


NUTRI_APP_ID = os.environ['NUTRI_APP_ID']
NUTRI_APP_KEY = os.environ['NUTRI_APP_KEY']

NUTRI_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = os.environ["SHEETY_URL"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

headers = {
    'x-app-id': NUTRI_APP_ID,
    'x-app-key': NUTRI_APP_KEY,
    'Content-Type': 'application/json'
}


user_input = input("Which exercise have you done ?")

nutri_api_config = {
    "query": user_input,
    "gender": GENRE,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,

}

headers_sheety = {"Authorization": f"Bearer {BEARER_TOKEN}"}


response = requests.post(NUTRI_API_URL, json=nutri_api_config, headers=headers)
result = response.json()
today = datetime.today()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercises = result['exercises']
for data in exercises:
    exercise = data['name'].title()
    duration = data['duration_min']
    calories = data['nf_calories']
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(SHEETY_URL, json=body, headers=headers_sheety)

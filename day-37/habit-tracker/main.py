import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "python"
TOKEN = os.version["TOKEN"]
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Language learning graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#  response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#  print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.today().strftime("%Y%m%d")


def generate_pixel_config(quantity):
    return {
        "date": today,
        "quantity": str(quantity)
    }


#  response = requests.post(post_pixel_endpoint, json=generate_pixel_config(0.5), headers=headers)
#  print(response.text)
#  let's update bc i want to display the time in min now
graph_config = {
    "unit": "min"
}
#  response = requests.put(post_pixel_endpoint, json=graph_config, headers=headers)
#  print(response.text)
#  Now let's change the value as well
response = requests.post(post_pixel_endpoint, json=generate_pixel_config(30), headers=headers)
print(response.text)

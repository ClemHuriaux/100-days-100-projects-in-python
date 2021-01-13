import requests
import os

SHEETY_URL = os.environ["SHEETY_URL"]
BEARER_TOKEN = os.environ["SHEETY_BEARER_TOKEN"]

headers_sheety = {"Authorization": f"Bearer {BEARER_TOKEN}"}


class DataManager:

    @staticmethod
    def get_data_from_api():
        get_url = f"{SHEETY_URL}/prices"
        response = requests.get(get_url, headers=headers_sheety)
        return response.json()['prices']

    @staticmethod
    def fill_iata_code(destination):
        put_url = f"{SHEETY_URL}/prices/{destination['id']}"
        body = {
            "price": {
                "iataCode": destination['iataCode']
            }
        }
        requests.put(put_url, json=body, headers=headers_sheety)

    @staticmethod
    def fill_users_doc(user):
        post_url = f"{SHEETY_URL}/users"
        body = {
            "user": {
                "firstName": user["first name"],
                "lastName": user["last name"],
                "email": user["email"]
            }
        }
        requests.post(post_url, json=body, headers=headers_sheety)

    @staticmethod
    def get_customer_emails():
        customers_endpoint = f"{SHEETY_URL}/users"
        response = requests.get(customers_endpoint, headers=headers_sheety)
        data = response.json()
        customer_data = data["users"]
        return customer_data

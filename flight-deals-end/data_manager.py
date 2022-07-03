from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/723bdf2ed078033a458b93f67d37c466/cheapFlight/工作表1"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/723bdf2ed078033a458b93f67d37c466/cheapFlight/工作表2"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["工作表1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["工作表2"]
        return self.customer_data
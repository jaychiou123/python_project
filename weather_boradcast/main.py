import requests
from twilio.rest import Client

api_key = "a879e2042984dc34f3d2e7a9285efc87"
paramters = {
    "lat": 25.032969,
    "lon": 121.565414,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
account_sid = "ACda0e3734fa670ae18b8441cf6f81b4a0"
auth_token = "9ac40e0b6883ee2fda12a1ae727c7996"
client = Client(account_sid, auth_token)

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", paramters)
response.raise_for_status()

data = response.json()
data_list = data["hourly"]
weather_id_list = [data["hourly"][i]["weather"][0]["id"] for i in range(0, 12)]
if any(i > 700 for i in weather_id_list):
    print("Bring an umbrella!!")
    message = client.messages \
        .create(
        body="It might rain, so bring an umbrella.",
        from_='+13512000611',
        to='+886939862682'
    )
else:
    print("Good weather!")
    message = client.messages \
        .create(
        body="Don't worry, today is a good day.",
        from_='+13512000611',
        to='+886939862682'
    )

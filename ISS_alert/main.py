import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 25.032969 # Your latitude
MY_LONG = 121.565414 # Your longitude

my_mail = "jay912145@gmail.com"
password = "prniebnwidnvddeu"
receive = "jay912145@yahoo.com.tw"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

while(True):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    #If the ISS is close to my current position
    if abs(iss_longitude - MY_LONG) < 5 and abs(iss_latitude - MY_LAT) < 5 and (time_now > sunset or time_now < sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=my_mail, password=password)
            connect.sendmail(from_addr=my_mail, to_addrs=my_mail, msg="Subject:Look up now!!!\n\nIss is right above you. Look up and make a wish.")
    time.sleep(60)





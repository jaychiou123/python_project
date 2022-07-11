from bs4 import BeautifulSoup
import requests
import smtplib

my_mail = "jay912145@gmail.com"
password = "prniebnwidnvddeu"
receive = "jay912145@gmail.com"
TARGET_PRICE = 200
headers = {
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url="https://www.amazon.com/-/zh_TW/Timberland-%E7%94%B7%E6%AC%BE"
                            "-Earthkeepers-Rugged-15-2/dp/B004L36W7C/ref=sr_1_55?"
                            "keywords=timberland%2Bboots%2Bfor%2Bmen&qid=1657538764&sprefix"
                            "=timber%2Caps%2C322&sr=8-55&th=1&psc=1", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name="span", class_="a-price-whole")
price = float(price.get_text().split(".")[0])
if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_mail, password=password)
        connect.sendmail(
            from_addr=my_mail,
            to_addrs=receive,
            msg=f"Subject: Low price alert!\n\nThe price of the item you are looking for is below {TARGET_PRICE}. "
                f"Go ahead to buy it.\nhttps://www.amazon.com/-/zh_TW/Timberland-%E7%94%B7%E6%AC%BE-"
                f"Earthkeepers-Rugged-15-2/dp/B004L36W7C/ref=sr_1_55?keywords=timberland%2Bboots%2Bfor%2Bmen&qid"
                f"=1657538764&sprefix=timber%2Caps%2C322&sr=8-55&th=1&psc=1")
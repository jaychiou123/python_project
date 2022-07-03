import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key_for_Stock = "GSJIG47YJK34LJPS"
api_key_for_news = "bef988259724460f80b24dc6a1f73080"
account_sid = "ACda0e3734fa670ae18b8441cf6f81b4a0"
auth_token = "9ac40e0b6883ee2fda12a1ae727c7996"

para_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_for_Stock,

}

para_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": api_key_for_news
}
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news = requests.get("https://newsapi.org/v2/everything", para_news)
news.raise_for_status()
article_list = news.json()["articles"]
three_articles = article_list[:3]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock = requests.get("https://www.alphavantage.co/query", para_stock)
stock.raise_for_status()
day = datetime.today().date()
two_day = []
while len(two_day) < 2:
    day = day - timedelta(days=1)
    if stock.json()["Time Series (Daily)"].__contains__(str(day)):
        two_day.append(float(stock.json()["Time Series (Daily)"][str(day)]["4. close"]))

diff = two_day[0]-two_day[1]
percen = (diff / two_day[0])*100
if abs(percen) > 5:
    print("Get News")
if diff > 0:
    message = f"TSLA: 🔺{percen}%\n"
else:
    message = f"TSLA: 🔻{percen}%\n"
# total_message = message + f"Headlines:{article_list[0]['title']}\nBrief: {article_list[0]['description']}"
formatted_articles = [f"{message}\nHeadline: {article['title']}. " \
                      f"\nBrief: {article['description']}" for article in three_articles]
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages \
                    .create(
                         body=article,
                         from_='+13512000611',
                         to='+886939862682'
                     )

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


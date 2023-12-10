import requests
from twilio.rest import Client
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("groupprojhackthenest@gmail.com", "joemama!22")


    # account_sid = 'AC8d3a21849e43ae8e0886a75bac741aee'
    # auth_token = SMS_TKN
    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    # from_='+18444801049',
    # body='Hello from Twilio',
    # to='+18777804236'
    # )

    # print(message.sid)
    # Don't work

STOCK_NAME = "NVDA"
COMPANY_NAME = "NVIDIA Corp"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "EHGL1SJUYHLB3CDE"
NEWS_API_KEY = "94ae0b563ace46ae83fc42f41eaef314"
SMS_SID = "AC8d3a21849e43ae8e0886a75bac741aee"
SMS_TKN = "d73364f9e93d9e542962ab947fd1a73c"



stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
resp = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = resp.json()["Time Series (Daily)"]
data_values = [value for (key, value) in data.items()]
yesterday_data = data_values[0]
yesterday_close_price = yesterday_data["4. close"]
two_days_before_data = data_values[1]
two_day_before_close_price = two_days_before_data["4. close"]

difference = abs(float(yesterday_close_price) - float(two_day_before_close_price))
print(difference)
percent_difference = (difference/float(yesterday_close_price)) * 100

if percent_difference > .1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_resp = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_articles = news_resp.json()["articles"]
    top_3_articles = news_articles[:3]
    list_of_3_articles = [f"Title: {articles['title']}\n\t Summary: {articles['description']}" for articles in top_3_articles]
    email_body = "\n".join(list_of_3_articles)
    server.sendmail("groupprojhackthenest@gmail.com", "zalexep@gmail.com", email_body.encode("utf-8"))
    print("Ya got some mail!")


server.quit()

    
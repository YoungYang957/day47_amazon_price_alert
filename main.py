import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
           'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'}

response = requests.get("https://www.amazon.com/know-theres-tunnel-under-Ocean/dp/B0BP3W1JPB/ref=sr_1_4?crid=2KRCLQ9KSMW0F&keywords=lana+del+rey+vinyl+record&qid=1685125443&sprefix=lana+del+rey+v%2Caps%2C96&sr=8-4",headers=headers)
response.raise_for_status()
response_new = response.text

soup = BeautifulSoup(response_new,"lxml")

price = soup.find(name="span", class_="a-offscreen").getText()
price_float = float(price.split("$")[1])


if price_float < 25:
    message = "you can buy now"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        result = connection.login("EMAIL", "PASSWORD")
        connection.sendmail(
            from_addr= "jinyuanyang957@gmail.com",
            to_addrs= "jinyuanyang957@gmail.com",
            msg= f"Subject: Amazon sales\n\n{message}".encode("utf-8")


        )

from bs4 import BeautifulSoup
import smtplib
import requests

link = "https://www.amazon.com/Keychron-Wireless-Bluetooth-Mechanical-Keyboard/dp/B07YB32H52/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B07YB32H52&psc=1&pd_rd_w=5fPbZ&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=PGEGA9T7SKHB2W8YZFNQ&pd_rd_r=1e7c6fec-e06a-4444-88de-5ed1efd4e9a7&pd_rd_wg=eITHi"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'}
response = requests.get(link, headers=headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "html.parser")
price = soup.find(name='span', attrs={"class": "a-size-medium a-color-price priceBlockDealPriceString",
                                      "id": "priceblock_dealprice"}).text
price = float(price.split("$")[1])
print(price)

# Part 2
SMTP_ADDRESS = 'smtp.gmail.com'
EMAIL = "<EMAIL>"
PASSWORD = "<PASSWORD>"

pruduct_name = soup.find(id="productTitle").get_text().strip()
print(pruduct_name)

BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{pruduct_name} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{link}"
        )

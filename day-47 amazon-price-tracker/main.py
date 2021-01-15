import os
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#### IMPORTANT ####
''' This code works, but Amazon disallow bots to scrap their site with an authentication.
So it might works at the beginning but not for a long time '''
options = Options()
options.headless = True
chrome_driver_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
'''I decided to add selenium in this project in order to make it work. But this in the real
project, selenium is not used'''

my_email = os.environ['MY_EMAIL']
my_password = os.environ['MY_EMAIL_PASSWORD']


TARGET_PRICE = 3000.0
AMAZON_URL = os.environ['AMAZON_URL']
CLASS_PRICE = "a-size-medium a-color-price priceBlockBuyingPriceString"
CLASS_TITLE = "a-size-large product-title-word-break"

driver.get(AMAZON_URL)
price = driver.find_element(By.ID, "priceblock_ourprice")
title = driver.find_element(By.ID, "productTitle")

complete_price = ""
for digits in price.text.split():
    digits = digits.replace(",", ".")
    try:
        float(digits)
    except ValueError:
        continue
    else:
        complete_price += digits

complete_price = float(complete_price)
if complete_price < TARGET_PRICE:
    message = f"The article '{title.text}' is under the max price you set ({TARGET_PRICE}€). It's time ! \n" \
              f"{AMAZON_URL} \n" \
              f"PS: It's Clem ;)"
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg=f"Subject:Amazon Price Alert ! \n\n"
                                f"{message}".encode('utf-8'))


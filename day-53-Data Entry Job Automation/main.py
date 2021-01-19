import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

CHROME_DRIVER_PATH = r'C:\chromedriver.exe'
GOOGLE_FORM_LINK = os.environ.get('GOOGLE_FORM_LINK')
ZILLOW_LINK = os.environ.get('ZILLOW_LINK')
ZILLOW_END_POINT = "https://www.zillow.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
}


def format_price(price):
    price = price.split("+")[0]
    price = price.split("/")[0]
    price = price.split(" ")[0]
    return price


response = requests.get(ZILLOW_LINK, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
all_get = soup.find_all(name="div", class_='list-card-info')

all_links = [f"{ZILLOW_END_POINT}{card.find('a')['href']}" if card.find('a')['href'].startswith('/b')
             else card.find('a')['href'] for card in all_get]

all_addresses = [card.find("address").text for card in all_get]

all_prices = soup.find_all(name="div", class_="list-card-price")
all_prices = [format_price(price.text) for price in all_prices]

browser = webdriver.Chrome(CHROME_DRIVER_PATH)
browser.get(GOOGLE_FORM_LINK)
sleep(1)


for address, price, link in zip(all_addresses, all_prices, all_links):
    address_input = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
                                                  '/div/div[1]/input')

    price_input = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/'
                                                'div/div[1]/input')

    link_input = browser.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div'
        '/div[1]/input')

    button = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    address_input.send_keys(address)
    price_input.send_keys(price)
    link_input.send_keys(link)
    button.click()
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    sleep(1)

browser.quit()

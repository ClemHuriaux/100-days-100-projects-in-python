from selenium import webdriver
import selenium.common.exceptions as ex
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
timeout = time.time() + 5
five_min = time.time() + 60*5
items = []
for i in range(17):
    try:
        items.append(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="product{i}"]'))
        ))
    except ex.NoSuchElementException:
        time.sleep(1)
item_ids = [item.get_attribute("id") for item in items]

big_cookie = driver.find_element_by_id("bigCookie")

while True:
    try:
        big_cookie.click()
    except ex.ElementClickInterceptedException:
        time.sleep(1)
    else:
        if time.time() > timeout:
            all_prices = driver.find_elements_by_css_selector("#store span")
            item_prices = []
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    # TODO: issue here when arrived at million
                    cost = int(element_text.replace(",", ""))
                    item_prices.append(cost)

            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            money_element = driver.find_element_by_id("cookies").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            money_element = money_element.split(" ")
            cookie_count = int(money_element[0])

            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element_by_id(to_purchase_id).click()

            print(item_prices)
            timeout = time.time() + 5

        if time.time() > five_min:
            cookie_per_s = driver.find_element_by_id("cps").text
            print(cookie_per_s)
            break


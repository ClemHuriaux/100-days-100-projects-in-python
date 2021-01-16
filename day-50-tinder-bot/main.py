import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as ex


FACEBOOK_USERNAME = os.environ.get("FACEBOOK_USERNAME")
FACEBOOK_PASSWORD = os.environ.get("FACEBOOK_PASSWORD")

url = "https://tinder.com/"
chrome_driver_path = r"C:\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver_path)

browser.get(url)
delay = 3


def wait_to_load(XPATH):
    try:
        return WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, XPATH)))
    except TimeoutException:
        print("Loading took too much time!")


#  connection button:
wait_to_load('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()

#  connect with Facebook:
wait_to_load('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

#  connection with Facebook
base_window = browser.window_handles[0]
fb_login_window = browser.window_handles[1]
browser.switch_to.window(fb_login_window)

email_input = browser.find_element_by_xpath('//*[@id="email"]')
password_input = browser.find_element_by_xpath('//*[@id="pass"]')
email_input.send_keys(FACEBOOK_USERNAME)
time.sleep(2)
password_input.send_keys(FACEBOOK_PASSWORD)
time.sleep(1)
password_input.send_keys(Keys.ENTER)

#  switch back to main page
browser.switch_to.window(base_window)
print(browser.title)

#  Dismiss requests
time.sleep(5)
wait_to_load('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(1)
wait_to_load('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
time.sleep(1)
wait_to_load('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

for n in range(100):

    time.sleep(1)

    try:
        print("called")
        like_button = browser.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #  In case it matches
    except ex.ElementClickInterceptedException:
        try:
            match_popup = browser.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
            match_popup.click()

        #  Handle loading issues
        except ex.NoSuchElementException:
            time.sleep(2)



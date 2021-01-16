import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 200
PROMISED_UP = 100
CHROME_DRIVER_PATH = r'C:\chromedriver.exe'
TWITTER_EMAIL = os.environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')


class InternetSpeedTwitterBot:

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = None
        self.down = None

    def get_internet_speed(self, url):
        self.browser.get(url)
        #  Dismiss cookie warning
        self.browser.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]').click()
        #  Start test
        self.browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        sleep(60)
        #  Dismiss add
        self.browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]'
                                           '/div/div/div[2]/a').click()
        self.down = self.browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                       '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]'
                                                       '/span').text

        self.up = self.browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(f"down: {self.down}\n")
        print(f"up: {self.up}\n")

    def tweet_at_provider(self):
        url = 'https://twitter.com/'
        self.browser.get(url)
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]'
                                           '/a[2]').click()
        sleep(1)
        email_input = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form'
                                                         '/div/div[1]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)
        password_input = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/'
                                                            'form/div/div[2]/label/div/div[2]/div/input')
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        
        sleep(5)
        #  Complain
        tweet_input = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/'
                                                         'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/'
                                                         'div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
                                                         '/div/div/div')
        tweet_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I "
                              f"pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(1)
        #  Click on the Button to post
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                           'div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div'
                                           '/div[2]/div[4]/div/div/div[2]/div[3]/div').click()

        sleep(5)
        self.browser.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed("https://www.speedtest.net/")
bot.tweet_at_provider()

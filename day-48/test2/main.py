from selenium import webdriver

chrome_driver_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_article = driver.find_element_by_css_selector("#articlecount a")
print(number_of_article.text)
driver.quit()
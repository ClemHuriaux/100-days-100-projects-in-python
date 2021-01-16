from selenium import webdriver

chrome_driver_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}
print(events)

driver.quit()
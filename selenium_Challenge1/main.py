from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = '/Users/mouadzeghraoui/PycharmProjects/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.python.org")

Time_list = driver.find_elements_by_css_selector('.event-widget .menu time')
Time = [Time.text for Time in Time_list]
event_name_list = driver.find_elements_by_css_selector(".event-widget .menu li a")
Event_name = [Event_name.text for Event_name in event_name_list]
events = {}

for n in range(len(Event_name)):
    events[n] = {
        "time": Time[n],
        "name": Event_name[n]
    }
print(events)
driver.close()

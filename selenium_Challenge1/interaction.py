from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = '/Users/mouadzeghraoui/PycharmProjects/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(article_count.text)
driver.close()



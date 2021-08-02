from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/mouadzeghraoui/PycharmProjects/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_xpath('//*[@id="cookie"]')

# fname.send_keys('Mouad')


while True:
    try:
        money = int(driver.find_element_by_xpath('//*[@id="money"]').text)
        time_machine = int(driver.find_element_by_css_selector("#buyTime\ machine b").text.split("-")[1].replace(',', ''))
        portal = int(driver.find_element_by_css_selector("#buyPortal b").text.split("-")[1].replace(',', ''))
        Alchemy_lab = int(driver.find_element_by_css_selector("#buyAlchemy\ lab b").text.split("-")[1].replace(',', ''))
        shipment = int(driver.find_element_by_css_selector("#buyShipment b").text.split("-")[1].replace(',', ''))
        mine = int(driver.find_element_by_css_selector("#buyMine b").text.split("-")[1].replace(',', ''))
        factory = int(driver.find_element_by_css_selector("#buyFactory b").text.split("-")[1].replace(',', ''))
        grandma = int(driver.find_element_by_css_selector("#buyGrandma b").text.split("-")[1].replace(',', ''))
        cursor = int(driver.find_element_by_css_selector("#buyCursor b").text.split("-")[1].replace(',', ''))

        if money > time_machine:
            driver.find_element_by_css_selector("#buyTime\ machine b").click()
        elif money > portal:
            driver.find_element_by_css_selector("#buyPortal b").click()
        elif money > Alchemy_lab:
            driver.find_element_by_css_selector("#buyAlchemy\ lab b").click()
        elif money > shipment:
            driver.find_element_by_css_selector("#buyShipment b").click()
        elif money > mine:
            driver.find_element_by_css_selector("#buyMine b").click()
        elif money > factory:
            driver.find_element_by_css_selector("#buyFactory b").click()
        elif money > grandma:
            driver.find_element_by_css_selector("#buyGrandma b").click()
        elif money > cursor:
            driver.find_element_by_css_selector("#buyCursor b").click()
        else:
            cookie.click()
    except:
        pass
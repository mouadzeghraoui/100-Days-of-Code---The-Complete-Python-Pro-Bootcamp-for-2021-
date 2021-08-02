from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/mouadzeghraoui/PycharmProjects/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
Sign_Up = driver.find_element_by_xpath('/html/body/form/button')


fname.send_keys('Mouad')
lname.send_keys('Zegh')
email.send_keys('MZ@example.com')
Sign_Up.click()


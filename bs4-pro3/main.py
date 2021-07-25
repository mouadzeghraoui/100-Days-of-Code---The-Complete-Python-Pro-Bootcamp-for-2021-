from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Reversing a list using reversed()
def Reverse(lst):
    return [ele for ele in reversed(lst)]


options = Options()
options.headless = True
driver = webdriver.Chrome()

driver.get("https://www.empireonline.com/movies/features/best-movies-2")

soup = BeautifulSoup(driver.page_source, "html.parser")
titles = soup.find_all(name='h3', class_='jsx-4245974604')

titles = [title.string for title in titles]

titles[99] = "1) The Godfather"
titles[88] = "12) The Godfather Part II"
titles[51] = "49) Trainspotting"
titles = [title.split(") ")[1] for title in titles]
ordered_titles_list = Reverse(titles)

with open('your_file.txt', 'w') as f:
    for item in ordered_titles_list:
        f.write("%s\n" % item)
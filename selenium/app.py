from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Config to not open browser on test execution

driver = webdriver.Chrome(executable_path="browsers/chromedriver.exe", options=options)
driver.get("https://www.zup.com.br/contato")
driver.maximize_window()

sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "lxml")

print(soup.prettify())
print(soup.find("div", {"class": "text-city-contato"}).text)
print(soup.find("p", {"class": "par-contato"}).text)

driver.close()

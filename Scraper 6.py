import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service("C:/Users/Zak/Desktop/gf.exe")
driver = webdriver.Firefox(service=service)
driver.get('https://www.imdb.com/list/ls050274118/')
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()

qualificaitons = []
# Find the ul with the specific class 'ipc-inline-list'
ul_element = soup.find('ul', class_='ipc-inline-list')

# Extract the text from all li elements inside the ul
qualifications = [li.text for li in ul_element.find_all('li')]
print(qualifications)
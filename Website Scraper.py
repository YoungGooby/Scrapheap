import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service("C:/Users/Zak/Desktop/gf.exe")
driver = webdriver.Firefox(service=service)
driver.get('https://www.biographyonline.net/people/famous-100.html')
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()
ol_tag = soup.find('ol')
names = []
for li_tag in ol_tag.find_all("li"):
    names.append(li_tag.get_text(strip=True))
print(names)

df = pd.DataFrame({'Name' : names})
df.to_csv("names.csv", index=False, encoding='utf-8')
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service("C:/Users/Zak/Desktop/gf.exe")
driver = webdriver.Firefox(service=service)
driver.get('https://www.imdb.com/list/ls050274118/')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"}

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()
names = []
qualifications = []
actor_containers = soup.find_all("div", class_="lister-item-content")
for index, actor_containers in enumerate(actor_containers):
    name_tag = actor_containers.find('a')
    if name_tag:
        actor_name = name_tag.text.strip()
        names.append(actor_name)
    qualifications_list = actor_containers.find('ul', class_='ipc-inline-list')
    if qualifications_list:
        actor_qualifications = [li.text.strip() for li in qualifications_list.find_all('.kwvPJV')]
        qualifications.append(', '.join(actor_qualifications))  # Join the qualifications into a string
    else:
        qualifications.append('N/A')  # In case qualifications are missing

# Check if the lengths of names and qualifications match
if len(names) != len(qualifications):
    print(f"Mismatch: {len(names)} names and {len(qualifications)} qualifications")
    print("Names list:", names)
    print("Qualifications list:", qualifications)
else:
    # Create a DataFrame and save it to CSV
    df = pd.DataFrame({'Name': names, 'Qualifications': qualifications})
    df.to_csv("names.csv", index=False, encoding='utf-8')
    print(df)
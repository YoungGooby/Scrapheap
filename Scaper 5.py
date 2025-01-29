from bs4 import BeautifulSoup  
import requests

try: 
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()

    soup = BeautifulSoup
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd

URL = 'https://www.flashscore.com/match/2JDks1o7/#match-summary'
#URL2 = 'https://www.flashscore.com/match/2JDks1o7/#match-statistics;0'
#URL3 = 'https://www.flashscore.com/match/2JDks1o7/#lineups;1'
#page = requests.get(URL).text

driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
driver.get(URL)

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.quit()

odd = soup.find('tr', class_ = 'odd')
odds = odd.find_all(class_ = 'odds-wrap')
for odd in odds:
    if '[' in odd['eu']:
        odd1 = odd['eu'].split('[')[0]
        odd2 = odd['eu'].split(']')[1]
        print(odd1)
        print(odd2)
    else:
        odd1 = odd['eu']
        odd2 = odd.text

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

URL = 'https://www.flashscore.com/match/2JDks1o7/#match-summary'
URL2 = 'https://www.flashscore.com/match/2JDks1o7/#match-statistics;0'
URL3 = 'https://www.flashscore.com/match/2JDks1o7/#lineups;1'
#page = requests.get(URL).text

driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
driver.get(URL2)

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.quit()

odds = soup.find_all(class_ = 'odds-wrap')

for odd in odds:
    print(odd['alt'])
    odd1 = odd['alt'][:4]
    odd2 = odd['alt'][-4:]
    
    print(odd1)
    print(odd2)
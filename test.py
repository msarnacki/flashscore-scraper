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
driver.get(URL3)

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.quit()

lineups = soup.find('table', class_='parts')
#print(lineups)

names_home = []
for tr in lineups.find_all('td', class_='summary-vertical fl'):
    name_home = tr.find_all(class_='name')
    #print(names_home)
    for name in name_home:
        if '(' in name.text:
            #print(name.text[:-4])
            names_home.append(name.text[:-4])
            #match.append(name.text[:-4])
        else:
            #print(name.text)
            names_home.append(name.text)
            #match.append(name.text)

names_away = []
for tr in lineups.find_all('td', class_='summary-vertical fr'):
    name_away = tr.find_all(class_='name')
    for name in name_away:
        if '(' in name.text:
            #print(name.text[:-4])
            names_away.append(name.text[:-4])
            #match.append(name.text[:-4])
        else:
            #print(name.text)
            names_away.append(name.text)
            #match.append(name.text)
    
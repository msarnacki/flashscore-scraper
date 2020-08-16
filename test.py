import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://www.flashscore.com/match/2JDks1o7/#match-summary'
URL2 = 'https://www.flashscore.com/match/2JDks1o7/#match-statistics;0'
URL3 = 'https://www.flashscore.com/match/2JDks1o7/#lineups;1'
#page = requests.get(URL).text

driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
driver.get(URL2)

time.sleep(3)
driver.get(URL3)
time.sleep(3)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.quit()

lineups = soup.find('table', class_='parts')
#print(lineups)

team_1 = []
for tr in lineups.find_all('td', class_='summary-vertical fl'):
    names_home = tr.find_all(class_='name')
    for name in names_home:
        if '(' in name.text:
            print(name.text[:-4])
        else:
            print(name.text)
        
#for tr in lineups.find_all('td', class_='summary-vertical fr'):
#    names_away = tr.find_all(class_='name')
#    for name in names_away:
        #print(name.text)
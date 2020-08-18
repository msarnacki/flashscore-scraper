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

stats = ['Ball Possession', 'Goal Attempts', 'Shots on Goal', 'Shots off Goal', 'Blocked Shots', 'Free Kicks', 'Corner Kicks',
         'Offsides', 'Goalkeeper Saves', 'Fouls', 'Red Cards', 'Yellow Cards', 'Total Passes', 'Completed Passes', 'Tackles',
         'Attacks', 'Dangerous Attacks']

stats_home = soup.find_all(class_="statText statText--homeValue")
stats_away = soup.find_all(class_="statText statText--awayValue")
    
#adding stats to the list (home > away > home > ...), match, 1 half, 2 half - 15 stats for each
statistics = []
j = 0
for i in range(3*len(stats)):
    if stats_home[j].findNext('div').text == stats[i%len(stats)]:
        statistics.append(stats_home[j].text)
        statistics.append(stats_away[j].text)
        j += 1
        print(j)
    else:
        statistics.extend(['', ''])
        
print(statistics)
print(len(statistics))

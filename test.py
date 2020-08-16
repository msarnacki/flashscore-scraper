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
driver.get(URL)

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.quit()

regex = re.compile('.*detailMS__incidentRow incidentRow--*.')
incidents = soup.find_all("div", {"class": regex})
print(incidents)
for incident in incidents:
    print(incident.text)
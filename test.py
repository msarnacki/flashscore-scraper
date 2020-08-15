import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://www.flashscore.com/match/2JDks1o7/#match-summary'
URL2 = 'https://www.flashscore.com/match/2JDks1o7/#match-statistics;0'
#page = requests.get(URL).text

driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
driver.get(URL)

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.get(URL2)
time.sleep(2)
stats_home = soup.find_all(class_="statText statText--homeValue")
#stats_home = soup.find_all(class_="statText statText--homeValue")
for stat in stats_home:
    print(stat.text)    

driver.quit()
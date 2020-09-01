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

'''driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
driver.get(URL)

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.quit()
'''
start = time.time()

def print_progress(match_num, season):
    print('Match number ' + str(match_num) + ' in ' + season + ' - Time spent: ' + str(time.time() - start))
    
for i in range(100000):
    print_progress(i, 'PL20192020')
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd

URL = 'https://www.flashscore.com/match/2JDks1o7/#match-summary'
URL2 = 'https://www.flashscore.com/match/2JDks1o7/#match-statistics;0'
URL3 = 'https://www.flashscore.com/match/2JDks1o7/#lineups;1'
#page = requests.get(URL).text

'''driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
driver.get(URL2)

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

driver.quit()
'''
def set_urls_xlsx(path):
    df = pd.read_excel(path, usecols = ['URL', 'Done'])
    urls = df['URL'].tolist()
    done1 = df['Done'].tolist()
    i = 0
    while done1[i]=='x':
        print(i)
        i += 1
    
    df.at[i, 'Done'] = 'x'
    df.to_excel(path)
    
set_urls_xlsx('C:/Users/Maciek/Desktop/python_projects/flashscore_scraper/urls.xlsx')
    
#url = 'https://www.flashscore.com/football/germany/bundesliga-2016-2017/results/'
#print(url.split('/')[-3])

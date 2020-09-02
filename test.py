import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
import os

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

urls_path = 'urls.xlsx'

def get_urls_xlsx(path):
    df = pd.read_excel(path, usecols = ['URL'])
    urls1 = df['URL'].tolist()
    #print(urls1)
    
    file_names = os.listdir('data')
    #print(file_names)
    files_league = [f.split('.')[0] for f in file_names]
    #print(files_league)
    
    urls2 = []
    for url in urls1:
        url_league = url.split('/')[-3]   
        if (url_league not in files_league) and (url_league != ''):
           urls2.append(url)

    #print(urls2)
    return urls2

get_urls_xlsx(urls_path)
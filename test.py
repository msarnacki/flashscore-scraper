import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd
import os

def driver_get_source_match_summary(url):
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'summary-content')))
        print('page loaded')
    except TimeoutError:
        print('loading took too much')

    #time for loading all elements
    #time.sleep(3.5)
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def driver_get_source_match_stats(url):
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'statContent')))
        print('page loaded')
    except TimeoutError:
        print('loading took too much')

    #time for loading all elements
    #time.sleep(3.5)
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    return soup
    
def driver_get_source_match_lineups(url):
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'lineups-wrapper')))
        print('page loaded')
    except TimeoutError:
        print('loading took too much')

    #time for loading all elements
    #time.sleep(3.5)
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def driver_get_source_season(url):
    driver.get(url)
    
    #time for loading all elements
    time.sleep(3.5)

    try:
        button_cookies = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
        button_cookies.click()
    except:
        print("cookies already closed")

    #click "more matches" until it is possible
    while('event__more' in driver.page_source):
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'event__more.event__more--static')))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button_more = driver.find_element_by_class_name('event__more.event__more--static')
        button_more.click()
        #time.sleep(5)
        
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    return soup



URL = 'https://www.flashscore.com/match/2JDks1o7/#match-summary'
URL2 = 'https://www.flashscore.com/match/2JDks1o7/#match-statistics;0'
URL3 = 'https://www.flashscore.com/match/2JDks1o7/#lineups;1'
#page = requests.get(URL).text

start = time.time()

driver = webdriver.Chrome() 
#driver.get(URL)

#time.sleep(2)

#page = driver.page_source

#soup = BeautifulSoup(page, 'html.parser')

soup = driver_get_source_match_summary(URL)

league_round = soup.find('span', class_ = 'description__country').find('a').text
print(league_round)

odd = soup.find('tr', class_ = 'odd')
odds = odd.find_all(class_ = 'odds-wrap')
for odd in odds:
    if '[' in odd['eu']:
        odd1 = odd['eu'].split('[')[0]
        odd2 = odd['eu'].split(']')[1]
    else:
        odd1 = odd['eu']
        odd2 = odd.text

    print(odd1)
    print(odd2)
    
    
soup = driver_get_source_match_stats(URL2)

stats_home = soup.find_all(class_="statText statText--homeValue")
stats_away = soup.find_all(class_="statText statText--awayValue")

for i in range(len(stats_home)):
    print(stats_home[i].text)


soup = driver_get_source_match_lineups(URL3)


lineups = soup.find('table', class_='parts')
print(lineups)

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

print(names_home)
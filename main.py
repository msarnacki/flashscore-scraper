import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.flashscore.com/football/england/premier-league/results/'

driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
driver.get(URL)

#time for loading all elements
time.sleep(3)
#close cookies notification
button_cookies = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
button_cookies.click()

#click "more matches" until it is possible
while('event__more' in driver.page_source):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button_more = driver.find_element_by_class_name('event__more.event__more--static')
    button_more.click()
    time.sleep(2)
    
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')

res = soup.find_all(class_='event__match event__match--static event__match--oneLine')

ids = []

for re in res:
    ids.append(re.get('id'))
        
ids = [id[4:] for id in ids]
#print(ids)    

for id in ids[:1]:    
    match = []
    match.append(id)
    
    ###urls for match
    url_match_summary = 'https://www.flashscore.com/match/'+id+'/#match-summary'
    url_match_stats = 'https://www.flashscore.com/match/'+id+'/#match-statistics;0'
    
    #print(url)
    driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
    driver.get(url_match_summary)
    time.sleep(1)
    page = driver.page_source
    driver.quit()
    
    soup = BeautifulSoup(page, 'html.parser')
    
    ###
    #MATCH SUMMARY
    ###
    
    teams1 = soup.find_all("div", {"class":"tname__text"})
    for teams in teams1:
        teams2 = teams.find_all("a", {"class":"participant-imglink"})
        for team in teams2:
            #print(team.text)
            match.append(team.text)
            
    scores = soup.find_all(class_='scoreboard')
    for score in scores:    
        #print(score.text)
        match.append(score.text)
    
    h1_score_home = soup.find(class_="p1_home")
    #print(h1_score_home.text[0])
    match.append(h1_score_home.text[0])
    
    h1_score_away = soup.find(class_="p1_away")
    #print(h1_score_away.text[0])
    match.append(h1_score_away.text[0])
    
    h2_score_home = soup.find(class_="p2_home")
    #print(h2_score_home.text[0])
    match.append(h2_score_home.text[0])
    
    h2_score_away = soup.find(class_="p2_away")
    #print(h2_score_away.text[0])
    match.append(h2_score_away.text[0])
    
    ###
    #STATS
    ###
    driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
    driver.get(url_match_stats)
    time.sleep(1)
    page = driver.page_source
    driver.quit()
    
    soup = BeautifulSoup(page, 'html.parser')
    
    stats_home = soup.find_all(class_="statText statText--homeValue")
    for stat in stats_home:
        print(stat.text)    
    
    print(match)
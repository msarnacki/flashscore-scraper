import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

#laptop
#driver = webdriver.Chrome('C:/Users/Maciej/Desktop/Programy/chromedriver.exe') 
#pc
driver = webdriver.Chrome() 
#driver = webdriver.Firefox() 
#driver.fullscreen_window()
driver.maximize_window()

### 
# this part would appear multiple times in the code
###
def driver_get_source(url):
    driver.get(url)
    
    #time for loading all elements
    time.sleep(2.5)
    
    if 'football' in url:
        #close cookies notification
        button_cookies = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
        button_cookies.click()
    
        #click "more matches" until it is possible
        while('event__more' in driver.page_source):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button_more = driver.find_element_by_class_name('event__more.event__more--static')
            
            button_more.click()
            time.sleep(5)
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    
    return soup

url_results = 'https://www.flashscore.com/football/england/premier-league/results/'
url_match_prefix = 'https://www.flashscore.com/match/'

###
# get source code from main page with results
###
soup = driver_get_source(url_results)

###
# find and save ids of all matches
###
res = soup.find_all(class_='event__match event__match--static event__match--oneLine')
ids = []

for red in res:
    ids.append(red.get('id'))
        
ids = [id[4:] for id in ids]
#print(ids)    

###
# going through matches
###

for id in ids[:1]:    
    match = []
    match.append(id)
    
    ###urls for match
    url_match_summary = url_match_prefix+id+'/#match-summary'
    url_match_stats = url_match_prefix+id+'/#match-statistics;0'
    url_lineups = url_match_prefix+id+'/#lineups;1'
    
    ###
    #MATCH SUMMARY
    ###
    
    #print(url_match_summary)
    soup = driver_get_source(url_match_summary)
    
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
    soup = driver_get_source(url_match_stats)
    
    stats_home = soup.find_all(class_="statText statText--homeValue")
    stats_away = soup.find_all(class_="statText statText--awayValue")
    
    #adding stats to the list (home > away > home > ...), match, 1 half, 2 half - 15 stats for each
    for i in range(len(stats_home)):
        #print(stats_home[i].text)    
        match.append(stats_home[i].text)
        #print(stats_away[i].text)    
        match.append(stats_away[i].text)
    
    ###
    #LINEUPS
    ###
    soup = driver_get_source(url_lineups)
    
    lineups = soup.find('table', class_='parts')
    #print(lineups)

    for tr in lineups.find_all('td', class_='summary-vertical fl'):
        names_home = tr.find_all(class_='name')
        for name in names_home:
            if '(' in name.text:
                #print(name.text[:-4])
                match.append(name.text[:-4])
            else:
                #print(name.text)
                match.append(name.text)
    
    for tr in lineups.find_all('td', class_='summary-vertical fr'):
        names_away = tr.find_all(class_='name')
        for name in names_away:
            if '(' in name.text:
                #print(name.text[:-4])
                match.append(name.text[:-4])
            else:
                #print(name.text)
                match.append(name.text)
     
    ###    
    # INCIDENTS
    ###
    
    #####################
    #poprawić oznaczenia gol/zmiana/kartka itd
    regex = re.compile('.*detailMS__incidentRow incidentRow--*.')
    incidents = soup.find_all("div", {"class": regex})
    #print(incidents)
    for incident in incidents:
        #print(incident.text)
        
        
        match.append(incident.get_text(strip=True))
        
    driver.quit()
    
    print(match)
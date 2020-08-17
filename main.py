import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd

start = time.time()

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

################################
incidents_cols = []
for i in range(40):
    incidents_cols.append("incident_"+str(i+1))

column_names = ['match_id', 'home_team', 'away_team', 'FT_home_sc', 'FT_away_sc', 'FH_home_sc', 'FH_away_sc', 'SH_home_sc', 'SH_away_sc',
                'FT_home_possession','FT_away_possession', 'FT_home_goal_attempts', 'FT_away_goal_attempts', 'FT_home_shots_on_goal', 'FT_away_shots_on_goal',
                'FT_home_shots_off_goal', 'FT_away_shots_off_goal', 'FT_home_blocked_shots', 'FT_away_blocked_shots', 'FT_home_freekicks', 'FT_away_freekicks',
                'FT_home_corners', 'FT_away_corners', 'FT_home_offsides', 'FT_away_offsides', 'FT_home_gk_saves', 'FT_away_gk_saves', 'FT_home_fouls', 'FT_away_fouls',
                'FT_home_yellow_cards', 'FT_away_yellow_cards', 'FT_home_passes', 'FT_away_passes', 'FT_home_passes_completed', 'FT_away_passes_completed',
                'FT_home_tackles', 'FT_away_tackles', 'FT_home_attacks', 'FT_away_attacks', 'FT_home_dangerous_attacks', 'FT_away_dangerous_attacks',
                'FH_home_possession','FH_away_possession', 'FH_home_goal_attempts', 'FH_away_goal_attempts', 'FH_home_shots_on_goal', 'FH_away_shots_on_goal',
                'FH_home_shots_off_goal', 'FH_away_shots_off_goal', 'FH_home_blocked_shots', 'FH_away_blocked_shots', 'FH_home_freekicks', 'FH_away_freekicks',
                'FH_home_corners', 'FH_away_corners', 'FH_home_offsides', 'FH_away_offsides', 'FH_home_gk_saves', 'FH_away_gk_saves', 'FH_home_fouls', 'FH_away_fouls',
                'FH_home_yellow_cards', 'FH_away_yellow_cards', 'FH_home_passes', 'FH_away_passes', 'FH_home_passes_completed', 'FH_away_passes_completed',
                'FH_home_tackles', 'FH_away_tackles', 'FH_home_attacks', 'FH_away_attacks', 'FH_home_dangerous_attacks', 'FH_away_dangerous_attacks',
                'SH_home_possession','SH_away_possession', 'SH_home_goal_attempts', 'SH_away_goal_attempts', 'SH_home_shots_on_goal', 'SH_away_shots_on_goal',
                'SH_home_shots_off_goal', 'SH_away_shots_off_goal', 'SH_home_blocked_shots', 'SH_away_blocked_shots', 'SH_home_freekicks', 'SH_away_freekicks',
                'SH_home_corners', 'SH_away_corners', 'SH_home_offsides', 'SH_away_offsides', 'SH_home_gk_saves', 'SH_away_gk_saves', 'SH_home_fouls', 'SH_away_fouls',
                'SH_home_yellow_cards', 'SH_away_yellow_cards', 'SH_home_passes', 'SH_away_passes', 'SH_home_passes_completed', 'SH_away_passes_completed',
                'SH_home_tackles', 'SH_away_tackles', 'SH_home_attacks', 'SH_away_attacks', 'SH_home_dangerous_attacks', 'SH_away_dangerous_attacks',
                'home_player_1', 'home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10',  'home_player_11',
                'home_sub_1', 'home_sub_2', 'home_sub_3', 'home_sub_4', 'home_sub_5', 'home_sub_6', 'home_sub_7', 'home_sub_8', 'home_sub_9',
                'away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10',  'away_player_11',
                'away_sub_1', 'away_sub_2', 'away_sub_3', 'away_sub_4', 'away_sub_5', 'away_sub_6', 'away_sub_7', 'away_sub_8', 'away_sub_9']

column_names.extend(incidents_cols)
#################################

url_results = 'https://www.flashscore.com/football/england/premier-league/results/'
url_match_prefix = 'https://www.flashscore.com/match/'

###
# get source code from main page with results
###
soup = driver_get_source(url_results)

###
# find and save ids of all matches
###
res = soup.find_all(True, {"class":['event__match event__match--static event__match--oneLine', 'event__match event__match--static event__match--last event__match--oneLine']})
ids = []

for red in res:
    ids.append(red.get('id'))
        
ids = [id[4:] for id in ids]
print(ids)    
print(len(ids))

###
# going through matches
###

matches = []

#for id in ids[-2:]:  
for id in ids:    
    match = []
    match.append(id)
    
    ###urls for match
    url_match_summary = url_match_prefix+id+'/#match-summary'
    url_match_stats = url_match_prefix+id+'/#match-statistics;0'
    url_lineups = url_match_prefix+id+'/#lineups;1'
    
    #print(url_match_summary)
    
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
    
    if len(names_home) == 18:
        for i in range(2):
            names_home.append('')
            names_away.append('')
            
    match.extend(names_home)
    match.extend(names_away)
    
    ###    
    # INCIDENTS
    ###
    regex_incidentRow = re.compile('.*detailMS__incidentRow incidentRow--*.')
    incidents = soup.find_all("div", {"class": regex_incidentRow})
    #print(incidents)
    for incident in incidents:
        team = ""
        minute = ""
        incident_name = ""
        who = ""
        who2 = ""
        
        child = incident.findChildren(recursive= False)
        for inc in child:
            
            #time
            if any(string in ['time-box','time-box-wide'] for string in inc.get('class')):
                minute = str(inc.text)
            #team
                if 'incidentRow--away' in inc.findParent(recursive = False).get('class'):
                    team = "A"
                elif 'incidentRow--home' in inc.findParent(recursive = False).get('class'):
                    team = "H"   
            #type of incidents
            elif 'soccer-ball' in inc.get('class'):
                incident_name = "G-"
            elif 'y-card' in inc.get('class'):
                incident_name = "Y-"
            elif 'r-card' in inc.get('class'):
                incident_name = "R-"
            elif 'substitution-in' in inc.get('class'):
                incident_name = "S-"
            #main person
            elif any(string in ['substitution-in-name','participant-name'] for string in inc.get('class')):
                who = str(inc.text)
            #second person / (penalty) etc.
            elif any(string in ['substitution-out-name','assist-note-name', 'subincident-name'] for string in inc.get('class')):
                who2 = str(inc.text)
                if 'substitution-out-name' in inc.get('class'):
                    if 'incidentRow--away' in inc.findParent(recursive = False).get('class'):
                        who2 = who2[:-1]
                    elif 'incidentRow--home' in inc.findParent(recursive = False).get('class'):
                        who2 = who2[1:]
            
        incident_str = team + minute + incident_name + who + '-' + who2    
        #print(incident_str)
        match.append(incident_str)
        
    #print(match)
    while len(match) < len(column_names):
        match.append('')
    matches.append(match)
    
    end = time.time()
    print(str(len(matches)) + " - " + str(end-start))
    
driver.quit()

df = pd.DataFrame(matches, columns = column_names)
print(df.head())

df.to_excel("Premier League 19/20.xlsx")
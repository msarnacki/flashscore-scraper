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
#print(incidents)
for incident in incidents:
    team = ""
    time = ""
    incident_name = ""
    who = ""
    who2 = ""
    
    child = incident.findChildren(recursive= False)
    for inc in child:
        
        #print(inc.text)
        #print(inc.get('class'))
        #print("\n AAA \n")
        
        
        #time
        if any(string in ['time-box','time-box-wide'] for string in inc.get('class')):
            time = str(inc.text)
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
                    
    incident_str = team + time + incident_name + who + '-' + who2    
    print(incident_str)
        
    #print("\n BBB \n")
    
    #print(incident.text)
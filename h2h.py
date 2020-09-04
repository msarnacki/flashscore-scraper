import time

from bs4 import BeautifulSoup
from selenium import webdriver

def get_matches_info(matches, how_many):
    for i, match in enumerate(matches):
        if i == how_many:
            break
        
        teams = match.find_all(class_ = 'name')
        team1 = teams[0].text
        team2 = teams[1].text
    
        score = match.find(class_ = 'score').text
        
        print(str(i) + '. ' + team1 + ' ' + score + ' ' + team2)


driver = webdriver.Chrome() 
#driver = webdriver.Firefox() 
#driver.fullscreen_window()
#driver.maximize_window()

#example scheduled match info from first round of next Premier League season
url_h2h = 'https://www.flashscore.com/match/j9iuZEuo/#h2h;overall'

driver = webdriver.Chrome()
driver.get(url_h2h)

time.sleep(3)

#closing cookies
try:
    button_cookies = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
    button_cookies.click()
except:
    print("cookies already closed")

#get source code of page
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')


### CLICKING 4 TIMES
#this part is not necessary because even matches that are not shown shown are in the source code
for i in range(2):
    #gets list of elements with arrows (arrows are always with "Show more matches")
    show_more = driver.find_elements_by_class_name('arrow')

    #click first more and wait a second
    show_more[0].click()
    time.sleep(1)
    
    #click  second more and wait a second
    show_more[1].click()
    time.sleep(1)
###


page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

#this line takes only matches from {Overall} section in H2H and not from {HOMETEAM - Home} or {AWAYTEAM - Away}
overall = soup.find(id = 'tab-h2h-overall')

home_matches = overall.find(class_ = 'h2h_home').find_all(class_ = 'highlight')
away_matches = overall.find(class_ = 'h2h_away').find_all(class_ = 'highlight')
mutual_matches = overall.find(class_ = 'h2h_mutual').find_all(class_ = 'highlight')

#getting info about matches in overall section
#matches = overall.find_all(class_ = 'highlight')
#print(matches)
print("Home team last matches")
get_matches_info(home_matches, 15)

print("Away team last matches")
get_matches_info(away_matches, 15)

print("VS each other last matches")
get_matches_info(mutual_matches, 5)

'''for i, match in enumerate(home_matches):
    teams = match.find_all(class_ = 'name')
    team1 = teams[0].text
    team2 = teams[1].text

    score = match.find(class_ = 'score').text
    
    print(str(i) + '. ' + team1 + ' ' + score + ' ' + team2)

for i, match in enumerate(away_matches):
    teams = match.find_all(class_ = 'name')
    team1 = teams[0].text
    team2 = teams[1].text

    score = match.find(class_ = 'score').text
   
    print(str(i) + '. ' + team1 + ' ' + score + ' ' + team2)


for i, match in enumerate(mutual_matches):
    teams = match.find_all(class_ = 'name')
    team1 = teams[0].text
    team2 = teams[1].text

    score = match.find(class_ = 'score').text
    
    print(str(i) + '. ' + team1 + ' ' + score + ' ' + team2)
'''
# script scrapes more matches than 15 for a team, but if you want only 15 you could add some loops and if statements to get obly 15 for a team


driver.quit()
import time

from bs4 import BeautifulSoup
from selenium import webdriver

#function getting h2h matches info
def get_matches_info(matches, how_many):
    for i, match in enumerate(matches):
        # breaks a loop when how_many matches are scraped
        if i == how_many:
            break
        
        #getting names
        teams = match.find_all(class_ = 'name')
        team1 = teams[0].text
        team2 = teams[1].text
        #getting score
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

#get lists of matches
# find chooses table
# find_all gets every row with matches from that table 
home_matches = overall.find(class_ = 'h2h_home').find_all(class_ = 'highlight')
away_matches = overall.find(class_ = 'h2h_away').find_all(class_ = 'highlight')
mutual_matches = overall.find(class_ = 'h2h_mutual').find_all(class_ = 'highlight')


#print(matches)
print("Home team last matches")
get_matches_info(home_matches, 15)

print("Away team last matches")
get_matches_info(away_matches, 15)

print("VS each other last matches")
get_matches_info(mutual_matches, 5)


driver.quit()
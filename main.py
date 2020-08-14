import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.flashscore.pl/pilka-nozna/anglia/premier-league/wyniki/'
#page = requests.get(URL)

driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 

driver.get(URL)


time.sleep(3)
button_cookies = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
button_cookies.click()


#click "more" until it is possible
while('event__more' in driver.page_source):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button_more = driver.find_element_by_class_name('event__more.event__more--static')
    button_more.click()
    time.sleep(0.5)
    

time.sleep(2)

page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')

res = soup.find_all(class_='event__match event__match--static event__match--oneLine')

ids = []

for re in res:
    ids.append(re.get('id'))
        
ids = [id[4:] for id in ids]
print(ids)    

for id in ids[:1]:    
    url = 'https://www.flashscore.pl/mecz/'+id+'/#szczegoly-meczu'
    print(url)
    driver = webdriver.Chrome('C:/Users/Maciek/Desktop/Programy/chromedriver.exe') 
    driver.get(url)
    time.sleep(1)
    
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    
    scores = soup.find_all(class_='scoreboard')
    print(scores)
    
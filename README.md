# FlashScore scraper

It is my first web scraping script. I am interested in football and stiatistics of all kind and that's why I chose to scrape match details and results from FlashScore.com.

## How does it work?
Firstly, the script look what seasons are already scraped based on files in /data directory. It creates list of urls it needs to scrape. Then for every url it gets ids of all matches on a given page (scrolls and presses "More" button untill there are more matches to load). For example it may be page with results of all maches in Premier League in season 19/20.
Next thing is opening every match and getting match details.
At the end everything is stored in pandas dataframe and saved into excel files.

Before time optimalization getting data from one season took between 50 and 80 minutes. Using **WebdriverWait** made scraping about **5 times faster**.
To get all the data from one season script needs to work about 10-18 minutes depending on how much data there is. For newer matches and ones from more popular leagues it takes more time because data is more precise.

Main script (the one descriped above) is **[main.py](../master/main.py)**.

Previous version of script is in [archive](../master/archive) directory. It could only script one season at a time, was about 4-5 times slower and had many bugs.

## Scraped data
Teams and lineups (first squad and subs), score, referee, betting odds, statistics (fulltime, first half and second half for every statistic) for example: ball possession, shots on target, shots off target, saves, cards and passes.
For every match scraped are also all incidents that happend during a match. They are for example: goals, yellow and red cards, substitutions. For every of them there are also more details (scorer, assist, sub in - sub out, own goal, penalty kick missed, VAR).

Scraped data includes 196 columns. For example in one Premier League season there are 380 matches.

## Technologies used:
- Python 3
- Spyder
- Selenium
- chromedriver / geckodriver
- BeautifulSoup4
- pandas
- git

## Fragments of scraped data

<p align="left">
<img src="img/part1.png"/>
</p>
<p align="left">
<img src="img/part2.png"/>
</p>
<p align="left">
<img src="img/part3.png"/>
</p>
<p align="left">
<img src="img/part4.png"/>
</p>

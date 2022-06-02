<h1> Twitter scraper selenium </h1>
<p> Python's package to scrap Twitter's front-end easily with selenium.  </p>


[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://opensource.org/licenses/MIT) [![Python >=3.6.9](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green.svg)](https://github.com/shaikhsajid1111/facebook_page_scraper/graphs/commit-activity)

# Twitter_scraper_without_API

this codes were developed to extract information from the twitter without using API as there are a limitation and costs for using official twitter API. yu can extract based on your keyword and time frame (in minutes). you can extract unlimitted number of twittes. 


## Pre-requests

 - Python 3.6+
 - Browsers(Firefox)

## Instalation 

you can install from source code using 

    git clone https://github.com/HamedMinaeizaeim/twitter_scraper_without_API.git
 and then run 
 

    Python setup.py install 
   or you can run 
   

    pip install -r requirements.txt
alternatively, you can in stall using **PyPl** : 

   

     pip install twitter_scraper_without_API
    




## How to use 

to use this library, you just need to import the TwitterScrapper scrapper class and then specify your keyword search. By default, it will return all twitter within a minute. you can change it to extract twitts in the last n minutes. Here is a code to do that: 

     from src.twitter_scraper import TwitterScrapper
     twitter = TwitterScrapper('bitcoin')
     twitter.last_n_mins = 3
     twitter.fetch_data()

## Export option

you can export data as json, panda (Dataframe) and csv

    df = twitter.store_data('dataFrame')
    csv = twitter.store_data('csv')
    json = twitter.store_data('json')


## Privacy

there is no issue with privacy in this library and search is based on publicly avaialble information 

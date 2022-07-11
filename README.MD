<h1> Twitter scraper selenium </h1>
<p> Python's package to scrape Twitter's front-end easily with selenium.  </p>


[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://opensource.org/licenses/MIT) [![Python >=3.6.9](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green.svg)](https://github.com/shaikhsajid1111/facebook_page_scraper/graphs/commit-activity)

# Twitter_scraper_without_API

This code was developed to extract information from twitter without using API as there are a limitation and costs for using official twitter API. You can extract based on your keyword and time frame (in minutes). You can extract unlimitted number of tweets. 


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
alternatively, you can install using **PyPl** : 

   

     pip install twitter_scraper_without_API
    




## How to use 

To use this library, you just need to import the TwitterScraper scraper class and then specify your keyword search. By default, it will return all tweets within a minute. You can change it to extract tweets in the last n minutes. Here is a code to do that: 

     from src.twitter_scraper_without_api import TwitterScraper
     twitter = TwitterScraper('bitcoin')
     twitter.last_n_mins = 3
     twitter.fetch_data()

## Export option

You can export data as json, panda (Dataframe) and csv

    df = twitter.store_data('dataFrame')
    csv = twitter.store_data('csv')
    json = twitter.store_data('json')


## Privacy

There is no issue with privacy in this library and search is based on publicly avaialble information 

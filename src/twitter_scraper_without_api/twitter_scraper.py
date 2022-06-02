from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pytz
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
import datetime
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.parse import quote
from .element_finder import Finder
from .driver_initialisation import DriverInitilizer
from .driver_utils import Utilities
import re, json, os, csv
import dateutil

class TwitterScrapper:
    
    def __init__(self, keyword):
        self.keyword = keyword
        self.since = self.set_since()
        self.until = self.set_untill()
        self.url = "https://twitter.com/search?q={}%20until%3A{}%20since%3A{}&src=typed_query&f=live".format(
            quote(keyword), self.until, self.since)
        self.driver = self.setup_driver()
        self.retry = 10
        self.data = {}
        self._last_n_mins = 1

    def __repr__(self):
        return "TwitterScrapper('bitcoin', 60 )"

    def __str__(self):
        return ""

    @property
    def last_n_mins(self):
        return self._last_n_mins

    @last_n_mins.setter
    def last_n_mins(self, value):
        if str(value).isnumeric():
            self._last_n_mins = value
        else:
            print("you must enter numeric value in mints - 1 mins defult value was replaced")
            self._last_n_mins = 1

    @staticmethod
    def str_to_datetime(str_datetime):
        datetime_old_zone = dateutil.parser.isoparse(str_datetime)
        #datetime_old_zone = datetime.strptime(str_datetime, "%Y-%m-%dT%H:%M:%S.%z")
        nz_datetime_time = datetime_old_zone.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Pacific/Auckland"))
        return nz_datetime_time

    @staticmethod
    def convert_json_to_dataframe(json_data):
        df=[]
        for key in json_data:
            df=[pd.json_normalize(json_data[key]) for key in json_data]
        return pd.concat(df)

    def set_since(self):
        yesterday = datetime.now()-timedelta(days=1)
        return yesterday.strftime('%Y-%m-%d')

    def set_untill(self):
        tomorrow = datetime.now()+timedelta(days=1)
        return tomorrow.strftime('%Y-%m-%d')

    def __check_tweets_presence(self, tweet_list):
        if len(tweet_list) <= 0:
            self.retry -= 1

    def __check_retry(self):
        return self.retry <= 0

    def setup_driver(self):
        # driver = webdriver.Firefox(
        #     executable_path=r"C:\Users\Hamed\PycharmProjects\Twitter_Scraper\geckodriver.exe",
        #     firefox_profile=self.setup_profile())
        firefox = DriverInitilizer()
        driver = firefox.set_driver_for_browser()
        driver.get(self.url)
        driver.set_page_load_timeout(6000)
        return driver


    def obtain_info_from_tweet(self, tweet):
        name = Finder._Finder__find_name_from_post(tweet)
        status, tweet_url = Finder._Finder__find_status(tweet)
        replies = Finder._Finder__find_replies(tweet)
        retweets = Finder._Finder__find_shares(tweet)
        username = tweet_url.split("/")[3]
        status = status[-1]
        is_retweet = Finder._Finder__is_retweet(tweet)
        posted_time = Finder._Finder__find_timestamp(tweet)
        posted_time = TwitterScrapper.str_to_datetime(posted_time)
        content = Finder._Finder__find_content(tweet)
        likes = Finder._Finder__find_like(tweet)
        images = Finder._Finder__find_images(tweet)
        videos = Finder._Finder__find_videos(tweet)
        hashtags = re.findall(r"#(\w+)", content)
        mentions = re.findall(r"@(\w+)", content)
        profile_picture = "https://twitter.com/{}/photo".format(username)
        link = Finder._Finder__find_external_link(tweet)
        return link, profile_picture, mentions, hashtags,\
               videos, images, likes, content, posted_time,\
               is_retweet, status, username, retweets, replies,\
               tweet_url, name


    def update_tweet_data(self, link, profile_picture, mentions, hashtags,
               videos, images, likes, content, posted_time,
               is_retweet, status, username, retweets, replies,
               tweet_url, name):
        self.data[status] = {
            "tweet_id": status,
            "username": username,
            "name": name,
            "profile_picture": profile_picture,
            "replies": replies,
            "retweets": retweets,
            "likes": likes,
            "is_retweet": is_retweet,
            "posted_time": posted_time,
            "content": content,
            "hashtags": hashtags,
            "mentions": mentions,
            "images": images,
            "videos": videos,
            "tweet_url": tweet_url,
            "link": link
        }

    def fetch_data(self):
        #try:
        all_ready_fetched_posts = []
        time.sleep(4)
        present_tweets = Finder._Finder__fetch_all_tweets(self.driver)
        self.__check_tweets_presence(present_tweets)
        all_ready_fetched_posts.extend(present_tweets)
        latest_time_now = datetime.now()
        latest_time_now = latest_time_now.replace(tzinfo=None).astimezone(pytz.timezone("Pacific/Auckland"))
        ref_date_time = latest_time_now-timedelta(minutes=self._last_n_mins)

        while (latest_time_now-ref_date_time).total_seconds()>0:

            for tweet in present_tweets:

                link, profile_picture, mentions, hashtags, \
                videos, images, likes, content, posted_time, \
                is_retweet, status, username, retweets, replies, \
                tweet_url, name = self.obtain_info_from_tweet(tweet)
                self.update_tweet_data(link, profile_picture, mentions, hashtags,
                                       videos, images, likes, content, posted_time,
                                       is_retweet, status, username, retweets, replies,
                                       tweet_url, name)

                if (posted_time-latest_time_now).total_seconds()<0:
                    latest_time_now = posted_time

            Utilities._Utilities__scroll_down(self.driver)
            Utilities._Utilities__wait_until_completion(self.driver)
            Utilities._Utilities__wait_until_tweets_appear(self.driver)
            present_tweets = Finder._Finder__fetch_all_tweets(self.driver)
            present_tweets = [post for post in present_tweets if post not in all_ready_fetched_posts]
            self.__check_tweets_presence(present_tweets)
            all_ready_fetched_posts.extend(present_tweets)
            if self.__check_retry() is True:
               break

    def store_data(self, format='Json'):
        if format.lower()=='json':
            return self.data
        elif format.lower()=='dataframe':
            return TwitterScrapper.convert_json_to_dataframe(self.data)
        elif format.lower()=='csv':
            df = TwitterScrapper.convert_json_to_dataframe(self.data)
            return df.to_csv()
        else:
            print("it dose not sopport that format")



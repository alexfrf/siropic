# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:54:31 2021

@author: aleex
"""


import pandas as pd
import numpy as np
import requests
from selenium import webdriver # SELENIUM
from bs4 import BeautifulSoup # BEAUTIFULSOUP
import time
import os, os.path
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.common.action_chains import ActionChains
from github import Github
import shutil
import tweepy


#from pynput.keyboard import Key,Controller
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET_KEY'
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET_KEY'

#keyboard = Controller()

pat = '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'

ruta = 'C:\\Users\\aleex\\Data Science Projects\\Portfolio/Siro/Pics'
github = Github(pat)
repo = github.get_user().get_repo('siropic')
files = repo.get_contents(path="Pics")

file_count = len(files)
num = np.random.randint(file_count)
pict = files[num]
pict = pict.path

file = repo.get_contents(pict)   
sfile = "https://raw.githubusercontent.com/alexfrf/siropic/master/{}".format(pict)
r = requests.get(sfile, stream=True)
if r.status_code == 200:
    with open('img.png', 'wb') as f:
        for chunk in r:
            f.write(chunk)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
status = ""
imagepath = f

api.update_with_media(imagepath, status)
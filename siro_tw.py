# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:54:31 2021

@author: aleex
"""


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup # BEAUTIFULSOUP
import time
import os, os.path
<<<<<<< HEAD
=======
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
>>>>>>> de0b0d47a95953ff035baaacd1f8942a88e3300d
import sys
from github import Github
#import shutil
import tweepy

#from pynput.keyboard import Key,Controller
<<<<<<< HEAD
CONSUMER_KEY = 'ttZybl14j6YMaBd6taf1UxggL'
CONSUMER_SECRET = 'D8bC2vMqg9cUmsT62EXHMA5euYdUe8kLlk11IEI5ZJIJSqUuz0'
ACCESS_KEY = '1133178014844555264-2eJnefpphT7GnevyjQFDzYNLeGT7Xk'
ACCESS_SECRET = 'ML3s8sj1pEJmjfBF3o3lOVNHcTIt8aITIVpumz81cWvck'

#keyboard = Controller()

ruta = '/app/Pics/'
files=[]
for i in os.listdir(ruta):
    files.append(ruta+i)
        
file_count = len(files)
num = np.random.randint(file_count)
pict = files[num]
filename = pict

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
=======
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
filename = 'temp.jpg'
r = requests.get(sfile, stream=True)
if r.status_code == 200:
    with open(filename, 'wb') as f:
        for chunk in r:
            f.write(chunk)
            
else:
    print('Error downloading image')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
>>>>>>> de0b0d47a95953ff035baaacd1f8942a88e3300d

user = api.me()
status = ""
imagepath = filename

<<<<<<< HEAD
api.update_with_media(imagepath, status)
=======
api.update_with_media(imagepath, status)
os.remove(filename)
>>>>>>> de0b0d47a95953ff035baaacd1f8942a88e3300d

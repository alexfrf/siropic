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
#from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.common.action_chains import ActionChains
from github import Github
#import shutil
import tweepy

#from pynput.keyboard import Key,Controller
CONSUMER_KEY = 'ttZybl14j6YMaBd6taf1UxggL'
CONSUMER_SECRET = 'D8bC2vMqg9cUmsT62EXHMA5euYdUe8kLlk11IEI5ZJIJSqUuz0'
ACCESS_KEY = '1133178014844555264-2eJnefpphT7GnevyjQFDzYNLeGT7Xk'
ACCESS_SECRET = 'ML3s8sj1pEJmjfBF3o3lOVNHcTIt8aITIVpumz81cWvck'

#keyboard = Controller()

"""

pat = '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'

ruta = 'C:\\Users\\aleex\\Data Science Projects\\Portfolio/Siro/Pics'
github = Github(pat)
repo = github.get_user().get_repo('siropic')
files = repo.get_contents(path="Pics")
"""
files=[]
for i in os.listdir('/Pics'):
    if '.png' in i:
        files.append(i)
        
file_count = len(files)
num = np.random.randint(file_count)
pict = files[num]
filename = pict

"""

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
    
"""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()
status = ""
imagepath = filename

api.update_with_media(imagepath, status)
os.remove(filename)
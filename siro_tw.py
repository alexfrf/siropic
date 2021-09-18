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
import sys
from github import Github
#import shutil
import tweepy

#from pynput.keyboard import Key,Controller
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

user = api.me()
status = ""
imagepath = filename

api.update_with_media(imagepath, status)
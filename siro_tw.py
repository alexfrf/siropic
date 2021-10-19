# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:54:31 2021

@author: aleex
"""


import pandas as pd
import numpy as np
import requests
import time
import os, os.path
import sys
from github import Github
import tweepy
import os

# Getting our Tweepy keys from an excel file containing our personal tokens

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']



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


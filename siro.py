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
import base64
#from pynput.keyboard import Key,Controller


#keyboard = Controller()


username = "samesiropic"
password = "hakanc10"
pat = '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'
message_bytes = pat.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

ruta = 'C:\\Users\\aleex\\Data Science Projects\\Portfolio/Siro/Pics'
github = Github(pat)
repo = github.get_user().get_repo('siropic')
files = repo.get_contents(path="Pics")



"""
try:
    path, dirs, files = next(os.walk(ruta))
except StopIteration:
    pass


"""
file_count = len(files)
num = np.random.randint(file_count)
pict = files[num]
pict = pict.path

link = "https://twitter.com"

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


# driver.get(link)
# time.sleep(3)
# driver.maximize_window()
# driver.execute_script("window.scrollTo(0, 600)")
process = 0

for i in range(1, 10):
    try:
        driver = webdriver.Chrome("C:\\Users\\aleex\\chromedriver_win32/chromedriver.exe")
        driver.get(link)
        time.sleep(3)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0, 600)")
        inicio = driver.find_element_by_xpath('//span[@role="button"]')
        inicio.click()
        process = 1
    except Exception as e:
        #driver.close()
        print ('Restarting!')
        continue
    else:
        break
file = repo.get_contents(pict)   
sfile = "https://raw.githubusercontent.com/alexfrf/siropic/master/{}".format(pict)
request = requests.get(sfile, stream=True)
#img = Image.open("https://raw.githubusercontent.com/alexfrf/siropic/master/{}".format(pict))
#img.crop((0, 0, img.size[0], 400)).save(pict)    
if process==1:
    driver.find_element_by_xpath('//a[@data-testid="signupButton"]').click()
    time.sleep(3)
    user=driver.find_element_by_name('session[username_or_email]')
    user.send_keys(username)
    pw= driver.find_element_by_xpath('//input[@name="session[password]"]')
    pw.click()
    pw.send_keys(password)
    driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]').click()
    # driver.find_element_by_xpath('//a[@data-testid="SideNav_NewTweet_Button"]').click()
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR,"input[data-testid='fileInput']").send_keys(sfile)
    try:
        print("...uploading", sfile)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.js-show-preview'))
        )
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        # it was a successful upload...
        # Now send the tweet by clicking the button
        driver.find_element_by_css_selector('button.tweet-action').click()
     #driver.find_element_by_xpath('//div[@class="css-18t94o4 css-1dbjc4n r-1niwhzg r-42olwf r-sdzlij r-1phboty r-rs99b7 r-5vhgbc r-mvpalk r-ti0u9o r-2yi16 r-1qi8awa r-1ny4l3l r-o7ynqc r-6416eg r-lrvibr"]').click()
    #driver.find_element_by_xpath('//a[@class="css-4rbku5 css-18t94o4 css-901oao r-k200y r-14j79pv r-1loqt21 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-vc4b81 r-dnmrzs r-bcqeeo r-1udh08x r-1udbk01 r-3s2u2q r-qvutc0"]').click()
    time.sleep(5)
    """
    cuenta = driver.find_element_by_xpath('//label[@data-testid="searchPeople_label"]')
    
    cuenta.click()
    cuenta.send_keys('@sirolopez')
    time.sleep(10)
    #driver.find_element_by_xpath('//div[@data-testid="TypeaheadUser"]')[0].click()
    
    try:
        keyboard.press(Key['down arrow'])
        keyboard.release(Key['down arrow'])
    except:
        keyboard.press(Key['down'])
        keyboard.release(Key['down'])
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Done']"))
        ).click()
    time.sleep(10)
    """
    element = driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]')

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetButtonInline"]'))
        ).click()
    time.sleep(10)
    driver.close()
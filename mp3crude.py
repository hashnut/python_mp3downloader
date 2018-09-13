#! python3
# test.py - Launches a map in the browser using an address from the
# Windows execute(Win+R)  or command line. (https://mp3juices.cc)

import os, sys, pyperclip

from time import sleep
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def downFunc(keyword):

     # Find searchbar and type keyword
     songElem = driver.find_element_by_id('query')
     songElem.send_keys(keyword)

     # Find and push search button
     searchElem = driver.find_element_by_id('button')
     searchElem.click()

     # Find download button and push it (2 download buttons)
     
     sleep(15)
     downElem = driver.find_element_by_class_name('download')
     downElem.click()
     
          
     sleep(25)
     down2Elem = driver.find_element_by_css_selector('a.url')
     down2Elem.click()


     
     # Clear serchbar for next song
     songElem.clear()
     
     sleep(20)



# mp3 downloading website
mp3Link = 'https://mp3juices.cc'


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--disable-gpu")


# 'chromedriver', chrome_options=options
# put above inside .Chrome(HERE!)

driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.get(mp3Link)

# Make user Input and store in the list
keywordList = []

# Enter the song info, seperated by slash or comma
userInput = ' '.join(sys.argv[1:])

keywordRegex = re.compile(r'[^/,\r\n]+')
keywordList = keywordRegex.findall(userInput)

while (len(keywordList) > 0):
          downFunc(keywordList[0])
          del keywordList[0]

sleep(30)
driver.quit()
sys.exit()









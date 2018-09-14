#! python3
# test.py - Launches a map in the browser using an address from the
# Windows execute(Win+R)  or command line. (https://savetomp3.com/ko/)

import os, sys, pyperclip

from time import sleep
import re

from selenium import webdriver

# mp3 downloading website
mp3Link = 'https://savetomp3.com/ko/'


while True:
     # driver = webdriver.Chrome('chromedriver', chrome_options=options)
     driver = webdriver.Chrome()
     # Enter the song info, seperated by slash or comma
     # Make user Input and store in the list
     userInput = ' '.join(sys.argv[1:])
     # userInput = 'havana, all of me'

     keywordRegex = re.compile(r'[^/,\r\n]+')
     keywordList = keywordRegex.findall(userInput)
     print(keywordList)

     while (len(keywordList) > 0):
               driver.get(mp3Link + keywordList[0])
               # Find and push search button
               sleep(7)
               searchElem = driver.find_element_by_class_name('download-mp3')
               sleep(3)
               searchElem.click()
               sleep(10)
               del keywordList[0]

     sleep(10)
     driver.quit()
     sys.exit()









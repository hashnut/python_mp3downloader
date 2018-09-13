#! python3
# test.py - Launches a map in the browser using an address from the
# command line or clipboard. (https://y2mate.com)
# mp3 too good at goodbyes
# mp3
# my love / lose yourself / havana trump cover

import webbrowser, sys, requests
import pyperclip

if len(sys.argv) > 1:
     # Get user input arguments and combine as single string
     keyword = '%20'.join(sys.argv[1:])
     print(keyword)
else:
     # Get song info or url from clipboard
     keyword = pyperclip.paste()

search_link = 'https://y2mate.com/search/' + keyword



# check internet connection
res = requests.get(serach_link)
res.raise_for_status()

mp3Soup = bs4.BeautifulSoup(res.text)
elem_downLink = mp3Soup.select('.item-thumbnail')



# diplay text while downloading mp3 file
print('Downloading...')  

from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://savetomp3.com/ko/나였으면')

time.sleep(5)

el = driver.find_element_by_class_name('download-mp3')
print(el.text)

el.click()
print('Downloading...')

time.sleep(30)

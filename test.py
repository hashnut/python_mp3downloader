import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

# driver 를 설정합니다.
driver = webdriver.Chrome()

# api 가 처음 접근하는 url 을 설정합니다.
# 네이버 로그인 페이지로 접근합니다. 자세한 url은, 크롬 `command + option + i` 키를 누르면 개발자 모드로 변경되어서, 사용하고 싶은 부분의 HTML을 긁어올수 있습니다.
driver.get('https://nid.naver.com/nidlogin.login')

# url 접근후 3초간 기다려줍니다. 이유는 명령어에 접근하는 시간이랑, 실제로 코드가 적용되는 시간이 차이가 있어서, 컴퓨터가 더 빠르면(?) 다음 명령어가 씹히는 경우도 있습니다.
# driver.implicitly_wait(3)

# 'naver_id' 에 naverID 를, 'password' 에 비밀번호를 입력하면, 자동으로 robot이 입력을 해준다. 

driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('password')

# 로그인 버튼을 클릭 해줍니다.

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

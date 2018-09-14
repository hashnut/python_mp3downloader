### python_mp3downloader

### 파이썬 webdriver module, Firefox를 이용하여 커맨드 라인에서 간편하게 유투브 음악을 mp3 형태로 다운받습니다.

---

### Prerequsite :

- Python3 (Latest version is recommemded)

- 3rd party modules (pyperclip, selenium)

- Add path of mp3.py in System variables (add github repository directory to your System variable! [Reference here](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/))

---

### How it works? 

해당 소스코드는 2개의 실행 버전이 있습니다. (앞의 버전을 추천)

<br/> 

### '실행(Win+R)' 키를 눌러서 바로 다운받기

원하는 검색어나 유투브 링크를 복사하고 '실행(Win+R)' 창에 'mp3와 검색어나 링크'를 누르고 엔터를 치면 됩니다. 

(예시 1: 'mp3 https://www.youtube.com/watch?v=aMcjxSThD54&t=1097s')
(예시 2: 'mp3 i want this song')

여러 파일을 다운 받고 싶을 때는 콤마(,)나 슬래시(/)를 통해 구분하면 됩니다.
(예시 3: 'mp3 some love song, some love song2 / some love song3')

파일 다운로드당 최대 20초의 시간이 할당되어 순차적으로 다운로드가 진행됩니다.

크롬 브라우저가 열리며 자동으로 다운로드가 시작하고, 후에 다운이 끝나면 10초 정도 후에 크롬이 자동 종료 됩니다.

(가끔 에러가 뜰 때는 조금 느리지만 에러가 없는 버전을 사용해 보세요. mp3 대신 mp3slow를 치면 됩니다!)

<br/>

### 커맨드 창으로 다운받기

'실행(Win+R)'창에 mp3window를 누르면 cmd 창에서 음악 파일을 다운 받을 수 있는 창이 나옵니다.

![1](https://user-images.githubusercontent.com/26838115/45490587-79273e00-b7a2-11e8-840d-b6271812c5a4.png)

위의 커맨드 라인에서 원하는 음악에 해당하는 검색어를 입력하면 다운로드가 진행되고, 다운로드가 끝나면 다시 원하는 검색어를 입력합니다.

'quit'를 누르면 프로그램을 종료합니다.

커맨드 창은 소요시간이 더 크므로, '실행(Win+R)'키로 바로 다운받는 것을 추천합니다.

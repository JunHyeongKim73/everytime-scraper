import emoji
import telegram
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

ID = 'YOURID'
PW = 'YOURPW'

keyword_list = ['실험', '피험자', '연구', '사례', '참가']
title_list = []
f = open('titles.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    line = line.strip()
    if not line: break
    title_list.append(emoji.demojize(line))
f.close()

webdriver_options = webdriver.ChromeOptions()
webdriver_options.add_argument('--headless') #내부 창을 띄울 수 없으므로 설정
webdriver_options.add_argument('--no-sandbox')
webdriver_options.add_argument('--disable-dev-shm-usage')
webdriver_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')

driver = webdriver.Chrome('chromedriver', options=webdriver_options)
driver.implicitly_wait(1)

# 로그인 페이지에서 로그인하기
url = 'https://everytime.kr/login'
driver.get(url)

driver.find_element(By.NAME, 'userid').send_keys(ID)
driver.find_element(By.NAME, 'password').send_keys(PW)
driver.find_element(By.XPATH, '//*[@id="container"]/form/p[3]/input').click()
driver.implicitly_wait(5)

# 새 글이 올라왔는지 확인하기
isUpdated = False
for i in range(1, 5):
    title = driver.find_element(By.XPATH, f'//*[@id="container"]/div[4]/div[24]/div/a[{i}]/p')
    title = title.text
    title = emoji.demojize(title)
    
    hasKeyWord = False
    for keyword in keyword_list:
        if keyword in title:
            hasKeyWord = True
            break
    
    if hasKeyWord and title not in title_list:
        for j in range(4, 0, -1):
            title_list[j] = title_list[j-1]
        title_list[0] = title   

        isUpdated = True

driver.quit()

# 새 글이 올라왔다면 텔레그램 메세지 보내기
if isUpdated:
    f = open('titles.txt', 'w', encoding='utf-8')
    for title in title_list:
        f.write(emoji.emojize(title)+'\n')
    f.close()

    TOKEN = 'YOURTOKEN'
    USER_ID = 'USERID'
    
    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id=USER_ID, text='새 글이 올라왔습니다!')
    
    now = datetime.now()
    print(f'{now.day}일 {now.hour}시 {now.minute}분')
    print('message send complete!')
    print()
else:
    now = datetime.now()
    print(f'{now.day}일 {now.hour}시 {now.minute}분')
    print('message did not send!')
    print()

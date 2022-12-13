# everytime_scraper
에브리타임 홍보게시판에 특정 단어를 포함한 제목의 글이 새로 올라오면</br> 텔레그램을 통해 메세지를 보내주는 웹 스크래핑 봇입니다. </br>

1시간마다 스크래핑을 진행하며 새로운 글이 올라오지 않았으면 메세지를 보내지 않습니다. </br>

Selenium의 chrome driver를 이용하여 구현하였습니다. </br>

Linux에서 chromeless로 작동하며, background에서 실행되도록 하려면 아래 코드를 입력하면 됩니다. </br>

## Run
```
git clone https://github.com/JunHyeongKim73/everytime_scraper.git
cd gcp
sh execute.sh &
```

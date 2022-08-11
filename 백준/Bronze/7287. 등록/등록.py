print("33")
print("sonjungwoo9")

#외부모듈을 사용한 정답은 아래입니다.-

import requests
import bs4

myId = "sonjungwoo9"

URL = "https://www.acmicpc.net/user/"+ myId

response = requests.get(URL)

soup = bs4.BeautifulSoup(response.text,"html.parser")


print(soup.find('div').find('span',{'id':'u-solved'}).text)
print(myId)

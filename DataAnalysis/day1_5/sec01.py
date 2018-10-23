count = '23,456'
#print(int(count))
#ValueError: invalid literal for int() with base 10: '23,456' => "," 때문에 숫자로 인식 못해서 생기는 에러

import re
from bs4 import BeautifulSoup
html = """
<ul>
    <li>   <a href="www.naver.com">naver</a></li>
    <li>   <a href="https://www.naver.com">naver</a></li>
    <li>   <a href="https://www.daum.com">daum</a></li>
    <li>   <a href="http://www.naver.com">naver</a></li>
</ul>
"""
# #정규식으로 href속성이 https인 것만 추출
# #https: 오고가는 문서를 엿보지 못하게 암호화해서 보내는 통신(비교적 안전하다.)
# soup = BeautifulSoup(html, "html.parser")
# li=soup.find_all(href=re.compile("^https://"))
# #print(li)
# for e in li :
#     print(e.attrs['href'])
# #urljoin  :  상대 주소를 표시
# #상대 경로로 웹 주소를 지정하는 방법
# #절대 경로 :  주소를 모두 표시
# #상대 경로 : 기준(필요하다) 으로 위치 표시
# #../ 로 경로 이동
# from  urllib.parse import urljoin
# base="http://example.com/html/a.html"
# print(urljoin(base,"b.html"))
# #"http://example.com/html/sub/c.html"
# print(urljoin(base,"sub/c.html"))
# #"http://example.com/index.html"
# print(urljoin(base,"../index.html"))
# #"http://example.com/img/sky.png"
# print(urljoin(base,"../img/sky.png"))
#
# print(urljoin(base,"http://other.com/test"))
# #http://를 사용하기 때문에 urljoin을 무시하고 그대로 사용하게 된다.
# #//를 사용하기 때문에 urljoin을 무시하고 그대로 사용하게 된다.
# print(urljoin(base,"//other.com/test"))
#

"""
1.http통신 
-http는 통신규약
-클라이언트는 주소를 통해 URL에 접근
http://www.naver.com: naver.com 에 있는 www라는 이름의 컴퓨터(서버)
-서버는 index.html문서(홈페이지 문서)를 클라이언트에게 전송
-클라이언트는 전송된 html문서를 해석하는 프로그램(웹브라우저)이 해석을 하여 결과를 화면에 출력
-서버와 클라이언트 간 통신 과정에서 서버가 클라이언트에게 응답코드를 html문서와 함께 전송
-대표적인 응답코드 : 200(정상), 4xx(페이지 주소 잘못, 없거나..),5xx(서버 내부 오류)
-쿠키,세션 정보 생성
-쿠기의 예 :id입력 란에 자동완성 기능 체크 설정 정보 등등(클라이언트 pc에 저장되어짐)
-세션 : 쿠키 정보를 서버에 저장

-실습주소
메인페이지 :http://www.hanbit.co.kr/index.html
로그인 페이지 주소 : http://www.hanbit.co.kr/member/login.html
마이 페이지 주소 : http://www.hanbit.co.kr/myhanbit/myhanbit.html
로그인 박스 정보 :  아이디 m-id 비밀번호 m-passwd
1)아이디와 /비밀번호 입력(화면 출력,login.html)
2)로그인 단추(화면 출력)
3)로그인 처리 (화면 출력 안됨, id/pw <->db서버 조회, login_proc.php)
4)로그인 된 상태(화면 출력)
"""
#파이썬으로 사이트 로그인 -> 개인정보 추출 -> 화면출력
#info = {"id":"test","pw":"1234"}
import requests

USER = "python96"
PASS = "gg244055"

session = requests.session()        #세션 객체 생성(송화기-통신선-수화기)
#세션 : 서버와 클라이언트가 연결됨
#세션 유지 : 연결 상태를 유지
#클라이언트에서 서버에 데이터를 데이터를 연결하기 위한 목저긍로 연결할때는 SESSION을 사용.


login_info = {
    "m_id":USER,
    "m_passwd":PASS
}
url_login="http://www.hanbit.co.kr/member/login_proc.php"
#실제 로그인 페이지 : 접근이 되지 않는 페이지(ID와PW가 같이 들어 와야 로그인됨)
#세션 연결 시도
res = session.post(url_login, data = login_info)
print(res)

url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
print(res)
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
mileage = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span").string
print("마일리지 :" +mileage+"점")

soup = BeautifulSoup(res.text, 'html.parser')
ecoin = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span").string
print("이코인 :" +ecoin+"원")

























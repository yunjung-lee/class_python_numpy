"""
api :  프로그램을 만들어서 사용하기 쉽게해주는 인터페이스
openapi : 서버에 연결하여 데이터를 주고 받는 형식


"""
#기상청
#http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
"""
구름조금
-------
-서울
-화성
-부산


구름 많음
-------
-제주도
-대구

{'구름 조금':['서울'], '구름 조금':['화성']} => {'구름 조금':['서울','화성']}  :으로 표현
"""

from bs4 import BeautifulSoup
import urllib.request as req
import os.path
#os : os=> 시스템의 운영체제,path =>움직임에 도움

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"       #forecast.xml의 문자열을 savename에 어싸인함
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print("서버로부터 날씨 정보 XML문서를 가져왔습니다.")
# forecast.xml 이 만들어져 있는지를 판별

xml = open(savename,mode="r", encoding="utf-8").read()
#print(xml)
soup = BeautifulSoup(xml,"html.parser")
#print(soup)

#{'구름 많음':['서울','파주','춘천'...],'비':['인천','원주'],'눈':['수원']}}
info = {}       # {'구름 조금':'서울', '구름 많음':'인천', '구름 조금':'부산'}
for location in soup.find_all('location'):
    name = location.find('city').string
    weather = location.find('wf').string
    if not(weather in info):
        info[weather]=[]        #info={'구름 조금':[],}      #info={'구름 조금':[서울],"구름많음':[]}     #info={'구름 조금':[서울],"구름많음':[인천]}
    info[weather].append(name)  #info={'구름 조금':[서울]}        #info={'구름 조금':[서울],"구름많음':[인천]}        #info={'구름 조금':[서울,부산],"구름많음':[인천]}
"""

"""

    # info[weather].append(name)
    # print(info)




#info = {'구름 조금':'서울', '구름 많음':'인천', '구름 조금':'부산'}
for locw in info :
    #print(locw,info[locw])
    print("+",locw)
    for name in info[locw]:
        print("|-",name)


























































































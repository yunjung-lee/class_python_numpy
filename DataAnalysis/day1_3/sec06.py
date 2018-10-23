#웹의 컨텐츠를 가져오기 위한 라이브러리

import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup


api = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?"
values = {
        'stnId':      '108'                                                      #['108','105']
}
params = urllib.parse.urlencode(values)                #딕셔너리 함수를 url 형식으로 코딩해주는 함수
# print(params)
url = api+"?"+params                    # url +? + fild명 +주소  : ? 는 url과 주소를 구분
# print("url = ",url)

data = req.urlopen(url).read().decode("utf-8")
# print(data)

soup = BeautifulSoup(data,'html.parser')
#BeautifulSoup의 객체를 만들어라 : 만들 객체에 대해 대상을 넣어주어야 한다 ( html.parser: 상수처럼 사용된다.).
# print(soup)

wf = soup.find("tmn").string
print(wf)



# url="http://www.weather.go.kr"
# mem=req.urlopen(url).read()
# txt=mem.decode("utf-8")
# print(txt)

# url ="https://www.kccistc.net:8443/images/main/img_visual_09000_3.jpg"
# savename = "test2.png"
# mem = req.urlopen(url).read()
# print(type(mem))
#
# with open(savename,mode="wb") as f:
#     f.write(mem)
#     print("저장되었습니다.")
#     #f=open(savename,mode="wb"), f.close()와 같은 의미
#
# # req.urlretrieve(url,"test.png")
# # print("이미지가 저장되었습니다.")
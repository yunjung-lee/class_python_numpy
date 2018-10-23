#html 안에 태그 명이 지정 되어있는 문서의 parsing

from bs4 import BeautifulSoup
import urllib.request as req          #특정 웹사이트로 접근하는 모듈

html = """
<html><body>
<div id = "test">
<h1>빅데이터 분석</h1>
<ul class="1ec">
<li>파이썬</li>
<li>머신러닝</li>
<li>통계분석</li>
</ul>
</div>
</body></html>
"""

#div#test :  # 을 중심으로 div라는 요소와 test라는 id을 표시
#ul.1ec     : .  을 중심으로 ul라는 요소와 1ec 라는 class표시
# > 하위 요소 표시
#test > h1
#test > ul > li:nth-child(1)  python          nth: n번째 , nth-child: 표시된 숫자번째의 자식
#test > ul > li:nth-child(2)    ML
#test > ul > li:nth-child(3)    SA


soup = BeautifulSoup(html, "html.parser")
print(soup)
# <html><body>
# <div id="test">
# <h1>빅데이터 분석</h1>
# <ul class="1ec">
# <li>파이썬</li>
# <li>머신러닝</li>
# <li>통계분석</li>
# </ul>
# </div>
# </body></html>

# res = soup.select_one("#test > h1")
# print(res)
# #<h1>빅데이터 분석</h1>
# res = soup.select_one("#test > h1").string
# print(res)
# #빅데이터 분석
# res = soup.select_one("h1").string
# print(res)
# #빅데이터 분석
# res = soup.select_one("div#test > h1").string
# print(res)
# #빅데이터 분석
# res = soup.select_one("body> div#test > h1").string
# print(res)
# #빅데이터 분석

res = soup.select_one("div#test > ul.1ec > li")
print(res)
#<li>파이썬</li>

res = soup.select_one("div#test > ul.1ec > li").string
print(res)
#파이썬

res = soup.li
print(res)
#<li>파이썬</li>


res = soup.li.string
print(res)
#파이썬


res = soup.li
res2=res.next_sibling.next_sibling
res3=res2.next_sibling.next_sibling
print(res.string)
print(res2.string)
print(res3.string)
# 파이썬
# 머신러닝
# 통계분석
myList = soup.select("div#test > ul.1ec > li")
myList = soup.select("div > ul > li")           # 같은 결과 :  동일한 이름의 요소가 하나뿐이기 때문일뿐임
for li in myList :
    print(li.string)
    # 파이썬
    # 머신러닝
    # 통계분석

#find에서 id로도 요소추출이 가능하다. :  구별자가 분명하면 구별자만으로도 추출이 가능하다.
test = soup.find(id="test")
print(test)






























































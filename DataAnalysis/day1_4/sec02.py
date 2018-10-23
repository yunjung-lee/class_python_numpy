#beautifulsoup : 파일을 가져올 수 있다.

from bs4 import BeautifulSoup
html='''
<html><body>
    <ul>
        <li>
        <a href = "http://www.naver.com"> naver
        </a>
        </li>
        <li>
        <a href = "http://www.daum.com"> daum
        </a>
        </li>
    </ul>
</body></html>
'''
soup = BeautifulSoup(html,'html.parser')
#html에서 대상을 검색하기 때문에 첫인자로 html ,
# print(soup)

link = soup.find("a")
#"a"가 들어가는 라인을 찾게 됨 : 1줄만
print(link)
# <a href="http://www.naver.com"> naver
#         </a>


link = soup.find_all("a")
#"a"가 들어가는 모든 라인을 찾게 됨  : 리스트
print(link)
#[<a href="http://www.naver.com"> naver</a>, <a href="http://www.daum.com"> daum</a>]

for i in link :
    print(i)
    # <a href="http://www.naver.com"> naver
    #         </a>
    # <a href="http://www.daum.com"> daum
    #         </a>

#link 에서 href의 내용만 추출하고 싶을때 :attrs를 사용 ->myhref = i.attrs['href']
#link 에서 text의 내용만 추출하고 싶을때 :string를 사용 ->str = i.string
for i  in link :
    myhref = i.attrs['href']
    print(myhref)
    # http://www.naver.com
    # http://www.daum.com
    str = i.string
    print(str)
    # naver
    # daum

html = """
<html><body>
<h1>빅데이터 분석</h1>
<p>데이터 수집</p>
<p>데이터 전처리</p>
<p>데이터 마이닝</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
#h1 = soup.find("h1")                 #이러한 사용을 간단하게 아래처럼 사용할 수 있다.
#h1 = soup.h1
#h1 = soup.body.h1           #soup안의 body를 찾고 그 아래 h1태그를 참조해라
h1 = soup.html.body.h1
print(h1)
p1 = soup.html.body.p
#첫번째 p만 추출됨
print(p1.string)
# 데이터 수집


#p2=p1.next_sibling   : sibling:형제 바로 옆에 문자를 찾는다.(이경우 엔터)
p2=p1.next_sibling.next_sibling
print(p2.string)
#데이터 전처리

p3=p2.next_sibling.next_sibling
print(p3.string)
#데이터 마이닝















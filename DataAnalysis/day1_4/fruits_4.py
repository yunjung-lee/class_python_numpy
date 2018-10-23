from bs4 import BeautifulSoup
fp = open("fruits.html", mode="r",encoding="utf-8")          #utf-8 :  세계적인 방식,EUC-KR : 한글 코딩방식
soup = BeautifulSoup(fp,"html.parser")
#print(soup)

# print(soup.select_one("li").string)
# #사과
# print(soup.select_one("li:nth-of-type(2)").string)
# #포도
# #print(soup.select_one("li:nth-of-type(10)").string)
# #AttributeError: 'NoneType' object has no attribute 'string' : 9개 까지이기 때문에 에러
#
# li_List = soup.select("li")
# print(len(li_List))
# for i in li_List:
#     print(i.string)
#
# pos1="li:nth-of-type("
# pos2 = ")"
# for i in range (9):
#     pos = pos1+str(i+1)+pos2        #li:nth-of-type(1)
#     print(soup.select_one(pos).string)
#     #print(soup.select_one(li:nth-of-type(i)).string)


# myList = soup.select("#ve-list > li")       #리스트
# print(len(myList))
# for i in range ( len(myList)):
#     print(soup.select("#ve-list > li")[i].string)

print(soup.select_one("#ve-list > li:nth-of-type(3)").string)
print(type(soup.select_one("#ve-list > li:nth-of-type(3)")))
# <class 'bs4.element.Tag'>  :리스트 구성 요소
print(type(soup.select("#ve-list > li:nth-of-type(3)")))
#  <class 'list'>
#select 함수는 리턴 결과가 리스트이므로, string함수를 사용할 수 없기 때문에
#soup.select("#ve-list > li:nth-of-type(3)")[0]같이 인덱스를 주어 접근한 뒤 string 함수 사용
#print(soup.select("#ve-list > li:nth-of-type(3)").string) :리스트라서 .ㄹ을 사용할 수 없다
print(soup.select("#ve-list > li:nth-of-type(3)"))
#  [<li class="black" data-lo="ko">가지</li>]
print(soup.select("#ve-list > li:nth-of-type(3)")[0].string)


#ve-list에서 data-lo의 결과가 us 인것만 추출
print(soup.select("#ve-list > li[data-lo='us']")[1])
#Traceback (most recent call last):
#   File "D:/Python Study/DataAnalysis/day1_4/fruits_4.py", line 45, in <module>            #에러발생 라인표시
#     print(soup.select("#ve-list > li[data-lo='us']")[2])
# IndexError: list index out of range : 2개뿐인 리스트에 3번째 결과를 요청하여 나온 에러


#class :  만들어져 있는 규칙이 있는 속성을 갖는 요소
#data-lo : 사용자가 임의로 편의를 위해 만든 요소
print(soup.select("#ve-list > li[class='black']"))
print(soup.select("#ve-list > li.black"))           #class이기 때문에 . 으로 처리할 수 있다.


#딕셔너리에 리스트를 저장
cond = {"data-lo":"us","class":"black"}
print(soup.find("li",cond))
#<li class="black" data-lo="us">아보카도</li>
print(soup.find("li",cond).string)
#아보카도
print(soup.find(id="ve-list").find("li",cond))
#<li class="black" data-lo="us">아보카도</li>
print(soup.find(id="ve-list").find("li",cond).string)
#아보카도


































































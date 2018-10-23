from bs4 import BeautifulSoup
import urllib.request as req

fp = open("color.html",encoding='utf-8')
soup = BeautifulSoup(fp,"html.parser")

# #print(soup)
# print(soup.select_one("#gr"))
# # <li id="gr">Gray</li>
# print(soup.select_one("#gr").string)
# # Gray
#
# #빈번한 사용으로 함수를 만들어 함수화
# #lambda 사용
# sel = lambda q:print(soup.select_one(q).string)
# #def sel(q): 와 같은 형식
#
# sel("#gr")
# # Gray
# sel("li#gr")
# # Gray
# sel("ul > li#gr")
# # Gray
# sel("#mycolor #gr")
# # Gray
# sel("#mycolor > #gr")
# # Gray
# sel("ul#mycolor > li#gr")
# # Gray
# sel("li[id='gr']")
# # Gray
# sel("li:nth-of-type(4)")
# # Gray
#
# print(soup.select("li")[3].string)
# # Gray
# print(soup.find_all("li")[3].string)
# # Gray

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url).read()
#print(res)
soup = BeautifulSoup(res,"html.parser")
# print(soup)

#mw-content-text > div > ul:nth-child(6) > li > ul > li > a =>:nth-child(6)오류가 많이 나서 지우기
#mw-content-text > div > ul > li > ul > li > a
alist = soup.select("#mw-content-text > div > ul > li > ul > li > a")
for a in alist :
    print(a.string)

myurl = "https://news.sbs.co.kr/news/endPage.do?news_id=N1004883776&plink=TOPHEAD&cooper=SBSNEWSMAIN"
res9=req.urlopen(myurl).read().decode("utf-8")
#읽어온 페이지 decode
soup9 = BeautifulSoup(res9,'html.parser')
#html문서로 파서해서 만들어줌
article = soup9.select("#container > div.w_inner > div.w_article > div.w_article_cont > div.w_article_left > div.article_cont_area > div.main_text > div")
#print(article)
#article =  list( string이 아니여서 string으로 만들어 줘야함)

import re
pat = re.compile("[^가-힣]+")
result = pat.sub(" ",res9)
# print(result)


nurl ="https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10405&docId=307066785&qb=67mF642w7J207YSw&enc=utf8&section=kin&rank=3&search_sort=0&spq=1"
nres=req.urlopen(nurl).read().decode("utf-8")
soupN = BeautifulSoup(nres,'html.parser')
nlist = soupN.select("#contents_layer_0 > div.end_content._endContents > div")
nlist = str(nlist[0])
pat = re.compile("[^가-힣ㅏ-ㅣ]")

print(pat.sub("",nlist))







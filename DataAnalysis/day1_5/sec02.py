import re
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse

# search_addr = "http://book.daum.net/search/bookSearch.do?query="
# search_word = "파이썬"
# search_word_enc=urllib.parse.quote(search_word)
# #urllib.parse.quote :  한글을 유니코드로 인코딩 하는 함수
# url = search_addr+search_word_enc
# request = req.Request(url)
# print(request)
#
# responce = req.urlopen(url)
# print(responce)
#
# html_data = responce.read()
# #print(html_data)
# data = BeautifulSoup(html_data,'html.parser')
# #파이썬 책을 검색했을때 나온 출력물들의 html
# print(data)

#파이썬, 자바, 자바스크립트 : 한장으로 출력

# search_addr = "http://book.daum.net/search/bookSearch.do?query="
# word = ["파이썬", "자바","자바스크립트"]
# url = search_addr
#
# for w in word :
#     search_word_enc=urllib.parse.quote(w)
#     url = url+search_word_enc
# html_data = req.urlopen(url).read()
# data = BeautifulSoup(html_data,'html.parser')
# res = data.select("#page_body > form > ul > li > dl > dd.price > div > span.prc > strong")
# print(res)





# search_addr = "http://book.daum.net/search/bookSearch.do?query="
# search_word = "파이썬"
# search_word2 = "자바"
# search_word3 = "자바스크립트"
#
# search_word_enc=urllib.parse.quote(search_word)
# search_word_enc2=urllib.parse.quote(search_word2)
# search_word_enc3=urllib.parse.quote(search_word3)
# #urllib.parse.quote :  한글을 유니코드로 인코딩 하는 함수
# url = search_addr+search_word_enc+search_word_enc2+search_word_enc3
# #print(search_word_enc)
#
# request = req.Request(url)
# print(request)
#
# responce = req.urlopen(url)
# print(responce)
#
# html_data = responce.read()
# #print(html_data)
# data = BeautifulSoup(html_data,'html.parser')
# #파이썬 책을 검색했을때 나온 출력물들의 html
# print(data)


# search_addr = "http://book.daum.net/search/bookSearch.do?query="
# word = ["파이썬", "자바","자바스크립트"]
# url = search_addr
#
# for w in word :
#     search_word_enc=urllib.parse.quote(w)
#     url = search_addr + search_word_enc
#     html_data = req.urlopen(url).read()
#     data = BeautifulSoup(html_data,'html.parser')
#     res = data.select("#page_body > form > ul > li > dl > dd.price > div > span.prc > strong")
#     for r in res :
#         print(r.string)
#     print("==="*50)


search_addr = "http://book.daum.net/search/bookSearch.do?query="
word = ["파이썬", "자바","자바스크립트"]
url = search_addr

for w in word :
    search_word_enc=urllib.parse.quote(w)
    url = search_addr + search_word_enc
    html_data = req.urlopen(url).read()

    data = BeautifulSoup(html_data,'html.parser')
#  '#page_body > form:nth-child(6) > ul > li:nth-child(1) > dl > dt > a'=>':'nth-child(6)=> 나오기 힘들기 때문에 지우고 for문
    res = data.select("#page_body > form > ul > li > dl > dt > a")
    for r in res :
        print(r.string)
    print("==="*50)














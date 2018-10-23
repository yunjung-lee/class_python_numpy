from bs4 import BeautifulSoup
import urllib.request as req          #특정 웹사이트로 접근하는 모듈


url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url).read()
#req.urlopen(url) : url을 열기
#req.urlopen(url).read()  : req.urlopen(url)을 읽어 드림
soup = BeautifulSoup(res,"html.parser")
#print(soup)
#exchangeList > li.on > a.head.usd > div > span.value
p=soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string
print(p)
print("usd/krw = ",p)


"""
#exchangeList > li.on > a.head.usd > div > span.value
의미 파악이 필요하다
"""





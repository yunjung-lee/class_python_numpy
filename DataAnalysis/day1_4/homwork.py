# 1. 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다. 다음 소스 코드를 완성하여 10자 이하인 단어의 개수가 출력되게 만드세요.
# words.txt 내용
#
# anonymously
# compatibility
# dashboard
# experience
# photography
# spotlight
# warehouse

f = open("words.txt","w")
data = """anonymously
compatibility
dashboard
experience
photography
spotlight
warehouse
"""

f.write(data)

f.close()
a=0
f=open("words.txt","r")
txt = f.readlines()
for t in txt :
    if len(t)<=11:
      a=a+1
print(a)


# 2. 표준 입력으로 정수와 문자열이 각 줄에 입력됩니다.
# 다음 소스 코드를 완성하여 입력된 숫자에 해당하는 단어 단위 N-gram을 출력하세요.
# 만약 입력된 문자열의 단어 개수가 입력된 정수 미만이라면 'wrong'을 출력하세요.
#
# 실행 결과
# 7 (입력)
# Python is a programming language that lets you work quickly (입력)
# Python is a programming language that lets
# is a programming language that lets you
# a programming language that lets you work
# programming language that lets you work quickly
a=[]
p=int(input("원하는 숫자를 입력하세요"))
t =input("원하는 문장을 입력하세요")
s = t.split(" ")
if len(s)< p:
    print('wrong')
else:
    for i in range(len(s) - (p - 1)):
        print (" ".join(s[i:(p+i)]))





from bs4 import BeautifulSoup
import urllib.request as req
import re

nurl ="https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10405&docId=307066785&qb=67mF642w7J207YSw&enc=utf8&section=kin&rank=3&search_sort=0&spq=1"
nres=req.urlopen(nurl).read().decode("utf-8")
soupN = BeautifulSoup(nres,'html.parser')
nlist = soupN.select("#contents_layer_0 > div.end_content._endContents > div")
nlist = str(nlist[0])
pat = re.compile("[^가-힣ㅏ-ㅣ]+")

print(pat.sub(" ",nlist))
"""
정규식
Beautifulsoup
아나콘다 : www.anaconda.com
인터프린터 : 작성코드 실행을 위해 코드르 기계어로 바꿔줌
모듈= class =>함수들의 모음

인터프린터들의 모음 : (setting) 개발 환경
개발환경의 여러가지 경우의 수를 모두 확인할 수 없어서 가상환경을 설정 =>아나콘다.
"""
from  konlpy.tag import Twitter
import codecs
from  bs4 import BeautifulSoup

##############토지 파일 형태소 분석 작업 코드 ##############################

fp=codecs.open("TOJI1.txt","r",encoding="ms949")
# encoding 방식은 utf-16,utf-8, ms949, euc-kr중 선택
# print(fp)
soup = BeautifulSoup(fp,"html.parser")
# print(soup)
text = soup.getText()
#print(text)

twitter = Twitter()
lines = text.split("\r\n")
word_dic = {}
for line in lines :
    malist = twitter.pos(line)
    for word in malist :
       # print(word[1])
        n = 0
        if word[1] == 'Noun' : #'명사라면'
            if not word[0] in word_dic:
                word_dic[word[0]]=0
            word_dic[word[0]]+=1
# print(word_dic)
#print(len(lines))
#한꺼번에 출력
#print(lines)
print("="*100)
keys=sorted(word_dic.items(),key=lambda x:x[1], reverse=True) #key=정렬 기준, reverse = 정렬 순, x에서 x[1]의 크기를 기준삼아
#print(keys)
#상위 50개의 키를 카운트 하라는 의미
for word,count in keys[:50]:
    print("{0},({1})".format(word,count,end = ""))




















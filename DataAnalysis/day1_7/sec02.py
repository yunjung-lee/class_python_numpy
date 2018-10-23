import codecs
from bs4 import BeautifulSoup

fp1 = codecs.open("bmwy.txt","r",encoding="euc-kr")
soup1 = BeautifulSoup(fp1,"html.parser")
text1 = soup1.getText()
a=text1.strip()

# print(b)

fp2 = codecs.open("bmwh.txt","r",encoding="euc-kr")
soup2 = BeautifulSoup(fp2,"html.parser")
text2= soup2.getText()
b=text2.strip()
# print(b)


#두 문자열간 비교를 하는 알고리즘
def ngram(s,num):
    res =[]
    # res 리스트의 길이는 얼마나 나올까요?
    slen = len(s) -num+1 # slen : 리스트 요소의 갯수
    for i in range(slen):
        ss=s[i:num+i]
        res.append(ss)
 #   print(res)
    return res
# N=2일때, 리턴 : ['오늘', '늘 ',' 상', '상공', '공회', '회의',.... ,'웠다']


#두 문자열간 유사도를 조사
def diff_ngram(sa,sb,num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    cnt =0
    r=[]
    for i in a:
        for j in b:
            if i==j:
                cnt+=1
                r.append(i)
    return cnt / len(a),r


#2-gram
res,word = diff_ngram(a,b,3)
print("2-gram",res)
from bs4 import BeautifulSoup
import urllib.request as req
import re
from konlpy.tag import Twitter
from collections import Counter

FS="text.txt"
FS2="text1.txt"
urlNews = "https://news.naver.com/main/read.nhn?oid=421&sid1=100&aid=0003537822&mid=shm&mode=LSD&nh=20180816152756"

def get_text(URL):
    RU=req.urlopen(URL).read()
    #print(RU)
    soup = BeautifulSoup(RU,"lxml",from_encoding="utf-8")
    #lxml :  안됨
#    print(soup)
    text = ""
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    #print(text)
    return text
# #articleBodyContents

def clean_file(myText):
    clean_file=re.sub('[a-zA-Z]',' ',myText)
    clean_file = re.sub('[\{\}\[\]\(\)\\\▶\,=\/@\'\"©\.!_·]'," ",clean_file)

    return clean_file



def main():
    OF1 = open(FS, "w", encoding='utf-8')
    #print(OF1)
    res = get_text(urlNews)
    OF1.write(res)
    OF1.close()
    OF1 = open(FS, "r", encoding='utf-8')
    text = OF1.read()
    OF2= open(FS2,"w", encoding='utf-8')
    clean_text = clean_file(text)
    OF2.write(clean_text)
    print(clean_text)
    OF1.close()
    OF2.close()



if __name__ == '__main__':
    main()



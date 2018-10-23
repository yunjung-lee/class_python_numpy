import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

# #UTF-16으로 인코딩 되어있음 : 파일을 열고 출력
# fp = codecs.open('BEXX0003.txt','r',encoding='utf=16')
# soup = BeautifulSoup(fp,'html.parser')
# #print(soup)
# body = soup.select_one('body > text')
# #print(body)
# text = body.getText()  #순수하게 텍스트만 추출,태그들은 모두 제거
# # print(text)
# results = []
# twitter = Twitter()
# lines = text.split('\r\n')
# #print(lines)
# for line in lines: #라인별로 형태소 분석
#     malist = twitter.pos(line, norm=True,stem=True)
#     res = []
#     for word in malist :
#        if not word[1] in ['Josa','Eomi','Punctuation','Foreign']:
#             res.append(word[0])  #분석 결과가 'Josa','Eomi','Punctuation','Foreign'가 아닌 단어 추출
#             #print(word)
#     r1= (' '.join(res))
#     results.append(r1)
#  #   print(r1)
#
# ###############################워드 추출############################################################
# #######################지금부터는 워드 -> 벡터화 ####################################################
# ###########################워드 임베딩##################################################################
#
toji_file =  'toji.data'
# with open(toji_file, "w", encoding='utf-8')as fp:
#     fp.write("\n".join(results))
#
# # 아래 문장에서 toji_file의 모든 내용을 읽어서 data저장
# #word2vec를 만들기 위해서 LineSentence를 이용하여 텍스트를 읽어드릴 수 있음
data = word2vec.LineSentence(toji_file)
# #print(data)
model = word2vec.Word2Vec(data,size=200, window=10, min_count=5,iter=10,sg=1)
# #size : 벡터의 차원
# # window= 앞뒤로 참조하는 단어 갯수(많을 수록 계산결과가 명확해진다.):속도등의 영향 때문에 무한정 늘릴 수 없다
# # min_count : 최소한 min=30, 30이상 등장한 단어들에 대해서만 임베딩 해라
# #sg :  CBOW(sg=0), Skop-Gram(sg=1) 중 택일
# #단어 앞 뒤의 참조되는 갯수 만큼의 단어들을 벡터 공간에 위치시켜 계산
# #iter : 반복
# model.save('toji.model')
# print('모델이 만들어 졌습니다.')

# 모델 불러오기
model1 = word2vec.Word2Vec.load('toji.model')
print(model.most_similar(positive=['땅','집']))









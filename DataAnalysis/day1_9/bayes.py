"""
1) 텍스트 -> 학습 -> 모델
2) 모델 -> 새로운 텍스트 입력 -> 분류 결과
"""
import math, sys
from konlpy.tag import Twitter
class BayesianFilter:
    def __init__(self):     #:java의 this=python의 self ,__init__:오타 주의
     #   print("생성자 함수")        self. : init에 붙어있는 함수=> 이름을 모두 써줘야한다.(self. 포함)
        self.words =set()       #중복된 데이터가 있더라도 하나만 있게된다.
        self.word_dict={}       #단어추가
        self.category_dict={}

     #전달 받은 text에 대한 형태소 분석
    def split(self,text):
        twitter = Twitter()
        mailList = twitter.pos(text,norm=True, stem=True)
        #print(mailList)
        results =[]
        for word in mailList:
            if not word[1] in ['Josa','Eomi','Punctuation']:
                results.append(word[0])
        #print(results)
        return results
    #inc_word :  단어를 카테고리에 추가
    def inc_word(self,word,category):       #카테고리를 만들고 그 카테고리에 단어를 추가하자
       # print(word,category)       # "파격 세일 - 오늘까지 30% 할인합니다.", "광고"
         if not category in self.word_dict:
             self.word_dict[category]={}        #딕셔너리 안에 딕셔너리가 들어가는 형태
         if not word in self.word_dict[category]:
             self.word_dict[category][word] = 0     #딕셔너리의 중첩 표현
         self.word_dict[category][word] += 1
         self.words.add(word)
         # # print("="*50)
         # print(self.word_dict)
         # # print("=" * 50)
         # print(self.words)

    def category_prob(self,category):
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]        #5개 : 광고 카테고리에 속하는 광고
        return category_v / sum_categories
    #'광고' => 5/10이 리턴, '중요' => 5/10이 리턴.


    def score(self,words,category):
    #words :['재고', '정리', '할인', '무료', '배송']
    #category : '광고'
        #print("score function : ", category)
        score = math.log(self.category_prob(category))
        print("스코어:",score)
        for word in words:
            score +=math.log(self.word_prob(word,category))
        return score

#카테도리 내부의 단어 출현 비율 계산
    def word_prob(self,word,category):
        n=self.get_word_count(word,category)+1        #카테고리 내부의 출현 빈도수
        d=sum(self.word_dict[category].values())+len(self.words)        #해당카테고리 단어수+전체 단어수
        #print(n/d)     #len(dict) : dictionary의 키의 갯수를 출력
        return n/d
        #d : 광고 카테고리에 속하는 단어들의 등장 횟수의 총합+분류 대상 문장을 구성하는-> 전체 단어의 수
        # print(n)

    def get_word_count(self,word,category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0

    #text='재고 , 정리 할인, 무료 배송'
    def predict(self,text):
        best_category = None
        words =self.split(text)
        score_list = []
        max_score = -sys.maxsize
        #print(words)        #['재고', '정리', '할인', '무료', '배송']
        for category in self.category_dict.keys():
            score = self.score(words,category)
            score_list.append((category,score))
            if score> max_score:
                max_score = score
                best_category=category
        return best_category,score_list



    def fit(self,text,category):
        #텍스트를 읽어 학습\
        word_list = self.split(text)
        for word in word_list :
            #print(word)
            self.inc_word(word,category)
        self.inc_category(category)


    #카테고리 계산 부분
    def inc_category(self,category):
        # print(category)
        if not category in self.category_dict:      #category_dict에 category (광고,중요) 가 없다면
             self.category_dict[category]=0
        self.category_dict[category] +=1
        # print(self.category_dict)





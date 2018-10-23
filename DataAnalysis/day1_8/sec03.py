# 1.오늘의 날씨 스크랩(네이버) : https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=422&aid=0000333483
# 2. 날씨 본문 내용을 텍스트 파일로 저장((output.txt)
# 3.데이터 정제(크리닝) -영어, 특수기호 제거(정규식)
# 4. 정제된 결과를 텍스트 파일로 저장(output_cleaned.txt)
# 5. 정제된 파일을 읽어서 형태소 분석 ->명서 추출 - > 빈도수 확인
# 6. 명사로 구성된 단어별 빈도수를 텍스트 파일로 저장(output_final.txt)
# 7. 상위 10개에 해당하는 단어를 시각화
#
# 8. 협업필터링(기계학습, 추천시스템)
# 9. 긍정/ 부정 감성분석 (word2vec,RNN 기반)
# 10. 마르코프 기반 문장 이해/생성 :  확률 기반 기계학습 ( deep learning 모델 보다 정확도가 떨어짐)

#----------------------------------------------------------------------------------------------

# 4. 정제된 결과를 텍스트 파일로 저장(output_cleaned.txt)
# 5. 정제된 파일을 읽어서 형태소 분석 ->명서 추출 - > 빈도수 확인

from konlpy.tag import Twitter
from collections import Counter


# #collections :모듈, Counter :  class(대문자 시작)
#
# colors = ['r','b','r','g','b','b']
# num = [1,2,3,3,3,4,4,4,4,5]
# cnt = Counter(colors)
# print(cnt)
# #Counter는 리스트 또는 튜플에 저장된 데이터를 딕셔너리 형태로 각각의 데이터가 등장한 횟수를 출력
# n=Counter(num)
# print(n.most_common())
# #most_common() 자동적으로 등장횟수별 자동정렬 출력
# print(n.most_common(3))
# #상위 3번째 까지만 출력

#명사 추출하는 함수
def get_tags(gtext,ntags=30):       #ntags=30 : 디폴트=>지정되지 않았을때 사용되어진다.
    twitter = Twitter()
    nouns = twitter.nouns(gtext)         #nouns() : 명사만 추출
#    print(nouns)
    count = Counter(nouns)
    return_list=[]
    for word, cnt in count.most_common(ntags):
        temp={'tag':word,'count':cnt}
#        print(temp)
        return_list.append(temp)
 #       print(return_list)
    return return_list

def main():
    text_file_name ="output_cleaned.txt"
    noun_count = 30
    output_file_name = "output_final.txt"
    open_text_file = open(text_file_name, "r")
    text = open_text_file.read()
    res=get_tags(text,noun_count)
    open_text_file.close()

    open_output_file = open(output_file_name,'w')
    for data in res :
        noun = data['tag']
        count = data['count']
        open_output_file.write("{} {}\n".format(noun,count))
        # 출력하는 형태 지정 : "{} {}\n".format(noun,count)
        #{} : 딕셔너리가 아니라 단어 1개를 받는 형식

if __name__=='__main__':
    main()














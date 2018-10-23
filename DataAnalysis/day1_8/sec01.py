"""
결과도출과 시각화
결과도출 : 통계
html div() : 구역 지정
html 스타일(많이 사용하는 폼을 지정해 놓는 것) 지정 : text만 입력하면 각각의 스타일이 자동으로 적용
html <!-- txet--> : 주석
"""
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
# 1.오늘의 날씨 스크랩(네이버) : https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=422&aid=0000333483
# 2. 날씨 본문 내용을 텍스트 파일로 저장((output.txt)

from bs4 import BeautifulSoup
import urllib.request as req


OUTPUT_FILE_NAME = 'output.txt'
URL='https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=422&aid=0000333483'

# 크롤링 함수 :
def get_text(AAA) :
    sourceFromURL = req.urlopen(AAA)
    soup= BeautifulSoup(sourceFromURL,'lxml',from_encoding='utf-8')
    print(soup)
    text = ""
    for item in soup.find_all('div',id='articleBodyContents'):
#        print(item.find_all(text=True))         #text=True : text인것들만 출력해라
        text = text+str(item.find_all(text=True))
#     #html.parser과 같은 기능에 더 빠른 lxml

    return text

# #모듈 import시 원하지 않는 모듈의 내용이 모두 실행 => 원하는 내용만 실행 if __name__=='__main__' :  으로 메인만 실행
def main():
    open_output_file = open(OUTPUT_FILE_NAME,"w")
    res = get_text(URL)
    #def get_text(AAA) : 호출
    open_output_file.write(res)
    open_output_file.close()

if __name__ == '__main__':
    main()


# get_text(URL)




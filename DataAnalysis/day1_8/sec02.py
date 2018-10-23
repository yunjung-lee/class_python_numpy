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
#아래 두 작업 수행
#입력  output.txt->데이터 정제(크리닝) ->output_cleande.txt ->출력
# 3.데이터 정제(크리닝) -영어, 특수기호 제거(정규식)
# 4. 정제된 결과를 텍스트 파일로 저장(output_cleaned.txt)

import re

INPUT_FILE_NAME = 'output.txt'
OUTPUT_FILE_NAME = "output_cleaned.txt"


#정제함수
def clean_text(myText):
    cleaned_text = re.sub("[a-zA-Z]",'',myText)
    cleaned_text = re.sub("[\{\}\[\]\(\)\\\\/▶,\'\"_↑㎜:…]", '', cleaned_text)
    #{},[],(),-,#,\ 등 특수문자를 사용할 때는 \기호 먼저 작성
    return cleaned_text


#메인
def main():
    read_file = open(INPUT_FILE_NAME,'r')
    write_file = open(OUTPUT_FILE_NAME,"w")
    text = read_file.read()
    print("before:")
    print(text)
    cleaned_text = clean_text(text)
    #def clean_text(myText): 호출
    print("after:")
    print(cleaned_text)
    write_file.write(cleaned_text)
    read_file.close()
    write_file.close()

if __name__ == "__main__":
    main()
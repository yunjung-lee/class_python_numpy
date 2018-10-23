"""
1.텍스트 분류
    -스팸/햄 메일
    -가장 많이 사용되는 방법 : 베이즈 정리를 이용한 텍스트 분류 방법인 '베이지안 필터'
*베이지안필터 : 카테고리 분류도 해준다.

2. 머신러닝
    -교사, 비교사, 강화학습
    -베이지안 필터는 교사 학습에 해당

3.모델 생성 과정
 스팸/햄 메일 입력 -> 메일 내용 학습 -> 모델
 새로운 메일 입력 ------------------>판단 :  스팸/햄 분류 결과 출력

---------다양한 입력에 대응 할 수 있는 것 : 모델(100% 완벽하지 않다. 확률임)---------------
스펨 분류기 : 통계,경험기반으로 임계치를 정해서 분륳

4. 모델 성능 평가
    -precision, recall, f-measure, support

5. 오류에 엄격해야한다.
    -암이 아닌데 암으로 분류 : False postive
    -암인데 암이 아닌 것으로 분류 : False negative(더 문제가 큼)

6.조건부 확률
    -어떤 A라는 사건이 일어났다는 조건하에서 다른 사건 B가 일어날 확률
    -P(B|A)
    -비가 내릴 확률 : P(비) , 교통사고가 발생할 확률 : P(교통사고)
    -비가 내리는 날에 교통사고가 발생할 확률? P(교통사고|비)
    -P(B|A)  = p(A교B)/P(A) (단, P(A)가 0이 아님) : A상황에서 B가 일어날 확률(동시에 일어날 확률)
    -P(A교B) = p(B|A)*P(A)
    -숫자 (1~20) 카드, A : 2의 배수가 나오는 사건, B : 3의 배수가 나오는 사건
    P(B|A) = P(A교B) /P(A) = (3/20)/(10/20) =3(6의 배수의 상황)/10(2의 배수의 상황) =30%  :표본 공간이 바뀜
            안경      노안경
    남자      5          7
    여자      6          4
    A : 남자일 사건, B: 안경을 쓰고 있을 사건
    P(B|A) = P(A교B)/P(A) = (5/22)/(12/22) = (5/12)

    -두 사건이 서로 독립인 경우 : P(A교B) = P(A)*P(B), P(A|B)(A,B 각각 단일사건)=P(A),P(B|A) = P(B)
    -두 사건이 서로 종속인 경우  : P(A교B) = P(B|A)*P(A), P(B|A) = P(A교B)/P(B)

7. 베이즈 정리 : 베이즈 정리를 이용한 분류기는 나이브베이즈 분류기
    P(B|A) = P(A|B)P(B)/P(A)
    P(A) : A가 일어날 확률
    P(B) : B가 일어날 확률
    P(B|A) : A가 일어난 후 B가 일어날 확률(사후 확률)
    P(A|B) : B가 일어난 후 A가 일어날 확률(사후 확률)
    -상점의 매출액을 예측하는 프로그램을 만든다고 가정.
    가장 잘 팔리는 상품 :  노트와  사인펜
    '전체 손님'.'노트를 구매한 손님','두 개를 모두 구매한 손님'
    전체 손님 수  : 100
    노트 손님 수  : 50
    사인펜 손님 수 : 20
    두 가지 모두 구매한 손님 수 : 10
    =====================================================
    다음 손님이 구입할 물건이 뭔지 예측?
    A : 노트를 구매 사건 (50/100)
    B : 사인펜 구매 사건 (20/100)
    두 가지 모두 구매 손님 수 (10/50)

    노트와 사인펜을 동시에 구매할 확률
    50/100*10/50=10/100
    20/100*10/20 = 10/100
    결론 :  B와 A의 결합확률 =  A와 B의 결합확률 (P(B|A)*P(A) = P(A|B)*P(B))

    P(B) 사인펜을 구입한다는 조건하에서 P(A)노트를 구입할 확률
    조건부 확률 P(A|B):P(B) 사인펜을 구입한다는 조건하에서 P(A)노트를 구입할 확률
    B와 A의 결합확률 : P(A|B)*P(B)

    P(A|B) = P(A교B)/P(B)
    P(A교B) = P(A|B)*P(B)
    P(B교A) = P(B|A)*P(A)
    P(B교A) = P(A교B)
    P(A교B) = P(B|A)*P(A) = P(A|B)*P(B)
    P(B|A) = (P(A|B)*P(B))/P(A)

8.나이브 베이즈 분류기
    -베이지안 필터는 나이브 베이즈 분류 알고리즘을 사용한 것이다.
    -나이브 베이즈 분류 알고리즘은 베이즈 정리를 사용한 분류 방법
    -베이즈 정리 :  A라는 사건이 B에 속하는지를 판단 할 때 사용
    A가 입력 텍스트(이메일), B가 카테고리 판정 결과(B1,B2,B3,..Bn: 스펨,햄)
    -원리 :  어떤 문장을 카테고리 분류할 때,나이브 베이즈 분류는 텍스트 내부에서 단어의 출현 비율을 조사.
            =>기반으로 텍스트를 어떤 카테고리 분류하는게 좋을지 판단
    -P(B|A) : 베이즈 정리에서 분모에 있는 P(A)는 입력 텍스트가 주어질 확률.
    어떤 카테고리를 판정하든 같은 입력텍스트가 주어지는 것이므로 (같은 값으로 생각할 수 있음) 따로 고려하지 않아도 됨
    P(B|A) = P(B)*P(A|B)
    P(B) : 각 카테고리로 분류될 확률(전체 문서에서 해당 카테고리의 문서일 확률)
    P(A|B) :A 는 입력텍스트의 단어의 집합,단어들의 순서는 고려하지 않고, 단어들만 표현한다.(Bag-of-Word;BOW)

    입력 텍스트 : A를 각 단어(aN)의 집합이라고 할때, P(A|B)?
    P(A|B) = P(a1|B)P(a2|B)...P(an|B)
    P(aN|B)? 단어가 카테고리에 속할 확률
    어떤 카테고리에 해당 단어가 출현한 확률을 계산
    출현율 = 출현 횟수 / 카테고리 전체 단어 수

9.베이즈 이론의 분류기:
    문장(메일) 입력 - 출력
    -----------------------------------------
    잘 지내셨조?-햄
    사주세요 제발 -스팸
    .....
    형님 강호동입니다. 언제 또 뵐 수 있나요? -스펨
    -----------------------------------------
    위의 분류는 사람이 함 => 교사학습-베이지안 필터
    오늘 날씨가 선선합니다. 저녁에 뵐까요? => 모델 =>햄/스펨

    입력만 받아서 분류없이 학습(워드투벡터(형태소 분류로 벡터공간에 배열) : 나누거나 묶음형성->클러스터(링),군집화)
    k-means(중앙값 찾기) : 단어들을 수치화 시켜 배열 ,군집의 중앙값(두 단어의 중앙값, 중앙값과 다음단어의 중앙값....)을 찾음


"""
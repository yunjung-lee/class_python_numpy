"""
문장의 유사도
엠그램
위키피디어 모델 이용 모델 만들기

N-GRAM(엠그램) : 문장 유사도 분석

레벤슈타인거리 : 두 개의 문자열이 어느 정도 다른가(편집거리 알고리즘)
=최장 공통 부분 수열(Traceback example:문자열 유사도(왼->오,위->아래 : 계산 순서 = 오른쪽 아래(가장 큰수:가장 큰 차이))
 - DNA배열 유사성 조사
  ex)가나다라, 가마바라 : 두 문자열의 편집거리(몇번 편집으로 두개가 동일해 지는가)를 수치로 나타냄
   -2번 편집으로 동일.
배열 : (문자열+1)*(문자열+1) 배열이 됨
"""

#레벤슈타인거리 구하기

def calc_distance(a,b):
    if a==b: return 0
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len
    if b=="" : return a_len

    #matrix를 만들고 초기화
    matrix =[[]  for i in range(a_len+1)]
    # print(matrix)
    # [[], [], [], [], []]
    for i in range(a_len+1):
        matrix[i]=[0 for j in range(b_len+1)]
     # 모두 0으로 초기화
    for i in range(a_len+1):
        matrix[i][0]=i
    for j in range(b_len+1):
        matrix[0][j]=j
    print(matrix)
  #  else: return print("계산을 해봐야 합니다.")
    # return a와 b사이의 거리

    for i in range(1,a_len+1):
        ac = a[i-1]     #"가나다라"에서 "가"
        for j in range(1,b_len+1):
            bc=b[j-1]       #"가마바라"에서 "가"
            cost = 0 if(ac==bc) else 1
#matrix[i][j]에서 문자 삽입, 제거, 변경 중 가장 작은 값을 대입
            matrix[i][j] = min(
                    matrix[i-1][j]+1,       #문자 삽입
                    matrix[i][j-1]+1,       #문자 제거
                    matrix[i-1][j-1]+cost       #문자 변경
                )
    return  matrix[a_len][b_len]

print(calc_distance("가나다라","가마바라")) #2출력 예상

#
samples = ["신촌역","화곡역","동대문입구역","신발","상공회의소"]
base =samples[0]
#
#
r=sorted(samples,key = lambda n : calc_distance(base,n) )
# #정렬 결과가 r
# #정렬 방식의 속성이 없어서 오름차순 정렬
# #정렬 대상 samples(list)
# #정렬기준key : 함수(lambda)의 결과값으로 오름차순 정렬
# #lambda n : n이 중요함=>samples요소가 for문이 없어도 순서대로 들어감
# #lambda n=[0,2,5,....]: 오름차순으로 r로 samples의 요소로 들어가서 아래 for문을 돌림
# #r리스트의 편집거리를 오름차순으로 정렬했울땨,
# #해당 역의 이름이 리스트의 요소로 출력됨

for n in r:
    print(calc_distance(base,n),n)
#
#
# for n in range(len(samples)):
#     calc_distance(base,samples[n] )
#



#N-GRAM : 두 문장사이에 유사도를 조사하는 방법
#n : 이웃한 문자의 수
#ex) "오늘 상공회의소에서 문자 비교 알고리즘을 배웠다."
#ex) "문자 비교 알고리즘을 오늘 상공회의소에서 배웠다."

# "오늘 상공회의소에서 문자 비교 알고리즘을 배웠다."
# #n을 2 로 한 경우,
# ['오늘', '늘 ',' 상', '상공', '공회', '회의',.... ,'웠다']
# "문자 비교 알고리즘을 오늘 상공회의소에서 배웠다."
# ['문자','자 ',' 비', '비교',..... ,'웠다']
#
# s에 전달된 문자열 길이가 10이라면, num이 2라면
# res 리스트의 길이는 얼마? len(s) -num+1





#두 문자열간 비교를 하는 알고리즘
def ngram(s,num):
    res =[]
    # res 리스트의 길이는 얼마나 나올까요?
    slen = len(s) -num+1 # slen : 리스트 요소의 갯수
    for i in range(slen):
        ss=s[i:num+i]
        res.append(ss)
    print(res)
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
a = "문자간 비교하는 알고리즘을 상공회의소에서 오늘 배웠다."
b = "오늘 상공회의소에서 문자 비교하는 방법을 배웠다."

#2-gram
res,word = diff_ngram(a,b,2)
print("2-gram",res, word)

#3-gram
res= diff_ngram(a,b,3)
print("3-gram",res)

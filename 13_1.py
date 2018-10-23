
# path='example.txt'
# data = open(path, encoding='utf=8').readline()          # 모드를 생략가능 => 생략하면 'r'
# print(data)                             #첫번째 한줄 출력

import json
path="example.txt"
records=[json.loads(line) for line in open(path, encoding='utf=8')]         #loads 함수가 데이터속 \를 없애고 출력    #print(records[0]['tz'])                                     #키['tz']를 이용해서 value를 추출할 수 있다.

#shift + f 로 원하는 키가 몇개 있나를 파일로 직접 가서 확인 가능

time_zones=[rec['tz'] for rec in records if 'tz' in rec]
#print(time_zones)

#print(time_zones[:20])

#time_zones의 결과값 중 한 항목 당 몇건씩이나 겹치는지 확인

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:             #해당 값(X)(도시명)이 이미 저장되어있는 경우
            counts[x]+=1
        else:                       #저장 안되어 있는 경우
            counts[x]=1

    return counts

counts = get_counts(time_zones)
# print(type(counts))
# print(counts['America/New_York'])                   #America/New_York의 횟수
# print(len(counts))                                  #tz 가 가지는 도시수
# print(len(time_zones))                              #tz가 있는 행의 갯수

from collections import defaultdict
def get_counts2(sequence):
    counts=defaultdict(int)                 #defaultdict => 0으로 초기화 하라
    for x in sequence:
        counts[x]+=1
    return counts

counts = get_counts2(time_zones)
# print(type(counts))
# print(counts['America/New_York'])                   #America/New_York의 횟수
# print(len(counts))                                  #tz 가 가지는 도시수
# print(len(time_zones))
# print(counts)
#가장 많이 등장한 10개를 출력
def top_counts(counts_dict, n=10):
    # for key,value in counts_dict.items():
    #     print(value)
    value_key_pairs=[(value,key) for key, value in counts_dict.items()]         #튜플
#    print(value_key_pairs)
#    value_key_pairs = [value for key, value in counts_dict.items()]             #key가 필요하다=> 튜플로 만듬
    value_key_pairs.sort()
#    print(value_key_pairs[-n:])

top_counts(counts,3)                           #상위 10개 도시 출력


from collections import Counter
counts =  Counter(time_zones)
# print(counts.most_common(10))                   #랭킹화
# print(counts)                                   #튜플로 묶음

eng='klakdhgkaoqnwekrdkufbiyoiautysear'
#print(Counter(eng))

#Pandas:데이터 분석 패키지(모듈(.py : 함수,클래스 등 구성요소의 묶음) 또는 패키지의 묶음)

from pandas import  DataFrame, Series
import pandas as pd
frame = DataFrame(records)      #데이터를 표현형태로 변환
# print(frame)
# print(frame.info())
#print(frame['tz'].fillna())

tz_counts = frame['tz'].value_counts()
#print(tz_counts[:10])



#시각화 matplotlib : 결측치 때문에 오류가 생기기 때문에 꼭 전처리 과정에서 처리를 해야함
#결측치 전처리 =
#ns :  not available(결측치)
clean_tz = frame['tz'].fillna("Missing")                    # tz : 키가 존재하지 않는 경우
#print(clean_tz)
clean_tz[clean_tz=='']='Unknown'         #na라고 함         #tz 키는 있지만, 값이 없는 경우(결측값)
#tz : ''
#tz : 키가 없음

print(type(clean_tz))
#<class 'pandas.core.series.Series'>
tz_counts=clean_tz.value_counts()


#시각화
import matplotlib.pyplot as plt
#print(tz_counts)
tz_counts[:10].plot(kind='barh')                #bar : 막대그래프, h: horizintal
#plt.show()

#print(frame.a.dropna())                         #na행 제거
#print([x.split()[0] for x in frame.a.dropna()])
#print(type([x.split()[0] for x in frame.a.dropna()]))
#<class 'list'>


#split예시
# x="test1 test2 test3"
# print(x.split())                                 #공백을 기준으로 나뉨


results=Series([x.split()[0] for x in frame.a.dropna()])
#print(results.value_counts()[:5])
#AttributeError: 'list' object has no attribute 'value_counts'
#<class 'Series'> =>로 변환해야 value_counts()가 가능
#자료구조에 따라 사용 함수가 다르다.:함수 사용법이 있는 메뉴얼이 있는데 그걸 확인해야 한다.
#help()

# print(frame.a.notnull())                        #null=> false로 대체
# print(frame[frame.a.notnull()])                 #null은 제외하고 출력
#print(len(frame))
#3560

cframe = frame[frame.a.notnull()]
#print(len(cframe))                                       #'a'키가 없는 행은 제거된 상태
#3440

#print(cframe.a)
#print(cframe['a'])                                  #위와 동일한 결과

#print(cframe.a.str.contains('Windows'))                #cftame의 a의 문자열이 'Windows'를 포함하고 있다는 문장
import numpy as np
os=np.where(cframe.a.str.contains('Windows'),"Windows","Not Windows")           #np.where : if 처럼 true/false형식으로 사용
print(os[:5])

#cframe을 os별로 'tz'값에 따라 그룹화
by_tz_os = cframe.groupby(['tz',os])                                #groupby : 그룹화를 하고 싶을 때 사용
agg_counts=by_tz_os.size().unstack().fillna(0)                      #unstack/stack : 재구성하는 pandas함수로 중요
print(agg_counts.sum(1).argsort())

indexer = agg_counts.sum(1).argsort()                               #agg_counts : 엑셀의 피벗테이블과 비슷함
print(indexer[:10])

count_subset = agg_counts.take(indexer)[-10:]                            #count_subset :  빈도수
print(count_subset)
# normed_subset = count_subset.div(count_subset.sum(1), axis =0 )         # normed_subset:정규화 =>비율
# normed_subset.plot(kind = 'barh', stacked = True)

count_subset.plot(kind = 'barh', stacked = True)
plt.show()
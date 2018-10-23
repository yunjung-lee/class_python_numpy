##########연속형 변수################
#연속형 변수 -> 기술통계량 집계 함수

# 그룹화 기준              그룹                                        요약
# 딕셔너리                  sum,count
# 시리즈         =>      min,max, mean, median              =>  그룹화,sum()
# 함수                std,var, quantile, first, last            그룹화,agg('sum')

# 1) 내장형 함수(sum,count...) 사용
# 2) 직접 함수를 만들어서 사용


import pandas as pd
import numpy as np
from pandas import DataFrame,Series

df = DataFrame({'group': ['a','a','a','b','b','b'],
                'value_1': np.arange(6),
                'value_2': np.random.randn(6)})
print(df)
#   group  value_1   value_2
# 0     a        0 -0.466380
# 1     a        1 -0.707217
# 2     a        2 -1.012695
# 3     b        3  0.290544
# 4     b        4  0.132432
# 5     b        5 -1.052202

grouped = df.groupby('group')
print(grouped)
# <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x03783210>

print(grouped.count())                                  # group 항목으로 묶이면서 항목별 다른 열들의 행 갯수를 샌다(na제외).
#        value_1  value_2
# group
# a            3        3
# b            3        3

print(grouped.sum())
#        value_1   value_2
# group
# a            3 -1.114733
# b           12  0.501867

#결과 중 value_2만 출력 하고 싶을때 : df => 데이터 프레임,value_2 => 시리즈
print(grouped.sum()["value_2"])
# group
# a    1.290631
# b   -2.194880
# Name: value_2, dtype: float64
print(type(grouped.sum()["value_2"]))
# <class 'pandas.core.series.Series'>


# 시리즈를 데이터프레임으로 변환
df2=DataFrame(grouped.sum()["value_2"])
print(type(df2))
# <class 'pandas.core.frame.DataFrame'>

print('='*50)

print(df)
#   group  value_1   value_2
# 0     a        0  0.171863
# 1     a        1  1.711392
# 2     a        2  1.643324
# 3     b        3  0.654445
# 4     b        4 -0.229945
# 5     b        5 -0.670893

print(grouped.min())                                        #최소
#         value_1   value_2
# group
# a            0  0.171863
# b            3 -0.670893

print(grouped.max())                                        #최대
#        value_1   value_2
# group
# a            2  1.711392
# b            5  0.654445

print(grouped.mean())                                        #평균
#        value_1   value_2
# group
# a            1  1.175526
# b            4 -0.082131

print(grouped.median())                                        #중앙값
#        value_1   value_2
# group
# a            1  1.643324
# b            4 -0.229945

print(grouped.std())                                        #표준편차
#        value_1   value_2
# group
# a          1.0  0.869864
# b          1.0  0.674920

print(grouped.var())                                        #분산
#        value_1   value_2
# group
# a            1  0.756664
# b            1  0.455517

print(grouped.quantile())                                        #분위수(0~1사이의 값)
# 0.5    value_1   value_2
# group
# a          1.0  1.643324
# b          4.0 -0.229945
#각 그룹별 최소값~최대값에 대해 지정된 위치값을 추출
# a: 0~2,b:3~5  0.1 = 10%위치
print(grouped.quantile(0.1))                                        #분위수(0~1사이의 값)

print(grouped.first())                                        #첫번째

print(grouped.last())                                        #마지막


#그룹별 기술통계량
print(grouped.describe()['value_1'])
#        count  mean  std  min  25%  50%  75%  max
# group
# a        3.0   1.0  1.0  0.0  0.5  1.0  1.5  2.0
# b        3.0   4.0  1.0  3.0  3.5  4.0  4.5  5.0
print(grouped.describe()['value_1'].T)
# group    a    b
# count  3.0  3.0
# mean   1.0  4.0
# std    1.0  1.0
# min    0.0  3.0
# 25%    0.5  3.5
# 50%    1.0  4.0
# 75%    1.5  4.5
# max    2.0  5.0


# 직접 함수를 만들어서 사용
def iqr_func(x):
    q3,q1 = np.percentile(x,[75,25])
    iqr=q3-q1
    return iqr

print(grouped.aggregate(iqr_func))
#         value_1   value_2
# group
# a            1  0.590795
# b            1  0.887290

print(grouped.agg(iqr_func))                                #agg : aggregate 의 축약
#        value_1   value_2
# group
# a            1  0.590795
# b            1  0.887290

print(grouped.quantile([0.75,0.25]))                        #만든 함수 검증 : 결과가 같다.
#              value_1   value_2
# group
# a     0.75      1.5  0.280411
#       0.25      0.5 -0.310384
# b     0.75      4.5  0.139183
#       0.25      3.5 -0.748107

#범주형 변수에서 특정 항목을 기준으로 맵핑(dict.get())
#LEE,Lee,lee=>lee : 모두 같은 범주로 묶어줌

df = DataFrame({'name': ['kim','KIM','Kim','LEE','Lee','lee','park','choi'],
             "value": [1,2,3,4,5,6,7,8],
           'value_2':[100,300,200,100,100,300,50,80]})

#name컬럼 값 => 새로운 컬럼 생성('kim','lee','others')

#db : 형식이 정해져 있는 데이터 => 정형데이터 : 다루기 용이하다.
#딕셔너리를 만들어서 치환

name_mapping = {'KIM':'kim','Kim':'kim','LEE':'lee','Lee':'lee','park':'others','choi':'others'}
#name_mapping에 의거하여 변환


#dict의 get이라는 함수의 정의되는 것은 딕셔너리에 맵핑되는 것이 있음 참조
#func이란 함수에 x란 값이 들어오면 get(x,x)의 함수로 전달되어 맵핑을 하거나 조건에 만족하지 않으면 두번째 인수에 의거하여 룰대로 출력
func = lambda x : name_mapping.get(x,x)                                  #get(바꿔주는 베이스 정보, 정보가 없으면 그대로 리턴)

print(df)
#    name  value  value_2
# 0   kim      1      100
# 1   KIM      2      300
# 2   Kim      3      200
# 3   LEE      4      100
# 4   Lee      5      100
# 5   lee      6      300
# 6  park      7       50
# 7  choi      8       80                                               #name_2의 변수가 추가되며 name_mapping에 의거하여 데이터 생성

df['name_2'] = df.name.map(func)
print(df)
#    name  value  value_2  name_2
# 0   kim      1      100     kim
# 1   KIM      2      300     kim
# 2   Kim      3      200     kim
# 3   LEE      4      100     lee
# 4   Lee      5      100     lee
# 5   lee      6      300     lee
# 6  park      7       50  others
# 7  choi      8       80  others

print(df.groupby('name_2').sum())
#         value  value_2
# name_2
# kim         6      600
# lee        15      500
# others     15      130

print(df.groupby(['name_2','name'])['value_2'].sum())
# name_2  name
# kim     KIM     300
#         Kim     200
#         kim     100
# lee     LEE     100
#         Lee     100
#         lee     300
# others  choi     80
#         park     50
# Name: value_2, dtype: int64



##################numpy의 배열 나누기-복습-############
#열방향 나누기 axis=1
#행방향 나누기 axis=0

print('='*50)
x=np.arange(18).reshape(3,6)
print(x)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]]
print('='*50)
print(np.hsplit(x,3))                                  # np.hsplit(x,3) :  x를 3개로 나누기
# [array([[ 0,  1],
#        [ 6,  7],
#        [12, 13]]), array([[ 2,  3],
#        [ 8,  9],
#        [14, 15]]), array([[ 4,  5],
#        [10, 11],
#        [16, 17]])]
print('='*50)
print(np.hsplit(x,(2,4)))                               #np.hsplit(x,(2,4)) =>x[:,:2],x[:,2:4],x[:,4:6]
# [array([[ 0,  1],
#        [ 6,  7],
#        [12, 13]]), array([[ 2,  3],
#        [ 8,  9],
#        [14, 15]]), array([[ 4,  5],
#        [10, 11],
#        [16, 17]])]
print('='*50)
print(np.split(x,3,axis=1))                                             # np.hsplit(x,3) ==np.split(x,3,axis=1)
# [array([[ 0,  1],
#        [ 6,  7],
#        [12, 13]]), array([[ 2,  3],
#        [ 8,  9],
#        [14, 15]]), array([[ 4,  5],
#        [10, 11],
#        [16, 17]])]
print('='*50)
print(np.split(x,(2,4),axis = 1))
# [array([[ 0,  1],
#        [ 6,  7],
#        [12, 13]]), array([[ 2,  3],
#        [ 8,  9],
#        [14, 15]]), array([[ 4,  5],
#        [10, 11],
#        [16, 17]])]
print('='*50)
x1,x2,x3 = np.hsplit(x,3)
print(x1)
# [[ 0  1]
#  [ 6  7]
#  [12 13]]

#########수직방향으로##############'
print('='*50)
print(x)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]]
print('='*50)
print(np.vsplit(x,3))
# [array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11]]), array([[12, 13, 14, 15, 16, 17]])]
print('='*50)
print(np.split(x,3,axis=0))
# [array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11]]), array([[12, 13, 14, 15, 16, 17]])]

# np.argmin(),np.argmax() =>np.arg : 색인에 대한 함수
print('='*50)
x=np.array([15,14,13,12,11,10])
print(x.min())
#10
print(x.max())
# 15
print(np.max(x))
#15
print(x.argmin())
#5
print(x.argmax())
#0
print(np.argmax(x))
#0

#배열에서 13이사인 색인의 위치를 출력
print(np.where(x>=13))
# (array([0, 1, 2], dtype=int32),)

#배열에서 13이상인 값들을 출력
print(x[np.where(x>=13)])

#배열에서 13이상의 값은 모두 100으로 치환하고 출력
print(np.where(x>=13,100,x))
# [100 100 100  12  11  10]

x2=[]
for i in list(x) : #array ->list
    if i>=13:
        x2.append(100)
    else:
        x2.append(i)
x2=np.asanyarray(x2)
print(x2)
# [100 100 100  12  11  10]

###########################집합단위의 연산############################################
#합집합
#교집합
#차집합
#대칭차집합

x=np.array([1,2,3,1,2,4])
print(np.unique(x))
# [1 2 3 4]

x=np.array([1,2,3,4])
y=np.array([3,4,6,5])
#교집합
print((np.intersect1d(x,y)))
# [3 4]

#합집합
print(np.union1d(x,y))
# [1 2 3 4 5 6]

#차집합
print(np.setdiff1d(x,y))
# [1 2]

#대칭차집합
print(np.setxor1d(x,y))
# [1 2 5 6]


x=np.array([1,2,3,4,5,6])
y=np.array([2,4])

#x내부에 y가 있는 여부를 확인
print(np.in1d(x,y))
# [False  True False  True False False]


## stack 함수  ##

#합치기
#1) 왼쪽에서 오른쪽으로 합치기
# -np.r_[x,y] 또는 np.hstack([x,y]) =>x오른쪽에 y

# 2)위에서 아래쪽으로 합치기 ->2차원 배열
#np.r_[[x],[y]], np.vstack([x,y])

#3) 두 개의 1차원 배열 -> 세로로 합치기 ->2차원 배열
# -np.c_[x,y] 또는 np.column_stack([x,y])

print('='*50)
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a)
# [1 2 3]

print(b)
# [4 5 6]

#좌우로 합치기
print(np.r_[a,b])
# [1 2 3 4 5 6]
print(np.hstack([a,b]))
# [1 2 3 4 5 6]

#위아래로 붙이기
print(np.r_[[a],[b]])
# [[1 2 3]
#  [4 5 6]]
print(np.vstack([a,b]))
# [[1 2 3]
#  [4 5 6]]
print(np.shape(np.vstack([a,b])))
# (2, 3)


#차원확대(1차원->2차원) 붙이기
print(np.c_[a,b])
# [[1 4]
#  [2 5]
#  [3 6]]
print(np.shape(np.c_[a,b]))
# (3, 2)
print(np.column_stack([a,b]))
# [[1 4]
#  [2 5]
#  [3 6]]





































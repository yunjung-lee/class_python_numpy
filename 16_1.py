import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

num = np.array(['3.14','-2.7','30'], dtype=np.string_)          #코드 이해 쉽게 : dtype=np.string_
# num=num.astype(int)
# print(num)
# ValueError: invalid literal for int() with base 10: '3.14'
num=num.astype(float).astype(int)
print(num)
# [ 3 -2 30] :  바로 int형 변형이 안되면 float으로 바꿨다가 바꿀 수 있다.
num=num.astype(float)
print(num)
# [ 3.14 -2.7  30.  ]


arr=np.arange(32).reshape((8,4))
print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]
#  [24 25 26 27]
#  [28 29 30 31]]
print(arr[[1,5,7,2],[0,3,1,2]])         #지정된 데이터 추출[[행번호],[열번호]]==>(행,열)순서쌍으로 요소 확인
# [ 4 23 29 10]
print(arr[[1,5,7,2]][:,[0,3,1,2]])      #[[행]][:,[열]] : 연속의 의미==>행 1,5,7,2번 index에 해당하는 행
# [[ 4  7  5  6]
#  [20 23 21 22]
#  [28 31 29 30]
#  [ 8 11  9 10]]
print(arr[[1,5,7,2]][:,[3,1]])          #[[행]][:,[열]] : 연속의 의미==>index행에 대한 열 1,3번 index에 해당하는 열
# [[ 7  5]
#  [23 21]
#  [31 29]
#  [11  9]]

import random

walk = []
position =0
steps=1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1         #randint,randn,rannormal
    position+=step
    walk.append(position)
print("position : ",position)
# position :  18
print("walk : ",walk)
# walk :  [-1, 0, 1, 0, -1, -2, -1, -....]

print(min(walk))
# -7
print(max(walk))
# 28

# print(abs(walk))                              #abs : 절대값 변환

obj = Series([1,2,-3,4])
print(obj)
# 0    1
# 1    2
# 2   -3
# 3    4
# dtype: int64
print(obj.values)                           #values : 값만 추출함(속성, 함수)
# [ 1  2 -3  4]
print(obj.index)                            #index :  인덱스 추출
# RangeIndex(start=0, stop=4, step=1)

#인덱스 지정
obj =  Series([1,2,-3,4],index=['x','y','z','k'])           #index의 이름을 직접 부여
print(obj)
# 지정 인덱스 출력
# x    1
# y    2
# z   -3
# k    4
# dtype: int64
print(obj['y'])
# 2

obj['x']=10
print(obj)
# x    10
# y     2
# z    -3
# k     4
# dtype: int64

#여러개를 참조하는 방법
# print(obj['x','y'])
# # KeyError: ('x', 'y')
print(obj[['x','y','z']])           #index 1개 참조시 [],2개이상 참조시 [[]]
# x    10
# y     2
# z    -3
# dtype: int64
print('='*50)

print(obj>0)                        #조건식 사용 가능
# x     True
# y     True
# z    False
# k     True
# dtype: bool
print(obj[obj>0])                   #조건식으로 추출 가능
# x    10
# y     2
# k     4
# dtype: int64
print(obj*2)                        # 사칙연산 가능
# x    20
# y     4
# z    -6
# k     8
# dtype: int64
print(np.exp(obj))                  # 지수승
# x    22026.465795
# y        7.389056
# z        0.049787
# k       54.598150
# dtype: float64


# null(초기화 되지 않은 상태), na(결측치)
print(obj)
print('a' in obj)                       #in : 특정 문자가 있는지 확인
print('x' in obj)                       # 열: 특징, 행 : 관측치

print('='*50)

#key & value->Series->index & value 변환(key=>index,value=>value)
sdata = {'Ohio': 35000, 'Texas': 71000, "Oregon":16000, "Utah":5000}
obj3=Series(sdata)                                                      #dictionaly도 Series로 변환 가능
print(obj3)
# Ohio      35000
# Texas     71000
# Oregon    16000
# Utah       5000
# dtype: int64
print(type(obj3))
# <class 'pandas.core.series.Series'>

states = ['California','Ohio','Oregon','Texas']
obj99 = Series(states)                              #list를 Series로 변환
# print(obj99)
# # 0    California
# # 1          Ohio
# # 2        Oregon
# # 3         Texas
# # dtype: object

obj4 = Series(sdata, index=states)                  #sdata를 사용하여 index는 states기준으로 Series자료구조 변환
print(obj4)
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# dtype: float64
print(pd.isnull(obj4))
# California     True
# Ohio          False
# Oregon        False
# Texas         False
# dtype: bool

#일반적인 개념 nan : 숫자가 아닌 문자같은 것.
#na : 값이 누락, null : 값이 초기화 되지 않은 상태
#pandas개념 : 혼용하여 사용
#isnull함수 : na(null,nan) 인지 아닌지 확인

print(obj4+obj3)                                # 교집합만의 value만 출력

obj4.name = 'population'
obj.index.name = 'state'
print(obj4)
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# Name: population, dtype: float64

obj4.index=['w','x','y','z']                    #index를 직접 변환
print(obj4)
# w        NaN
# x    35000.0
# y    16000.0
# z    71000.0
# Name: population, dtype: float64

data = {
    'state' : ['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year': [2000,2001,2002,2001,2002],
    'pop': [1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data)                                         #series 들의 묶음과 같음
print(frame)
#     state  year  pop
# 0    Ohio  2000  1.5
# 1    Ohio  2001  1.7
# 2    Ohio  2002  3.6
# 3  Nevada  2001  2.4
# 4  Nevada  2002  2.9

print(DataFrame(data, columns=['year','state','pop']))          # column의 순서 변경(임시적)
#    year   state  pop
# 0  2000    Ohio  1.5
# 1  2001    Ohio  1.7
# 2  2002    Ohio  3.6
# 3  2001  Nevada  2.4
# 4  2002  Nevada  2.9

frame = DataFrame(data, columns=['year','state','pop'])         #fram으로 완전히 순서 변경
frame2= DataFrame(data, columns=['year','state','pop','debt'], index=['one','two','three','four','five'])
print(frame2)
#        year   state  pop debt
# one    2000    Ohio  1.5  NaN
# two    2001    Ohio  1.7  NaN
# three  2002    Ohio  3.6  NaN
# four   2001  Nevada  2.4  NaN
# five   2002  Nevada  2.9  NaN

print(frame2['state'])                                  # 원하는 열만 출력
# one        Ohio
# two        Ohio
# three      Ohio
# four     Nevada
# five     Nevada
# Name: state, dtype: object
print(frame2['year'])
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# Name: year, dtype: int64

print(frame2.ix['three'])                       #ix : 특정 index(행)만 참조

#두개 이상의 열 또는 행을 추출 => [[]]사용
# print(frame2[['year','state']])
#
# print(frame2.ix[['three','five']])

print(frame2)
frame2['debt']=16.5
print(frame2)
#        year   state  pop  debt
# one    2000    Ohio  1.5  16.5
# two    2001    Ohio  1.7  16.5
# three  2002    Ohio  3.6  16.5
# four   2001  Nevada  2.4  16.5
# five   2002  Nevada  2.9  16.5
# frame2['debt']=np.arange(3)
# print(frame2)
# # ValueError: Length of values does not match length of index
frame2['debt']=np.arange(5)
print(frame2)
#        year   state  pop  debt
# one    2000    Ohio  1.5     0
# two    2001    Ohio  1.7     1
# three  2002    Ohio  3.6     2
# four   2001  Nevada  2.4     3
# five   2002  Nevada  2.9     4

print('='*50)

val = Series([-1.2,-1.5,-1.7],index=['two','three','five'])
print(val)
# two     -1.2
# three   -1.5
# five    -1.7
# dtype: float64

#길이가 다른 데이터 열을추가시 -> 시리즈를 생성하여 추가
frame2['debt']=val                # index를 지정하여  value 변경(index의 숫자가 동일하지 않아도 index가 지정되어있어서 대입가능)
print(frame2)

# 새로운 열 추가 : 동부에 속하는 Ohio는 True, 나머지는 False로 한다.(조건 제시형)
frame2['eastern']=frame2.state=='Ohio'
print(frame2)
#        year   state  pop  debt  eastern
# one    2000    Ohio  1.5   NaN     True
# two    2001    Ohio  1.7  -1.2     True
# three  2002    Ohio  3.6  -1.5     True
# four   2001  Nevada  2.4   NaN    False
# five   2002  Nevada  2.9  -1.7    False

#열 제거
del frame2['eastern']
print(frame2)
#        year   state  pop  debt
# one    2000    Ohio  1.5   NaN
# two    2001    Ohio  1.7  -1.2
# three  2002    Ohio  3.6  -1.5
# four   2001  Nevada  2.4   NaN
# five   2002  Nevada  2.9  -1.7

print(frame2.columns)
# Index(['year', 'state', 'pop', 'debt'], dtype='object')
print(frame2.index)
# Index(['one', 'two', 'three', 'four', 'five'], dtype='object')

pop = {'Nevada' : {2001 : 2.4,2002:2.9},'Ohio' : {2000 : 1.5,2001:1.7,2002:3.6}}
frame3 = DataFrame(pop)
print(frame3)
#       Nevada  Ohio
# 2000     NaN   1.5
# 2001     2.4   1.7
# 2002     2.9   3.6

# 열과 행 바꿈(transfer)
print(frame3.T)
#         2000  2001  2002
# Nevada   NaN   2.4   2.9
# Ohio     1.5   1.7   3.6

# frame4 = DataFrame(pop,index=[2001,2002,2003])                #index 지정을 하려면 DataFrame을 사용해야한다.(딕셔너리엔 index가 없음)
# print(frame4)
# # AttributeError: 'list' object has no attribute 'astype'
frame4 = DataFrame(frame3,index=[2001,2002,2003])
print(frame4)
#       Nevada  Ohio
# 2001     2.4   1.7
# 2002     2.9   3.6
# 2003     NaN   NaN

print(frame3)
#       Nevada  Ohio
# 2000     NaN   1.5
# 2001     2.4   1.7
# 2002     2.9   3.6
pdata = {'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}              #[:-1] : 마지막 행 제외,[:2] : 0,1 행만 출력
frame5=DataFrame(pdata)
print(frame5)
#       Ohio  Nevada
# 2000   1.5     NaN
# 2001   1.7     2.4

pdata = {'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada']}
#'Nevada'-모두 출력이기 때문에 [:-1]사용으로 자료가 없는 'Ohio'의 2002는 NaN이 된다.
frame5=DataFrame(pdata)
print(frame5)
#         Ohio  Nevada
# 2000   1.5     NaN
# 2001   1.7     2.4
# 2002   NaN     2.9








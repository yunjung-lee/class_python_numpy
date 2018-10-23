# 데이터 프레임 정렬: Dataframe.sort_values()
# 튜플 정렬 : sorted(tuple,key)
# 리스트 정렬 : sort(),sorted(list)
import pandas as pd

pdf = pd.DataFrame({'seq':[1,3,2],'name':['park','lee','choi'],'age' : [30,20,40]})
print(pdf)
#    seq  name  age
# 0    1  park   30
# 1    3   lee   20
# 2    2  choi   40

#정렬 기준을 정할 수 있다.
print(pdf.sort_values(by=['seq']))                                      #seq중심으로 오름차순
#    seq  name  age
# 0    1  park   30
# 2    2  choi   40
# 1    3   lee   20

print(pdf.sort_values(by=['seq'],axis=0,ascending=False))
#    seq  name  age
# 1    3   lee   20
# 2    2  choi   40
# 0    1  park   30

print('='*50)

pdf.sort_values(by=['seq'],axis=0)
print(pdf)
#    seq  name  age
# 0    1  park   30
# 1    3   lee   20
# 2    2  choi   40

pdf.sort_values(by=['seq'],axis=0,inplace=True)                             #inplace=True : 정렬 기준을 저장(없으면 따로 저장:변수 = 변수.sort_values...)
print(pdf)
#    seq  name  age
# 0    1  park   30
# 2    2  choi   40
# 1    3   lee   20

import numpy as np
pdf = pd.DataFrame({'seq':[1,3,np.nan],'name':['park','lee','choi'],'age' : [30,20,40]})

pdf.sort_values(by=['seq'],axis=0,inplace=True,na_position='first')                             #na_position='first' : na의 정렬 기준 지정
print(pdf)
#    seq  name  age
# 2  NaN  choi   40
# 0  1.0  park   30
# 1  3.0   lee   20

pt = [(1,'park',30),(3,'lee',20),(2,'choi',40)]
print(pt)
# [(1, 'park', 30), (3, 'lee', 20), (2, 'choi', 40)]

print(sorted(pt,key=lambda ptf:ptf[0]))                                     #ptf[0] :  0번째 열에 맞춰 오름차순 정렬
# [(1, 'park', 30), (2, 'choi', 40), (3, 'lee', 20)]

print(sorted(pt,key=lambda ptf:ptf[1]))                                     #ptf[1] :  1번째 열에 맞춰 오름차순 정렬
# [(2, 'choi', 40), (3, 'lee', 20), (1, 'park', 30)]

print(sorted(pt,key=lambda ptf:ptf[2]))                                     #ptf[2] :  2번째 열에 맞춰 오름차순 정렬
# [(3, 'lee', 20), (1, 'park', 30), (2, 'choi', 40)]

print(sorted(pt,reverse=True, key=lambda ptf:ptf[2]))
# [(2, 'choi', 40), (1, 'park', 30), (3, 'lee', 20)]


#리스트 : sorted(list), sort
mlist = [9,4,1,2,7]

print(sorted(mlist))                                                     #정렬 된 결과가 저장이 따로 되진 않는다
# [1, 2, 4, 7, 9]

print(mlist)
# [9, 4, 1, 2, 7]

mlist.sort()                                                              #정렬 된 결과가 자동 저장
print(mlist)
# [1, 2, 4, 7, 9]


Seri = pd.Series([ 10.,11.,12.,13.,14.])
print(Seri)
# 0    10.0
# 1    11.0
# 2    12.0
# 3    13.0
# 4    14.0
# dtype: float64

print(Seri[3])
# 13.0

print(Seri[:3])
# 0    10.0
# 1    11.0
# 2    12.0
# dtype: float64

#평균이 12 이상인 행만 추출
print(Seri[Seri>=Seri.mean()])
# 2    12.0
# 3    13.0
# 4    14.0
# dtype: float64

print(Seri[[3,4,2]])
# 3    13.0
# 4    14.0
# 2    12.0
# dtype: float64

Seri_ix = pd.Series([10.,11.,12.,13.,14.],index=['a','b','c','d','e'])
print(Seri_ix)
# a    10.0
# b    11.0
# c    12.0
# d    13.0
# e    14.0
# dtype: float64

print(Seri_ix[['a','b','d']])
# a    10.0
# b    11.0
# d    13.0
# dtype: float64

print(Seri_ix.get(['a','b','d']))
# a    10.0
# b    11.0
# d    13.0
# dtype: float64

Seri_ix['c']=100
print(Seri_ix)
# a     10.0
# b     11.0
# c    100.0
# d     13.0
# e     14.0
# dtype: float64

#특정 인덱스가 있는지 확인
print('c' in Seri_ix)
# True

# ix, loc, iloc
# ix : 위치를 지정하여 데이터를 참조, 레이블을 이용하여 데이터를 참조
# 레이블을 이용하여 데이터 참조 시 ix속성에 수치값을 주는 경우에는 loc와 동일한 결과
# loc : 레이블을 이용하여 데이터를 참조(위치를 이용하여 참조할 수 없다.)
# iloc : 위치를 이용하여 데이터를 참조(레이블을 이용하여 참조할 수 없다.)

Seri = pd.Series(np.nan, index=[19,18,17,16,15,1,2,3,4,5])
print(Seri)
# True
# 19   NaN
# 18   NaN
# 17   NaN
# 16   NaN
# 15   NaN
# 1    NaN
# 2    NaN
# 3    NaN
# 4    NaN
# 5    NaN
# dtype: float64

print(Seri.iloc[:3])                                   #0~2번 행까지 추출
# 19   NaN
# 18   NaN
# 17   NaN
# dtype: float64

print(Seri.loc[:3])                                   #0~7번 행까지 3번이라는 인덱스가 있는 행까지 추출
# 19   NaN
# 18   NaN
# 17   NaN
# 16   NaN
# 15   NaN
# 1    NaN
# 2    NaN
# 3    NaN
# dtype: float64

print(Seri.ix[:3])                                   #0~7번 행까지 3번이라는 인덱스가 있는 행까지 추출
# 19   NaN
# 18   NaN
# 17   NaN
# 16   NaN
# 15   NaN
# 1    NaN
# 2    NaN
# 3    NaN
# dtype: float64

from pandas import DataFrame

df = DataFrame({'c1': [0,1,2,3],
                'c2': [4,5,6,7],
                'c3':[8,9,10,np.nan]},index=['r1','r2','r3','r4'])
print(df.index)
# Index(['r1', 'r2', 'r3', 'r4'], dtype='object')
print(df.columns)
# Index(['c1', 'c2', 'c3'], dtype='object'

df_r1 = DataFrame(df,index=['r1'])
print(df_r1)
#     c1  c2   c3
# r1   0   4  8.0
print(type(df_r1))
# <class 'pandas.core.frame.DataFrame'>

df_r1 = DataFrame(df,index=['r1','r3'])
print(df_r1)
#     c1  c2    c3
# r1   0   4   8.0
# r3   2   6  10.0

df_c1 = DataFrame(df,columns=['c1','c3'])
print(df_c1)
#     c1    c3
# r1   0   8.0
# r2   1   9.0
# r3   2  10.0
# r4   3   NaN

#기존의 데이터프레임으로부터 원하는 특정 부분만 추출하여 새로운 데이터프레임 생성
df_ex = DataFrame(df,index=['r3','r1'],columns=['c3','c1'])
print(df_ex)
#       c3  c1
# r3  10.0   2
# r1   8.0   0

#기존의 데이터프레임으로부터 원하는 특정 부분만 참조
print(df[['c1','c3']])
#     c1    c3
# r1   0   8.0
# r2   1   9.0
# r3   2  10.0
# r4   3   NaN

df['csum']=df['c1']+df['c2']
print(df)
#     c1  c2    c3  csum
# r1   0   4   8.0     4
# r2   1   5   9.0     6
# r3   2   6  10.0     8
# r4   3   7   NaN    10

df = df.assign(cmul=df['c1']*df['c2'])
print(df)
#     c1  c2    c3  csum  cmul
# r1   0   4   8.0     4     0
# r2   1   5   9.0     6     5
# r3   2   6  10.0     8    12
# r4   3   7   NaN    10    21

df = df.assign(cmul2=lambda  x:x.c1*x.c2)                   # lambda :  df가 x로 들어가서 뒤에 계산식 수행 수 cmul2에 값이 대입
print(df)
#     c1  c2    c3  csum  cmul  cmul2
# r1   0   4   8.0     4     0      0
# r2   1   5   9.0     6     5      5
# r3   2   6  10.0     8    12     12
# r4   3   7   NaN    10    21     21

#행이나 열 삭제: drop,del
print(df.drop(['cmul','cmul2'],axis=1))
#     c1  c2    c3  csum
# r1   0   4   8.0     4
# r2   1   5   9.0     6
# r3   2   6  10.0     8
# r4   3   7   NaN    10

print(df.drop(['r1','r3'],axis=0))
#     c1  c2   c3  csum  cmul  cmul2
# r2   1   5  9.0     6     5      5
# r4   3   7  NaN    10    21     21

print(df.drop(['r1','r3']))                                 # axis=0 기본값이라 생략 가능
#     c1  c2   c3  csum  cmul  cmul2
# r2   1   5  9.0     6     5      5
# r4   3   7  NaN    10    21     21

del df['csum']
print(df)
#     c1  c2    c3  cmul  cmul2
# r1   0   4   8.0     0      0
# r2   1   5   9.0     5      5
# r3   2   6  10.0    12     12
# r4   3   7   NaN    21     21

print(df['c1'])
# r1    0
# r2    1
# r3    2
# r4    3
# Name: c1, dtype: int64

print(df.c1)
# r1    0
# r2    1
# r3    2
# r4    3
# Name: c1, dtype: int64

print(df[0:2])
#     c1  c2   c3  cmul  cmul2
# r1   0   4  8.0     0      0
# r2   1   5  9.0     5      5

print(df['c1'][0:2])
# r1    0
# r2    1
# Name: c1, dtype: int64

print(df.c2[0:2])
# r1    4
# r2    5
# Name: c2, dtype: int64

print(df.loc['r1'])
#     c1  c2   c3  cmul  cmul2
# r1   0   4  8.0     0      0
# r2   1   5  9.0     5      5

print(df.loc[['r1','r2']])
#     c1  c2   c3  cmul  cmul2
# r1   0   4  8.0     0      0
# r2   1   5  9.0     5      5
print(df.iloc[0:2])
#     c1  c2   c3  cmul  cmul2
# r1   0   4  8.0     0      0
# r2   1   5  9.0     5      5

print(df[0:2])
#     c1  c2   c3  cmul  cmul2
# r1   0   4  8.0     0      0
# r2   1   5  9.0     5      5

print('='*50)
print(df[df['c1']<=1])
#     c1  c2   c3  cmul  cmul2
# r1   0   4  8.0     0      0
# r2   1   5  9.0     5      5

s=['c1','c2']
print(df[s])
#     c1  c2
# r1   0   4
# r2   1   5
# r3   2   6
# r4   3   7

















































































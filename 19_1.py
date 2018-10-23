import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import pytest

############연속형 변수의 이산화(2개 형태로 나눈다 또는 2개의 항(범주)으로 나눈다.)######################################
## ex :  학점
from pandas.tests.groupby.test_value_counts import bins

np.random.seed(777)
df = DataFrame({'c1':np.random.randn(20),                # np.random.randn(20): 정규분포형 난수 20개 발생
                'c2' : ['a','a','a','a','a','a','a','a','a','a',
                        'b','b','b','b','b','b','b','b','b','b']})
print(df)
#           c1 c2
# 0  -0.468209  a
# 1  -0.822825  a
# ...
# 18  0.914787  b
# 19  0.265041  b

#'c1을 최소-최대값 구간을 10개로 균등하게 분할

print(np.linspace(1,2,10))                              #np.linspace(1,2,10) :  구간을 균등하게 분할=>np.linspace(시작,끝,구간 개수)
# [1.         1.11111111 1.22222222 1.33333333 1.44444444 1.55555556
#  1.66666667 1.77777778 1.88888889 2.        ]

bins = np.linspace(df.c1.min(),df.c1.max(),10)
# [-1.75244452 -1.34715503 -0.94186554 -0.53657605 -0.13128656  0.27400294
#   0.67929243  1.08458192  1.48987141  1.8951609 ]
#
df['c1_bin'] = np.digitize(df['c1'], bins)                                # np.digitize() : 수치화 해주는 함수
print(df)
# # # ValueError: setting an array element with a sequence.         #bins = 변수 선언
#
print(df.groupby('c1_bin')['c1'].size())                            #df.groupby('c1_bin')['c1'].size() : 'c1_bin'로 그룹화 시켰을 때 'c1'의 크기
# c1_bin
# 1     2
# 2     2
# 3     5
# 4     2
# 5     2
# 6     1
# 7     5
# 10    1
# Name: c1, dtype: int64

print(df.groupby('c1_bin')['c1'].mean())                            #df.groupby('c1_bin')['c1'].mean() : 'c1_bin'로 그룹화 시켰을 때 'c1'의 평균
# c1_bin
# 1    -1.577770
# 2    -1.278457
# 3    -0.699377
# 4    -0.453856
# 5     0.099830
# 6     0.544809
# 7     0.883176
# 10    1.895161
# Name: c1, dtype: float64

print(df.groupby('c1_bin')['c1'].std())                            #df.groupby('c1_bin')['c1'].std() : 'c1_bin'로 그룹화 시켰을 때 'c1'의 표준편차
# c1_bin
# 1     0.247027
# 2     0.063959
# 3     0.105535
# 4     0.020298
# 5     0.233643
# 6          NaN
# 7     0.090416
# 10         NaN
# Name: c1, dtype: float64

print(df.groupby('c1_bin')['c2'].value_counts())                    #df.groupby('c1_bin')['c2'].value_counts() : 'c1_bin'로 그룹화 시켰을 때 'c2'의 값의 갯수
# c1_bin  c2
# 1       a     1
#         b     1
# 2       a     1
#         b     1
# 3       b     3
#         a     2
# 4       a     1
#         b     1
# 5       a     1
#         b     1
# 6       b     1
# 7       a     4
#         b     1
# 10      b     1

print(df[df['c1_bin']==2])                                         #'c1_bin'열의 값이 2와 같은 행(2번째 구간)을 출력
# Name: c2, dtype: int64
#           c1 c2  c1_bin
# 7  -1.323683  a       2
# 16 -1.233231  b       2

print('='*50)

print(df['c1_bin'])
# 0      4
# 1      3
# 2      5
# 3      3
# 4      7
# 5      7
# 6      7
# 7      2
# 8      1
# 9      7
# 10     6
# 11    10
# 12     3
# 13     1
# 14     3
# 15     3
# 16     2
# 17     4
# 18     7
# 19     5
# Name: c1_bin, dtype: int32

#pd.get_dummies : 더미 구간
print(pd.get_dummies(df['c1_bin'],prefix='c1'))                     #'c1_bin'의 구간(10구간) 값이 열로 만들어진다.
#     c1_1  c1_2  c1_3  c1_4  c1_5  c1_6  c1_7  c1_10
# 0      0     0     0     1     0     0     0      0
# 1      0     0     1     0     0     0     0      0
# 2      0     0     0     0     1     0     0      0
# 3      0     0     1     0     0     0     0      0
# 4      0     0     0     0     0     0     1      0
# 5      0     0     0     0     0     0     1      0
# 6      0     0     0     0     0     0     1      0
# 7      0     1     0     0     0     0     0      0
# 8      1     0     0     0     0     0     0      0
# 9      0     0     0     0     0     0     1      0
# 10     0     0     0     0     0     1     0      0
# 11     0     0     0     0     0     0     0      1
# 12     0     0     1     0     0     0     0      0
# 13     1     0     0     0     0     0     0      0
# 14     0     0     1     0     0     0     0      0
# 15     0     0     1     0     0     0     0      0
# 16     0     1     0     0     0     0     0      0
# 17     0     0     0     1     0     0     0      0
# 18     0     0     0     0     0     0     1      0
# 19     0     0     0     0     1     0     0      0

print('='*50)
# np.where : 많이 사용
print(df.c1.mean())
# -0.15307715643591518

df['high_low'] = np.where(df['c1']>=df.c1.mean(),'high','low')      #df['high_low']의 컬럼 하나를 np.where로 조건을 써서 만들기
print(df)
#           c1 c2 high_low
# 0  -0.468209  a      low
# 1  -0.822825  a      low
# ...
# 18  0.914787  b     high
# 19  0.265041  b     high

print(df.groupby('high_low'))
# <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x0388EC30>           # 주소 출력

print(df.groupby('high_low')['c1'].size())
# high_low
# high     9
# low     11
# Name: c1, dtype: int64

print(df.groupby('high_low')['c1'].mean())
# high_low
# high    0.783945
# low    -0.919732
# Name: c1, dtype: float64

print(df.groupby('high_low')['c1'].std())
# high_low
# high    0.543661
# low     0.437074
# Name: c1, dtype: float64

Q1=np.percentile(df['c1'],25)                       #25%위치 = Q1 : 오름차순 정렬(Q1<Q3)

Q3=np.percentile(df['c1'],75)                       #75%위치 = Q3

# <25,25<= and <75 ,75<=
df['n_m_l'] = np.where(df['c1']>=Q3,'01_high',np.where(df['c1']>=Q1,'02_medium','03_low'))
print(df)
#           c1 c2  c1_bin high_low      n_m_l
# 0  -0.468209  a       4      low  02_medium
# 1  -0.822825  a       3      low     03_low
# 2  -0.065380  a       5     high  02_medium
# 3  -0.713362  a       3      low  02_medium
# 4   0.906351  a       7     high    01_high
# 5   0.766237  a       7     high  02_medium
# 6   0.826054  a       7     high    01_high
# 7  -1.323683  a       2      low     03_low
# 8  -1.752445  a       1      low     03_low
# 9   1.002449  a       7     high    01_high
# 10  0.544809  b       6     high  02_medium
# 11  1.895161  b      10     high    01_high
# 12 -0.769357  b       3      low  02_medium
# 13 -1.403096  b       1      low     03_low
# 14 -0.632468  b       3      low  02_medium
# 15 -0.558874  b       3      low  02_medium
# 16 -1.233231  b       2      low     03_low
# 17 -0.439504  b       4      low  02_medium
# 18  0.914787  b       7     high    01_high
# 19  0.265041  b       5     high  02_medium


##########데이터 재구조화######################################################
# 데이터 재구조화(reshaping) : pivot, stack, melt등의  함수 사용
# 자료의 데이터를 기준으로 열이나 행으로 구조를 변경(엑셀의 피벗테이블과 같은 방식)


data = DataFrame({'cust_id': ['c1', 'c1', 'c1', 'c2', 'c2', 'c2', 'c3', 'c3', 'c3'],
                 'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
                 'grade' : ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                 'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})
print(data)
#   cust_id prod_cd grade  pch_amt
# 0      c1      p1     A       30
# 1      c1      p2     A       10
# 2      c1      p3     A        0
# 3      c2      p1     A       40
# 4      c2      p2     A       15
# 5      c2      p3     A       30
# 6      c3      p1     B        0
# 7      c3      p2     B        0
# 8      c3      p3     B       10

#변경 내용 : 행 = 고객id, 열- 상품코드, 데이터 -구매금액
#     p1  p2  p3
# c1  30
# c2
# c3

dp = data.pivot(index='cust_id',columns='prod_cd',values='pch_amt')
print(dp)
# prod_cd  p1  p2  p3
# cust_id
# c1       30  10   0
# c2       40  15  30
# c3        0   0  10

dp = pd.pivot_table(data,index='cust_id',columns='prod_cd',values='pch_amt')
print(dp)
# prod_cd  p1  p2  p3
# cust_id
# c1       30  10   0
# c2       40  15  30
# c3        0   0  10

# index가 두개 이상이 될 경우, pivot은 불가능하지만 pivot_table은 가능함

dp = pd.pivot_table(data,index=['cust_id','grade'],columns='prod_cd',values='pch_amt')
print(dp)
# prod_cd        p1  p2  p3
# cust_id grade
# c1      A      30  10   0
# c2      A      40  15  30
# c3      B       0   0  10

print('ㅎ'*50)

dp = pd.pivot_table(data,index='cust_id',columns=['prod_cd','grade'],values='pch_amt')
print(dp)
# prod_cd    p1         p2         p3
# grade       A    B     A    B     A     B
# cust_id
# c1       30.0  NaN  10.0  NaN   0.0   NaN
# c2       40.0  NaN  15.0  NaN  30.0   NaN
# c3        NaN  0.0   NaN  0.0   NaN  10.0

print('ㅎ'*50)

dp = pd.pivot_table(data,index='cust_id',columns=['grade','prod_cd'],values='pch_amt')
print(dp)
# grade       A                B
# prod_cd    p1    p2    p3   p1   p2    p3
# cust_id
# c1       30.0  10.0   0.0  NaN  NaN   NaN
# c2       40.0  15.0  30.0  NaN  NaN   NaN
# c3        NaN   NaN   NaN  0.0  0.0  10.0

#stack : 쌓다라는 의미이기 때문에 테이블을 자료형으로 만드는 것
#unstack : 자료형을 테이블로 만들어줌
#같은 의미의 같은 형식을 R도 지원함

print('='*50)
#tuples은 리스트와 거의 비슷하지만 자료변경이 되지 않는다는 점이 다르다.
mul_index = pd.MultiIndex.from_tuples([('cust_1','2018'),
                           ('cust_1', '2019'),
                           ('cust_2', '2018'),
                           ('cust_2', '2019')])
print(mul_index)
# MultiIndex(levels=[['cust_1', 'cust_2'], ['2018', '2019']],
#            labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
# levels= : 범주
# labels= : 범주들의 순서를 나타냄

data = DataFrame(data=np.arange(16).reshape(4,4), index=mul_index,columns=['prd_1','prd_2','prd_3','prd_4'],dtype='int')
print(data)
#              prd_1  prd_2  prd_3  prd_4
# cust_1 2018      0      1      2      3
#        2019      4      5      6      7
# cust_2 2018      8      9     10     11
#        2019     12     13     14     15

data_stacked = data.stack()
print(data_stacked)
# cust_1  2018  prd_1     0
#               prd_2     1
#               prd_3     2
#               prd_4     3
#         2019  prd_1     4
#               prd_2     5
#               prd_3     6
#               prd_4     7
# cust_2  2018  prd_1     8
#               prd_2     9
#               prd_3    10
#               prd_4    11
#         2019  prd_1    12
#               prd_2    13
#               prd_3    14
#               prd_4    15
# dtype: int32

print(data_stacked.index)
# MultiIndex(levels=[['cust_1', 'cust_2'], ['2018', '2019'], ['prd_1', 'prd_2', 'prd_3', 'prd_4']],
#            labels=[[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]])

print('='*50)

data_stacked = data.stack()
print(data_stacked['cust_2']['2018'][['prd_1','prd_2']])                       # data_stacked[id][year][prd]
# prd_1    8
# prd_2    9
# dtype: int32

data.ix['cust_2','prd_4'] = np.nan
print(data)
#              prd_1  prd_2  prd_3  prd_4
# cust_1 2018      0      1      2    3.0
#        2019      4      5      6    7.0
# cust_2 2018      8      9     10    NaN
#        2019     12     13     14    NaN

print(data.stack())
# cust_1  2018  prd_1     0.0
#               prd_2     1.0
#               prd_3     2.0
#               prd_4     3.0
#         2019  prd_1     4.0
#               prd_2     5.0
#               prd_3     6.0
#               prd_4     7.0
# cust_2  2018  prd_1     8.0
#               prd_2     9.0
#               prd_3    10.0
#         2019  prd_1    12.0
#               prd_2    13.0
#               prd_3    14.0
# dtype: float64

print(data.stack(dropna=False))                         #dropna=True : 기본값
# cust_1  2018  prd_1     0.0
#               prd_2     1.0
#               prd_3     2.0
#               prd_4     3.0
#         2019  prd_1     4.0
#               prd_2     5.0
#               prd_3     6.0
#               prd_4     7.0
# cust_2  2018  prd_1     8.0
#               prd_2     9.0
#               prd_3    10.0
#               prd_4     NaN
#         2019  prd_1    12.0
#               prd_2    13.0
#               prd_3    14.0
#               prd_4     NaN
# dtype: float64

print('='*50)

print(data_stacked)
# cust_1  2018  prd_1     0
#               prd_2     1
#               prd_3     2
#               prd_4     3
#         2019  prd_1     4
#               prd_2     5
#               prd_3     6
#               prd_4     7
# cust_2  2018  prd_1     8
#               prd_2     9
#               prd_3    10
#               prd_4    11
#         2019  prd_1    12
#               prd_2    13
#               prd_3    14
#               prd_4    15
# dtype: int32

# unstack
print(data_stacked.unstack())
#              prd_1  prd_2  prd_3  prd_4
# cust_1 2018      0      1      2      3
#        2019      4      5      6      7
# cust_2 2018      8      9     10     11
#        2019     12     13     14     15

print(data_stacked.unstack(level=-1))                                   # level=-1 :  기본값
#              prd_1  prd_2  prd_3  prd_4
# cust_1 2018      0      1      2      3
#        2019      4      5      6      7
# cust_2 2018      8      9     10     11
#        2019     12     13     14     15

print(data_stacked.unstack(level=0))                                     # level= : -1=>prd, 0=>cust , 1=> year
#             cust_1  cust_2
# 2018 prd_1       0       8
#      prd_2       1       9
#      prd_3       2      10
#      prd_4       3      11
# 2019 prd_1       4      12
#      prd_2       5      13
#      prd_3       6      14
#      prd_4       7      15

print(data_stacked.unstack(level=1))
#               2018  2019
# cust_1 prd_1     0     4
#        prd_2     1     5
#        prd_3     2     6
#        prd_4     3     7
# cust_2 prd_1     8    12
#        prd_2     9    13
#        prd_3    10    14
#        prd_4    11    15

print('='*50)

data_stacked_unstacked=data_stacked.unstack(level=-1)
print(data_stacked_unstacked)
#              prd_1  prd_2  prd_3  prd_4
# cust_1 2018      0      1      2      3
#        2019      4      5      6      7
# cust_2 2018      8      9     10     11
#        2019     12     13     14     15
print(type(data_stacked_unstacked))
# <class 'pandas.core.frame.DataFrame'>

#reset_index : 인덱스를 컬럼으로..
dsu_df = data_stacked_unstacked.reset_index()
print(dsu_df)
#   level_0 level_1  prd_1  prd_2  prd_3  prd_4
# 0  cust_1    2018      0      1      2      3
# 1  cust_1    2019      4      5      6      7
# 2  cust_2    2018      8      9     10     11
# 3  cust_2    2019     12     13     14     15

dsu_df = dsu_df.rename(columns = {'level_0':'custID','level_1':'year'})
print(dsu_df)
#    custID  year  prd_1  prd_2  prd_3  prd_4
# 0  cust_1  2018      0      1      2      3
# 1  cust_1  2019      4      5      6      7
# 2  cust_2  2018      8      9     10     11
# 3  cust_2  2019     12     13     14     15

#melt (R언어에도 같은 함수가 있음)
#열을 추출하여 데이터프레임으로 만듬
#열이름을 하나의 열로, 값을 다른 하나의 열로 만듬

print('='*50)

data = DataFrame({'cust_id': ['c1', 'c1','c2', 'c2'],
                 'prod_cd': ['p1', 'p2', 'p1', 'p2'],
                 'pch_cnt' : [1,2,3,4],
                 'pch_amt': [100,200,300,400]})
print(data)
#   cust_id prod_cd  pch_cnt  pch_amt
# 0      c1      p1        1      100
# 1      c1      p2        2      200
# 2      c2      p1        3      300
# 3      c2      p2        4      400

print('='*50)
print(pd.melt(data))
#    variable value
# 0   cust_id    c1
# 1   cust_id    c1
# 2   cust_id    c2
# 3   cust_id    c2
# 4   prod_cd    p1
# 5   prod_cd    p2
# 6   prod_cd    p1
# 7   prod_cd    p2
# 8   pch_cnt     1
# 9   pch_cnt     2
# 10  pch_cnt     3
# 11  pch_cnt     4
# 12  pch_amt   100
# 13  pch_amt   200
# 14  pch_amt   300
# 15  pch_amt   400

print('='*50)
print(pd.melt(data,id_vars=['cust_id','prod_cd']))
#   cust_id prod_cd variable  value
# 0      c1      p1  pch_cnt      1
# 1      c1      p2  pch_cnt      2
# 2      c2      p1  pch_cnt      3
# 3      c2      p2  pch_cnt      4
# 4      c1      p1  pch_amt    100
# 5      c1      p2  pch_amt    200
# 6      c2      p1  pch_amt    300
# 7      c2      p2  pch_amt    400

print('='*50)
data_melt = pd.melt(data,id_vars=['cust_id','prod_cd'],var_name='pch_cd',value_name='pch_value')
#   cust_id prod_cd   pch_cd  pch_value
# 0      c1      p1  pch_cnt          1
# 1      c1      p2  pch_cnt          2
# 2      c2      p1  pch_cnt          3
# 3      c2      p2  pch_cnt          4
# 4      c1      p1  pch_amt        100
# 5      c1      p2  pch_amt        200
# 6      c2      p1  pch_amt        300
# 7      c2      p2  pch_amt        400

print('='*50)
print(data)
#   cust_id prod_cd  pch_cnt  pch_amt
# 0      c1      p1        1      100
# 1      c1      p2        2      200
# 2      c2      p1        3      300
# 3      c2      p2        4      400

print(data_melt)
#   cust_id prod_cd   pch_cd  pch_value
# 0      c1      p1  pch_cnt          1
# 1      c1      p2  pch_cnt          2
# 2      c2      p1  pch_cnt          3
# 3      c2      p2  pch_cnt          4
# 4      c1      p1  pch_amt        100
# 5      c1      p2  pch_amt        200
# 6      c2      p1  pch_amt        300
# 7      c2      p2  pch_amt        400


print(data_melt.index)
# RangeIndex(start=0, stop=8, step=1)

print(data_melt.columns)
# Index(['cust_id', 'prod_cd', 'pch_cd', 'pch_value'], dtype='object')

data_melt_pivot = pd.pivot_table(data_melt,index=['cust_id','prod_cd'],columns='pch_cd',values='pch_value')
print(data_melt_pivot)
# pch_cd           pch_amt  pch_cnt
# cust_id prod_cd
# c1      p1           100        1
#         p2           200        2
# c2      p1           300        3
#         p2           400        4

print(data_melt_pivot.index)
#         p2           400        4
# MultiIndex(levels=[['c1', 'c2'], ['p1', 'p2']],
#            labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
#            names=['cust_id', 'prod_cd'])

print(data_melt_pivot.columns)
# Index(['pch_amt', 'pch_cnt'], dtype='object', name='pch_cd')
























































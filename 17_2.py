#결측치에 관련 된 함수
#데이터프레임 결측값 처리
#pandas에서는 결측값: NaN, None
#NaN :데이터 베이스에선 문자
#None : 딥러닝에선 행

# import pandas as pd
# from pandas import DataFrame as df

# df_left = df({
#     'a':['a0','a1','a2','a3'],
#     'b':[0.5, 2.2, 3.6, 4.0],
#     'key':['k0','k1','k2','k3']})
# df_right = df({
#     'c':['c0','c1','c2','c3'],
#     'd':['d0','d1','d2','d3'],
#     'key':['k2','k3','k4','k5']})
#
# df_all=pd.merge(df_left,df_right,how='outer',on='key')
# print(df_all)
# #      a    b key    c    d
# # 0   a0  0.5  k0  NaN  NaN
# # 1   a1  2.2  k1  NaN  NaN
# # 2   a2  3.6  k2   c0   d0
# # 3   a3  4.0  k3   c1   d1
# # 4  NaN  NaN  k4   c2   d2
# # 5  NaN  NaN  k5   c3   d3
#
#
# #null 판별
# print(pd.isnull(df_all))
# #        a      b    key      c      d
# # 0  False  False  False   True   True
# # 1  False  False  False   True   True
# # 2  False  False  False  False  False
# # 3  False  False  False  False  False
# # 4   True   True  False  False  False
# # 5   True   True  False  False  False
#
# print(df_all.isnull())
# #        a      b    key      c      d
# # 0  False  False  False   True   True
# # 1  False  False  False   True   True
# # 2  False  False  False  False  False
# # 3  False  False  False  False  False
# # 4   True   True  False  False  False
# # 5   True   True  False  False  False
#
# print(pd.notnull(df_all))
# #        a      b   key      c      d
# # 0   True   True  True  False  False
# # 1   True   True  True  False  False
# # 2   True   True  True   True   True
# # 3   True   True  True   True   True
# # 4  False  False  True   True   True
# # 5  False  False  True   True   True
#
# print(df_all.notnull())
# #        a      b   key      c      d
# # 0   True   True  True  False  False
# # 1   True   True  True  False  False
# # 2   True   True  True   True   True
# # 3   True   True  True   True   True
# # 4  False  False  True   True   True
# # 5  False  False  True   True   True
#
# # 특정 위치에 결측치 입력 : None ==> 결측치란 의미를 담고 있는 예약어
# df_all.ix[[0,1],['a','b']]=None
# print(df_all)
# #       a    b key    c    d
# # 0  None  NaN  k0  NaN  NaN
# # 1  None  NaN  k1  NaN  NaN
# # 2    a2  3.6  k2   c0   d0
# # 3    a3  4.0  k3   c1   d1
# # 4   NaN  NaN  k4   c2   d2
# # 5   NaN  NaN  k5   c3   d3
# #
# # a열(string)=None, b열(float) = NaN
#
#
# print(df_all[['a','b']].isnull())
# #        a      b
# # 0   True   True
# # 1   True   True
# # 2  False  False
# # 3  False  False
# # 4   True   True
# # 5   True   True
#
# #각 열의 결측치의 갯수 확인
# print(df_all.isnull().sum())
# # a      4
# # b      4
# # key    0
# # c      2
# # d      2
# # dtype: int64
#
# # 단일 열의 결측치의 갯수
# print(df_all['a'].isnull().sum())
# # 4
#
# #각 열의 결측치가 아닌 데이터의 갯수 확인
# print(df_all.notnull().sum())
# # a      2
# # b      2
# # key    6
# # c      4
# # d      4
# # dtype: int64
#
# print('='*50)
# print(df_all)
# # 각 행의 결측치의 합
# print(df_all.isnull().sum(1))
# # 0    4
# # 1    4
# # 2    0
# # 3    0
# # 4    2
# # 5    2
# # dtype: int64
#
# df_all['NaN_cnt']=df_all.isnull().sum(1)
# df_all['NotNaN_cnt']=df_all.notnull().sum(1)
# print(df_all)
#
# #결측값 여부?isnull(), notnull()
# #열단위 결측값 개수 : df.isnull().sum()
# #행단위 결측값 개수 : df.isnull().sum(1)
#
# import numpy as np
#
# df=df(np.arange(10).reshape(5,2),
#       index=['a','b','c','d','e'],
#       columns=['c1','c2'])
# print(df)
# #    c1  c2
# # a   0   1
# # b   2   3
# # c   4   5
# # d   6   7
# # e   8   9
#
# df.ix[['b','e'],['c1']]=None
# df.ix[['b','c'],['c2']]=None
# print(df)
#
# print(df.sum())                                     # sum() :  NaN=>0으로 취급하여 계산
# # c1    10.0
# # c2    17.0
# # dtype: float64
#
# print(df['c1'].sum())                               # 한 열 합계
# # 10.0
#
# print(df['c1'].cumsum())                            # cumsum() : 누적합계
# # a     0.0
# # b     NaN
# # c     4.0
# # d    10.0
# # e     NaN
# # Name: c1, dtype: float64
#
# print(df.mean())                                    #열기준 평균 : (0+4+6)/3,NaN=>제외
# # c1    3.333333
# # c2    5.666667
# # dtype: float64
#
# print(df.mean(1))                                   #행기준 평균
# # a    0.5
# # b    NaN
# # c    4.0
# # d    6.5
# # e    9.0
# # dtype: float64
#
#
# print(df.std())                                   #열기준 표준편차
# # c1    3.055050
# # c2    4.163332
# # dtype: float64
#
#
#
# #데이터프레임 컬럼간 연산 : NaN이 하나라도 있으면 NaN
# df['c3'] = df['c1']+df['c2']
# print(df)
# #     c1   c2    c3
# # a  0.0  1.0   1.0
# # b  NaN  NaN   NaN
# # c  4.0  NaN   NaN
# # d  6.0  7.0  13.0
# # e  NaN  9.0   NaN


import pandas as pd
import numpy as np
from pandas import DataFrame as df
from pandas import DataFrame


df=DataFrame(np.arange(10).reshape(5,2),
      index=['a','b','c','d','e'],
      columns=['c1','c2'])
df2=DataFrame({'c1':[1,1,1,1,1],
        'c4': [1, 1, 1, 1, 1]},
      index=['a','b','c','d','e'],
      columns=['c1','c2'])
df['c3'] = df['c1']+df['c2']
print(df)
#    c1  c2  c3
# a   0   1   1
# b   2   3   5
# c   4   5   9
# d   6   7  13
# e   8   9  17
print(df2)
#    c1  c2  c3
# a   0   1   1
# b   2   3   5
# c   4   5   9
# d   6   7  13
# e   8   9  17

print(df+df2)
#    c1   c2  c3
# a   1  NaN NaN
# b   3  NaN NaN
# c   5  NaN NaN
# d   7  NaN NaN
# e   9  NaN NaN

df = DataFrame(np.random.randn(5,3),columns=['c1','c2','c3'])
print(df)
#          c1        c2        c3
# 0 -0.362802  1.035479  2.200778
# 1 -0.793058 -1.171802 -0.936723
# 2 -0.033139  0.972850 -0.098105
# 3  0.744415 -1.121513  0.230542
# 4 -1.206089  2.206393 -0.166863

df.ix[0,0]=None
df.ix[1,['c1','c3']]=np.nan
df.ix[2,'c2']=np.nan
df.ix[3,'c2']=np.nan
df.ix[4,'c3']=np.nan
print(df)
#          c1        c2        c3
# 0       NaN -2.337590  0.416905
# 1       NaN -0.115824       NaN
# 2  0.402954       NaN -1.126641
# 3  0.348493       NaN -0.671719
# 4  1.613053 -0.799295       NaN

df_0=df.fillna(0)
print(df_0)
#          c1        c2        c3
# 0  0.000000 -0.020379 -0.234493
# 1  0.000000  2.103582  0.000000
# 2 -1.271259  0.000000 -2.098903
# 3 -0.030064  0.000000 -0.984602
# 4  0.083863 -0.811207  0.000000

df_missing = df.fillna('missing')
print(df_missing)
#          c1        c2        c3
# 0   missing -0.441011 -0.544838
# 1   missing   1.38941   missing
# 2  -1.77381   missing -0.855286
# 3 -0.287784   missing  0.280705
# 4  0.641317  -2.30403   missing
print('='*50)
print(df)
#          c1        c2        c3
# 0       NaN -0.018915 -1.348020
# 1       NaN  0.063360       NaN
# 2  0.157068       NaN  0.860016
# 3  0.525265       NaN -1.482895
# 4 -0.396621  0.958787       NaN
print(df.fillna(method='ffill'))                                # 바로 위의 값으로 대체
#          c1        c2        c3
# 0       NaN -0.018915 -1.348020
# 1       NaN  0.063360 -1.348020
# 2  0.157068  0.063360  0.860016
# 3  0.525265  0.063360 -1.482895
# 4 -0.396621  0.958787 -1.482895

print(df.fillna(method='pad'))                               # 전방위의 값으로 대체
#          c1        c2        c3
# 0       NaN -0.615965 -0.320598
# 1       NaN -1.488840 -0.320598
# 2  0.108199 -1.488840 -0.415326
# 3  0.521409 -1.488840 -1.533373
# 4  1.523713 -0.104133 -1.533373

print(df.fillna(method='bfill'))                               # 바로 아래의 값으로 대체
#          c1        c2        c3
# 0 -0.119579 -0.237205  0.276887
# 1 -0.119579  0.599437  0.268152
# 2 -0.119579 -0.320518  0.268152
# 3  0.509761 -0.320518 -0.127849
# 4  0.452650 -0.320518       NaN

print('='*50)
print(df)

print(df.fillna(method='ffill',limit=1))                                # 카피는 한번만(시계열 분석할 때 많이 쓰임)
#          c1        c2        c3
# 0       NaN  1.036202  1.100912
# 1       NaN -0.188820  1.100912
# 2  0.311029 -0.188820  0.533007
# 3  0.921236       NaN  0.230806
# 4  0.526154  0.972018  0.230806

print(df)
print(df.mean())
# c1    0.603361
# c2   -0.634602
# c3    0.530568
# dtype: float64

print(df.fillna(df.mean()))
#          c1        c2        c3
# 0  0.603361  0.537082  0.541512
# 1  0.603361 -1.567848  0.530568
# 2 -0.892919 -0.634602  1.213385
# 3  1.369121 -0.634602 -0.163193
# 4  1.333880 -0.873041  0.530568


# where : 특정 함수를 호출(
print(df.where(pd.notnull(df),df.mean(),axis='columns'))
#          c1        c2        c3
# 0 -0.301480 -2.056220  1.549218
# 1 -0.301480  0.546843  0.935090
# 2 -0.297645 -0.181675  0.934137
# 3  0.282334 -0.181675  0.321916
# 4 -0.889131  0.964353  0.935090

#결측치는 KNN으로 많이 대체한다. 또는 회귀모델로 채워넣기도 한다.
print('='*50)
print(df.mean()['c1'])
# -0.3512813307805664

print(df.fillna(df.mean()['c1']))
#          c1        c2        c3
# 0 -0.351281 -0.739683  0.768755
# 1 -0.351281  1.562016 -0.351281
# 2 -1.878074 -0.351281 -0.391961
# 3 -0.397853 -0.351281  1.108282
# 4  1.222083 -0.987635 -0.351281

print('='*50)
print(df)
print(df.mean()['c1':'c2'])
# c1   -0.916834
# c2    0.518672
print(df.fillna(df.mean()['c1':'c2']))
#          c1        c2        c3
# 0 -0.916834  1.133460  1.376126
# 1 -0.916834  0.465905       NaN
# 2 -0.849970  0.518672  1.218364
# 3 -1.537620  0.518672 -0.786485
# 4 -0.362911 -0.043349       NaN


df_2=pd.DataFrame({'c1':[1,2,3,4,5],
                    'c2':[6,7,8,9,10]})
df_2.ix[[1,3],['c2']]=np.nan                        # ix[[1,3],['c2']] : taget index number
print(df_2)
#    c1    c2
# 0   1   6.0
# 1   2   NaN
# 2   3   8.0
# 3   4   NaN
# 4   5  10.0


# pd.notnull(df_2['c2'])==True : 조건 ,df_2['c2'] : 참일때 결과,df_2['c1'] : 거짓일 때의 결과
df_2['c2_new'] = np.where(pd.notnull(df_2['c2'])==True,df_2['c2'],df_2['c1'])
print(df_2)
#    c1    c2  c2_new
# 0   1   6.0     6.0
# 1   2   NaN     2.0
# 2   3   8.0     8.0
# 3   4   NaN     4.0
# 4   5  10.0    10.0


































































































































































































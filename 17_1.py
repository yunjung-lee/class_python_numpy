import numpy as np
import pandas as pd
from pandas import DataFrame as df
from pandas import Series


#index 무시 : ignore_index
df_5 = df({
    'a':['a0','a1','a2'],
'b':['b0','b1','b2'],
'c':['c0','c1','c2'],
'd':['d0','d1','d2']}, index=["r0","r1","r2"])
df_6 = df({
    'a':['a3','a4','a5'],
'b':['b3','b4','b5'],
'c':['c3','c4','c5'],
'd':['d3','d4','d5']}, index=["r3","r4","r5"])

df_56_with_index = pd.concat([df_5,df_6])
print(df_56_with_index)
#      a   b   c   d
# r0  a0  b0  c0  d0
# r1  a1  b1  c1  d1
# r2  a2  b2  c2  d2
# r3  a3  b3  c3  d3
# r4  a4  b4  c4  d4
# r5  a5  b5  c5  d5

df_56_with_index = pd.concat([df_5,df_6],ignore_index=False)
print(df_56_with_index)
#      a   b   c   d
# r0  a0  b0  c0  d0
# r1  a1  b1  c1  d1
# r2  a2  b2  c2  d2
# r3  a3  b3  c3  d3
# r4  a4  b4  c4  d4
# r5  a5  b5  c5  d5

df_56_with_index = pd.concat([df_5,df_6],ignore_index=True)
print(df_56_with_index)
#     a   b   c   d
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
# 3  a3  b3  c3  d3
# 4  a4  b4  c4  d4
# 5  a5  b5  c5  d5

#keys= : 계층구조의 속성을 나타냄(데이터프레임의 찹조가 가능)
df_56_with_index = pd.concat([df_5,df_6],ignore_index=False,keys=['df5','df6'])
print(df_56_with_index)
#          a   b   c   d
# df5 r0  a0  b0  c0  d0
#     r1  a1  b1  c1  d1
#     r2  a2  b2  c2  d2
# df6 r3  a3  b3  c3  d3
#     r4  a4  b4  c4  d4
#     r5  a5  b5  c5  d5

print('ㅋ'*50)

print(df_56_with_index.ix['df5'])
#      a   b   c   d
# r0  a0  b0  c0  d0
# r1  a1  b1  c1  d1
# r2  a2  b2  c2  d2

print(df_56_with_index.ix['df5'][0:2])          # [0:2]로 인덱싱
#   a   b   c   d
# r0  a0  b0  c0  d0
# r1  a1  b1  c1  d1

df_56_with_index = pd.concat([df_5,df_6],ignore_index=False,keys=['df5','df6'],names=['df_name','row_number'])
print(df_56_with_index)
#                        a   b   c   d
# df_name row_number
# df5     r0          a0  b0  c0  d0
#         r1          a1  b1  c1  d1
#         r2          a2  b2  c2  d2
# df6     r3          a3  b3  c3  d3
#         r4          a4  b4  c4  d4
#         r5          a5  b5  c5  d5

print('ㅎ'*50)

df_7 = df({
    'a':['a0','a1','a2'],
'b':['b0','b1','b2'],
'c':['c0','c1','c2'],
'd':['d0','d1','d2']}, index=["r0","r1","r2"])
df_8 = df({
    'a':['a3','a4','a5'],
'b':['b3','b4','b5'],
'c':['c3','c4','c5'],
'd':['d3','d4','d5']}, index=["r2","r3","r4"])

df_78=pd.concat([df_7,df_8])
print(df_78)
#      a   b   c   d
# r0  a0  b0  c0  d0
# r1  a1  b1  c1  d1
# r2  a2  b2  c2  d2
# r2  a3  b3  c3  d3
# r3  a4  b4  c4  d4
# r4  a5  b5  c5  d5

# verify_integrity= : 무결성(동일한 행 번호) 검증(False : 기본값,Ture)
df_78=pd.concat([df_7,df_8],verify_integrity=False)
print(df_78)
#      a   b   c   d
# r0  a0  b0  c0  d0
# r1  a1  b1  c1  d1
# r2  a2  b2  c2  d2
# r2  a3  b3  c3  d3
# r3  a4  b4  c4  d4
# r4  a5  b5  c5  d5

# df_78=pd.concat([df_7,df_8],verify_integrity=True)
# print(df_78)
# # ValueError: Indexes have overlapping values: Index(['r2'], dtype='object') : r2행이 겹침

##############여기까지 데이터프레임 합치기#######################################################

##############여기서 부터 데이터프레임 + 시리즈 합치기##############################################
# 자료구조  : 데이터프레임, 시리즈, 페널

df_1 = df({
    'a':['a0','a1','a2'],
'b':['b0','b1','b2'],
'c':['c0','c1','c2'],
'd':['d0','d1','d2']}, index=[0,1,2])

Series_1 = pd.Series(['S1','S2','S3'],name='S')
print(Series_1)
# 0    S1
# 1    S2
# 2    S3
# Name: S, dtype: object

print(pd.concat([df_1,Series_1]))
#      a    b    c    d    0
# 0   a0   b0   c0   d0  NaN
# 1   a1   b1   c1   d1  NaN
# 2   a2   b2   c2   d2  NaN
# 0  NaN  NaN  NaN  NaN   S1
# 1  NaN  NaN  NaN  NaN   S2
# 2  NaN  NaN  NaN  NaN   S3

print("="*50)

print(pd.concat(([df_1,Series_1]),axis=1))
#      a   b   c   d   S
# 0  a0  b0  c0  d0  S1
# 1  a1  b1  c1  d1  S2
# 2  a2  b2  c2  d2  S3
print(pd.concat(([df_1,Series_1]),axis=1))


print(pd.concat(([df_1,Series_1]),axis=1,ignore_index=True))
#     0   1   2   3   4
# 0  a0  b0  c0  d0  S1
# 1  a1  b1  c1  d1  S2
# 2  a2  b2  c2  d2  S3

#Series끼리 합치기
Series_1 = pd.Series(['S1','S2','S3'],name='S')
Series_2 = pd.Series([0,1,2])
Series_3 = pd.Series([3,4,5])
print(pd.concat([Series_1,Series_2,Series_3]))
# 0    S1
# 1    S2
# 2    S3
# 0     0
# 1     1
# 2     2
# 0     3
# 1     4
# 2     5
# dtype: object

print(pd.concat(([Series_1,Series_2,Series_3]), axis=1))
#     S  0  1
# 0  S1  0  3
# 1  S2  1  4
# 2  S3  2  5

print(pd.concat(([Series_1,Series_2,Series_3]), axis=1,keys=['C0','C1','C2']))
#    C0  C1  C2
# 0  S1   0   3
# 1  S2   1   4
# 2  S3   2   5

Series_4 = pd.Series(['S1','S2','S3','S4'],index=['a','b','c','d'])
print(Series_4)
# a    S1
# b    S2
# c    S3
# d    S4
# dtype: object

print(df_1.append(Series_4,ignore_index=True))
#     a   b   c   d
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
# 3  S1  S2  S3  S4


Series_4 = pd.Series(['S1','S2','S3','S4'],index=['a','b','c','e'])
print(Series_4)

print(df_1.append(Series_4,ignore_index=True))
#     a   b   c    d    e
# 0  a0  b0  c0   d0  NaN
# 1  a1  b1  c1   d1  NaN
# 2  a2  b2  c2   d2  NaN
# 3  S1  S2  S3  NaN   S4

#Dataframe Join/Merge. 데이터 병합
# Merge : 속도가 빠른편이라 많이 사용한다.

df_left = df({
    'KEY':['a0','a1','a2','a3'],
    'b':['b0','b1','b2','b3'],
    'c':['c0','c1','c2','c3']})
df_right = df({
    'KEY':['a2','a3','a4','a5'],
    'd':['d0','d1','d2','d3'],
    'e':['e0','e1','e2','e3']})
print(df_left)
#   KEY   b   c
# 0  a0  b0  c0
# 1  a1  b1  c1
# 2  a2  b2  c2
# 3  a3  b3  c3
print(df_right)
#   KEY   d   e
# 0  a2  d0  e0
# 1  a3  d1  e1
# 2  a4  d2  e2
# 3  a5  d3  e3

#key 값이 같은 값들끼리 병합(동일한 열을 기준으로 병합(기본값))
df_merge_how_left = pd.merge(df_left,df_right)
print(df_merge_how_left)
#   KEY   b   c   d   e
# 0  a2  b2  c2  d0  e0
# 1  a3  b3  c3  d1  e1

# how='left' : 왼쪽을 기준으로 오른쪽을 붙임
df_merge_how_left = pd.merge(df_left,df_right,how='left')
print(df_merge_how_left)
#   KEY   b   c    d    e
# 0  a0  b0  c0  NaN  NaN
# 1  a1  b1  c1  NaN  NaN
# 2  a2  b2  c2   d0   e0
# 3  a3  b3  c3   d1   e1

# on='KEY' :  'KEY'를 기준으로 합치기
df_merge_how_left = pd.merge(df_left,df_right,how='left',on='KEY')
print(df_merge_how_left)
#   KEY   b   c    d    e
# 0  a0  b0  c0  NaN  NaN
# 1  a1  b1  c1  NaN  NaN
# 2  a2  b2  c2   d0   e0
# 3  a3  b3  c3   d1   e1

# df_left = df({
#     'KEY':['a0','a1','a2','a3'],
#     'b':['b0','b1','b2','b3'],
#     'c':['c0','c1','c2','c3']})
# df_right = df({
#     'KEY1':['a2','a3','a4','a5'],
#     'd':['d0','d1','d2','d3'],
#     'e':['e0','e1','e2','e3']})
#
# df_merge_how_left = pd.merge(df_left,df_right)
# print(df_merge_how_left)
# # pandas.errors.MergeError: No common columns to perform merge on. Merge options: left_on=None, right_on=None, left_index=False
### 동일한 키값이 있을 때만 merge 작업을 할 수 있다.

# # 동일한 키 값이 2개 이상 존재할 때 기준 키값을 제외하고는 동일한 키의 이름이 달라진다.
# df_left = df({
#     'KEY':['a0','a1','a2','a3'],
#     'd':['b0','b1','b2','b3'],
#     'c':['c0','c1','c2','c3']})
# df_right = df({
#     'KEY':['a2','a3','a4','a5'],
#     'd':['d0','d1','d2','d3'],
#     'e':['e0','e1','e2','e3']})
#
# df_merge_how_left = pd.merge(df_left,df_right,how='left',on='KEY')
# print(df_merge_how_left)
# #   KEY d_x   c  d_y    e
# # 0  a0  b0  c0  NaN  NaN
# # 1  a1  b1  c1  NaN  NaN
# # 2  a2  b2  c2   d0   e0
# # 3  a3  b3  c3   d1   e1


#how='right' : 오른쪽을 기준으로 병합
df_merge_how_left = pd.merge(df_left,df_right,how='right',on='KEY')
print(df_merge_how_left)
#   KEY    b    c   d   e
# 0  a2   b2   c2  d0  e0
# 1  a3   b3   c3  d1  e1
# 2  a4  NaN  NaN  d2  e2
# 3  a5  NaN  NaN  d3  e3

# how='inner' :  키를 기준으로 교집합(KEY=a2,a3)을 구함
df_merge_how_left = pd.merge(df_left,df_right,how='inner',on='KEY')
print(df_merge_how_left)
#   KEY   b   c   d   e
# 0  a2  b2  c2  d0  e0
# 1  a3  b3  c3  d1  e1

# how='outer' :  키를 기준으로 합집합(KEY=a0,a1a2,a3,a4,a5)을 구함
df_merge_how_left = pd.merge(df_left,df_right,how='outer',on='KEY')
print(df_merge_how_left)
#   KEY    b    c    d    e
# 0  a0   b0   c0  NaN  NaN
# 1  a1   b1   c1  NaN  NaN
# 2  a2   b2   c2   d0   e0
# 3  a3   b3   c3   d1   e1
# 4  a4  NaN  NaN   d2   e2
# 5  a5  NaN  NaN   d3   e3

# indicator=True : 데이터가 어디의 데이터프레임에 있었는지 나타냄
df_merge_how_left = pd.merge(df_left,df_right,how='outer',on='KEY',indicator=True)
print(df_merge_how_left)
#   KEY    b    c    d    e      _merge
# 0  a0   b0   c0  NaN  NaN   left_only
# 1  a1   b1   c1  NaN  NaN   left_only
# 2  a2   b2   c2   d0   e0        both
# 3  a3   b3   c3   d1   e1        both
# 4  a4  NaN  NaN   d2   e2  right_only
# 5  a5  NaN  NaN   d3   e3  right_only

df_left = df({
    'KEY':['a0','a1','a2','a3'],
    'a':['b0','b1','b2','b3'],
    'd':['b0','b1','b2','b3'],
    'c':['c0','c1','c2','c3']})
df_right = df({
    'KEY':['a2','a3','a4','a5'],
    'b':['d0','d1','d2','d3'],
    'c':['d0','d1','d2','d3'],
    'd':['e0','e1','e2','e3']})

print(pd.merge(df_left,df_right,how="inner",on="KEY",suffixes=('_left','_right')))
#     KEY   a d_left c_left   b c_right d_right
# 0  a2  b2     b2     c2  d0      d0      e0
# 1  a3  b3     b3     c3  d1      d1      e1

print('-_-_'*50)

df_left = df({
    'a':['a0','a1','a2','a3'],
    'b':['b0','b1','b2','b3']},
    index = ['k0','k1','k2','k3'])
df_right = df({
    'c':['c0','c1','c2','c3'],
    'd':['e0','e1','e2','e3']},
    index= ['k2','k3','k4','k5'])
#인덱스 기준으로 데이터프레임 합치는 작업 : pd.merge(), join()
print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='left'))
#      a   b    c    d
# k0  a0  b0  NaN  NaN
# k1  a1  b1  NaN  NaN
# k2  a2  b2   c0   e0
# k3  a3  b3   c1   e1

print(df_left.join(df_right,how='left'))
#      a   b    c    d
# k0  a0  b0  NaN  NaN
# k1  a1  b1  NaN  NaN
# k2  a2  b2   c0   e0
# k3  a3  b3   c1   e1

print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='right'))
#       a    b   c   d
# k2   a2   b2  c0  e0
# k3   a3   b3  c1  e1
# k4  NaN  NaN  c2  e2
# k5  NaN  NaN  c3  e3

print(df_left.join(df_right,how='right'))
#       a    b   c   d
# k2   a2   b2  c0  e0
# k3   a3   b3  c1  e1
# k4  NaN  NaN  c2  e2
# k5  NaN  NaN  c3  e3

print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='inner'))
#      a   b   c   d
# k2  a2  b2  c0  e0
# k3  a3  b3  c1  e1

print(df_left.join(df_right,how='inner'))
#      a   b   c   d
# k2  a2  b2  c0  e0
# k3  a3  b3  c1  e1

print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='outer'))
#       a    b    c    d
# k0   a0   b0  NaN  NaN
# k1   a1   b1  NaN  NaN
# k2   a2   b2   c0   e0
# k3   a3   b3   c1   e1
# k4  NaN  NaN   c2   e2
# k5  NaN  NaN   c3   e3

print(df_left.join(df_right,how='outer'))
#       a    b    c    d
# k0   a0   b0  NaN  NaN
# k1   a1   b1  NaN  NaN
# k2   a2   b2   c0   e0
# k3   a3   b3   c1   e1
# k4  NaN  NaN   c2   e2
# k5  NaN  NaN   c3   e3







































































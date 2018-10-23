#여러개의 데이터프레임들을 합쳐서 한개의 데이터프레임으로 만들기
#데이터의 합치(같은 관측치)는 기준 :  관측치로 합친다.(concat)

import pandas as pd
import numpy as np
from pandas import DataFrame as df

df_1 = df({
    'a':['a0','a1','a2'],
'b':['b0','b1','b2'],
'c':['c0','c1','c2'],
'd':['d0','d1','d2']}, index=[0,1,2])
df_2 = df({
    'a':['a3','a4','a5'],
'b':['b3','b4','b5'],
'c':['c3','c4','c5'],
'd':['d3','d4','d5']}, index=[3,4,5])

print(df_1)
#     a   b   c   d
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
print(df_2)
#     a   b   c   d
# 3  a3  b3  c3  d3
# 4  a4  b4  c4  d4
# 5  a5  b5  c5  d5

df_12_axis0=pd.concat([df_1,df_2],axis=0)                   # axis= : 0이 기본값 0=행기준 합치기
print(df_12_axis0)
#     a   b   c   d
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
# 3  a3  b3  c3  d3
# 4  a4  b4  c4  d4
# 5  a5  b5  c5  d5


df_3 = df({
    'e':['e0','e1','e2'],
'f':['f0','f1','f2'],
'g':['g0','g1','g2'],
'h':['h0','h1','h2']}, index=[0,1,2])


df_13_axis1=pd.concat([df_1,df_3],axis=1)
print(df_13_axis1)
#     a   b   c   d   e   f   g   h
# 0  a0  b0  c0  d0  e0  f0  g0  h0
# 1  a1  b1  c1  d1  e1  f1  g1  h1
# 2  a2  b2  c2  d2  e2  f2  g2  h2

df_4 = df({
    'a':['a0','a1','a2'],
'b':['b0','b1','b2'],
'c':['c0','c1','c2'],
'e':['e0','e1','e2']}, index=[0,1,3])
#df_1과 df_4를 outer_join(외부조인) 수행

print("="*50)
print(df_1)
#     a   b   c   d
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
print("="*50)
print(df_4)
#     a   b   c   e
# 0  a0  b0  c0  e0
# 1  a1  b1  c1  e1
# 3  a2  b2  c2  e2

print("="*50)
#join='outer' :두 데이터프레임의 컬럼에 대한 합집합의 의미
df_14_outer = pd.concat([df_1,df_4],join='outer')
print(df_14_outer)
#     a   b   c    d    e
# 0  a0  b0  c0   d0  NaN
# 1  a1  b1  c1   d1  NaN
# 2  a2  b2  c2   d2  NaN
# 0  a0  b0  c0  NaN   e0
# 1  a1  b1  c1  NaN   e1
# 3  a2  b2  c2  NaN   e2

print("="*50)
#join='inner' :두 데이터프레임의 컬럼에 대한 교집합의 의미
df_14_inner = pd.concat([df_1,df_4],join='inner')
print(df_14_inner)
#     a   b   c
# 0  a0  b0  c0
# 1  a1  b1  c1
# 2  a2  b2  c2
# 0  a0  b0  c0
# 1  a1  b1  c1
# 3  a2  b2  c2

#axis = 1, index를 그대로 사용할 때  : join_axes
print("="*50)
print(df_1)
print(df_4)

df_14_outer_axis1 = pd.concat([df_1,df_4],join='outer',axis=1)
print(df_14_outer_axis1)
#      a    b    c    d    a    b    c    e
# 0   a0   b0   c0   d0   a0   b0   c0   e0
# 1   a1   b1   c1   d1   a1   b1   c1   e1
# 2   a2   b2   c2   d2  NaN  NaN  NaN  NaN
# 3  NaN  NaN  NaN  NaN   a2   b2   c2   e2

df_14_inner_axis1 = pd.concat([df_1,df_4],join='inner',axis=1)
print(df_14_inner_axis1)
#     a   b   c   d   a   b   c   e
# 0  a0  b0  c0  d0  a0  b0  c0  e0
# 1  a1  b1  c1  d1  a1  b1  c1  e1

# join_axes=[df_1.index] : df_1.index를 기준으로 합쳐짐
df_14_join_axes_axis1 = pd.concat([df_1,df_4],join_axes=[df_1.index],axis=1)
print(df_14_join_axes_axis1)
#     a   b   c   d    a    b    c    e
# 0  a0  b0  c0  d0   a0   b0   c0   e0
# 1  a1  b1  c1  d1   a1   b1   c1   e1
# 2  a2  b2  c2  d2  NaN  NaN  NaN  NaN
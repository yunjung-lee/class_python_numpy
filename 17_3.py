import pandas as pd
import numpy as np
from pandas import DataFrame , Series
import datetime
from datetime import datetime

#결측값을 갖고 있는 행이나 열 전체를 제거

df = DataFrame(np.random.randn(5,4),columns=['c1','c2','c3','c4'])
print(df)
df.ix[2,'c2']=np.nan
df.ix[[0,1],'c1']=np.nan

print(df)
#          c1        c2        c3        c4
# 0       NaN  1.188608  1.592305  0.197392
# 1       NaN  1.710974 -1.290963  1.308893
# 2 -0.693920       NaN -0.304018  0.562946
# 3 -0.200167  0.900530  0.516246 -0.067986
# 4 -0.807780  0.094278 -0.207367  0.070497

#dropna() : 줄 전체 제거 (axis= 0:행 , 1 : 열)
df_drop_row = df.dropna(axis=0)
print(df_drop_row)
#          c1        c2        c3        c4
# 3 -0.120495  0.721763 -2.585237  0.570430
# 4  0.355886  1.039329 -0.537244  0.611651

df_drop_row = df.dropna(axis=1)
print(df_drop_row)
#          c3        c4
# 0 -0.060127 -0.668219
# 1 -0.484853 -1.004333
# 2  0.592989  0.252000
# 3 -0.396224 -0.611459
# 4  0.580234  0.450050

print(df['c1'].dropna())                            #c1열에서 결측치를 제거한 나머지 자료
# 2   -0.633699
# 3   -0.096051
# 4   -0.359511
# Name: c1, dtype: float64

print(df[['c1','c2','c3']].dropna(axis=0))                #결측치가 있는 행(0,1,2)들은 모두 삭제
#          c1        c2        c3
# 3 -0.876961  0.306564  2.257250
# 4  0.399126  1.516620  1.142257

print(df[['c1','c2','c3']].dropna(axis=1))               #결측치가 있는 열(c1,c2)들은 모두 삭제
#          c3
# 0  0.135507
# 1  1.138836
# 2 -0.986941
# 3  0.855425
# 4  0.870875

print(df.ix[[2,4],['c1','c2','c3']].dropna(axis=0))
#          c1        c2        c3
# 4  0.796496  1.723393 -0.521022


#보간 : 실측값 사이에 nan이 섞여있으면 결측지 값을 실제 값들 의 간격에 의거하여 채워 넣는 방법
#자주 사용하는 방법은 아니다

# '11/9/2018':문자형식 중 날짜형식
datestrs = ['9/11/2018','9/12/2018','9/13/2018','9/14/2018']
dates = pd.to_datetime(datestrs)
print(dates)
# DatetimeIndex(['2018-11-09', '2018-12-09', '2018-09-13', '2018-09-14'], dtype='datetime64[ns]', freq=None)

ts = Series([1,np.nan,np.nan,10],index=dates)                    #Series의 행번호를 날짜의 리스트를 인덱스로 시리즈를 만든다.
print(ts)
# 2018-09-11     1.0
# 2018-09-12     NaN
# 2018-09-13     NaN
# 2018-09-14    10.0
# dtype: float64

#interpolate() : 선형적으로 비례하여 결측값을 보간
ts_ite_linear = ts.interpolate()
print(ts_ite_linear)
# 2018-09-11     1.0
# 2018-09-12     4.0
# 2018-09-13     7.0
# 2018-09-14    10.0
# dtype: float64

datestrs = ['9/11/2018','9/13/2018','9/14/2018','9/20/2018']
dates = pd.to_datetime(datestrs)
print(dates)
# DatetimeIndex(['2018-09-11', '2018-09-13', '2018-09-14', '2018-09-20'], dtype='datetime64[ns]', freq=None)

ts_ite_linear = ts.interpolate(method='time')
print(ts_ite_linear)
# 2018-09-11     1.0
# 2018-09-12     4.0
# 2018-09-13     7.0
# 2018-09-14    10.0
# dtype: float64

df = DataFrame({'c1':[1,np.nan,np.nan,10],
                'c2': [1,3,np.nan,10]})

df_v = df.interpolate(method='values')
print(df_v)
#      c1    c2
# 0   1.0   1.0
# 1   4.0   3.0
# 2   7.0   6.5
# 3  10.0  10.0

# fillna :  결측값을 다른값으로 대체=> 결측값만 처리
# replace :  결측값을 대체 => 모든 값을 대체 가능

ser = Series([1,2,3,4,np.nan])
print(ser)
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    NaN
# dtype: float64

# #replace(대치받을 값, 대치 할 값)
# ser = ser.replace(2,20)
# print(ser)
# # 0     1.0
# # 1    20.0
# # 2     3.0
# # 3     4.0
# # 4     NaN
# # dtype: float64
# ser = ser.replace(np.nan,5)
# print(ser)
# # 0     1.0
# # 1    20.0
# # 2     3.0
# # 3     4.0
# # 4     5.0
# # dtype: float64

print(ser.replace([1,2,3,4,np.nan],[6,7,8,9,10]))
# 0     6.0
# 1     7.0
# 2     8.0
# 3     9.0
# 4    10.0
# dtype: float64

print(ser.replace({1:6,2:8,3:9,4:7,np.nan:10}))                     # 딕셔너리 구조 활용 가능{변경 이전값 : 변경 이후 값}
# 0     6.0
# 1     8.0
# 2     9.0
# 3     7.0
# 4    10.0
# dtype: float64

df =DataFrame({'c1':['a_old','b','c','d','e'],'c2' : [1,2,3,4,5,],'c3':[6,7,8,9,np.nan]})
print(df)
#       c1  c2   c3
# 0  a_old   1  6.0
# 1      b   2  7.0
# 2      c   3  8.0
# 3      d   4  9.0
# 4      e   5  NaN

print(df.replace({'c1':'a_old'},{'c1':'a_new'}))
#       c1  c2   c3
# 0  a_new   1  6.0
# 1      b   2  7.0
# 2      c   3  8.0
# 3      d   4  9.0
# 4      e   5  NaN

print(df.replace({'c3':np.nan},{'c3':10}))
#       c1  c2    c3
# 0  a_old   1   6.0
# 1      b   2   7.0
# 2      c   3   8.0
# 3      d   4   9.0
# 4      e   5  10.0


# key1처럼 중복이 되는 데이터가 있다. 중복을 찾는 함수가 있다.=>key1&key2가 같이 중복체크를 하면 2행만 중복이다.
data={'key1':['a','b','b','c','c'],'key2':['x','w','w','x','y'],'col':[1,2,3,4,5]}
df = pd.DataFrame(data)
print(df)
#  key1 key2  col
# 0    a    x    1
# 1    b    w    2
# 2    b    w    3
# 3    c    x    4
# 4    c    y    5


#duplicated(['key1']) : key1에 대한 중복 확인, keep= : first가 기본값,false : 중복이 있음 모두 True
print(df.duplicated(['key1'],keep=False))
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# dtype: bool

#duplicated(['key1','key2']) : 두개 모두 중복 인것 찾는 다.
print(df.duplicated(['key1','key2']))
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# dtype: bool

#1개만 남기고 나무지 중복은 제거
print("="*50)
print(df)
# drop_duplicates(['key1']) :  key1을 기준으로 중복된 하위값의 행(keep='first': 기본값) 삭제하여 하나만 남기는 함수
print(df.drop_duplicates(['key1'],keep='first'))
#   key1 key2  col
# 0    a    x    1
# 1    b    w    2
# 3    c    x    4

# drop_duplicates(['key1'],keep='last') :  key1을 기준으로 중복된 상위 값의 행 삭제
print(df.drop_duplicates(['key1'],keep='last'))
#   key1 key2  col
# 0    a    x    1
# 2    b    w    3
# 4    c    y    5

# df.drop_duplicates(['key1'],keep=False) : key1을 기준으로 중복된 모든 값의 행 삭제
print(df.drop_duplicates(['key1'],keep=False))
#   key1 key2  col
# 0    a    x    1































































































#결측치 처리 연습 & 데이터프레임 사용

from pandas import DataFrame,Series
import pandas as pd
#pd.DataFrame()                      #pandas 안의 DataFrame이기 때문에 앞에 pd로 from없이도 진행할 수 있다.
import numpy as np
#print(np.random.randn(5,3))         #5행3열의 난수 발생
#표준정규분포, 평균(기댓값) : 0 , 표준편차 :1   => 난수를 발생하라는 의미
#표준정규분포 : 종모양의 분포도를 갖는 자료
df=pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
#print(df)
#print(type(df))                     #DataFrame에서만 사용할 수 있는 함수가 있기 때문에 그 함수를 사용하려면 확인이 필요하다.
#print(type(df['W']))                 #pandas.core.series.Series :  표를 구성하는 열이나 행은 Series

# print(df.drop('E'))                  #E행렬을 제외한 나머지를 프린트=> 자료가 바뀐건 아니다.
# df=df.drop('E')                    #E행렬을 제외 함 =>자료가 바뀜
# print(df)

# print(df.shape)
# print(df.loc['A'])                      #loc : 행만 추출,열 추출 불가
# print(df.iloc[0])                      #iloc : i=index
# print(df.loc[['A','B']])                #여러 행을 참조할때 []*len(참조행)
# print(df.loc[['A','B'],['X','Y']])

d={'A' : [1,2,np.nan],'B' : [5,np.nan,np.nan],'C' : [1,2,3]}            #nan(not a number) :  np의 형식
# print(d)

df=pd.DataFrame(d)
# print(df)
# print(type(df))
#
# print(df.dropna())                          #nan 이 있는 행이 출력 삭제
# print(df.dropna(axis=1))                    #axis=0(행),1(열) 출력 삭제
# print(df.dropna(thresh=1))
# #      A    B  C
# # 0  1.0  5.0  1
# # 1  2.0  NaN  2
# # 2  NaN  NaN  3
# print(df.dropna(thresh=2))
# #      A    B  C
# # 0  1.0  5.0  1
# # 1  2.0  NaN  2
# print(df.dropna(thresh=3))
# #      A    B  C
# # 0  1.0  5.0  1

# print(df['A'].fillna(value="imsi"))
# # 0       1
# # 1       2
# # 2    imsi
# # Name: A, dtype: object
# print(df.fillna(value="imsi"))
# #       A     B  C
# # 0     1     5  1
# # 1     2  imsi  2
# # 2  imsi  imsi  3
#
#
print(df)
#A열에 대해서 na값을 A열의 평균으로 대체
print(df['A'].mean())
print(df['A'].fillna(value=(df['A'].mean())))







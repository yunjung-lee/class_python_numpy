import numpy as np
import pandas as pd
from pandas import DataFrame as df
from pandas import Series as ser

# 1. 두 개의 데이터프레임을 만들고 merge 명령으로 합친다. 단 데이터프레임은 다음 조건을 만족해야 한다.
# 1.각각 5 x 5 이상의 크기를 가진다.
# 2.공통 열을 하나 이상 가진다. 다만 공통 열의 이름은 서로 다르다.

df_1 = df({'a1':np.arange(7),
           'a2' :np.random.randn(7),
           'a3': np.random.randn(7),
           'a4': np.random.randn(7),
           'a5': np.random.randn(7),
           'a6': np.random.randn(7)},index=['a','b','c','d','e','f','g'])

df_2 = df({'b1':np.arange(7),
           'b2' :np.random.randn(7),
           'b3': np.random.randn(7),
           'b4': np.random.randn(7),
           'b5': np.random.randn(7),
           'b6': np.random.randn(7)},index=['a','b','c','d','e','f','g'])
df_fin = pd.merge(df_1,df_2,left_index=True,right_index=True)

# print(df_fin)

# 2.어느 회사의 전반기(1월 ~ 6월) 실적을 나타내는 데이터프레임과 후반기(7월 ~ 12월) 실적을 나타내는 데이터프레임을 만든 뒤 합친다.
# 실적 정보는 "매출", "비용", "이익" 으로 이루어진다. (이익 = 매출 - 비용).
#
# 또한 1년간의 총 실적을 마지막 행으로 덧붙인다.
A1 = df({'1월':[20,10],
         '2월': [29, 19],
         '3월': [22, 12],
         '4월': [25, 15],
         '5월': [26, 16],
         '6월': [21, 9],},index=['매출','비용'])

A2 = df({'7월':[18,10],
         '8월': [29, 15],
         '9월': [20, 12],
         '10월': [25, 17],
         '11월': [24, 16],
         '12월': [22, 9],},index=['매출','비용'])

A=pd.concat([A1,A2],axis=1)
A=np.transpose(A)
A['이익'] = A['매출']-A['비용']
A=np.transpose(A)
A['total']=np.sum(A,axis=1)

print(A)

# 3. 다음 행렬과 같은 배열이 있다.
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#               11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# 1.이 배열에서 3의 배수를 찾아라.
# 2.이 배열에서 4로 나누면 1이 남는 수를 찾아라.
# 3.이 배열에서 3으로 나누면 나누어지고 4로 나누면 1이 남는 수를 찾아라.

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
v_3=x%3==0
x_3=x[v_3]

v_4=x%4==1
x_4=x[v_4]


x_m=np.append(x_3,x_4)
x_m=np.sort(x_m)
print(x_m)


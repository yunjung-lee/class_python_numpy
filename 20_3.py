#####차원 축소#######################
#ex) 벡터의 연산=>스칼라


import pandas as pd
import numpy as np
from pandas import DataFrame, Series

x=np.arange(12).reshape(3,4)
print(x)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# np.ravel() : 다차원 배열 -> 1차원 배열
print(np.ravel(x))                                          # np.ravel()  : 병합하여 차원을 축소
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(np.ravel(x,order="C"))                                # order="C" : 컬럼 방향 default
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(np.ravel(x,order="F"))                                # order="F" : 행 방향
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

print(np.ravel(x,order="K"))                                # order="K" : 메모리 저장 순서,거의 사용 안한다.
# [ 0  1  2  3  4  5  6  7  8  9 10 11]


y=np.arange(12).reshape(2,3,2)
print(y)
# [[[ 0  1]
#   [ 2  3]
#   [ 4  5]]
#
#  [[ 6  7]
#   [ 8  9]
#   [10 11]]]

print(np.ravel(y,order="C"))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]


import matplotlib.pyplot as plt

# plt.plot([1,2,3,4])                             # y좌표를 입력한 것임 : x좌표는 지정하지 않으면 자연적으로 순서번호로 입력
# plt.ylabel('sample number')
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.ylabel('sample number')
# plt.show()

data={'a':np.arange(50),
      'c': np.random.randint(0,50,50),
      'd': np.random.rand(50)}
data['b']=data['a']+10*np.random.randn(50)          #dict에 추가
data['d']=np.abs(data['d'])*100
print(data)

# plt.scatter('a','b',c='b',s='d',data=data)                # c=:  색상 지정 color(c), s= : 크기 size(s)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()                                          #  마지막 plt.show() 다음 설정을 모두 한 화면에 보여줌

mu, sigma =100,15                                   #평균이 100, 표준편차가 15
x=mu+sigma*np.random.randn(10000)                   #평균이 100, 표준편차가 15인 난수 10000발생 =>100을 중심으로 종모양의 히스토그램을 그려준다.
n, bins,patches = plt.hist(x,bins=50,density=1)     # density=1 : 확률 밀도 함수
print('n=',n)
print('bins=',bins)
print('patches=',patches)
plt.title('histogram')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()




































































































































































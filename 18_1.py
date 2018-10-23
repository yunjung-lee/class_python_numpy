import numpy as np
import pandas as pd
from pandas import DataFrame , Series
import matplotlib.pyplot as plt


#데이터의 중복처리
# a a a b b c c => a b c : unique()함수 : pandas.Series
#  a a a b b c c => a-3 b-2 c-2 : value_count()함수
#bins= : 구간을 설정하여 구간에 얼마나 들어가 있는지 확인하는 함수, 거의 사용되지 않는 속성
        # 시각화의 막대그래프에서 구간 설정에 많이 쓰임

df = DataFrame({'a':['a1','a1','a2','a2','a3','a3'],
            'b':['b1','b1','b1','b1','b2',np.nan],
           'c':[1,1,3,4,4,4,]})

print(df['a'].unique())                 #중복 제외하고 출력
# ['a1' 'a2' 'a3']
print(df['b'].unique())
# ['b1' 'b2' nan]
print(df['c'].unique())
# [1 3 4]

print(df['a'].value_counts())           # 중복된 개수를 확인
# a1    2
# a2    2
# a3    2
# Name: a, dtype: int64
print(df['b'].value_counts())
# b1    4
# b2    1
# Name: b, dtype: int64
print(df['c'].value_counts())
# 4    3
# 1    2
# 3    1
# Name: c, dtype: int64


print(df['c'].value_counts(normalize=True))             # normalize=True : 중복된 비율을 확인
# 4    0.500000
# 1    0.333333
# 3    0.166667
# Name: c, dtype: float64

print(df['c'].value_counts(sort=True,ascending=False))       # sort=True,ascending=False : 내림차순 정렬(기본값)_
# 4    3
# 1    2
# 3    1
# Name: c, dtype: int64

print(df['c'].value_counts(sort=True,ascending=True))
# 3    1
# 1    2
# 4    3
# Name: c, dtype: int64

print(df['c'].value_counts(sort=False))                 #정렬을 안함 : ascending=이 필요치 않음
# 1    2
# 3    1
# 4    3
# Name: c, dtype: int64

print(df['b'].value_counts())                           #nan :  나오지 않음
# print(df['b'].value_counts(dropna = True))            # 기본값 :  위의 결과와 같음
print(df['b'].value_counts(dropna=False))
# b1     4
# b2     1
# NaN    1
# Name: b, dtype: int64

print(df['c'].value_counts(bins=[0,1,2,3,4,5],sort=False))
# (-0.001, 1.0]    2        #-0.001 을 포함하지 않기 때문에 0부터라고 보면 된다.
# (1.0, 2.0]       0
# (2.0, 3.0]       1
# (3.0, 4.0]       3
# (4.0, 5.0]       0
# Name: c, dtype: int64


####################################표준 정규분포 : 데이터의 표준화#######################################################################

# 표준화(scaling) : 변수들간의 scale(척도)이 서로 다른 경우, 직접적인 상호간의 비교를 할 수 없음.
# 기계학습을 하고 모델링을 만드는 과정에서 문제가 발생, 만들더라도 모델의 정확한 예측을 기대하기 힘듬.

# 모델링 하기 앞서 변수들 간의 척도가 다른 경우 => 표준화
# 모집단이 정규분포를 따를 경우 : 좌우대칭되는 분포도를 갖는다.
# 표준화 방법 : 평균 : 0, 표준편차 : 1인 표준정규분포로 표준화 ==> 가장 많이 사용되는 표준화
# 표준화 = (x-mean())/std()
# 정규화 = (x-min )/(max-min)
# 정규화의 범위=> 0=<정규화=<1
# 신경망(머신 러닝)의 모델을 만들 때 데이터들이 큰 편차를 갖으면 변수들 업데이트과정에서 비정상적인 값으로 유도되어질 수 있다.
# 표준화 작업 :  표준화, 정규화 , scipy.stats사용 , from sklearn.preprocessing import StandardScaler 사용 등등.






from numpy import *

np.random.seed(777)
data = np.random.randint(30, size = (6,5))
print(data)
# [[ 7 15 27  6 23]
#  [17  7 29 20  7]
#  [25 14 26 24  7]
#  [18 13 14  0 27]
#  [ 1 18 20  5  7]
#  [ 1 27  7 10 18]]

#numpy의 mean & std 를 이용해서 표준화(정규분포)
print((data - mean(data,axis=0))/std(data,axis=0))                 #axis= 0:column, 1: 행 단위로 평균
# [[-0.49518366 -0.11026357  0.82828875 -0.56906519  0.98934396]
#  [ 0.60522448 -1.4334264   1.08314682  1.07926157 -0.94896257]
#  [ 1.48555099 -0.27565892  0.70085971  1.55021208 -0.94896257]
#  [ 0.71526529 -0.44105428 -0.82828875 -1.27549095  1.47392059]
#  [-1.15542855  0.38592249 -0.06371452 -0.68680282 -0.94896257]
#  [-1.15542855  1.87448068 -1.72029201 -0.09811469  0.38362317]]

# numpy의 mean & std 를 이용한 정규화


import scipy.stats as ss

data_standadized_ss=ss.zscore(data)
print(data_standadized_ss)
# [[-0.49518366 -0.11026357  0.82828875 -0.56906519  0.98934396]
#  [ 0.60522448 -1.4334264   1.08314682  1.07926157 -0.94896257]
#  [ 1.48555099 -0.27565892  0.70085971  1.55021208 -0.94896257]
#  [ 0.71526529 -0.44105428 -0.82828875 -1.27549095  1.47392059]
#  [-1.15542855  0.38592249 -0.06371452 -0.68680282 -0.94896257]
#  [-1.15542855  1.87448068 -1.72029201 -0.09811469  0.38362317]]
from sklearn.preprocessing import StandardScaler
ds = StandardScaler().fit_transform(data)
print(ds)
# [[-0.49518366 -0.11026357  0.82828875 -0.56906519  0.98934396]
#  [ 0.60522448 -1.4334264   1.08314682  1.07926157 -0.94896257]
#  [ 1.48555099 -0.27565892  0.70085971  1.55021208 -0.94896257]
#  [ 0.71526529 -0.44105428 -0.82828875 -1.27549095  1.47392059]
#  [-1.15542855  0.38592249 -0.06371452 -0.68680282 -0.94896257]
#  [-1.15542855  1.87448068 -1.72029201 -0.09811469  0.38362317]]


# X~N(0,1) 표준화
# 조건 : 정규분포를 따름, 이상치(특이값, outlier)가 없음
# z=(x-mean)/std : 이중 이상치가 평균(mean)에 영향을 많이 받음
# 이상치의 영향을 피하는 방법 : 평균값 대신 중앙값 사용, IQR(InterQuantileRange) -3사분위수(75%)-1사분위(25%)- 을 이용함
# 이상치가 섞여있는 데이터를 표준화 하는 방법
# 1. 이상치를 제거한 후 표준화 수행 ->분석, 모델링
# 2. 중앙값, IQR값을 사용해서 표준화

from sklearn.preprocessing import StandardScaler, RobustScaler

np.random.seed(777)
mu,sigma = 10,2                                                      #변수 초기화
x = mu+sigma*np.random.randn(100)
print(x)
# [ 9.06358241  8.35435029  9.8692398   8.57327615 11.81270177 11.53247346
#  11.65210814  7.35263443  6.49511095 12.00489814 11.08961891 13.79032181
#   8.46128509  7.19380816  8.73506499  8.88225266  7.53353723  9.12099296
#  11.82957452 10.53008186  7.2332597  11.37102361 10.91218183  9.07725147
#  10.18940061  6.91437679 14.9587392  10.91373352  9.37225444 10.04207476
#  11.92158632 10.11696579  9.10793566 10.63839428 11.68233725  6.93447601
#   9.43683148 13.48890542  8.65152218 11.17680246 13.60872693 14.11250052
#  12.90916337  9.72317662 10.68574377  8.54476304  7.1921078   7.51877762
#   9.11303567  9.90534968 11.51536872  9.69582815  9.45744199  8.80032005
#   5.94619175 10.66068481  9.338338    9.93011567 10.57949608  8.7874601
#   9.46319145 12.38295504 10.31522662 12.34964951 12.64182004  8.30392543
#  11.49141479  9.3767574   7.89786923  7.84700635 10.90121931 10.81748164
#   7.14091696 12.03485442  9.83645853  9.23216313  9.52354965 10.01757724
#  11.04093677 10.80740904  9.19643565  8.60550947 11.29196545  9.44893372
#   9.24157942 13.93607003 10.40499388 10.74539455 11.96269195 11.47292464
#  12.82260161  9.74696455 11.10631468  8.36892803 11.07740504  5.56441007
#   8.18741563  7.07575024  8.64487024 13.04560761]

# plt.hist(x)
# plt.show()

print(np.mean(x))
# 10.014107058424933
print(np.std(x))
# 1.9171489776981916

x[98:100] = 100                                              # x[98:100] : 가장 끝 2개
print(x)

print(np.mean(x))
# 11.79720227993895
print(np.std(x))
# 12.741059695068776

# plt.hist(x, bins=np.arange(0,102,2))
# plt.show()


# reshape 의 음수(-1)을 넣으면 나머지 숫자에 비례하여 자동 계산 :  나머지가 생기는 숫자는 에러
print(x.shape)
# (100,)
x=x.reshape(50,2)
print(x.shape)
# (50, 2)
x=x.reshape(-1,1)
print(x.shape)
# (100, 1)
x=x.reshape(-1,2)
print(x.shape)
# (50, 2)
x=x.reshape(-1,4)
print(x.shape)
# (25, 4)

x=x.reshape(-1,1)
print(x.shape)
print(x[0:10])                                          #2차원
# [[ 9.06358241]
#  [ 8.35435029]
#  [ 9.8692398 ]
#  [ 8.57327615]
#  [11.81270177]
#  [11.53247346]
#  [11.65210814]
#  [ 7.35263443]
#  [ 6.49511095]
#  [12.00489814]]


xss = StandardScaler().fit_transform(x)
print(xss)

# 이상치 제거(표준화 5이상이면 이상치로 취급해 없애도 된다.)
xss_in = xss[xss<5]
print(xss_in)

plt.hist(xss_in, bins=np.arange(-3.0,3.0,0.2))              # 표준화 과정에서 이상치가 영향을 미침
# plt.show()

print(median(x))                                              # 중앙값
# 9.917732674869148
print(mean(x))                                                #평균
# 11.79720227993895
# 중앙값 < 평균 : 중앙값을 기준으로 좌측보다 우측의 편차가 더 크다.
print(percentile(x, 25, axis=0))                                #1사분위수
# [8.77436132]
print(percentile(x, 75, axis=0))                                #3사분위수
# [11.39649887]
Q1 = percentile(x, 25, axis=0)                                # 1사분위수
Q3 = percentile(x, 75, axis=0)                                # 3사분위수
IQR = Q3-Q1
print(IQR)
# [2.62213754]


#이상치가 포함된 데이터의 중앙값과 iqr을 이용해서 표준화 : RobustScaler()=> 중앙값(중위수) 이용
x_rs = RobustScaler().fit_transform(x)
print(x_rs[-10:])
# [[ 1.10782477]
#  [-0.06512554]
#  [ 0.45328744]
#  [-0.59066491]
#  [ 0.44226222]
#  [-1.66021901]
#  [-0.65988798]
#  [-1.08384186]
#  [34.35451645]
#  [34.35451645]]
print(np.median(x_rs))
# 0.0
print(np.mean(x_rs))
# 0.7167700301529704
print(np.std(x_rs))
# 4.859035611526193

x_rs_in =x_rs[x_rs<5]
plt.hist(x_rs_in, np.arange(-3.0,3.0,0.2))
plt.show()

# 이상치가 평균에 영향을 미치기 때문에 평균값 보다 중위수를 사용하면 이상치의 영향을 덜 받기 때문에 표준화 작업에 더 유용하다
# StandardScaler() : 평균을 사용하여 표준화
# RobustScaler() :  중앙값,IQR을 사용하여 표준화
# StandardScaler()보다 RobustScaler()가 이상값이 있는 데이터의  표준화에 더 유용한 함수이다.
################정규분포 형태의 데이터의 표준화#######################################













###########################정규화###########################################33
# 정규화 : 최대값과 최소값을 이용하여 0~1 사이의 값을 갖는다.
# 머신러닝(인공신경망)에서 아주 많이 사용하는 함수

import numpy as np
import pandas as pd
import sklearn.preprocessing

from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler,minmax_scale, Binarizer, binarize

X =np.array(([[10.,-10.,1.],
              [5.,0.,2.],
              [0.,10.,3]]))

#             중간  기말  등수
print(X.max())
# 10.0
print(X.max(axis=0))
# [10. 10.  3.]
print(X.max(axis=1))
# [10.  5. 10.]

print(X.max(axis=0)-X.min(axis=0))
# [10. 20.  2.]


# 정규화 (min-max scale) :  열단위 계산
print((X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0)))
# [[1.  0.  0. ]
#  [0.5 0.5 0.5]
#  [0.  1.  1. ]]

mms = MinMaxScaler()
xmms = mms.fit_transform(X)
print(xmms)
# [[1.  0.  0. ]
#  [0.5 0.5 0.5]
#  [0.  1.  1. ]]

xmms2=minmax_scale(X, axis=0, copy=True)
print(xmms2)
# [[1.  0.  0. ]
#  [0.5 0.5 0.5]
#  [0.  1.  1. ]]

#######################이진화#######################################################
# 이진화(0,1) 0이나 1로 나타냄
# 변수의 값이 연속형에 해당하는 변수(신장, 몸무게, 온도)일 때 값을 0또는 1로 변환 : 이진화
# 기준값이 필요함 : 기준값보다 작다, 크다로 판별
# 임계값(threshold) : 변환 기준이 되는 값
# 예 ) 당뇨병 유/무 확인
# 사용 : 회귀분석, 텍스트 마이닝 등에서 사용
# Binarizer 로 분석

X =np.array(([[10.,-10.,1.],
              [5.,0.,2.],
              [0.,10.,3.]]))

binarizer = Binarizer().fit(X)
print(binarizer)
# Binarizer(copy=True, threshold=0.0)                               # copy= : True 복사하여 함수에 사용, False :  직접 함수에 사용
print(binarizer.transform(X))
# [[1. 0. 1.]
#  [1. 0. 1.]
#  [0. 1. 1.]]

binarizer = Binarizer(threshold=2.0)
print(binarizer.transform(X))

#Binarizer().fit(X) 보다 binarize가 편하다.
print(binarize(X,threshold=2.0))
# [[1. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 1.]]
print(X)
# [[ 10. -10.   1.]
#  [  5.   0.   2.]
#  [  0.  10.   3.]]
print(binarize(X,threshold=2.0,copy=False))
# [[1. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 1.]]
print(X)
# [[1. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 1.]]


# 범주형 변수 -> 이진화 : 원핫인코딩 필요
# 성별 : 남(0),여(1)로 인코딩 하겠다.
# 연령 :  20대(0),30대(1),40대(2),50대(3)로 인코딩 하겠다.
# 성적 : A(0),B(1),..,F(5)로 인코딩 하겠다.
#SN 성별 연령대 성적
#1   0    0     1
#2   1    3     0
#....
# 원핫 인코딩 : 인공신경망 모델에서 원핫인코딩으로 변환 => 변환이 없으면 숫자들을 연속성자료로 인식=>숫자사이의 관계 형성)
# 성별(0,1) => 0:01, 1:10
# 연령대(0~3)=> 0:1000, 2:0100, 3:0010, 4:0001
# 성적(0~5) => 0:10000,1:01000, 3:00100, 4:00010, 5:00001
# from sklearn.preprocessing import OneHotEncoder 함수 사용

# # 번호판 판별기
# 1)52가 1234
#     5 : 0000010000
#     2 : 0010000000
#     가
#     1
#     2
#     3
#     4
# 2)코드를 판별기에 입력
# 3)판별기는 판별 결과를
# 0 0.05 0 0 0 0.9 0.05 0 0 0
# 0000010000 => 5

from sklearn.preprocessing import OneHotEncoder

data_train = np.array([[0,0,0],[0,1,1],[0,2,2],[1,0,3],[1,1,4]])
#열 : 성별(2(0,1)), 연령대(3(0,1,2)), 성적(5(0,1,2,3,4))

enc = OneHotEncoder()                       #thing
print(enc.fit(data_train))
# OneHotEncoder(categorical_features='all', dtype=<class 'numpy.float64'>,
#        handle_unknown='error', n_values='auto', sparse=True)

print(enc.active_features_)                                 # 범주의 값을 fit정보로 나타냄
# [0 1 2 3 4 5 6 7 8 9]
#남,여,20,30,40,A,B,C,D,F
#성별 범쥐 2개(0,1),연령대 범주 3개(2,3,4),등급 범주 5개(5,6,7,8,9)
#10가지 등급이 존재함을 나타냄
print(enc.n_values_)                                        #범주의 구성
# [2 3 5]

print(enc.feature_indices_)
#[ 0  2  5 10]          #성별은 0이상 2미만, 연령은 2이상 5미만, 등급은 5이상 10미만

#여성(1),40대(2),등급:D(3)
data_new = np.array([[1,2,3]])
print(enc.transform(data_new).toarray())
# [[0. 1. 0. 0. 1. 0. 0. 0. 1. 0.]]

################그룹 바이 ############################################
# 혼합된 데이터를 요소별로 나눠서 처리 후 다시 합치는 분석방법












































































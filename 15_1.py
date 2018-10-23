#집계함수(aggregate function : sum)
#축(axis)를 지정. 기본값 : None(전체) ==> 행렬 전체를 연산
#axis = None 행렬 전체를 하나의 배열로 보고 집계 연산 수행(sum) => 45
#axis = 0(행기준)  행 기준으로 각각의 행에 대한 동일한 인덱스의 요소를 하나의 배열로 보고 집계 연산 수행 =>12 15 18
#axis = 1(열기준)  열 기준으로 각각의 행에 대한 열 값들에 대한 집계 연산 수행 => 6 15 24
# 1 2 3
# 4 5 6
# 7 8 9

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# a = np.arange(1,10).reshape(3,3)
# print(a)
# print(np.sum(a, axis=None))                 #축을 지정하지 않았기 때문에 모든 축을 기준으로 계산하여 스칼라로 계산됨
# # 45
# print(np.sum(a, axis=0))                    # 특정 축을 기준으로 계산되어 축이 하나가 줄어듬
# # [12 15 18]
# print(np.sum(a, axis=1))
# # [ 6 15 24]
#
# print('='*50)
#
# print(np.max(a))                            #축을 지정하지 않아서 스칼라를 갖는다.
# # 9
# print(np.max(a,axis=0))                     #행기준
# # [7 8 9]
# print(np.max(a,axis=1))
# # [3 6 9]
#
# # cumsum() : 누적 합계
# print(np.cumsum(a))                         #누적합계 => 1차원으로 결과 값
# # [ 1  3  6 10 15 21 28 36 45]
#
# print(np.cumsum(a,axis=0))                  #행단위로 계산되서 동일 열끼리의 계산이 된다.
# # [[ 1  2  3]
# #  [ 5  7  9]
# #  [12 15 18]]
# print(np.cumsum(a,axis=1))                 #열단위로 계산되서 동일 행끼리의 계산이 된다.
# # [[ 1  3  6]
# #  [ 4  9 15]
# #  [ 7 15 24]]
#
# #np.cumsum(a,axis=0) ==a.cumsum(axis=0) : 표시방법
#
#
# # median(a) : 중간값
# print(np.median(a))                         #1~9(홀수개)까지의 중간값이기 때문에 5.0
# # a=np.arange(1,5).reshape(2,2)
# # print(np.median(a))                         #1~4(짝수개)까지의 중간값이기 때문에 2와 3의 사이값 : 2.5 => flot
# print(np.median(a,axis=0))
# # [4. 5. 6.]
# print(np.median(a,axis=1))
# # [2. 5. 8.]
#
# #np.std() : 표준편차
# print(np.std(a))
# # 2.581988897471611
# print(np.std(a,axis=0))
# # [2.44948974 2.44948974 2.44948974]                # 동일한 간격이기 때문에 같은 값을 갖는다.
# print(np.std(a,axis=1))
# # [0.81649658 0.81649658 0.81649658]
#
# print('='*50)
#
# a=np.arange(1,25).reshape(4,6)
# b=np.arange(25,49).reshape(4,6)
#
# print(a+b)                                          #브로드캐스팅 필요없이 계산
# print(a+100)                                        #100으로 이뤄진(4,6)의 배열로 브로드캐스팅
#
#
# new_arr = np.full_like(a,10)
# print(a+new_arr)                                  #브로드캐스팅 : (a+new_arr) == (a+10)
# print(a+10)
#
# a=np.arange(5).reshape(1,5)                         #np.arange(5) => 1D .reshape(1,5) => 2D
# b=np.arange(5).reshape(5,1)
# print(a)
# # [[0 1 2 3 4]]
# print(b)
# # [[0]
# #  [1]
# #  [2]
# #  [3]
# #  [4]]
# print(a+b)                                          # a,b => (5,5) matrix
# # [[0 1 2 3 4]
# #  [1 2 3 4 5]
# #  [2 3 4 5 6]
# #  [3 4 5 6 7]
# #  [4 5 6 7 8]]
#
#
# # np.copy : 배열 복사
# a = np.random.randint(0,9,(3,3))
# print(a)
#
# a1 = np.copy(a)
# a1[:,0] =99                                        #a에게 바로 적용되진 않고 a=a1으로 작성해야 된다.
# print(a1)
# print(a)
#
# uns = np.random.random((3,3))
# print(uns)
# uns1=uns
# uns2=uns
# uns3=uns
# print('='*50)
# uns1.sort()
# print(uns1)
# uns1.sort(axis=0)
# print(uns1)
# uns1.sort(axis=1)           #생략(axis=-1)  = 마지막 축이 기준(행,열), 3차원 (행,열, 깊이)\
# # axis=1 == axis=-1(2D) ==> 3D : depth
# print(uns1)
#
# # np.argsort() : 오름차순으로 sorting 하여 index 값 출력
# a=np.array([40,30,10,20])
# j=np.argsort(a)
# print(j)
# print(a[j])
# print(np.sort(a))           # print(a[j]) == print(np.sort(a))
#
# print('='*50)
#
# # np.sort(a,axis=0)[::-1]
# x=np.array([14,13,11,15,12,16,10])
# xrev = np.sort(x)[::-1]                    # [::-1] : 오름차순으로 정렬 된 배열을 뒤에서 부터 참조하는 구문
# print(xrev)
# # [16 15 14 13 12 11 10]
#
# # print(np.argsort(x))
# # # [6 2 4 1 0 3 5]
#
# print(np.argsort(-x))                       # np.argsort(x)에 대한 invers
# # [5 3 0 1 4 2 6]
# print(x[np.argsort(-x)])
# # [16 15 14 13 12 11 10]
#
# # print(np.sort(x))                       #정렬 결과만 사본으로 리턴 ,오름차순으로 정렬
# # print(x)                                #원 배열은 그대로
#
# # x.sort()                                #배열 자체를 정렬
# # print(x)


arr = np.arange(0,2*3*4)                    #0~23(24개)
v=arr.reshape([2,3,4])                      #1차원 => 3차원 변환 : 행(row)->axis=0 ,열(col)->axis=1,깊이(depth)->axis=2
print(v)

#--------------deep learning----------------------------
# y_hat = w1*1+w2*2+w3*3+….+b
# y_yhat = min(error)  w, b updating
# 사용 도구  다차원 array
# 다차원 array :  tensor flow, keras, caffe,………..


# 텐서(tensor) 텐서플로우(flow)
# [
# 1번째 행
# [[ 0  1  2  3]    #1번째 컬럼
#  [ 4  5  6  7]    #2번째 컬럼
#  [ 8  9 10 11]]    #3번째 컬럼
#   d1  d2 d3 d4
#
# 2번째 행
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]
# ]
print(np.sum(v, axis=0))
# [[12 14 16 18]
#  [20 22 24 26]
#  [28 30 32 34]]
print(np.sum(v, axis=1))
# [[12 15 18 21]
#  [48 51 54 57]]
print(np.sum(v, axis=2))
# [[ 6 22 38]
#  [54 70 86]]

print(v.sum())
print(v.ndim)

#집계함수 : 사용하면 차원의 변화가 생긴다.
res1= v.sum(axis=0)             #2*3*4 =?3*4
print(res1.shape)
res2= v.sum(axis=1)             #2*3*4 =?2*4
print(res2.shape)
res3= v.sum(axis=2)             #2*3*4 =?2*3
print(res3.shape)
























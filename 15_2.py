#슬라이싱 인덱싱
#실제 파일을 읽어서 슬라이싱등을 연습

import numpy as np
import matplotlib.pyplot as plt


# a1 = np.arange(24)
# a2 = np.arange(24).reshape((4,6))
# a3 = np.arange(24).reshape((2,3,4))
# a1[5] = 1000
# a2[0,1] = 1000
# a3[1,0,1] = 1000            #2번째 행, 1번째 열, 2번째 depth
#
# print(a2)
#
#
# #a2에서 7~10,13~16을 추출해서 출력
#
# print(a2[1:3,1:5])
# print(a2[1:-1,1:-1])
# a2[:,1:3]=99
# print(a2)
#
# a1=np.arange(1,25).reshape(4,6)
# even_a=a1%2 ==0
# print(a1[even_a])
#

import pandas as pd

# rain = pd.read_csv('seattle.csv')
# # print(rain)
# # rain_r = rain['PRCP']                   #변수 PRCP를 추출
# # print(type(rain_r))
# # # <class 'pandas.core.series.Series'>
#
# rain_r = rain['PRCP'].values                #.values : 배열로 추출
# print(rain_r)
# print(type(rain_r))
# # <class 'numpy.ndarray'>
# print("데이터 크기:",len(rain_r))
# # 데이터 크기: 365
# days_a = np.arange(0,365)
# con_jan = days_a<31                         #Ture : 31, False : 334
# print(con_jan)
# print(con_jan[:40])
# print(rain_r[con_jan] )                        #rain_r[con_jan] : Ture 만 참조 ==1월 데이터 참조
#
# #1월달 강수량의 총합
# print(np.sum(rain_r[con_jan]))
# #940
#
# # 평균 : mean,  중앙값 : median
# #1월달 평균 강수량
# print(np.mean(rain_r[con_jan]))
# #30.322580645161292
# print(np.median(rain_r[con_jan]))
#
# #팬시 인덱싱: 배열에 인덱스 배열을 전달해서 데이터를 참조
# a=np.arange(1,25).reshape((4,6))
# print([a[0,0],a[1,1],a[2,2],a[3,3]])
# # [1, 8, 15, 22]
# print(a[[0,1,2,3],[0,1,2,3]])
# # [ 1  8 15 22]
#
# print(a[:,[1,2]])                           #1과2열만 참조(열단위로 참조 가능)
# # [[ 2  3]
# #  [ 8  9]
# #  [14 15]
# #  [20 21]]
# print(a[:,[1,3]])
# # [[ 2  4]
# #  [ 8 10]
# #  [14 16]
# #  [20 22]]
#
# #ravel(배열을 1차원으로 ), reshape매서드-배열 형태를 변경
# a=np.random.randint(1,10,(2,3))
# print(a)
# print(a.ravel())                                # ravel() : 임시적으로 1차원으로 바꿈
# print(a)
#
# b=a.ravel()
# print(b)
#
# #배열 변경, 삭제 , 추가.....
# #resize : 배열의 크기(데이터의 크기(원본 데이터)가 변경된다.) 변경=> 요소 수 변경
# # reshape : 배열 변경(요소 수 변경 안됨) => 원본데이터 유지
#
# print("="*50)
# a=np.random.randint(1,10,(2,6))
# print(a)
# # [[5 2 9 6 8 1]
# #  [8 7 2 2 1 9]]
# a.resize((6,2))                                   #모양 변경
# print(a)
# # [[5 2]
# #  [9 6]
# #  [8 1]
# #  [8 7]
# #  [2 2]
# #  [1 9]]
# a.resize((2,10))                                   #사이즈 증가 변경
# print(a)
# # [[5 2 9 6 8 1 8 7 2 2]
# #  [1 9 0 0 0 0 0 0 0 0]]                           #모자라는 숫자는 0으로 채움
#
# a.resize((3,3))                                   #모양 변경 &사이즈 감소
# print(a)
# # [[2 5 6]                                          #앞에서 부터 채워넣고 남은 나머지(2 1 9)삭제
# #  [2 5 8]
# #  [7 4 7]]
#
#
# #axis=를 이용하여 방향을 지정
#
# a=np.arange(1,10).reshape(3,3)
# b=np.arange(10,19).reshape(3,3)
#
# # np.append(a,b) :  a배열 뒤에 b 배열을 추가한다.(axis지정 안하면 1D)
# res = np.append(a,b)                              #res라는 새로운 배열을 만듬
# print(res)
# print(a)                                          #a는 변함 없음
#
# print("="*50)
# res = np.append(a,b,axis=0)                       #axis=0 :  행방향 ,  2차원 배열
# print(res)
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [ 7  8  9]
# #  [10 11 12]
# #  [13 14 15]
# #  [16 17 18]]
#
# print("="*50)
# res=np.arange(10,20).reshape(2,5)
# print(res)
# # np.append(a,res,axis=0)
# # # 기준 축과 shape이 다르면 append오류가 발생한다.
# res = np.append(a,b,axis=1 )                       #axis=1 : 열 방향 ,  2차원 배열
# print(res)                                          #3*6
# #shape이 다르므로 오류
# # x=np.arange(10,20).reshape(2,5)
# # x=np.append(res,x,axis=1)
#
# # insert(a,1,99,axis=1) : 다른 요소로 대치함
# a=np.arange(1,10).reshape(3,3)
# a=np.insert(a,2,99,axis=0)                          #행방향 2번 인덱스를 중심으로 모든 행이 바뀜
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [99 99 99]
# #  [ 7  8  9]]
# print(a)
# # a=np.insert(a,1,99)
# # print(a)
# a=np.insert(a,1,99,axis=1)                          #열방향 1번 인덱스를 중심으로 모든 행이 바뀜
#
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [99 99 99]
# #  [ 7  8  9]]
# a=np.arange(1,10).reshape(3,3)
# print(np.delete(a,1))
# # [1 3 4 5 6 7 8 9]
#
#
# #a배열의 1번 인덱스 행 제거한 후 출력
# a=np.arange(1,10).reshape(3,3)
# print(np.delete(a,1,axis=0))
#
#
# #a배열의 1번 인덱스 열 제거한 후 출력
# a=np.arange(1,10).reshape(3,3)
# print(np.delete(a,1,axis=1))
#
# print("="*50)
#
# # 배열 간의 결합(빈번함) :  concatenate, vstack, hstack
#
# a=np.arange(1,7).reshape(2,3)
# print(a)
# b=np.arange(7,13).reshape(2,3)
# print(b)
# res = np.concatenate((a,b))                                       #((a,b)) : 튜플형이기 때문에 이중 괄호
# print(res)
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [ 7  8  9]
# #  [10 11 12]]
# res = np.concatenate((a,b),axis=0)
# print(res)
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [ 7  8  9]
# #  [10 11 12]]
# res = np.concatenate((a,b),axis=1)
# print(res)
# # [[ 1  2  3  7  8  9]
# #  [ 4  5  6 10 11 12]]

#vstack, hstack : 많이 사용
a=np.arange(1,7).reshape(2,3)
print(a)
b=np.arange(7,13).reshape(2,3)
print(b)
print(np.vstack((a,b)))
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(np.vstack((a,b,a,b)))
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

print("="*50)

print(np.hstack((a,b)))
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
print(np.hstack((a,b,a,b,a,b)))
# [[ 1  2  3  7  8  9  1  2  3  7  8  9  1  2  3  7  8  9]
#  [ 4  5  6 10 11 12  4  5  6 10 11 12  4  5  6 10 11 12]]

print("="*50)

# 분할 hsplit,vsplit
a=np.arange(1,25).reshape(4,6)
res = np.hsplit(a,2)
print(res)
# [array([[ 1,  2,  3],
#        [ 7,  8,  9],
#        [13, 14, 15],
#        [19, 20, 21]]),
#   array([[ 4,  5,  6],
#        [10, 11, 12],
#        [16, 17, 18],
#        [22, 23, 24]])]

res = np.hsplit(a,3)
print(res)
# [array([[ 1,  2],
#        [ 7,  8],
#        [13, 14],
#        [19, 20]]),
#  array([[ 3,  4],
#        [ 9, 10],
#        [15, 16],
#        [21, 22]]),
#  array([[ 5,  6],
#        [11, 12],
#        [17, 18],
#        [23, 24]])]

res = np.vsplit(a,2)
print(res)
# [array([[ 1,  2,  3,  4,  5,  6],
#        [ 7,  8,  9, 10, 11, 12]]), array([[13, 14, 15, 16, 17, 18],
#        [19, 20, 21, 22, 23, 24]])]

x=np.array([1,2])                               # []_ list를 array에 집어넣어서 배열로 만듬
print(x.dtype)
# int32
x=np.array([1.,2.])
print(x.dtype)
# float64
x=np.array([1.,2.],dtype = np.int64)                # dtype = np.int64 : 배열을 만들 때 부터 int64으로 지정 해줌
print(x.dtype)

x= np.array([[1,2],[3,4]])
y= np.array([[5,6],[7,8]])
v= np.array([9,10])
w= np.array([11,12])

#벡터의 내적(dot함수 사용)
print(np.dot(v,w))                              #9*11+10*12=219
# 219
print(v.dot(w))
# 219

#행렬과 벡터의 곱
print(x.dot(v))                                     #rank : 1 => array(배열)
# [29 67]
print(np.dot(x,y))
# [[19 22]
#  [43 50]]

x= np.array([[1,2],[3,4]])
print(x.T)                                          # T : 전체 행렬( 행과 열을 바꿔 줌)

print("="*50)

x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
y=np.empty_like(x)
print(y)

for i in range(4):
    y[i,:] = x[i,:]+v
print(y)
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]

print("="*50)

#np.tile(v,(4,1)) : v를 행방향으로 4번, 열방향으로  1번 반복해라 =>tile : 반복을 하는 함수
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
vv=np.tile(v,(4,1))
print(vv)
# [[1 0 1]
#  [1 0 1]
#  [1 0 1]
#  [1 0 1]]

vv=np.tile(v,(3,2))
print(vv)
# [[1 0 1 1 0 1]
#  [1 0 1 1 0 1]
#  [1 0 1 1 0 1]]

# prod() : 곱셈을 하는 함수
a=np.array([[1,2],[4,5]])
s = np.prod(a)
print(s)
# 40

a=np.array([[1,2],[4,5]])
s = np.prod(a,axis=0)
print(s)
# [ 4 10]

a=np.array([[1,2],[4,5]])
s = np.prod(a,axis=1)
print(s)
# [ 2 20]

# max 최대값 구하는 연산자
a=np.array([[1,2],[4,5]])
s = np.max(np.prod(a,axis=1))                       # 딥러닝에서 많이 사용되는 구문
print(s)
# 20


# #data : list
# data = [[828.659973,833.450012,828.349976,1247700,831.659973],
# [823.02002,828.070007,821.655029,1597800,828.070007],
# [819.929993,824.400024,818.97998,1281700,824.159973],
# [819.359985,823,818.469971,1304000,818.97998],
# [819,823,816,1053600,820.450012],
# [816,820.958984,815.48999,1198100,819.23999],
# [811.700012,815.25,809.780029,1129100,813.669983],
# [809.51001,810.659973,804.539978,989700,809.559998]]
# data = np.array(data)
# print(data.shape)
# print(data)
#
# print("="*50)
#
# data = np.transpose(data)
# print(data.shape)
# print(data)
#
# x = data[:-1].transpose.astype(np.float32)
# y = data[-1:].transpose.astype(np.float32)
#
#
# #transpose연산의 연산형태
# # =>data
# # 1 2 3 4 A
# # 2 3 4 5 B
# # 1 4 3 4 A
# #
# # =>x
# # 1 2 3 4
# # 2 3 4 5
# # 1 4 3 4
# #
# # =>y
# # 1 2 1
# # 2 3 4
# # 3 4 3
# # 4 5 4
#
# # x(5,4) * w(4,1) = y(5,1)
#
# print(x.shape)
# print(y.shape)


#diabetes
xy =  np.loadtxt('data/diabetes.csv', delimiter=',',dtype=np.int32)
print(xy)
xdata = xy[:,0:-1]
ydata = xy[:,[-1]]
print(xdata)

print("="*50)

print(ydata)


# 다음 배열은 첫번째 행(row)에 학번, 두번째 행에 영어 성적, 세번째 행에 수학 성적을 적은 배열이다.
# 영어 성적을 기준으로 각 열(column)을 재정렬하라.
# array([[  1,    2,    3,    4],
#        [ 46,   99,  100,   71],
#        [ 81,   59,   90,  100]])
#
# 실수로 이루어진 5 x 6 형태의 데이터 행렬을 만들고 이 데이터에 대해 다음과 같은 값을 구한다.
# 1.전체의 최댓값
# 2.각 행의 합
# 3.각 열의 평균

a=np.array([[  1,    2,    3,    4],
            [ 46,   99,  100,   71],
            [ 81,   59,   90,  100]])
a=np.transpose(a)
b=a[a[:,1].argsort()]
b=np.transpose(b)

# 실수로 이루어진 5 x 6 형태의 데이터 행렬을 만들고 이 데이터에 대해 다음과 같은 값을 구한다.
c=np.arange(1,300,10).reshape((5,6))

# 1.전체의 최댓값
d=np.max(c)
# 2.각 행의 합
e=np.sum(c,axis=1)
# 3.각 열의 평균
f=np.mean(c,axis=0)
print(b)




















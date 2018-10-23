import numpy as np
import matplotlib.pyplot as plt                         # 시각화 도구
# a=np.array([[1,2,3],[4,5,6]])
# b = np.ones_like(a)                                     # _like : a 배열과 같은 형태로 1을 채워넣은 배열을 만들어라
# print(b)
#
#
# #데이터 생성 함수
#
# #0~1범위 내에서 균등 간격으로 5개의 수를 생성
# a=np.linspace(0,1,5)
# print(a)
# # a=np.linspace(0,100)                                    # 생성 숫자를 지정하지 않으면 50개 생성
# # print(a)
# # plt.plot(a,'o')
# # plt.show()
#
#
# a=np.arange(0,10,2,np.float)                               #list의  data 생성 방식과 동일(시작,끝+1,간격)
# print(a)
# print(type(a))
# # plt.plot(a,'*')
# # plt.show()
#
# #정규분포
# mean = 0                    #평균
# std = 1                     #표준편차
# a = np.random.normal(mean,std,10000)
# print(a)
# # plt.hist(a,bins=200)                                #bins : 막대그래프의 갯수
# # plt.show()
#
#
# #균등분포[0<=x<1]
# a=np.random.rand(10000)
# # plt.hist(a,bins=20)
# # plt.show()
#
# #randint : 범위 내에서 균등하게 나온다.
# a=np.random.randint(-100,100,size=10000)
# print(a)
# # plt.hist(a,bins=10)
# # plt.show()

# a=np.random.randint(0,10,(2,3))
# print('a=', a)
# b=np.random.randint(0,10,(2,3))
# print('b=', b)
#
# #save() : 배열을 바이너리 형태로 저장(용량이 작아서 빠름)
# np.save('myarr1',a)                             #myarr1.npy
#
# np.savez('myarr2',a,b)                             #myarr2.npz
#
# print("myarr1",np.load('myarr1.npy'))
# # print("myarr2",np.load('myarr2.npz'))
# npzfiles=np.load('myarr2.npz')
# print(npzfiles.files)                             #배열의 형식을 알수 없기에 형식을 먼저 출력
# # ['arr_0', 'arr_1']
# print(npzfiles['arr_0'])
# print(npzfiles['arr_1'])
#
# print(np.loadtxt('simple.csv', dtype=np.int) )          # 띄어 쓰기로 구분하기 때문에 , 가 있는 문서는 구분자를 줘야한다.
#
# #skiprows=1 : 첫줄이 문자열이고 형식이 다르다면 스킵
# #문자와 숫자가 뒤섞여 있는 자료
# #('i','S20','f') : i= 숫자, S20=b(바이너리)문자, f=실수
# data = np.loadtxt('height.csv', delimiter=',' ,skiprows=1,dtype={'names':('order','name','height(cm)'),'formats': ('i','S20','f')})
# print(data)
#
# #배열을 텍스트파일로 저장
# data = np.random.random((3,4))
# print(data)
# np.savetxt('saved.csv',data,delimiter=',')
# print(np.loadtxt('saved.csv',delimiter=','))
#
# arr=np.random.random((5,2,3))
# print(type(arr))
# print(arr.shape)
# print(len(arr))
# print(arr.ndim)
# print(arr.size)
# print(arr)
# print(arr.dtype)
#
# # astype : 데이터 타입 변환 = > 원본을 변형시키진 않는다.
# print(arr.astype(np.int))
# # astype : 데이터 타입 변환 = > 원본을 변형.
# arr=arr.astype(np.int)
# print(arr)
# arr=arr.astype(np.float)
# print(arr)
#
# #numpy안의 함수 정보 확인
# print(np.info(np.ndarray.dtype))

# # reshape: 배열 형식을 바꿔주는 함수
a=np.arange(1,10).reshape(3,3)
# print(a)
#
b=np.arange(9,0,-1).reshape(3,3)
# print(b)
#
# print(a-b)
# # np.subtract(a,b) == (a-b)
# print(np.subtract(a,b))
#
# print(a+b)
# # np.add(a,b) == (a-b)
# print(np.add(a,b))
#
# print(a/b)
# # np.divide(a,b) == (a/b)
# print(np.divide(a,b))
#
# print(a*b)
# # np.multiply(a,b) == (a*b)
# print(np.multiply(a,b))
#
# print(b)
# # exp :
# print(np.exp(b))
# # [[8.10308393e+03 2.98095799e+03 1.09663316e+03]
# #  [4.03428793e+02 1.48413159e+02 5.45981500e+01]
# #  [2.00855369e+01 7.38905610e+00 2.71828183e+00]]
# #2.71828183e+00(자연 상수)
#
# # sqrt : 제곱근( 절대치이기 때문에 항상 양수)
# print(np.sqrt(a))
# print(a)
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.log(a))
# a=np.arange(1,5).reshape(2,2)
# b=np.arange(9,5,-1).reshape(2,2)
# print(a)
# print(b)
# # dot : 벡터의 내적 구하는 함수
# #(1,2,3) (4,5,6) = 1*4+2*5+3*6=32
# print(np.dot(a,b))
# #
# #a,b 모두 array 이기에 비교연산 가능
# print(a==b)
# print(type(a==b))
# # <class 'numpy.ndarray'>
#
# #행렬 전체를 비교, 모두 동일한 것인가 ?
# print(np.array_equal(a,b))
# #False
#

#축에 대한 이해를 바탕으로 벡터의 연산을 이해
#축을 따로 지정하지 않으면 전체 행렬을 계산
# print(a.sum())
# print(np.sum(a))
#
# print(a)
#axis =0 : 행을 기준으로 각 행의 동일한 인덱스 요소를 그룹화 해라
print(a.sum(axis=0))
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# [12 15 18]

#axis =1 : 열을 기준으로 각 열의 동일한 인덱스 요소를 그룹화 해라
print(a.sum(axis=1))
# [[1 2 3]  :6
#  [4 5 6]  :15
#  [7 8 9]]  :24
# [ 6 15 24]


#연습문제
# 다음 행렬과 같은 행렬이 있다.
m = np.array([[ 0,  1,  2,  3,  4],
              [ 5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14]])
# 1.이 행렬에서 값 7 을 인덱싱한다.
print(m[1, 2:3])
# 2.이 행렬에서 값 14 을 인덱싱한다.
print(m[2, 4:])
# 3.이 행렬에서 배열 [6, 7] 을 슬라이싱한다.
print(m[1, 1:3])
# 4.이 행렬에서 배열 [7, 12] 을 슬라이싱한다.
print(m[[1,2],[2,2]])
# 5.이 행렬에서 배열 [[3, 4], [8, 9]] 을 슬라이싱한다
print(m[0:2, 3:])
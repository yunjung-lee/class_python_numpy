import numpy as np
# print(np.__version__)
#
# list1=[1,2,3,4]             #python's list
# print("list=", list1)
# a=np.array(list1)
# print("array=",a)
# print(a.shape)             #rank : 4, shape : (4,)=>blank ==1
# # (4,)
# b=np.array([[1,2,3],[4,5,6]])
# print(b)
# print(b.shape)
# print(b[0,0])               #count : start 0
# print(type(b))
# # <class 'numpy.ndarray'>
# print(type(list1))
# # <class 'list'>
#
# print(a[2])
#
# #벡터화 연산#
# #개념 : 배열의 각 요소에 대한 반복 연산을 하나의 명령으로 처리
#
# #벡터화 연산을 하지 않은 일반적인 반복문 연산(속도가 느림)
# data = [1,2,3,4,5]
# ans = []
# for i in data :
#     ans.append(2*i)
# print(ans)
#
# #벡터화 연산(for 반복문이 없음)-> 속도가 무척 빠름
# x=np.array(data)
# print(2*x)              #x=array
# # [ 2  4  6  8 10]
# print(2*data)           #data = list
# # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print("="*50)
#
#
# a=np.array([1,2,3])
# b=np.array([10,20,30])
# print(a*2+b)
# print(a==2)
# print(b>10)
# print((a==2)&(b>10))
# print(a.shape)              #shape
# print(a.ndim)               #rank : dimension
# print(a.dtype)
# # int32   : type ==int, 32byte
#
#
# a=np.zeros(4)
# print(a)
# # [0. 0. 0. 0.]  : . != int
# print(type(a))
# #<class 'numpy.ndarray'> : 자료구조의 타입
# print(a.dtype)
# #float64                 : 자료형(data)의 타입
#
#
# a=np.zeros((2,2))               #np.zeros : 매트릭스의 0으로 초기화
# print(a)
# # [[0. 0.]
# #  [0. 0.]]
# a=np.ones((2,3))                #np.ones : 매트릭스의 1로 초기화
# print(a)
# # [[1. 1. 1.]
# #  [1. 1. 1.]]
# a=np.full((2,3),5)              #np.full((2,3),5) :  매트릭스의 5로 초기화
# print(a)
# # [[5 5 5]
# #  [5 5 5]]
# a=np.eye(5)                     #np.eye(n) : nxn의 단위행렬
# print(a)
# # [[1. 0. 0. 0. 0.]
# #  [0. 1. 0. 0. 0.]
# #  [0. 0. 1. 0. 0.]
# #  [0. 0. 0. 1. 0.]
# #  [0. 0. 0. 0. 1.]]
#
# print(range(20))                #range(0, 20)로 표시되지만 0~19 까지임
# print(np.array(range(20)).reshape(4,5))    #1D(20,) -> 2D(4,5)
# c=np.array(range(20)).reshape(4,5)
# print(len(c))                   #행의 개수
# print(len(c[0]))                #0번(첫번째) 열의 길이  = 0번 열에 있는 요소(값) 개수
# print(c.ndim)                   #rank : 2
# print(c.shape)                  #shape : (4,5)
#
# print('='*50)
# print(c)
# print('='*50)
# print(c>10)                     #비교 연산이기 때문에 False / True만 갖는다.
# print('='*50)
#
#
# #조건에 따른  data 대체 및 자료출력
# print(c[c>10])
# #[11 12 13 14 15 16 17 18 19]               #행렬에 상관없이 조건[c>10] 만족 자료만 출력
#
# c[c>10]=99                              #조건[c>10] 만족하는 data를 자료변형(대체)
# print(c)
# # [[ 0  1  2  3  4]
# #  [ 5  6  7  8  9]
# #  [10 99 99 99 99]
# #  [99 99 99 99 99]]


#numpy :  indexing & sliceing
arr=np.arange(0, 3*2*4)                     # 0~(3*2*4-1) 까지의 배열
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
print(arr)
print(len(arr))
v=arr.reshape([3,2,4])                      # 3차원 배열
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]
#
#  [[ 8  9 10 11]
#   [12 13 14 15]]
#
#  [[16 17 18 19]
#   [20 21 22 23]]]
print(v)
print(len(v))                           #3x2x4 의 배열에서 첫번째인  3
print(len(v[0]))                        #3x2x4 의 배열에서 두번째인  2
print(len(v[0][0]))                     #3x2x4 의 배열에서 세번째인  4

#indexing
a=arr=np.arange(0, 3*4)
a=a.reshape([3,4])
print(a)

b=np.array([0,1,2,3,4])
print(b[2])
print(b[-1])
#다차원 배열을 슬라이싱 할 때 사용되는 콤마(,)로 차원을 구분(축)
print(a)
print(a[0,1])
print(a[-1,-1])

print(a[0,:])                           # [0,:] : 행과 열을 , 로 구분 0인행과 : 로 표현된 전체 열 =>  행 추출
# [0 1 2 3]

#두번째 열 전체
print(a[:,1])
#두번째 행의 두번째 열부처 끝까지
print(a[1,1:])

print(a[:2,:2])



#인덱싱:행을 지정 , 슬라이싱 : 추출 열 지정  => 모두 합해서 슬라이싱이라고 함
print(a[1, :])                          # (4,) => rank =1D
#[4 5 6 7]
print(a[1, :].shape)


print(a[1:2, :])                        #(1,4) => rank = 2D
#[[4 5 6 7]]
print(a[1:2, :].shape)

a=np.array([[1,2],[3,4],[5,6]])
print(a.shape)
print(a)

print(a[0,0])                           #1행 1열 = 1
print(a[1,1])                           #2행 2열 = 4
print(a[2,0])                           #3행 1열 = 5
print(a[[0,1,2],[0,1,0]])               #[[0,1,2],[0,1,0]] => [0,1,2]행,[0,1,0]열 : [[0,0]:1행 1열 = 1,[1,1]2행 2열 = 4,[2,0]3행 1열 = 5]
# [1 4 5]
print(a[0,0],a[1,1],a[2,0])             # 배열이 아닌 스칼라의 나열
# 1 4 5
print([a[0,0],a[1,1],a[2,0]])           #list로 나옴
print(np.array([a[0,0],a[1,1],a[2,0]])) #list를 배열로 전환

a=np.array([[1,2],[3,4],[5,6]])         #array
print(a[0,0],a[1,1],a[2,0])             #스칼라

#리스트 => np.array => 배열 => reshape => 인덱싱\
#임의의 numpy배열 a에 대해
#a[[row1,row2],[col1,col2]] ??
#a[row1,row2]과 a[col1,col2] 라는 두개의 배열 요소들의 집합
a=np.array([[1,2],[3,4],[5,6]])
s=a[[0,1],[1,1]]
print(s)
# [2 4]


#부울린 값 참조
lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

x=np.array(lst)

bool_ind=x%2
print(bool_ind)
# [[1 0 1]                  #x를 2로 나눈 나머지
#  [0 1 0]
#  [1 0 1]]
bool_ind=(x%2==0)               #우선순위 % > == > = ( 괄호는 없어도 되지마 헤깔릴까봐 묶어줌)
print(bool_ind)
# [[False  True False]
#  [ True False  True]
#  [False  True False]]
print(x[bool_ind])
#[2 4 6 8]
print(x[x%2==0])
#[2 4 6 8]

# bool_ind_arr=np.array([                 #bool의 배열화
#     [False,True,False],
#     [True,False,True],
#     [False,True,False]
# ])
# print(type(lst))
# #<class 'list'>
# print(type(bool_ind_arr))
# #<class 'list'>
#
#
# #lst안에서 bool_ind_arr값의 변수값과 위치가 같은 것을 대응
# res = x[bool_ind_arr]
# print(res)


#에러메세지...다른 파일도 언급될 수 있으나 실행파일의 에러만 보면 됨
#구체적으로 원인을 밝힐때도 있지만 대부분 메세지가 러프하게 나온다.(별 도움이 안됨)
#에러메세지를 구글링을 통해서 확인











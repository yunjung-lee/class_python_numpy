# a=123
# if a%2==1:
#     print('홀수')
# else:
#     print('짝수')
#
# if a%2: #a%2 == 0생략
#     print('홀수')
# else:
#     print('짝수')
# a=0
# if a:
#     print('홀수')
# else:
#     print('짝수')
# # 입력 받은 정수가 음수/양수 인지 0인지?
# b=int(input())      #input()은 class 'str'로 입력됨
# #print(b+1)      #b=input() 일때 에러(class 'str')이기 때문에 =>print(b+'1') ==991
# print(type(b))
#
# if b<0:
#     print('음수')
# else:
#     if b>0 :
#         print("양수")
#     else:
#         print('제로')

# print('='*50)
#
# # 루프(가장 많이 사용)
# for i in range(10):
#     print(i,end=", ")
# print()
# for i in range(0,10):
#     print(i,end=", ")
# print()
# for i in range(0,10,1):
#     print(i,end=", ")
# print()
# for i in range(10-1,-1,-1):
#     print(i,end=", ")
# print()
# for i in reversed(range(10)):       #역순으로 정렬
#     print(i,end=", ")
# print()
#
# s=0
# for i in range(5):
#     s+=i
#     print(s)
#
# s=''                                #s=문자 =>error
# for i in range(5):
#     s+=str(i+1) +" "                    #s=문자 =>error :i 를 문자로 만들어서 에러없이 출력
#     print(s)
#
# a=[1,3,5]
# print(a[0],a[1],a[2])
# print(a)
# a[0]=a[2]           #변수 대체
# print(a)
# a.append(11)        #변수 추가
# print(a)
#
# #a리스트 역순으로 출력 : 11,5,3,5
#
# for i in reversed (a):
#     print(i)
# for i in reversed (range(len(a))):
#     print(a[i])
# for i in range(len(a)-1,-1,-1):
#     print(a[i])
#
# a,b=3,8
# print(a,b)
# a,b=b,a             #변수 교환
# print(a,b)
#
#
# #튜플 :  리스트의 상수 버전(값의 변화가 없음)
# t=(1,3,5)
# print(t)
# print(t[0])
# #t[0]=9          #타입 에러 => TypeError: 'tuple' object does not support item assignment
# print(t[1])
#
# t2=(100,200)
# print(t2, type(t2))
# t22=100,200             # 튜플의 입력 방식은 ()를 사용유무를 떠나서 동일한 결과를 갖는다.
# print(t22, type(t22))
# t3,t4 = t2
# print(t2)
# print(t3)
# print(t4)
#
# def order(a,b):
#     if a<b:
#         return a,b
#     return b,a
# print(order(9,4))
# print(order(4,9))
# min,max = order(9,4)            #위의 구문과 같은 결과를 갖는다.
# print(min,max)
# _,max = order(9,4)            #_ :  해당 자료는 출력하지 않는다.
# print(min,max)

# #리스트의 중복 값 제거
# ns = [1,3,5,1,3,5,1,3,5]
# unique =[]
# for i in ns:
#     #unique에 i값이 없다면
#     if not i in unique:
#        unique.append(i)
# print(unique)
# unique = list(set(ns))
# print(unique)
#
# ns=[2,4,6,1,3,5]
# for i in range(len(ns)):
#     print(i,ns[i],end=', ')
# print()
# j=0
# for i in ns:
#     print(j,i)
#     j+=1
# # enumerate함수 => 튜플로 들어감, 첫번째  순번(index) : 0
# for i in enumerate(ns):
#     print(i,i[0],i[1])
# for i,j in enumerate(ns):
#     print(i,j)
# def dummy():
#     pass
# #pass : 아무것도 실행하지 않는 예약어
# print(dummy())

#
# # cost_function : 유효성평가에 사용 => 많이 쓰인다.
# def cost_function(xx,yy,ww):
# #    print(xx)
#     cost = 0
#     for i in range(len(x)):
#         hx = ww * x[i]      #hx함수 = 10 * x :  예측하는 함수 =>머신러닝에서 사용
# #        print(hx)
#         cost+=(hx-y[i])**2      #cost : 오차의 제곱(오차가 커보임)의 합(모델의 잘못을 확인)
#     return cost/len(xx)
#
# x=[1,2,3]
# y=[1,2,3]
# #xy의 그래프 => x=y
# #y=w*x
#
# w=10
# print(cost_function(x,y,w))
# #호출 하였기에 호출 결과print(xx) 출력 후, print(cost_function(x,y,w))로 돌아옴 : None
# print(cost_function(x,y,5))
# print(cost_function(x,y,1))         #오차 없이 cost=0
# xxx,yyy=[],[]
# for i in range(-50,50):
# #    print(i)
#     w = i/10            #w = -5.0~4.9
#     c=cost_function(x,y,w)
#  #   print(w,c)
#     xxx.append(w)
#     yyy.append(c)
#
#
# import matplotlib.pyplot as plt
# plt.plot(xxx,yyy)
#
# plt.plot(xxx,yyy,'bo')
# plt.show()


#딕셔너리 :리스트와 함께 많이 쓰이는 자료구조(머신러닝에서)
a= dict(name = 'kim', age = 20)
print(a)
print(a['name'])            #keys 에는  ' '가 쓰임
a['addr']='seoul'
print(a)
#출력 형식
print(a.keys())
print(a.values())
print(a.items())
#각 요소 분리추출
for k in a.keys():
    print(k)

for k in a.keys():
    print(k,a[k])

for v in a.values():
    print(v)

for items in a.items():
    print(items,items[0],items[1])

for k,v in a.items():
    print(k,v)

for k in a:         #딕셔너리 인 경우 k in a에서 k는 key값
    print(k, a[k])

print(a.keys())         #dict_keys(['name', 'age', 'addr'])
print(list(a.keys()))

for k in reversed(list(a.keys())):
    print(k,a[k])


a=[1,3,5,7,9]
print(a[1])
print(a[-1])
print(a[2])
print(a[-2])
print(a[len(a)-1])            #print(a[len(a)]) error
print(a)                        #a 전체
print(a[:])
print(a[0:])
print(a[0:len(a)])
print(a[0:len(a)//2])       #앞의 절반 추출
print(a[:len(a)//2])
print(a[len(a)//2:len(a)])      #뒤의 절반 추출
print(a[len(a)//2:])
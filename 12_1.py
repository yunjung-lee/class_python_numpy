#sliceing :

# a=[1,3,5,7,9,0,2,4,6,8]
# # print(a[len(a)-1:0:-1])         # 모두 프린트 하고 싶으면 0이면 안된다
# # print(a[len(a)-1:-1:-1])        #[] : 확인이 필요
# print(a[len(a)-1::-1])          #모두 프린트 됨
#
# print(a[::-2])                  #2칸 간격으로 출력
# print(a[-2::-2])                #맨 뒤가 음수이기때문에 역순 출력 :  맨 앞도 음수여야 한다.

# #폴더에 cars.csv파일 호출
# def read_car():
#     f=open('cars.csv','r')
#     row=[]
#     for row in f:
#          # print(row)                 #"Volvo 142E",21.4,4,121,109,4.11,2.78,18.6,1,1,4,2
#          # print(row.strip())         #line 단위 문자열 : "Volvo 142E",21.4,4,121,109,4.11,2.78,18.6,1,1,4,2
#          print(row.strip().split(','))      #list로 바뀜 : ['"Volvo 142E"', '21.4', '4', '121', '109', '4.11', '2.78', '18.6', '1', '1', '4', '2']
#
# mycar = read_car()

# #data폴더에 있는 문서를 읽어와 텍스트로 저장하는 방법
# import csv
# def read_car():
#     f=open('Data/cars.csv','r')
#     rows=[]
#     for row in f:
#          rows.append(row.strip().split(','))
#     f.close()
#     return  rows
#
#
# def write_car(rows):
#     f=open('cars_w.txt','w',newline='')         #newline='': 라인사이의 공백 제거
#     writer=csv.writer(f, delimiter = ':')       #delimiter = ':' =>?
#     for row in rows:
#         writer.writerow(row)
#     f.close()
#
# mycar = read_car()
# write_car(mycar)

import numpy as np          #행렬연산을 빠르게 해주는 연산
a=np.array([1,3,5])         #,로 이루어진 리스트 : 1차원, [[[]]] :  3차원
print(a)
print(type(a))              #<class 'numpy.ndarray'> :ndarray=>n차원 배열

b=np.arange(7)
print(b)
b+=1                #numpy계열의 벡터(b=행벡터)
print(b)            #broadcasting : 더해지는 행렬에 맞춰 모양을 바꾸는 방식
#[0,1,2,3,4,5,6]
#[1,1,1,1,1,1,1] : 위의 b와 합
#[1,2,3,4,5,6,7]

print(b<4)
print(b[b<4])

c=np.arange(3,7,0.1)
print(c)

d=np.arange(15)
print(d.shape)              #15개의 요소가 있는 1차원 배열을 표시

d=np.arange(15).reshape(3,5)            #3행 5열로 표시
print(d)
print(d.shape)
print(d+1)                              #요소간의 덧셈이기 때문에 +1의 1도 3행5열을 갖는다.
print(d[d>5])

print("="*50)

print(d[0])             #0 번째 행만 출력
print(d[-1])            #마지막 행만 출력
print(d[0][0])          #1행 참조 1열 출력
print(d[0,0])           #1행1열 출력
print(d[-1][-1])
print(d[-1,-1])

# d2=np.arange(15).reshape(2,3,4)            #24개의 데이터가 필요한데 15빡에 없어서 에러
# print(d2)
# print(d2.shape)
#

# d2=np.arange(24).reshape(2,3,4)
# print(d2)
# print(d2.shape)
#
# d2=np.arange(48).reshape(2,3,4,2)
# print(d2)
# print(d2.shape)

print(d[:])
print(d[::-1])          #열의 역순
print(d[::-1][::-1])            #열의 역순의 역순
print(d[::-1,::-1])             #열과 행의 역순

print(d[1:3,2:4])
print(d.sum())
print(d.sum(axis=0))            #axis :0은 열 덧셈 1은 행 덧셈 =>자주 나옴
print(d.sum(axis=1))

#길이가 1~10인 정사각형 중, 길이가 짝수인 정사각형 넓이
areas = []
#방법 1
# for i in range(1,11):
#     if i%2==0:
#         areas.append(i*i)
#방법2
areas=[i*i for i in range(1,11) if i %2==0]
#for문을 돌면서 i를 하나씩 가져오고, if 조건에 맞는 i만 계산하는 데로 보낸다.
#구문 작성
print('areas:',areas)

#[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
areas2=[(i,j) for i in range(3) for j in range(3)]          # 이중 for문
print('areas2:',areas2)

students = ['아톰','똘이','몽키','철이']
for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다.'.format(number+1,name))          #.format: .앞의 형식으로 표현형식 지정=>자주쓰임

#{'1':"아톰",'2':"똘이"}
stu_dic={
   '{}번'.format(number+1):name for number,name in enumerate(students)
}
print(stu_dic)

#zip
students = ['아톰','똘이','몽키','철이']
scores = [80,70,90,100]
stu_dic2={
    students[number]:scores[number] for number,name in enumerate(students)
}
stu_dic3={
    students:scores for students,scores in zip(students,scores)
}
print(stu_dic3)

a1=[i for i in range(5)]
print(a1)

a2=[0 for i in range(5)]
print(a2)

a3=[0 for _ in range(5)]            #i가 의미가 없기 때문에  '_'로 바꾸어도 된다.
print(a3)

a4=[[0,1] for i in range(5)]        #행렬을 구성하는 요소를 주어도 만족한다.
print(a4)

a5=[[i,1] for i in range(5)]
print(a5)

a6=[[i,i*2+1] for i in range(5)]       # 요소들의 초기화에 사용 한다.
print(a6)

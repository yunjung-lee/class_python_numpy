# range(5) : 범위가 있는 레인지를 만든다.
print(range(5))
print(list(range(5)))           #list로 만들 수 있다.list와 배열은 다르다.
print(list(range(0,5)))         #print(list(range(5)))와 동일 값을 가진다.
print(list(range(3,8)))         #범위를 지정
print(list(range(3,8,2)))       #간격을 줄 수 있다. :  이 경우 홀수만이라고 말할 수 있다.
print(list(range(8,-5,-2)))     #8~-4까지의 짝수

#sort 함수  : 리턴 값이 없는 함수
#sorted함수 :  값 정렬 후 결과를 리스트로 리턴하는 함수

print(sorted([5,3,4]))
print(sorted(['d','t','c','b']))
print(sorted("seoul"))

ss= sorted([5,3,4])
print(ss)
print(type(ss))

data= sorted([5,3,4])
print(sorted(data))
print(data)

data2=[5,3,4]
print(data2.sort())         #None
data2.sort()
print(data2)

#ZIP 함수 : 자료들을 묶어주는 함수(자료들은 동일한 갯수로 이루어져 있어야 한다.)
print(list(zip([1,2,3])))           #인수들이 많아야 의미가 있다.
print(list(zip([1,2,3],[4,5,6])))   #tuple형태로 출력
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip([1,2],[4,5,6])))     #짝이 맞지 않을 때 (맞는 것만 표현)
print(list(zip('xyz','ijk')))

print('='*15,'내 장 함 수','='*15) # python설치시 무조건 깔려있는 함수

print('='*15,'외 장 함 수','='*15)
#pickle :  객체 상태를 유지하면서 파일 입출력 모듈
#dump 함수를 이용하여 사용

import pickle                       #객체 저장/로드
f=open('sleep.txt','wb')             #write binary
#{} :딕셔너리 -중첩가능(메모리 한계), -키 하나에 객체가 여러개 가능
data = {1:'big', 2:'data'}
pickle.dump(data,f)                 #대상을 저장,어디에..,기능 안에 write기능이 있다.
# f.write(data)                       #딕셔너리와 같은 객체의 상태를 유지하면서 파일 입출력이 가능하게 만드는 모듈
f.close()

f=open('sleep.txt','rb')
data = pickle.load(f)
print(data)


#glob : 특정 파일(ex : cvs)을 가져오는 함수
import glob
print(glob.glob('s*'))

#random : 난수(컴퓨터 수: 컴퓨터에서 임의로 생성 ->0~1까지의 임의의 수) 생성 함수
#정규분포(분포도를 갖는 난수 타입),균등분포(일정한 간격을 가진 분포) 등으로 생성
import random
print(random.random())
for i in range(1,7):
   a=(random.randint(1,46))
   print(a)

a=set([1,2,2,3])
print(len(a))


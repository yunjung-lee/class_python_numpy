#map(적용하고자 하는 함수,데이터) : 데이터를 함수에 적용해라 => 다른 함수들과 복합적으로 사용되어진다.

def two_times(num):
    res=[]
    for n in num :
        res.append(num*n)
    return res

print(two_times([1,2,3]))
#결과 값이 none : 함수 호출하여 수행한 결과가 리턴되지 않았다(return 문의 부재=>return res 삽입)

def two_times(num):
    res=[]
    for n in num :
        res.append(num*2)
        return res              #return 의 위치 때문에 반복되지 못하고 끝난다.

print(two_times([1,2,3]))


def two_times(num):
    res=[]
    for n in num :
        res.append(n*2)
    return res

print(two_times([1,2,3]))


def two_times(num):
    res=[]
    for n in num :
        res.append(n*2)
    return res

res = two_times([1,2,3])
print(res)

def two_times(num):
    res=[]
    for n in num :
        res.append(n*2)

res = two_times([1,2,3])
print(res)

def two_times(num) :  return num*2
print(map(two_times,[1,2,3]))       #함수 객체의 주소 호출 : <map object at 0x0150D210>
# map 함수를 출력하면 map객체가 나온다.
#map 함수 결과를 리스트로 변환하여 보이기 위해 list함수를 사용한다.

def two_times(num) :  return num*2
print(list(map(two_times,[1,2,3])))

#lambda함수 : 함수 구문을 간략화 시키는데 목적이 있다.
print(list(map(lambda x:x*2 ,[1,2,3])))

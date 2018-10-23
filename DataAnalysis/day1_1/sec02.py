#함수 :  어떤 기능을 수행하는 것
# 1. 사용자가 직접 만든 함수
# 2. 제공되는 함수

def sum(a,b) : #함수 정의
    return  a+b

print(sum(3,5)) #함수 호출

def sum2(*v) :  #함수 정의와 호출의 인수는 동일 갯수 여야 한다. =TypeError: sum2() takes 1 positional argument but 2 were given : *사용 =>인수의 갯수와 상관없이 전달받고자 한다
    sum = 0
    for i in v:
        sum +=i
    return sum
print(sum2(1,2))
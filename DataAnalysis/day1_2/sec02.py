print(abs(-2))            #절대값
print(all([2,5,-7,'a']))  #모두가 참이냐? 0이 거짓이기 때문에 0이 없으면(0이 아닌 모든수) 참
print(any([1,2,0]))       #하나라도 참이면 참
print(any([0,""]))        # ""도 거짓

name = ['dildong', 'sunsin', "sejong"]
for n in name :
    print(n)

for n in ['dildong', 'sunsin', "sejong"]:
    print(n)

#enumerate : index가 포함되어있는 형식으로 리턴되는 함수
for n in enumerate(['dildong', 'sunsin', "sejong"]):
    print(n[1]) #순서나 이름만을 불러올 수 있다.

    # (0, 'dildong')
    # (1, 'sunsin')
    # (2, 'sejong')

for i,n in enumerate(['dildong', 'sunsin', "sejong"]):
    print(i,n)


#  eval()              #문자열로 된 수식,함수 등을 실행한 결과값을 리턴해주는 함수
print(eval('1+2'))

print(eval('int(3.14)'))

a=input("입력하세요")   #입력값은 녹색 : scanner class , java와 다르기 때문에 타입지정이 없어도 됨
print(a)

print(len("today"))     #len으로 길이를 확인 할 수 있다.
print(type("today"))    # <class 'str'>
print(len([3,4,5]))
print(type([3,4,5]))    #<class 'list'>
print(type(['t','o','d','a','y']))  #<class 'list'>
print(list("today"))

a=list("today")
print(type(a))






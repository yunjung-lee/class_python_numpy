a= 4.2E7 #4.2*10의 7승
print(a)

a= 4.2E-7 #4.2*10의 -7승
print(a)

print(7/4) #1.75
print(7//4) #1 : 몫
print(7%4) #나머지
msg="""
Life is \ntoo short
You need Python
"""
#\t : tap, \n : 줄바꾸기
print(msg)

print("-"*100)

a="Life"
print(a[-2])
print(a[1:3])
#[시작: 끝+1]

print("I eat {0} apples. so I was sick for {1} days". format(3,5)) #format function 인자는  , 로 구분 : 1,0의 숫자는 위치를 바꿔도 된다.

pi=3.14
print("{0:10.4f}".format(pi))
#10.4f : 10자리 숫자를 소숫점 4째짜리까지 표현하는 형식으로 표현하라

a=","
print(a.join('abcd')) #a를 join하는 변수에 집어 넣어라

msg="Life is too short"
msg = msg.replace("Life","Your leg")
print(msg)

print(msg.split()) # 공백문자를 기준으로 자르기 => list 형태로 나타남
msg2 = "life : is :too : short"
print(msg2.split(":"))

a = [1,2,3,['a','b','c']]
print(a[-1][0])  #a[-1]을 하나의 변수로 보고 다시 위치[0]를 넣으면 된다.

a = [1,2,3,['a','b',['c','d']]]
print(a[3][2][0])

print("="*50)

a=[4,5,6]
a[2]=7
print(a)
print(a[1:2])

a[1:2]=['a','b','c'] #  len(a) = 5, [4,a,b,c,7]
# a[1]=['a','b','c'] :  len(a) = 3, [4,[a,b,c],7]
print(a)
print(len(a))

# a[1:3]=[]   : del과 같은 기능
del a[1:3]
print(a)

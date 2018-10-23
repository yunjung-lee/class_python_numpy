#함축적 for 문
#자료 구조 연습 리스트(라이브러리와 티플은 잘 안쓰인다.)와 키라이브러리
#정규표현식 : 빈번한 작업을 간단하게 만들게 된다.
# 패키지들

#함축적 for문  : 리스트 아래 작성 가능

a = [1,2,3,4]
res = []
for num in a:
    res.append(num*2)
print(res)

#리스트 내포 이용한 코드 : 코드가 간결해지는 장점

res = [num*2 for num in a]
print(res)

#a  리스트의 요소값이 짝수인 경우만 2배를 하여 res에 저장 , 홀수는 그대로
#[1,2,3,4] => [1,4,3,8]
res = [num*2 for num in a if num%2==0]
print(res)

res=[x*y for x in range(2,5)
        for y in range(1,10)]
print(res)


#[표현식 for 항목1 in 반복개체 if 조건문1
        # for 항목2 in 반복개체 if 조건문2
        # for 항목3 in 반복개체 if 조건문3
        # for 항목4 in 반복개체 if 조건문4
        # for 항목5 in 반복개체 if 조건문5]

a = [1,2,3,4,5]
res = []
for n in a:
    if n % 2 ==1:
        res.append(n*2)
    else:
        res.append(n)
print(res)

res = [n*2  if n%2 ==1  else n for n in a ]
print(res)

msg = "How are you? fine thank you. and you?"

#리스트 내포를 이용하여 모음(aeiou)을 제거를 한 후 msg출력

#msg = [n for n in msg ]  # 리스트의 요소로 분해
v='aeiou'
print([''.join(a for a in msg if a not in v)])

msg = [''.join(n for n in msg if n !='a'and n !='e' and n !='i'and n !='o'and n !='u')]
print(msg)

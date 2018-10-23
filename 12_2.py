#빅데이터 분석, 딥러닝, 머신 러닝

import random

#seed : 주어진 숫자를 바탕으로 난수 생성(발생한 난수는 바뀌지 않는다.)
random.seed(999)
#난수 발생 5를 지정하였기에 0~4까지 난수발생
a=[random.randrange(100) for _ in range(10)]
print(a)
#데이터 -> 훈련데이터(주어진 데이터의 70% 정도)/테스트데이터(30%) -> 모델 -> 테스트데이터입력 -> 모델평가 -> 평가 결과에 따른 feedback
#알고리즘을 바꿔 모델을 바꿨을 때 학습 및 테스트 데이터가 바뀌면 비교할 수 없으므로 같은 데이터를 바뀌지 않아야 한다.
#데이터는 랜덤하게 훈련데이터와 테스트 데이터를 나누기 때문에 나오는 랜덤으로 나오는 숫자가 항상 같기 위해 seed를 이용한다.

print([i for i in range(10)])           #9까지숫자 리스트로 출력

print([i for i in a])                   #random a가 리스트로 출력
#a=[86, 10, 72, 73, 68, 62, 61, 16, 82, 40]
print([i for i in a if i % 2])          #i % 2이 if를 만나서 거짓이 됨

print([i for i in a if i % 2][::-1])     # 출력을 역순으로

print([i for i in a [::-1] if i % 2])   # a를 불러올 때 역순으로

print([i for i in reversed(a) if i % 2])

a1=[random.randrange(100) for _ in range(10)]
a2=[random.randrange(100) for _ in range(10)]
a3=[random.randrange(100) for _ in range(10)]
b=[a1,a2,a3]
print(b)
print(sum([1,3,5]))

print([sum(i) for i in b])
print(sum([sum(i) for i in b]))

print([0 for i in b for j in i])            #차원 감소: 차원에서 data를 빼내서 1차원의 리스트화
                                            #차원 축소(PCA) : 차원의 축소를 위해서 data의 가공이 들어가기 때문에 data가 변한다.
print([i for i in b])

print([j for i in b for j in i if j % 2])

print([[j for j in i] for i in b])

print([[j for j in i if j % 2] for i in b])     #for 중첩구문일때 마지막 for의 오른쪽에서 행과 열을 판단

print("="*50)
print(b)
print([i for i in b[::-1]])                 #행바꿈
print([[j for j in i[::-1]] for i in b[::-1]])          #행과 열을 모두 바꿈

print(2**1000)
print(str(2**1000))
print(len(str(2**1000)))

#2**1000에 들어가는 숫자들의 합을 구하시오.
d=0
a= str(2**1000)
b=[i for i in a]

print(b)
print(len(b))
for i in b:
    d+=int(i)
print(d)

print(sum([int(i) for i in str(2**1000)]))

s='707'
print(s.count('7'))             #s에 7이 2개 있다는 의미

#1~100000 사이에 있는 7의 갯수를 세어보세요.
a=[str(i) for i in range(1,100001)]
print("_".join(a).count('7'))

#maria={'kor:94,'eng':91,'math':89,'sci':83}
#maria 딕셔너리에 저장된 점수의 평균을 출력하세요
import numpy as np

maria={'kor':94,'eng':91,'math':89,'sci':83}
a=np.mean([j for j in maria.values()])
print(a)

#어떤 자연수 n이 있을 때, d(n) 을 n의 각 자릿수 숫자들과 n자신을 더한 숫자라고 정의하자.
#예를들어 d(91) = 9 + 1 +91 = 101
#이 때, n을 d(n)의 제니레이터라고 한다. 91은 101의 제네레이터이다.
#어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91뿐 아니라 100도 있다.
#그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 셀프 넘버(self-number)라 한다.
#예를 들어 1,3,5,7,9,20,31은 셀프 넘버들이다.
#1이상이고 5000보다 작은 모든 셀프 넘버들의 합을 구하여라.


n=[[i for i in str(b)] for b in range(1,5000)]
for b in range(1,5000):
    n[b-1].append(str(b))
m=list(map(int,i) for i in n)
print(sum(set(range(1,5000)-set(m.sum(axis=1)))))




#print(m.sum(axis=0))
print(n)
# i=567
# for t in str(i):
#     print(int(t)+1)
#
# set(range(1,5))-set(range(1,3))             #{1,2,3,4}-{1,2}={3.4}







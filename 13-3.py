import numpy as np

#trees = np.loadtxt('Data/trees.csv', delimiter=",",skiprows=1)                  #shape : (31, 3)
#delimiter="," : 구분자(나눌때)를 이용해서 나눠서 읽어드림 ,skiprows=1(첫줄부터 몇번째 줄까지 없앨것인지
trees = np.loadtxt('Data/trees.csv', delimiter=",",skiprows=1,unpack=True)          #shape :(3, 31)
# unpack=True : 행과 열의 전환(읽어들이는 방식부터 바뀜)
print(trees.shape)           #31행 3열 -> 3열 31행(unpack=True)
print(trees[:-1])           # 둘레, 높이 (회귀 모델의 x1,x2)
print("="*50)
print(trees[[-1]])          #부피 (회귀모델의 y)
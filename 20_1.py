####################데이터프레임의 문자열 컬럼들을 합치는 등의 작업으로 새로운 컬럼 생성#######################################
#이용함수 apply


import pandas as pd
import numpy as np
from pandas import DataFrame, Series

# df = pd.DataFrame({'id' : [1,2,10,20,100,200],
#                    "name":['aaa','bbb','ccc','ddd','eee','fff']})
# print(df)
#
# #컬럼을 변경하여 새로운 컬럼을 생성
# #새로운 id 컬럼을 원래의 id 컬럼을 기준으로 자리수를 맞춰주기 위해 5자리로 통일(부족한 자릿수는 앞자리에 0을 채워 넣는다.)하며 만듬
# df['id_2']=df['id'].apply(lambda x:"{:0>5d}".format(x))
# print(df)
# #     id name   id_2
# # 0    1  aaa  00001
# # 1    2  bbb  00002
# # 2   10  ccc  00010
# # 3   20  ddd  00020
# # 4  100  eee  00100
# # 5  200  fff  00200
#
# # #format():앞자리의 형식으로 ()안의 인자의 모양을 바꿔준다.
# #
# # x=3.141592
# # print("{:.2f}".format(x))
# # # 3.14
# #
# # print("{:+.2f}".format(x))
# # # +3.14
# #
# # x=-3.141592
# # print("{:+.2f}".format(x))
# # # -3.14
# #
# # x=2.718
# # print("{:.0f}".format(x))                                           # 정수를 출력하라(소수 점 첫째자리에서 반올림)
# # # 3
# #
# # x=3.147592
# # print("{:.2f}".format(x))                                           # .2f(소수 점 셋째자리에서 반올림)
# # # 3.15
# #
# # x=5
# # print("{:0>2d}".format(x))                                          # 0>2D(D: 너비가 2, 0으로 채워라 )
# # # 05
# #
# # x=7777777777
# # print("{:0>5d}".format(x))                                          # 0>2D(D: 너비가 5, 0으로 채워라 ,너비 이상은 무시=>원 형태 유지)
# # # 7777777777
# # print("{:,}".format(x))
# # # 7,777,777,777
# #
# # x=0.25
# # print("{:.2%}".format(x))
# # # 25.00%
# #
#
# #name + id_2 :재구성 => 두개의 컬럼이 결합(apply대상이 2개의 컬럼이 됨)
# df['id_name'] = df[['id_2','name']].apply(lambda  x: '_'.join(x))               #축을 지정 하지 않으면 안됨
# print(df)
# #     id name   id_2 id_name
# # 0    1  aaa  00001     NaN
# # 1    2  bbb  00002     NaN
# # 2   10  ccc  00010     NaN
# # 3   20  ddd  00020     NaN
# # 4  100  eee  00100     NaN
# # 5  200  fff  00200     NaN
#
# df['id_name'] = df[['id_2','name']].apply(lambda  x: '_'.join(x),axis=1)               #축을 1로 지정
# print(df)
# #     id name   id_2    id_name
# # 0    1  aaa  00001  00001_aaa
# # 1    2  bbb  00002  00002_bbb
# # 2   10  ccc  00010  00010_ccc
# # 3   20  ddd  00020  00020_ddd
# # 4  100  eee  00100  00100_eee
# # 5  200  fff  00200  00200_fff
#
# df['id_name'] = df[['id_2','name']].apply(lambda  x: '_'.join(x),axis=1)
# print(df)
# #     id name   id_2    id_name
# # 0    1  aaa  00001  00001_aaa
# # 1    2  bbb  00002  00002_bbb
# # 2   10  ccc  00010  00010_ccc
# # 3   20  ddd  00020  00020_ddd
# # 4  100  eee  00100  00100_eee
# # 5  200  fff  00200  00200_fff
#
#
# #id를 소숫점 이하로 나타내는 새로운 열을 추가
# df['id_3']=df['id'].apply(lambda x: "{:.2f}".format(x))
# print(df)
# #     id name   id_2    id_name    id_3
# # 0    1  aaa  00001  00001_aaa    1.00
# # 1    2  bbb  00002  00002_bbb    2.00
# # 2   10  ccc  00010  00010_ccc   10.00
# # 3   20  ddd  00020  00020_ddd   20.00
# # 4  100  eee  00100  00100_eee  100.00
# # 5  200  fff  00200  00200_fff  200.00
#
# df['name_3']=df['name'].apply(lambda x:x.upper())                                       #upper() : 대문자로 바꿔줌
# print(df)
# #     id name   id_2    id_name    id_3 name_3
# # 0    1  aaa  00001  00001_aaa    1.00    AAA
# # 1    2  bbb  00002  00002_bbb    2.00    BBB
# # 2   10  ccc  00010  00010_ccc   10.00    CCC
# # 3   20  ddd  00020  00020_ddd   20.00    DDD
# # 4  100  eee  00100  00100_eee  100.00    EEE
# # 5  200  fff  00200  00200_fff  200.00    FFF
#
#
# # id_name_3  컬럼추가
# # id_name_3  => 1.00:AAA
#
# df['id_name_3'] = df[['id_3','name_3']].apply(lambda x: ':'.join(x),axis=1)
# print(df)
# #     id name   id_2    id_name    id_3 name_3   id_name_3
# # 0    1  aaa  00001  00001_aaa    1.00    AAA    1.00:AAA
# # 1    2  bbb  00002  00002_bbb    2.00    BBB    2.00:BBB
# # 2   10  ccc  00010  00010_ccc   10.00    CCC   10.00:CCC
# # 3   20  ddd  00020  00020_ddd   20.00    DDD   20.00:DDD
# # 4  100  eee  00100  00100_eee  100.00    EEE  100.00:EEE
# # 5  200  fff  00200  00200_fff  200.00    FFF  200.00:FFF
#

###################################################################################################################
#groupby 집계함수
# 1.딕셔너리를 이용해서 그룹화

#위.. 딕셔너리로 만들어서 열을 키로 자료를 밸류로 나타냄
# data= : 데이터를 넣고 컬럼과 인덱스로 자료를 구분.
df = DataFrame(data=np.arange(20).reshape(4,5),columns=['c1','c2','c3','c4','c5'],index=['r1','r2','r3','r4'])
print(df)
#     c1  c2  c3  c4  c5
# r1   0   1   2   3   4
# r2   5   6   7   8   9
# r3  10  11  12  13  14
# r4  15  16  17  18  19

# row_g1 = r1+r2 : 행단위 계산으로 새로운 행 생성(같은 열의 성분이 더해진다.: sum())
# row_g2 = r3+r4
mdr = {'r1':'row_g1','r2':'row_g2','r3':'row_g3','r4':'row_g4'}
gbr = df.groupby(mdr)
print(gbr.sum())
#         c1  c2  c3  c4  c5
# row_g1   0   1   2   3   4
# row_g2   5   6   7   8   9
# row_g3  10  11  12  13  14
# row_g4  15  16  17  18  19

mdr = {'r1':'row_g1','r2':'row_g1','r3':'row_g2','r4':'row_g2'}
gbr = df.groupby(mdr)
print(gbr.sum())
#         c1  c2  c3  c4  c5
# row_g1   5   7   9  11  13
# row_g2  25  27  29  31  33

print(gbr.mean())
#           c1    c2    c3    c4    c5
# row_g1   2.5   3.5   4.5   5.5   6.5
# row_g2  12.5  13.5  14.5  15.5  16.5

print(gbr.std())
#               c1        c2        c3        c4        c5
# row_g1  3.535534  3.535534  3.535534  3.535534  3.535534
# row_g2  3.535534  3.535534  3.535534  3.535534  3.535534


# col_g1 = c1+c2 : 열단위 계산으로 새로운 열 생성(같은 행의 성분이 더해진다.: sum()) : 꼭 axis = 1을주어야 한다.
# col_g2 = c3+c4+c5
mdc = {'c1':'col_g1','c2':'col_g1','c3':'col_g2','c4':'col_g2','c5':'col_g2'}
gbc = df.groupby(mdc,axis=1)                                                            #꼭 axis = 1을주어야 한다.
print(gbc.sum())
#     col_g1  col_g2
# r1       1       9
# r2      11      24
# r3      21      39
# r4      31      54


print(type(mdr))
# <class 'dict'>

print(mdr)
# {'r1': 'row_g1', 'r2': 'row_g1', 'r3': 'row_g2', 'r4': 'row_g2'}


# dic -> Series
# Series를 이용한 그룹화

msr = Series(mdr)
print(type(msr))
# <class 'pandas.core.series.Series'>

print(msr)
# r1    row_g1
# r2    row_g1
# r3    row_g2
# r4    row_g2
# dtype: object

print(df.groupby(msr).sum())                                        # 딕셔너리와 같은 결과
#         c1  c2  c3  c4  c5
# row_g1   5   7   9  11  13
# row_g2  25  27  29  31  33

msc = Series(mdc)
print(df.groupby(msc,axis=1).sum())
#     col_g1  col_g2
# r1       1       9
# r2      11      24
# r3      21      39
# r4      31      54

#함수를 이용한 그룹화
# 딕셔너리나 시리즈 대신 선언되는 rgf로 그룹화(df에 대한 정보가 x에 전달)
def rgf(x) :
    if x == 'r1' or x == 'r2':
        rg = 'row_g1'
    else:
        rg = 'row_g2'
    return rg

# 딕셔너리나 시리즈의 모습에 맞춰서 그룹화 하여 그룹화 계산 함수의 결과에 맞춰 데이터프레임 생성
print(df.groupby(rgf).sum())




















































































































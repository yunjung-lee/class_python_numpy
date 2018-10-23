import pandas as pd
from pandas import DataFrame,Series
import numpy as np

# abalone = pd.read_csv('abalone.txt',sep=',',names=['Sex', 'Length', 'Diam', 'Height',	'Whole_weight',	'Shucked_weight',	'Viscera_weight',	'Shell_weight','Rings'],header=None)
# print(abalone)
# #      Sex  Length   Diam  ...    Viscera_weight  Shell_weight  Rings
# # 0      M   0.455  0.365  ...            0.1010        0.1500     15
# # [4177 rows x 9 columns]
#
# print(np.sum(pd.isnull(abalone)))                                    #true :  결측치 ,sum :  true만 계산
# # Sex               0
# # Length            0
# # Diam              0
# # Height            0
# # Whole_weight      0
# # Shucked_weight    0
# # Viscera_weight    0
# # Shell_weight      0
# # Rings             0
# # dtype: int64
#
# print(abalone.describe())                                           #describe() : 기술 통계를 구하는 함수==R의 summary()
# grouped = abalone['Whole_weight'].groupby(abalone['Sex'])
# print(grouped)
# # [8 rows x 8 columns]
# # <pandas.core.groupby.groupby.SeriesGroupBy object at 0x07A64770>
#
# print(grouped.size())                                                #그룹단위의 크기
# # Sex
# # F    1307
# # I    1342
# # M    1528
# # Name: Whole_weight, dtype: int64
#
# print(grouped.sum())                                                #그룹단위의 '전체 무게의 합계
# # Sex
# # F    1367.8175
# # I     578.8885
# # M    1514.9500
# # Name: Whole_weight, dtype: float64
#
# print(grouped.mean())                                                #그룹단위의 '전체 무게의 평균
# # Sex
# # F    1.046532
# # I    0.431363
# # M    0.991459
# # Name: Whole_weight, dtype: float64
#
# print(abalone.groupby(abalone['Sex']).mean())                       #abalone의 'Sex'를 기준으로 그룹화 한 뒤 열단위 평균
# #        Length      Diam    ...      Shell_weight      Rings
# # Sex                        ...
# # F    0.579093  0.454732    ...          0.302010  11.129304
# # I    0.427746  0.326494    ...          0.128182   7.890462
# # M    0.561391  0.439287    ...          0.281969  10.705497
# #
# # [3 rows x 8 columns]
#
# print(abalone.groupby(abalone['Sex']).mean())
#
# # np.where(조건, 참, 거짓)
# abalone['length_cat'] = np.where(abalone.Length>np.median(abalone.Length),'length_long','length_short')     # length_cat : 범주형 변수
#
# print(abalone[['Length','length_cat']][:10])
#
# # sex   length_cat
# # F    length_long :  평균값(Whole_weigth)
# # F    length_short
# # I    0.431363
# # M    0.991459
#
# print(abalone['Whole_weight'].groupby([abalone['Sex'],abalone['length_cat']]).mean())
# # Sex  length_cat
# # F    length_long     1.261330
# #      length_short    0.589702
# # I    length_long     0.923215
# #      length_short    0.351234
# # M    length_long     1.255182
# #      length_short    0.538157
# # Name: Whole_weight, dtype: float64
#
# print(abalone.groupby(['Sex','length_cat'])['Whole_weight'].mean())
# # Sex  length_cat
# # F    length_long     1.261330
# #      length_short    0.589702
# # I    length_long     0.923215
# #      length_short    0.351234
# # M    length_long     1.255182
# #      length_short    0.538157
# # Name: Whole_weight, dtype: float64
#
# #성별로 그룹화 한 다음, for문 사용하여 그룹 이름별로 데이터셋을 출력
# print('='*50)
# print(abalone[['Sex','length_cat','Whole_weight','Rings']])
#
# print(abalone[['Sex','length_cat','Whole_weight','Rings']].groupby('Sex').mean())
# #      Whole_weight      Rings
# # Sex
# # F        1.046532  11.129304
# # I        0.431363   7.890462
# # M        0.991459  10.705497
#
#
# # abalone의 4개의 열에 대해서 성별에 대해 그룹화 함: 성별에 대해 그룹화 한 데이타 정보까지 오는 것
#
# print('='*50)
# for sex, group_data in abalone[['Sex','length_cat','Whole_weight','Rings']].groupby('Sex'):
#     print(sex)
#     #      Sex    length_cat  Whole_weight  Rings
#     # 0      M  length_short        0.5140     15
#     # 1      M  length_short        0.2255      7
#     # ...   ..           ...           ...    ...
#     # 4176   M   length_long        1.9485     12
#     #
#     # [4177 rows x 4 columns]
#     print(group_data[:5])
#     print(group_data[:5])
#     #     Whole_weight      Rings
#     # Sex
#     # F        1.046532  11.129304
#     # I        0.431363   7.890462
#     # M        0.991459  10.705497
#
# print('='*50)
# for (sex,length_cat), group_data in abalone[['Sex','length_cat','Whole_weight','Rings']].groupby(['Sex','length_cat']):
#     print(sex)
#
#
# df=DataFrame([[1.4,np.nan],
#               [7.1,-4.5],
#               [np.nan,np.nan],
#               [0.75,-1.3]],
#              index=['a','b','c','d'],
#              columns=['one','two'])
# print(df)
# #     one  two
# # a  1.40  NaN
# # b  7.10 -4.5
# # c   NaN  NaN
# # d  0.75 -1.3
# print(df.sum())
# # one    9.25
# # two   -5.80
# # dtype: float64
#
# print(df.sum(axis =1))
# # a    1.40
# # b    2.60
# # c    0.00
# # d   -0.55
# # dtype: float64
#
# print(df.mean())
# # one    3.083333
# # two   -2.900000
# # dtype: float64
#
# print(df.mean(axis = 1))
# # a    1.400
# # b    1.300
# # c      NaN
# # d   -0.275
# # dtype: float64
#
# # print(df.mean(axis = 1), skipna=False)
#
# print('='*50)
#
# print(df)
# print(df.idxmax())
# # one    b
# # two    d
# # dtype: object

import json

db = json.load(open('database.json'))
print(len(db))
# 6636
print(db[0])
# {'id': 1008, 'description': 'Cheese, caraway', 'tags': [], 'manufacturer': '', 'group': 'Dairy and Egg Products', 'portions': [{'amount': 1, 'unit': 'oz', 'grams': 28.35}], 'nutrients': [{'value': 25.18, 'units': 'g', 'description': 'Protein', 'group': 'Composition'}, {'value': 29.2, 'units': 'g', 'description': 'Total lipid (fat)', 'group': 'Composition'}, {'value': 3.06, 'units': 'g', 'description': 'Carbohydrate, by difference', 'group': 'Composition'}, {'value': 3.28, 'units': 'g', 'description': 'Ash', 'group': 'Other'}, {'value': 376.0, 'units': 'kcal', 'description': 'Energy', 'group': 'Energy'}, {'value': 39.28, 'units': 'g', 'description': 'Water', 'group': 'Composition'}, {'value': 1573.0, 'units': 'kJ', 'description': 'Energy', 'group': 'Energy'}, {'value': 0.0, 'units': 'g', 'description': 'Fiber, total dietary', 'group': 'Composition'}, {'value': 673.0, 'units': 'mg', 'description': 'Calcium, Ca', 'group': 'Elements'}, {'value': 0.64, 'units': 'mg', 'description': 'Iron, Fe', 'group': 'Elements'}, {'value': 22.0, 'units': 'mg', 'description': 'Magnesium, Mg', 'group': 'Elements'}, {'value': 490.0, 'units': 'mg', 'description': 'Phosphorus, P', 'group': 'Elements'}, {'value': 93.0, 'units': 'mg', 'description': 'Potassium, K', 'group': 'Elements'}, {'value': 690.0, 'units': 'mg', 'description': 'Sodium, Na', 'group': 'Elements'}, {'value': 2.94, 'units': 'mg', 'description': 'Zinc, Zn', 'group': 'Elements'}, {'value': 0.024, 'units': 'mg', 'description': 'Copper, Cu', 'group': 'Elements'}, {'value': 0.021, 'units': 'mg', 'description': 'Manganese, Mn', 'group': 'Elements'}, {'value': 14.5, 'units': 'mcg', 'description': 'Selenium, Se', 'group': 'Elements'}, {'value': 1054.0, 'units': 'IU', 'description': 'Vitamin A, IU', 'group': 'Vitamins'}, {'value': 262.0, 'units': 'mcg', 'description': 'Retinol', 'group': 'Vitamins'}, {'value': 271.0, 'units': 'mcg_RAE', 'description': 'Vitamin A, RAE', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mg', 'description': 'Vitamin C, total ascorbic acid', 'group': 'Vitamins'}, {'value': 0.031, 'units': 'mg', 'description': 'Thiamin', 'group': 'Vitamins'}, {'value': 0.45, 'units': 'mg', 'description': 'Riboflavin', 'group': 'Vitamins'}, {'value': 0.18, 'units': 'mg', 'description': 'Niacin', 'group': 'Vitamins'}, {'value': 0.19, 'units': 'mg', 'description': 'Pantothenic acid', 'group': 'Vitamins'}, {'value': 0.074, 'units': 'mg', 'description': 'Vitamin B-6', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, total', 'group': 'Vitamins'}, {'value': 0.27, 'units': 'mcg', 'description': 'Vitamin B-12', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mcg', 'description': 'Folic acid', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, food', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg_DFE', 'description': 'Folate, DFE', 'group': 'Vitamins'}, {'value': 93.0, 'units': 'mg', 'description': 'Cholesterol', 'group': 'Other'}, {'value': 18.584, 'units': 'g', 'description': 'Fatty acids, total saturated', 'group': 'Other'}, {'value': 8.275, 'units': 'g', 'description': 'Fatty acids, total monounsaturated', 'group': 'Other'}, {'value': 0.83, 'units': 'g', 'description': 'Fatty acids, total polyunsaturated', 'group': 'Other'}, {'value': 0.324, 'units': 'g', 'description': 'Tryptophan', 'group': 'Amino Acids'}, {'value': 0.896, 'units': 'g', 'description': 'Threonine', 'group': 'Amino Acids'}, {'value': 1.563, 'units': 'g', 'description': 'Isoleucine', 'group': 'Amino Acids'}, {'value': 2.412, 'units': 'g', 'description': 'Leucine', 'group': 'Amino Acids'}, {'value': 2.095, 'units': 'g', 'description': 'Lysine', 'group': 'Amino Acids'}, {'value': 0.659, 'units': 'g', 'description': 'Methionine', 'group': 'Amino Acids'}, {'value': 0.126, 'units': 'g', 'description': 'Cystine', 'group': 'Amino Acids'}, {'value': 1.326, 'units': 'g', 'description': 'Phenylalanine', 'group': 'Amino Acids'}, {'value': 1.216, 'units': 'g', 'description': 'Tyrosine', 'group': 'Amino Acids'}, {'value': 1.682, 'units': 'g', 'description': 'Valine', 'group': 'Amino Acids'}, {'value': 0.952, 'units': 'g', 'description': 'Arginine', 'group': 'Amino Acids'}, {'value': 0.884, 'units': 'g', 'description': 'Histidine', 'group': 'Amino Acids'}, {'value': 0.711, 'units': 'g', 'description': 'Alanine', 'group': 'Amino Acids'}, {'value': 1.618, 'units': 'g', 'description': 'Aspartic acid', 'group': 'Amino Acids'}, {'value': 6.16, 'units': 'g', 'description': 'Glutamic acid', 'group': 'Amino Acids'}, {'value': 0.439, 'units': 'g', 'description': 'Glycine', 'group': 'Amino Acids'}, {'value': 2.838, 'units': 'g', 'description': 'Proline', 'group': 'Amino Acids'}, {'value': 1.472, 'units': 'g', 'description': 'Serine', 'group': 'Amino Acids'}, {'value': 25.18, 'units': 'g', 'description': 'Protein', 'group': 'Composition'}, {'value': 29.2, 'units': 'g', 'description': 'Total lipid (fat)', 'group': 'Composition'}, {'value': 3.06, 'units': 'g', 'description': 'Carbohydrate, by difference', 'group': 'Composition'}, {'value': 3.28, 'units': 'g', 'description': 'Ash', 'group': 'Other'}, {'value': 376.0, 'units': 'kcal', 'description': 'Energy', 'group': 'Energy'}, {'value': 39.28, 'units': 'g', 'description': 'Water', 'group': 'Composition'}, {'value': 1573.0, 'units': 'kJ', 'description': 'Energy', 'group': 'Energy'}, {'value': 0.0, 'units': 'g', 'description': 'Fiber, total dietary', 'group': 'Composition'}, {'value': 673.0, 'units': 'mg', 'description': 'Calcium, Ca', 'group': 'Elements'}, {'value': 0.64, 'units': 'mg', 'description': 'Iron, Fe', 'group': 'Elements'}, {'value': 22.0, 'units': 'mg', 'description': 'Magnesium, Mg', 'group': 'Elements'}, {'value': 490.0, 'units': 'mg', 'description': 'Phosphorus, P', 'group': 'Elements'}, {'value': 93.0, 'units': 'mg', 'description': 'Potassium, K', 'group': 'Elements'}, {'value': 690.0, 'units': 'mg', 'description': 'Sodium, Na', 'group': 'Elements'}, {'value': 2.94, 'units': 'mg', 'description': 'Zinc, Zn', 'group': 'Elements'}, {'value': 0.024, 'units': 'mg', 'description': 'Copper, Cu', 'group': 'Elements'}, {'value': 0.021, 'units': 'mg', 'description': 'Manganese, Mn', 'group': 'Elements'}, {'value': 14.5, 'units': 'mcg', 'description': 'Selenium, Se', 'group': 'Elements'}, {'value': 1054.0, 'units': 'IU', 'description': 'Vitamin A, IU', 'group': 'Vitamins'}, {'value': 262.0, 'units': 'mcg', 'description': 'Retinol', 'group': 'Vitamins'}, {'value': 271.0, 'units': 'mcg_RAE', 'description': 'Vitamin A, RAE', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mg', 'description': 'Vitamin C, total ascorbic acid', 'group': 'Vitamins'}, {'value': 0.031, 'units': 'mg', 'description': 'Thiamin', 'group': 'Vitamins'}, {'value': 0.45, 'units': 'mg', 'description': 'Riboflavin', 'group': 'Vitamins'}, {'value': 0.18, 'units': 'mg', 'description': 'Niacin', 'group': 'Vitamins'}, {'value': 0.19, 'units': 'mg', 'description': 'Pantothenic acid', 'group': 'Vitamins'}, {'value': 0.074, 'units': 'mg', 'description': 'Vitamin B-6', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, total', 'group': 'Vitamins'}, {'value': 0.27, 'units': 'mcg', 'description': 'Vitamin B-12', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mcg', 'description': 'Folic acid', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, food', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg_DFE', 'description': 'Folate, DFE', 'group': 'Vitamins'}, {'value': 0.324, 'units': 'g', 'description': 'Tryptophan', 'group': 'Amino Acids'}, {'value': 0.896, 'units': 'g', 'description': 'Threonine', 'group': 'Amino Acids'}, {'value': 1.563, 'units': 'g', 'description': 'Isoleucine', 'group': 'Amino Acids'}, {'value': 2.412, 'units': 'g', 'description': 'Leucine', 'group': 'Amino Acids'}, {'value': 2.095, 'units': 'g', 'description': 'Lysine', 'group': 'Amino Acids'}, {'value': 0.659, 'units': 'g', 'description': 'Methionine', 'group': 'Amino Acids'}, {'value': 0.126, 'units': 'g', 'description': 'Cystine', 'group': 'Amino Acids'}, {'value': 1.326, 'units': 'g', 'description': 'Phenylalanine', 'group': 'Amino Acids'}, {'value': 1.216, 'units': 'g', 'description': 'Tyrosine', 'group': 'Amino Acids'}, {'value': 1.682, 'units': 'g', 'description': 'Valine', 'group': 'Amino Acids'}, {'value': 0.952, 'units': 'g', 'description': 'Arginine', 'group': 'Amino Acids'}, {'value': 0.884, 'units': 'g', 'description': 'Histidine', 'group': 'Amino Acids'}, {'value': 0.711, 'units': 'g', 'description': 'Alanine', 'group': 'Amino Acids'}, {'value': 1.618, 'units': 'g', 'description': 'Aspartic acid', 'group': 'Amino Acids'}, {'value': 6.16, 'units': 'g', 'description': 'Glutamic acid', 'group': 'Amino Acids'}, {'value': 0.439, 'units': 'g', 'description': 'Glycine', 'group': 'Amino Acids'}, {'value': 2.838, 'units': 'g', 'description': 'Proline', 'group': 'Amino Acids'}, {'value': 1.472, 'units': 'g', 'description': 'Serine', 'group': 'Amino Acids'}, {'value': 93.0, 'units': 'mg', 'description': 'Cholesterol', 'group': 'Other'}, {'value': 18.584, 'units': 'g', 'description': 'Fatty acids, total saturated', 'group': 'Other'}, {'value': 8.275, 'units': 'g', 'description': 'Fatty acids, total monounsaturated', 'group': 'Other'}, {'value': 0.83, 'units': 'g', 'description': 'Fatty acids, total polyunsaturated', 'group': 'Other'}, {'value': 25.18, 'units': 'g', 'description': 'Protein', 'group': 'Composition'}, {'value': 29.2, 'units': 'g', 'description': 'Total lipid (fat)', 'group': 'Composition'}, {'value': 3.06, 'units': 'g', 'description': 'Carbohydrate, by difference', 'group': 'Composition'}, {'value': 3.28, 'units': 'g', 'description': 'Ash', 'group': 'Other'}, {'value': 376.0, 'units': 'kcal', 'description': 'Energy', 'group': 'Energy'}, {'value': 39.28, 'units': 'g', 'description': 'Water', 'group': 'Composition'}, {'value': 1573.0, 'units': 'kJ', 'description': 'Energy', 'group': 'Energy'}, {'value': 0.0, 'units': 'g', 'description': 'Fiber, total dietary', 'group': 'Composition'}, {'value': 673.0, 'units': 'mg', 'description': 'Calcium, Ca', 'group': 'Elements'}, {'value': 0.64, 'units': 'mg', 'description': 'Iron, Fe', 'group': 'Elements'}, {'value': 22.0, 'units': 'mg', 'description': 'Magnesium, Mg', 'group': 'Elements'}, {'value': 490.0, 'units': 'mg', 'description': 'Phosphorus, P', 'group': 'Elements'}, {'value': 93.0, 'units': 'mg', 'description': 'Potassium, K', 'group': 'Elements'}, {'value': 690.0, 'units': 'mg', 'description': 'Sodium, Na', 'group': 'Elements'}, {'value': 2.94, 'units': 'mg', 'description': 'Zinc, Zn', 'group': 'Elements'}, {'value': 0.024, 'units': 'mg', 'description': 'Copper, Cu', 'group': 'Elements'}, {'value': 0.021, 'units': 'mg', 'description': 'Manganese, Mn', 'group': 'Elements'}, {'value': 14.5, 'units': 'mcg', 'description': 'Selenium, Se', 'group': 'Elements'}, {'value': 1054.0, 'units': 'IU', 'description': 'Vitamin A, IU', 'group': 'Vitamins'}, {'value': 262.0, 'units': 'mcg', 'description': 'Retinol', 'group': 'Vitamins'}, {'value': 271.0, 'units': 'mcg_RAE', 'description': 'Vitamin A, RAE', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mg', 'description': 'Vitamin C, total ascorbic acid', 'group': 'Vitamins'}, {'value': 0.031, 'units': 'mg', 'description': 'Thiamin', 'group': 'Vitamins'}, {'value': 0.45, 'units': 'mg', 'description': 'Riboflavin', 'group': 'Vitamins'}, {'value': 0.18, 'units': 'mg', 'description': 'Niacin', 'group': 'Vitamins'}, {'value': 0.19, 'units': 'mg', 'description': 'Pantothenic acid', 'group': 'Vitamins'}, {'value': 0.074, 'units': 'mg', 'description': 'Vitamin B-6', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, total', 'group': 'Vitamins'}, {'value': 0.27, 'units': 'mcg', 'description': 'Vitamin B-12', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mcg', 'description': 'Folic acid', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, food', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg_DFE', 'description': 'Folate, DFE', 'group': 'Vitamins'}, {'value': 0.324, 'units': 'g', 'description': 'Tryptophan', 'group': 'Amino Acids'}, {'value': 0.896, 'units': 'g', 'description': 'Threonine', 'group': 'Amino Acids'}, {'value': 1.563, 'units': 'g', 'description': 'Isoleucine', 'group': 'Amino Acids'}, {'value': 2.412, 'units': 'g', 'description': 'Leucine', 'group': 'Amino Acids'}, {'value': 2.095, 'units': 'g', 'description': 'Lysine', 'group': 'Amino Acids'}, {'value': 0.659, 'units': 'g', 'description': 'Methionine', 'group': 'Amino Acids'}, {'value': 0.126, 'units': 'g', 'description': 'Cystine', 'group': 'Amino Acids'}, {'value': 1.326, 'units': 'g', 'description': 'Phenylalanine', 'group': 'Amino Acids'}, {'value': 1.216, 'units': 'g', 'description': 'Tyrosine', 'group': 'Amino Acids'}, {'value': 1.682, 'units': 'g', 'description': 'Valine', 'group': 'Amino Acids'}, {'value': 0.952, 'units': 'g', 'description': 'Arginine', 'group': 'Amino Acids'}, {'value': 0.884, 'units': 'g', 'description': 'Histidine', 'group': 'Amino Acids'}, {'value': 0.711, 'units': 'g', 'description': 'Alanine', 'group': 'Amino Acids'}, {'value': 1.618, 'units': 'g', 'description': 'Aspartic acid', 'group': 'Amino Acids'}, {'value': 6.16, 'units': 'g', 'description': 'Glutamic acid', 'group': 'Amino Acids'}, {'value': 0.439, 'units': 'g', 'description': 'Glycine', 'group': 'Amino Acids'}, {'value': 2.838, 'units': 'g', 'description': 'Proline', 'group': 'Amino Acids'}, {'value': 1.472, 'units': 'g', 'description': 'Serine', 'group': 'Amino Acids'}, {'value': 93.0, 'units': 'mg', 'description': 'Cholesterol', 'group': 'Other'}, {'value': 18.584, 'units': 'g', 'description': 'Fatty acids, total saturated', 'group': 'Other'}, {'value': 8.275, 'units': 'g', 'description': 'Fatty acids, total monounsaturated', 'group': 'Other'}, {'value': 0.83, 'units': 'g', 'description': 'Fatty acids, total polyunsaturated', 'group': 'Other'}]}

# json 형식 : { 키:밸류,키:밸류,키:{ 키:{키 :밸류}}},{        },{        },.........=> 보통 4단계이상 안간다.,2단계 정도임
print(db[0].keys())
# dict_keys(['id', 'description', 'tags', 'manufacturer', 'group', 'portions', 'nutrients'])
print(db[0]['nutrients'])
# [{'value': 25.18, 'units': 'g', 'description': 'Protein', 'group': 'Composition'}, {'value': 29.2, 'units': 'g', 'description': 'Total lipid (fat)', 'group': 'Composition'}, {'value': 3.06, 'units': 'g', 'description': 'Carbohydrate, by difference', 'group': 'Composition'}, {'value': 3.28, 'units': 'g', 'description': 'Ash', 'group': 'Other'}, {'value': 376.0, 'units': 'kcal', 'description': 'Energy', 'group': 'Energy'}, {'value': 39.28, 'units': 'g', 'description': 'Water', 'group': 'Composition'}, {'value': 1573.0, 'units': 'kJ', 'description': 'Energy', 'group': 'Energy'}, {'value': 0.0, 'units': 'g', 'description': 'Fiber, total dietary', 'group': 'Composition'}, {'value': 673.0, 'units': 'mg', 'description': 'Calcium, Ca', 'group': 'Elements'}, {'value': 0.64, 'units': 'mg', 'description': 'Iron, Fe', 'group': 'Elements'}, {'value': 22.0, 'units': 'mg', 'description': 'Magnesium, Mg', 'group': 'Elements'}, {'value': 490.0, 'units': 'mg', 'description': 'Phosphorus, P', 'group': 'Elements'}, {'value': 93.0, 'units': 'mg', 'description': 'Potassium, K', 'group': 'Elements'}, {'value': 690.0, 'units': 'mg', 'description': 'Sodium, Na', 'group': 'Elements'}, {'value': 2.94, 'units': 'mg', 'description': 'Zinc, Zn', 'group': 'Elements'}, {'value': 0.024, 'units': 'mg', 'description': 'Copper, Cu', 'group': 'Elements'}, {'value': 0.021, 'units': 'mg', 'description': 'Manganese, Mn', 'group': 'Elements'}, {'value': 14.5, 'units': 'mcg', 'description': 'Selenium, Se', 'group': 'Elements'}, {'value': 1054.0, 'units': 'IU', 'description': 'Vitamin A, IU', 'group': 'Vitamins'}, {'value': 262.0, 'units': 'mcg', 'description': 'Retinol', 'group': 'Vitamins'}, {'value': 271.0, 'units': 'mcg_RAE', 'description': 'Vitamin A, RAE', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mg', 'description': 'Vitamin C, total ascorbic acid', 'group': 'Vitamins'}, {'value': 0.031, 'units': 'mg', 'description': 'Thiamin', 'group': 'Vitamins'}, {'value': 0.45, 'units': 'mg', 'description': 'Riboflavin', 'group': 'Vitamins'}, {'value': 0.18, 'units': 'mg', 'description': 'Niacin', 'group': 'Vitamins'}, {'value': 0.19, 'units': 'mg', 'description': 'Pantothenic acid', 'group': 'Vitamins'}, {'value': 0.074, 'units': 'mg', 'description': 'Vitamin B-6', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, total', 'group': 'Vitamins'}, {'value': 0.27, 'units': 'mcg', 'description': 'Vitamin B-12', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mcg', 'description': 'Folic acid', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, food', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg_DFE', 'description': 'Folate, DFE', 'group': 'Vitamins'}, {'value': 93.0, 'units': 'mg', 'description': 'Cholesterol', 'group': 'Other'}, {'value': 18.584, 'units': 'g', 'description': 'Fatty acids, total saturated', 'group': 'Other'}, {'value': 8.275, 'units': 'g', 'description': 'Fatty acids, total monounsaturated', 'group': 'Other'}, {'value': 0.83, 'units': 'g', 'description': 'Fatty acids, total polyunsaturated', 'group': 'Other'}, {'value': 0.324, 'units': 'g', 'description': 'Tryptophan', 'group': 'Amino Acids'}, {'value': 0.896, 'units': 'g', 'description': 'Threonine', 'group': 'Amino Acids'}, {'value': 1.563, 'units': 'g', 'description': 'Isoleucine', 'group': 'Amino Acids'}, {'value': 2.412, 'units': 'g', 'description': 'Leucine', 'group': 'Amino Acids'}, {'value': 2.095, 'units': 'g', 'description': 'Lysine', 'group': 'Amino Acids'}, {'value': 0.659, 'units': 'g', 'description': 'Methionine', 'group': 'Amino Acids'}, {'value': 0.126, 'units': 'g', 'description': 'Cystine', 'group': 'Amino Acids'}, {'value': 1.326, 'units': 'g', 'description': 'Phenylalanine', 'group': 'Amino Acids'}, {'value': 1.216, 'units': 'g', 'description': 'Tyrosine', 'group': 'Amino Acids'}, {'value': 1.682, 'units': 'g', 'description': 'Valine', 'group': 'Amino Acids'}, {'value': 0.952, 'units': 'g', 'description': 'Arginine', 'group': 'Amino Acids'}, {'value': 0.884, 'units': 'g', 'description': 'Histidine', 'group': 'Amino Acids'}, {'value': 0.711, 'units': 'g', 'description': 'Alanine', 'group': 'Amino Acids'}, {'value': 1.618, 'units': 'g', 'description': 'Aspartic acid', 'group': 'Amino Acids'}, {'value': 6.16, 'units': 'g', 'description': 'Glutamic acid', 'group': 'Amino Acids'}, {'value': 0.439, 'units': 'g', 'description': 'Glycine', 'group': 'Amino Acids'}, {'value': 2.838, 'units': 'g', 'description': 'Proline', 'group': 'Amino Acids'}, {'value': 1.472, 'units': 'g', 'description': 'Serine', 'group': 'Amino Acids'}, {'value': 25.18, 'units': 'g', 'description': 'Protein', 'group': 'Composition'}, {'value': 29.2, 'units': 'g', 'description': 'Total lipid (fat)', 'group': 'Composition'}, {'value': 3.06, 'units': 'g', 'description': 'Carbohydrate, by difference', 'group': 'Composition'}, {'value': 3.28, 'units': 'g', 'description': 'Ash', 'group': 'Other'}, {'value': 376.0, 'units': 'kcal', 'description': 'Energy', 'group': 'Energy'}, {'value': 39.28, 'units': 'g', 'description': 'Water', 'group': 'Composition'}, {'value': 1573.0, 'units': 'kJ', 'description': 'Energy', 'group': 'Energy'}, {'value': 0.0, 'units': 'g', 'description': 'Fiber, total dietary', 'group': 'Composition'}, {'value': 673.0, 'units': 'mg', 'description': 'Calcium, Ca', 'group': 'Elements'}, {'value': 0.64, 'units': 'mg', 'description': 'Iron, Fe', 'group': 'Elements'}, {'value': 22.0, 'units': 'mg', 'description': 'Magnesium, Mg', 'group': 'Elements'}, {'value': 490.0, 'units': 'mg', 'description': 'Phosphorus, P', 'group': 'Elements'}, {'value': 93.0, 'units': 'mg', 'description': 'Potassium, K', 'group': 'Elements'}, {'value': 690.0, 'units': 'mg', 'description': 'Sodium, Na', 'group': 'Elements'}, {'value': 2.94, 'units': 'mg', 'description': 'Zinc, Zn', 'group': 'Elements'}, {'value': 0.024, 'units': 'mg', 'description': 'Copper, Cu', 'group': 'Elements'}, {'value': 0.021, 'units': 'mg', 'description': 'Manganese, Mn', 'group': 'Elements'}, {'value': 14.5, 'units': 'mcg', 'description': 'Selenium, Se', 'group': 'Elements'}, {'value': 1054.0, 'units': 'IU', 'description': 'Vitamin A, IU', 'group': 'Vitamins'}, {'value': 262.0, 'units': 'mcg', 'description': 'Retinol', 'group': 'Vitamins'}, {'value': 271.0, 'units': 'mcg_RAE', 'description': 'Vitamin A, RAE', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mg', 'description': 'Vitamin C, total ascorbic acid', 'group': 'Vitamins'}, {'value': 0.031, 'units': 'mg', 'description': 'Thiamin', 'group': 'Vitamins'}, {'value': 0.45, 'units': 'mg', 'description': 'Riboflavin', 'group': 'Vitamins'}, {'value': 0.18, 'units': 'mg', 'description': 'Niacin', 'group': 'Vitamins'}, {'value': 0.19, 'units': 'mg', 'description': 'Pantothenic acid', 'group': 'Vitamins'}, {'value': 0.074, 'units': 'mg', 'description': 'Vitamin B-6', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, total', 'group': 'Vitamins'}, {'value': 0.27, 'units': 'mcg', 'description': 'Vitamin B-12', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mcg', 'description': 'Folic acid', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, food', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg_DFE', 'description': 'Folate, DFE', 'group': 'Vitamins'}, {'value': 0.324, 'units': 'g', 'description': 'Tryptophan', 'group': 'Amino Acids'}, {'value': 0.896, 'units': 'g', 'description': 'Threonine', 'group': 'Amino Acids'}, {'value': 1.563, 'units': 'g', 'description': 'Isoleucine', 'group': 'Amino Acids'}, {'value': 2.412, 'units': 'g', 'description': 'Leucine', 'group': 'Amino Acids'}, {'value': 2.095, 'units': 'g', 'description': 'Lysine', 'group': 'Amino Acids'}, {'value': 0.659, 'units': 'g', 'description': 'Methionine', 'group': 'Amino Acids'}, {'value': 0.126, 'units': 'g', 'description': 'Cystine', 'group': 'Amino Acids'}, {'value': 1.326, 'units': 'g', 'description': 'Phenylalanine', 'group': 'Amino Acids'}, {'value': 1.216, 'units': 'g', 'description': 'Tyrosine', 'group': 'Amino Acids'}, {'value': 1.682, 'units': 'g', 'description': 'Valine', 'group': 'Amino Acids'}, {'value': 0.952, 'units': 'g', 'description': 'Arginine', 'group': 'Amino Acids'}, {'value': 0.884, 'units': 'g', 'description': 'Histidine', 'group': 'Amino Acids'}, {'value': 0.711, 'units': 'g', 'description': 'Alanine', 'group': 'Amino Acids'}, {'value': 1.618, 'units': 'g', 'description': 'Aspartic acid', 'group': 'Amino Acids'}, {'value': 6.16, 'units': 'g', 'description': 'Glutamic acid', 'group': 'Amino Acids'}, {'value': 0.439, 'units': 'g', 'description': 'Glycine', 'group': 'Amino Acids'}, {'value': 2.838, 'units': 'g', 'description': 'Proline', 'group': 'Amino Acids'}, {'value': 1.472, 'units': 'g', 'description': 'Serine', 'group': 'Amino Acids'}, {'value': 93.0, 'units': 'mg', 'description': 'Cholesterol', 'group': 'Other'}, {'value': 18.584, 'units': 'g', 'description': 'Fatty acids, total saturated', 'group': 'Other'}, {'value': 8.275, 'units': 'g', 'description': 'Fatty acids, total monounsaturated', 'group': 'Other'}, {'value': 0.83, 'units': 'g', 'description': 'Fatty acids, total polyunsaturated', 'group': 'Other'}, {'value': 25.18, 'units': 'g', 'description': 'Protein', 'group': 'Composition'}, {'value': 29.2, 'units': 'g', 'description': 'Total lipid (fat)', 'group': 'Composition'}, {'value': 3.06, 'units': 'g', 'description': 'Carbohydrate, by difference', 'group': 'Composition'}, {'value': 3.28, 'units': 'g', 'description': 'Ash', 'group': 'Other'}, {'value': 376.0, 'units': 'kcal', 'description': 'Energy', 'group': 'Energy'}, {'value': 39.28, 'units': 'g', 'description': 'Water', 'group': 'Composition'}, {'value': 1573.0, 'units': 'kJ', 'description': 'Energy', 'group': 'Energy'}, {'value': 0.0, 'units': 'g', 'description': 'Fiber, total dietary', 'group': 'Composition'}, {'value': 673.0, 'units': 'mg', 'description': 'Calcium, Ca', 'group': 'Elements'}, {'value': 0.64, 'units': 'mg', 'description': 'Iron, Fe', 'group': 'Elements'}, {'value': 22.0, 'units': 'mg', 'description': 'Magnesium, Mg', 'group': 'Elements'}, {'value': 490.0, 'units': 'mg', 'description': 'Phosphorus, P', 'group': 'Elements'}, {'value': 93.0, 'units': 'mg', 'description': 'Potassium, K', 'group': 'Elements'}, {'value': 690.0, 'units': 'mg', 'description': 'Sodium, Na', 'group': 'Elements'}, {'value': 2.94, 'units': 'mg', 'description': 'Zinc, Zn', 'group': 'Elements'}, {'value': 0.024, 'units': 'mg', 'description': 'Copper, Cu', 'group': 'Elements'}, {'value': 0.021, 'units': 'mg', 'description': 'Manganese, Mn', 'group': 'Elements'}, {'value': 14.5, 'units': 'mcg', 'description': 'Selenium, Se', 'group': 'Elements'}, {'value': 1054.0, 'units': 'IU', 'description': 'Vitamin A, IU', 'group': 'Vitamins'}, {'value': 262.0, 'units': 'mcg', 'description': 'Retinol', 'group': 'Vitamins'}, {'value': 271.0, 'units': 'mcg_RAE', 'description': 'Vitamin A, RAE', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mg', 'description': 'Vitamin C, total ascorbic acid', 'group': 'Vitamins'}, {'value': 0.031, 'units': 'mg', 'description': 'Thiamin', 'group': 'Vitamins'}, {'value': 0.45, 'units': 'mg', 'description': 'Riboflavin', 'group': 'Vitamins'}, {'value': 0.18, 'units': 'mg', 'description': 'Niacin', 'group': 'Vitamins'}, {'value': 0.19, 'units': 'mg', 'description': 'Pantothenic acid', 'group': 'Vitamins'}, {'value': 0.074, 'units': 'mg', 'description': 'Vitamin B-6', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, total', 'group': 'Vitamins'}, {'value': 0.27, 'units': 'mcg', 'description': 'Vitamin B-12', 'group': 'Vitamins'}, {'value': 0.0, 'units': 'mcg', 'description': 'Folic acid', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg', 'description': 'Folate, food', 'group': 'Vitamins'}, {'value': 18.0, 'units': 'mcg_DFE', 'description': 'Folate, DFE', 'group': 'Vitamins'}, {'value': 0.324, 'units': 'g', 'description': 'Tryptophan', 'group': 'Amino Acids'}, {'value': 0.896, 'units': 'g', 'description': 'Threonine', 'group': 'Amino Acids'}, {'value': 1.563, 'units': 'g', 'description': 'Isoleucine', 'group': 'Amino Acids'}, {'value': 2.412, 'units': 'g', 'description': 'Leucine', 'group': 'Amino Acids'}, {'value': 2.095, 'units': 'g', 'description': 'Lysine', 'group': 'Amino Acids'}, {'value': 0.659, 'units': 'g', 'description': 'Methionine', 'group': 'Amino Acids'}, {'value': 0.126, 'units': 'g', 'description': 'Cystine', 'group': 'Amino Acids'}, {'value': 1.326, 'units': 'g', 'description': 'Phenylalanine', 'group': 'Amino Acids'}, {'value': 1.216, 'units': 'g', 'description': 'Tyrosine', 'group': 'Amino Acids'}, {'value': 1.682, 'units': 'g', 'description': 'Valine', 'group': 'Amino Acids'}, {'value': 0.952, 'units': 'g', 'description': 'Arginine', 'group': 'Amino Acids'}, {'value': 0.884, 'units': 'g', 'description': 'Histidine', 'group': 'Amino Acids'}, {'value': 0.711, 'units': 'g', 'description': 'Alanine', 'group': 'Amino Acids'}, {'value': 1.618, 'units': 'g', 'description': 'Aspartic acid', 'group': 'Amino Acids'}, {'value': 6.16, 'units': 'g', 'description': 'Glutamic acid', 'group': 'Amino Acids'}, {'value': 0.439, 'units': 'g', 'description': 'Glycine', 'group': 'Amino Acids'}, {'value': 2.838, 'units': 'g', 'description': 'Proline', 'group': 'Amino Acids'}, {'value': 1.472, 'units': 'g', 'description': 'Serine', 'group': 'Amino Acids'}, {'value': 93.0, 'units': 'mg', 'description': 'Cholesterol', 'group': 'Other'}, {'value': 18.584, 'units': 'g', 'description': 'Fatty acids, total saturated', 'group': 'Other'}, {'value': 8.275, 'units': 'g', 'description': 'Fatty acids, total monounsaturated', 'group': 'Other'}, {'value': 0.83, 'units': 'g', 'description': 'Fatty acids, total polyunsaturated', 'group': 'Other'}]
print(db[0]['nutrients'][0])
# {'value': 25.18, 'units': 'g', 'description': 'Protein', 'group': 'Composition'}
print(db[0]['nutrients'][0]['value'])

print("ㅎ"*50)

nutrients = DataFrame(db[0]['nutrients'])
print(nutrients[:7])
#                    description        group units    value
# 0                      Protein  Composition     g    25.18
# 1            Total lipid (fat)  Composition     g    29.20
# 2  Carbohydrate, by difference  Composition     g     3.06
# 3                          Ash        Other     g     3.28
# 4                       Energy       Energy  kcal   376.00
# 5                        Water  Composition     g    39.28
# 6                       Energy       Energy    kJ  1573.00

# ['description', 'group', 'units', 'value']
info_keys = ['description', 'group', 'id', 'manufacturer']
print('='*50)
info = DataFrame(db, columns=info_keys)
# print(info['description'])
# print(info[:5])
print(info.info())
# [5 rows x 4 columns]
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 6636 entries, 0 to 6635
# Data columns (total 4 columns):
# description     6636 non-null object
# group           6636 non-null object
# id              6636 non-null int64
# manufacturer    5195 non-null object
# dtypes: int64(1), object(3)
# memory usage: 129.6+ KB
# None

#             대한민국(object)
# 출생 시,도 : 서울, 경기, 강원, ...., 제주(string, int......)

print('='*50)

print(pd.value_counts(info.group))
# None
# Vegetables and Vegetable Products    812
# Beef Products                        618
# Baked Products                       496
# Breakfast Cereals                    403
# Fast Foods                           365
# Legumes and Legume Products          365
# Lamb, Veal, and Game Products        345
# Sweets                               341
# Fruits and Fruit Juices              328
# Pork Products                        328
# Beverages                            278
# Soups, Sauces, and Gravies           275
# Finfish and Shellfish Products       255
# Baby Foods                           209
# Cereal Grains and Pasta              183
# Ethnic Foods                         165
# Snacks                               162
# Nut and Seed Products                128
# Poultry Products                     116
# Sausages and Luncheon Meats          111
# Dairy and Egg Products               107
# Fats and Oils                         97
# Meals, Entrees, and Sidedishes        57
# Restaurant Foods                      51
# Spices and Herbs                      41
# Name: group, dtype: int64

print('='*50)

nutrients=[]
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id']=rec['id']
    nutrients.append(fnuts)
print(nutrients)
print(nutrients.duplicated().sum())                 # duplicated() :  중복 체크

nutrients = nutrients.drop_duplicates()             # drop_duplicates() :  중복 삭제








































































































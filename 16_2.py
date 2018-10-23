import numpy as np
import pandas as pd

from pandas import DataFrame as df         # DataFrame으로 작성해서 난 에러는 df로 바꾸기

# # 파일 읽어오기
# # csv_test = pd.read_csv("test_csv_file.csv")
# # print(csv_test)
# # #    ID LAST_NAME  AGE
# # # 0   1       KIM   30
# # # 1   2      CHOI   25
# # # 2   3       LEE   41
# # # 3   4      PARK   19
# # # 4   5       LIM   36
# # print(csv_test.shape)
# # # (5, 3)
# #
# # text_test = pd.read_csv("test_text_file.txt",sep="|")
# # print(text_test)
# # #    ID  A  B  C  D
# # # 0  C1  1  2  3  4
# # # 1  C2  5  6  7  8
# # # 2  C3  1  3  5  7
# # text_test = pd.read_csv("test_text_file.txt",sep="|",index_col='ID')               #index_col= : index로 사용하고자 하는 column name
# # print(text_test)
# # #     A  B  C  D
# # # ID
# # # C1  1  2  3  4
# # # C2  5  6  7  8
# # # C3  1  3  5  7
# # text_test = pd.read_csv("test_text_file.txt",sep="|",index_col=0)               #index_col= : index로 사용하고자 하는 column number
# # print(text_test)
# # #     A  B  C  D
# # # ID
# # # C1  1  2  3  4
# # # C2  5  6  7  8
# # # C3  1  3  5  7
# #
# # print("="*250)
# #
# # text_test = pd.read_csv("text_without_column_name.txt",sep="|")             # 첫줄을 헤더로 인식해 정보를 잃음
# # print(text_test)
# # #    C1  1  2  3  4
# # # 0  C2  5  6  7  8
# # # 1  C3  1  3  5  7
# # text_test = pd.read_csv("text_without_column_name.txt",sep="|",header=None)             # header=None : 헤더 없음을 인식
# # print(text_test)
# # #     0  1  2  3  4
# # # 0  C1  1  2  3  4
# # # 1  C2  5  6  7  8
# # # 2  C3  1  3  5  7
# # text_test = pd.read_csv("text_without_column_name.txt",sep="|",header=None,names=['ID','A','B','C','D'])             # names= : 헤더에 이름 부여
# # print(text_test)
# # #    ID  A  B  C  D
# # # 0  C1  1  2  3  4
# # # 1  C2  5  6  7  8
# # # 2  C3  1  3  5  7
# # text_test = pd.read_csv("text_without_column_name.txt",sep="|",header=None,names=['ID','A','B','C','D'],index_col='ID')
# # print(text_test)
# # #     A  B  C  D
# # # ID
# # # C1  1  2  3  4
# # # C2  5  6  7  8
# # # C3  1  3  5  7
#
# #분석 결과를 파일로 저장
#
# data = {
#     'id' : ['a1','a2','a3','a4','a5'],
#     'x1' : [1,2,3,4,5],
#     'x2' : [3.0,4.5,3.2,4.0,3.5]
# }
# #아래와 같이 작성하면 행번호가 함께 생성
# data_df = DataFrame(data)
# print(data_df)
# #    id  x1   x2
# # 0  a1   1  3.0
# # 1  a2   2  4.5
# # 2  a3   3  3.2
# # 3  a4   4  4.0
# # 4  a5   5  3.5
#
# data_df = DataFrame(data, index=['a1','a2','a3','a4','a5'])
# print(data_df)
#
# print("="*50)
#
# data_df_2 = data_df.reindex(['a1','a2','a3','a4','a5','a6'])
# print(data_df_2)
# #      id   x1   x2
# # a1   a1  1.0  3.0
# # a2   a2  2.0  4.5
# # a3   a3  3.0  3.2
# # a4   a4  4.0  4.0
# # a5   a5  5.0  3.5
# # a6  NaN  NaN  NaN
#
# # data_df_2.to_csv() : DataFrame을 csv로 저장할 때 사용
# data_df_2.to_csv('data_df_2.csv',sep=',',na_rep='NaN')


#DataFrame속성작업
#index : 행이름을 부여하는 속성 dataframe을 만들때 직접 지정 가능
#copy의 초기값 : false
df_1=df(data =np.arange(12).reshape(3,4))
print(df_1)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
df_1=df(data =np.arange(12).reshape(3,4),index=['r0','r1','r2'])
print(df_1)
#     0  1   2   3
# r0  0  1   2   3
# r1  4  5   6   7
# r2  8  9  10  11
df_1=df(data =np.arange(12).reshape(3,4),index=['r0','r1','r2'],dtype=int,columns=['c0','c1','c2','c3'])
print(df_1)
#     c0  c1  c2  c3
# r0   0   1   2   3
# r1   4   5   6   7
# r2   8   9  10  11

#행과 열 전환
df_2=df(df_1.T)
print(df_2)
#     r0  r1  r2
# c0   0   4   8
# c1   1   5   9
# c2   2   6  10
# c3   3   7  11
print(df_1.T)
#     r0  r1  r2
# c0   0   4   8
# c1   1   5   9
# c2   2   6  10
# c3   3   7  11

print(df_1.axes)                        #axis : 축정보
# [Index(['r0', 'r1', 'r2'], dtype='object'), Index(['c0', 'c1', 'c2', 'c3'], dtype='object')]
print(df_1.dtypes)                      #data_type정보
# c0    int32
# c1    int32
# c2    int32
# c3    int32
# dtype: object
print(df_1.size)                        #데이터의 사이즈 확인
# 12

print(type(df_1))                       #자료구조
# <class 'pandas.core.frame.DataFrame'
print(df_1.values)                      #추출된 자료
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(type(df_1.values))                #추출된 자료구조
# <class 'numpy.ndarray'>

df_2=df(data={
    'class_1' : ['a','a','b','b','c'],
    'var_1' : np.arange(5),
    'var_2' : np.random.rand(5)},
    index=['r0','r1','r2','r3','r4'])
print(df_2)
#    class_1  var_1     var_2
# r0       a      0  0.531274
# r1       a      1  0.175335
# r2       b      2  0.959343
# r3       b      3  0.442552
# r4       c      4  0.862076

df_2=df({                                                           # data = : 속성을 지정하지 않아도 기본값으로 지정됨
    'class_1' : ['a','a','b','b','c'],
    'var_1' : np.arange(5),
    'var_2' : np.random.rand(5)},
    index=['r0','r1','r2','r3','r4'])
print(df_2)
#    class_1  var_1     var_2
# r0       a      0  0.531274
# r1       a      1  0.175335
# r2       b      2  0.959343
# r3       b      3  0.442552
# r4       c      4  0.862076

#index 확인
print(df_2.index)
# Index(['r0', 'r1', 'r2', 'r3', 'r4'], dtype='object')
print(df_2.ix[2:])                      #index를 활용한 슬라이싱 : [2:] =>2번부터 마지막까지(행범위 참조)
#    class_1  var_1     var_2
# r2       b      2  0.614414
# r3       b      3  0.611415
# r4       c      4  0.213260
print(df_2.ix[2])
print(df_2.head(3))                                 # 앞에서 3번째까지 슬라이싱
#    class_1  var_1     var_2
# r0       a      0  0.346856
# r1       a      1  0.461321
# r2       b      2  0.079013
# print(df_2.tail(3))                                 # 뒤에서 3번째까지 슬라이싱
# #    class_1  var_1     var_2
# # r2       b      2  0.079013
# # r3       b      3  0.221049
# # r4       c      4  0.100560
#
# print(df_2.columns)
# # Index(['class_1', 'var_1', 'var_2'], dtype='object')
# print(df_2['class_1'])
# # r0    a
# # r1    a
# # r2    b
# # r3    b
# # r4    c
# # Name: class_1, dtype: object
#
# #class_1과 var_2 컬럼 출력
# print(df_2)
# print(df_2[['class_1','var_2']])            #r언어 : c()
# #     class_1     var_2
# # r0       a  0.333455
# # r1       a  0.527994
# # r2       b  0.003908
# # r3       b  0.513808
# # r4       c  0.119298
#
# idx = ['r0','r1','r2','r3','r4']
#
# df_1 = df({'c1' : np.arange(5),
#            'c2' : np.random.randn(5)},
#           index=idx)
# print(df_1)
# #     c1        c2
# # r0   0  0.421806
# # r1   1  1.287233
# # r2   2  0.028156
# # r3   3 -0.591526
# # r4   4  0.287460
#
# new_idx = ['r0','r1','r2','r5','r6']
# # df_1 = df_1.reindex(new_idx)
# # print(df_1)
# # #      c1        c2
# # # r0  0.0  0.475256
# # # r1  1.0  0.491309
# # # r2  2.0  0.864039
# # # r5  NaN       NaN
# # # r6  NaN       NaN
#
# # df_1 = df_1.reindex(new_idx,fill_value=0)
# # print(df_1)
# # #     c1        c2
# # # r0   0 -0.062061
# # # r1   1  0.132808
# # # r2   2 -0.049169
# # # r5   0  0.000000
# # # r6   0  0.000000
#
# # df_1 = df_1.reindex(new_idx,fill_value='missing')
# # print(df_1)
# # #          c1       c2
# # # r0        0  1.29382
# # # r1        1  -0.3048
# # # r2        2  1.52637
# # # r5  missing  missing
# # # r6  missing  missing
#
# df_1 = df_1.reindex(new_idx,fill_value='NA')                # fill_value= : 위에 내용 주석이여야 함(데이터가 없어야 해서)
# print(df_1)
# #     c1         c2
# # r0   0 -0.0427524
# # r1   1   -2.05168
# # r2   2    1.90008
# # r5  NA         NA
# # r6  NA         NA
#
#
# #시계열 data : 시간의 흐름에 따라 달라짐(내용 안에 시간의 변수가 있다.)
#
# #help(pd.date_range)
# # date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)
# #     Return a fixed frequency DatetimeIndex.
# #
# #     Parameters
# #     ----------
# #     start : str or datetime-like, optional
# #         Left bound for generating dates.
# #     end : str or datetime-like, optional
# #         Right bound for generating dates.
# #     periods : integer, optional
# #         Number of periods to generate.
# #     freq : str or DateOffset, default 'D' (calendar daily)
# #         Frequency strings can have multiples, e.g. '5H'. See
# #         :ref:`here <timeseries.offset_aliases>` for a list of
# #         frequency aliases.
# #     tz : str or tzinfo, optional
# #         Time zone name for returning localized DatetimeIndex, for example
# #         'Asia/Hong_Kong'. By default, the resulting DatetimeIndex is
# #         timezone-naive.
# #     normalize : bool, default False
# #         Normalize start/end dates to midnight before generating date range.
# #     name : str, default None
# #         Name of the resulting DatetimeIndex.
# #     closed : {None, 'left', 'right'}, optional
# #         Make the interval closed with respect to the given frequency to
# #         the 'left', 'right', or both sides (None, the default).
# #     **kwargs
# #         For compatibility. Has no effect on the result.
# #
# #     Returns
# #     -------
# #     rng : DatetimeIndex
# #
# #     See Also
# #     --------
# #     pandas.DatetimeIndex : An immutable container for datetimes.
# #     pandas.timedelta_range : Return a fixed frequency TimedeltaIndex.
# #     pandas.period_range : Return a fixed frequency PeriodIndex.
# #     pandas.interval_range : Return a fixed frequency IntervalIndex.
# #
# #     Notes
# #     -----
# #     Of the four parameters ``start``, ``end``, ``periods``, and ``freq``,
# #     exactly three must be specified. If ``freq`` is omitted, the resulting
# #     ``DatetimeIndex`` will have ``periods`` linearly spaced elements between
# #     ``start`` and ``end`` (closed on both sides).
# #
# #     To learn more about the frequency strings, please see `this link
# #     <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.
# #
# #     Examples
# #     --------
# #     **Specifying the values**
# #
# #     The next four examples generate the same `DatetimeIndex`, but vary
# #     the combination of `start`, `end` and `periods`.
# #
# #     Specify `start` and `end`, with the default daily frequency.
# #
# #     >>> pd.date_range(start='1/1/2018', end='1/08/2018')
# #     DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
# #                    '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
# #                   dtype='datetime64[ns]', freq='D')
# #
# #     Specify `start` and `periods`, the number of periods (days).
# #
# #     >>> pd.date_range(start='1/1/2018', periods=8)
# #     DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
# #                    '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
# #                   dtype='datetime64[ns]', freq='D')
# #
# #     Specify `end` and `periods`, the number of periods (days).
# #
# #     >>> pd.date_range(end='1/1/2018', periods=8)
# #     DatetimeIndex(['2017-12-25', '2017-12-26', '2017-12-27', '2017-12-28',
# #                    '2017-12-29', '2017-12-30', '2017-12-31', '2018-01-01'],
# #                   dtype='datetime64[ns]', freq='D')
# #
# #     Specify `start`, `end`, and `periods`; the frequency is generated
# #     automatically (linearly spaced).
# #
# #     >>> pd.date_range(start='2018-04-24', end='2018-04-27', periods=3)
# #     DatetimeIndex(['2018-04-24 00:00:00', '2018-04-25 12:00:00',
# #                    '2018-04-27 00:00:00'], freq=None)
# #
# #     **Other Parameters**
# #
# #     Changed the `freq` (frequency) to ``'M'`` (month end frequency).
# #
# #     >>> pd.date_range(start='1/1/2018', periods=5, freq='M')
# #     DatetimeIndex(['2018-01-31', '2018-02-28', '2018-03-31', '2018-04-30',
# #                    '2018-05-31'],
# #                   dtype='datetime64[ns]', freq='M')
# #
# #     Multiples are allowed
# #
# #     >>> pd.date_range(start='1/1/2018', periods=5, freq='3M')
# #     DatetimeIndex(['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',
# #                    '2019-01-31'],
# #                   dtype='datetime64[ns]', freq='3M')
# #
# #     `freq` can also be specified as an Offset object.
# #
# #     >>> pd.date_range(start='1/1/2018', periods=5, freq=pd.offsets.MonthEnd(3))
# #     DatetimeIndex(['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',
# #                    '2019-01-31'],
# #                   dtype='datetime64[ns]', freq='3M')
# #
# #     Specify `tz` to set the timezone.
# #
# #     >>> pd.date_range(start='1/1/2018', periods=5, tz='Asia/Tokyo')
# #     DatetimeIndex(['2018-01-01 00:00:00+09:00', '2018-01-02 00:00:00+09:00',
# #                    '2018-01-03 00:00:00+09:00', '2018-01-04 00:00:00+09:00',
# #                    '2018-01-05 00:00:00+09:00'],
# #                   dtype='datetime64[ns, Asia/Tokyo]', freq='D')
# #
# #     `closed` controls whether to include `start` and `end` that are on the
# #     boundary. The default includes boundary points on either end.
# #
# #     >>> pd.date_range(start='2017-01-01', end='2017-01-04', closed=None)
# #     DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04'],
# #                   dtype='datetime64[ns]', freq='D')
# #
# #     Use ``closed='left'`` to exclude `end` if it falls on the boundary.
# #
# #     >>> pd.date_range(start='2017-01-01', end='2017-01-04', closed='left')
# #     DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03'],
# #                   dtype='datetime64[ns]', freq='D')
# #
# #     Use ``closed='right'`` to exclude `start` if it falls on the boundary.
# #
# #     >>> pd.date_range(start='2017-01-01', end='2017-01-04', closed='right')
# #     DatetimeIndex(['2017-01-02', '2017-01-03', '2017-01-04'],
# #                   dtype='datetime64[ns]', freq='D')
#
#
# # print(pd.date_range("2018-9-10","2019-9-30",freq='MS'))          #http://pandas.pydata.org/pandas-docs/stable/genindex.html#D 에서 찾아서 확인
# # # DatetimeIndex(['2018-10-01', '2018-11-01', '2018-12-01', '2019-01-01',
# # #                '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01',
# # #                '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01'],
# # #               dtype='datetime64[ns]', freq='MS')
#
#
# date_idx = pd.date_range('09/10/2018',periods=10,freq='D')
# print(date_idx)
# # DatetimeIndex(['2018-09-10', '2018-09-11', '2018-09-12', '2018-09-13',
# #                '2018-09-14', '2018-09-15', '2018-09-16', '2018-09-17',
# #                '2018-09-18', '2018-09-19'],
# #               dtype='datetime64[ns]', freq='D')
# df_2 = df({"c1": [10,20,30,40,50,10,20,30,40,50]},
#     index=date_idx)
# print(df_2)
# #             c1
# # 2018-09-10  10
# # 2018-09-11  20
# # 2018-09-12  30
# # 2018-09-13  40
# # 2018-09-14  50
# # 2018-09-15  10
# # 2018-09-16  20
# # 2018-09-17  30
# # 2018-09-18  40
# # 2018-09-19  50
#
# date_idx_2 = pd.date_range('09/5/2018',periods=20,freq='D')         #date_idx보다 날짜를 더 늘림
# print(date_idx_2)
# # DatetimeIndex(['2018-09-05', '2018-09-06', '2018-09-07', '2018-09-08',
# #                '2018-09-09', '2018-09-10', '2018-09-11', '2018-09-12',
# #                '2018-09-13', '2018-09-14', '2018-09-15', '2018-09-16',
# #                '2018-09-17', '2018-09-18', '2018-09-19', '2018-09-20',
# #                '2018-09-21', '2018-09-22', '2018-09-23', '2018-09-24'],
# #               dtype='datetime64[ns]', freq='D')
# # df_2 = df_2.reindex(date_idx_2)         #날짜 추가로 설정이 없는 날짜는 NaN
# # print(df_2)
# # #               c1
# # # 2018-09-05   NaN
# # # 2018-09-06   NaN
# # # 2018-09-07   NaN
# # # 2018-09-08   NaN
# # # 2018-09-09   NaN
# # # 2018-09-10  10.0
# # # 2018-09-11  20.0
# # # 2018-09-12  30.0
# # # 2018-09-13  40.0
# # # 2018-09-14  50.0
# # # 2018-09-15  10.0
# # # 2018-09-16  20.0
# # # 2018-09-17  30.0
# # # 2018-09-18  40.0
# # # 2018-09-19  50.0
# # # 2018-09-20   NaN
# # # 2018-09-21   NaN
# # # 2018-09-22   NaN
# # # 2018-09-23   NaN
# # # 2018-09-24   NaN
#
# # df_2 = df_2.reindex(date_idx_2,method='ffill')                  #ffill : 바로 앞의 데이터를 복사
# # print(df_2)
# # #               c1
# # # 2018-09-05   NaN
# # # 2018-09-06   NaN
# # # 2018-09-07   NaN
# # # 2018-09-08   NaN
# # # 2018-09-09   NaN
# # # 2018-09-10  10.0
# # # 2018-09-11  20.0
# # # 2018-09-12  30.0
# # # 2018-09-13  40.0
# # # 2018-09-14  50.0
# # # 2018-09-15  10.0
# # # 2018-09-16  20.0
# # # 2018-09-17  30.0
# # # 2018-09-18  40.0
# # # 2018-09-19  50.0
# # # 2018-09-20  50.0
# # # 2018-09-21  50.0
# # # 2018-09-22  50.0
# # # 2018-09-23  50.0
# # # 2018-09-24  50.0
#
#
# df_2 = df_2.reindex(date_idx_2,method='bfill')                  #bfill : 바로 뒤의 데이터를 복사
# print(df_2)
# #               c1
# # 2018-09-05  10.0
# # 2018-09-06  10.0
# # 2018-09-07  10.0
# # 2018-09-08  10.0
# # 2018-09-09  10.0
# # 2018-09-10  10.0
# # 2018-09-11  20.0
# # 2018-09-12  30.0
# # 2018-09-13  40.0
# # 2018-09-14  50.0
# # 2018-09-15  10.0
# # 2018-09-16  20.0
# # 2018-09-17  30.0
# # 2018-09-18  40.0
# # 2018-09-19  50.0
# # 2018-09-20   NaN
# # 2018-09-21   NaN
# # 2018-09-22   NaN
# # 2018-09-23   NaN
# # 2018-09-24   NaN
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#






















































































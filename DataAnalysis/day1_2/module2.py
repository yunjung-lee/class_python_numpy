#import + 모듈경로.이름

import DataAnalysis.day1_2.module1 as mymod  #외부에 구현되어있는 기능을 사용하기 위하여 import한다. => class를 가져온다
#print(mymod.sum(5,10))
print(mymod.ssum(2,3))

# import DataAnalysis.module1
# print(DataAnalysis.module1.sum(5,10))   : 원래 사용해야 하는 표현식인데 as를 써서 간단히 한다.

from DataAnalysis.day1_2.module1 import sum
#module1이라는 이름의 모듈에 있는 sum함수를 가져와라

print(sum(5,9))
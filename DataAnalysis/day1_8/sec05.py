# example.txt
# JSON 문서
# 속도가 빠르고, 트래픽이 적게 발생해 웹 상에서 자주 이용되는 형식의 데이터
# 지금까지 html, xml 문서의 데이터를 추출, 파싱해보았음
# JSON 문서에서의 데이터 추출 어떻게 이루어질까?

r=[i for i in range(5)]
#5번 돌아가는 i값으로 리스트를 만들고 그 리스트를 r이라고 하자

import json
path = 'example.txt'
# print(open(path, encoding='utf-8').readline())    # open함수의 default 값은 "r"
rec = [json.loads(line) for line in open(path, encoding='utf-8-sig')]   # json 문서를 읽는 방법
print(len(rec))
print(rec[0]['tz']) # 키가 'tz'인 항목의 값을 출력
# print(rec)

time_zones = [myRec['tz'] for myRec in rec if 'tz' in myRec]
# myRec에 'tz'키가 있다면, 'tz'키에 해당하는 값을 출력해 time_zones 리스트의 요소로 입력해라
# 'tz'키가 없다면, ''(결측값)으로 입력됨
# print(len(time_zones))  # 3440
# print(time_zones[:20])

from collections import defaultdict
#딕셔너리의 디폴트값을 0으로 초기화

def get_counts2(sequence):
    counts = defaultdict(int)           #0으로 초기화
    for x in sequence:
        counts[x]+=1
    return counts
counts = get_counts2(time_zones)



def get_counts(sequence):
    counts = {}
    # for x in sequence:            아래 for문과 같은 결과
    #     counts[x]+=1
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
        # print(x)

counts = get_counts(time_zones)
print(counts)
print(counts['America/New_York'])
print(len(counts))
print(len(time_zones))
"""
1.정규표현식 특수문자
    \d :  숫자 = [0-9] = [0123456789] 와 같은 의미
    대문자의 의미  :  반대의 의미(제외) , 같은 의미 = ^
    \D : 숫자가 아닌 것  = [^0-9]
    \w : 문자 + 숫자 = [0-9A-Za-z]
    \W : 문자+숫자가 아닌 것 = [^0-9A-Za-z]
    \s : Space문자 = [\t],[\n]
    \S : Spacd문자가 아닌 것 = [^\t],[^\n]

2.정규표현식 기호
    1) . =>의미 : 모든 문자(줄바꿈 문자(\n)는 제외)
        ex) t.y : t와 y사이의 어떤 문자가 와도 모두 매치
        try : 매치
        t7y : 매치
        tya : 매치안됨(t와 y사이에 문자가 없기 때문)

    2) * =>의미 :  여러번 반복, *앞에 있는 문자를 0번 이상 반복(0번일 반복되지 않을 수도 있다.)
        ex)정규식 : bu*s (u가 0번 이상 반복되어야 한다.)
            bs : 매치 (u가 0번 반복.)
            bus : 매치
            buuuuus : 매치
    3) + => 의미 : 여러번 반복. +앞의 문자를 1번 이상 반복
        ex) 정규식 bu+s (u가 1번 이상 반복되어야 한다.)
            bs : 매치가 안됨 (u가 0번 반복.)
            bus : 매치
            buuuuus : 매치

    4) {숫자} => 의미 : 반복 횟수를 제한
        ex){1,} :  최소 1번 이상 반복(+ 와 같은 의미)
           {0,} :  최소 0번 이상 반복(* 와 같은 의미)
           {3}  : 무조건 3번만 반복
               정규식 : bu{3}s  (무조건 u가 3번만 반복)
                bs : 매치가 안됨 (u가 0번 반복.)
                bus : 매치가 안됨
                buuus : 매치
           {2,5} : 2~5번 반복
                정규식 : bu{2,5}s
                 bus : 매치가 안됨
                 buuus : 매치
                 buuuuuuuus : 매치가 안됨
    5) ? => 의미 :  있어도 없어도 됨 {0,1}과 동일
        ex) 정규식 : bu?s
                 bs : 매치
                 bus : 매치

3. re모듈
-기본적으로 설치 되어져있음
-정규표현식으로 사용
    ex) import re
        pat = re.compile('bu*s')   #정규식 : 'bu*s'을 compile하는 패턴을 만드는 것

4. 정규식 그룹
    () : 그룹
        ex) 전화번호 정규식 : '\d{3}-\d{3}-\d{4}'      # '\d{2,3}-\d{3,4}-\d{4}' :  지역번호가 2개에서 3개까지 허용
            지역번호, 나머지 전화번호를 그룹으로 나누고자 한다면,
            '(\d{3})-(\d{3}-\d{4})' 으로 표현하면 됨.
            첫번째 그룹은 group(1), 두번째 그룹은 group(2)으로 사용.
            전체 전화번호를 모두 가지고 올 때는 group() or group(0)으로 표현하면 됨

"""

import re
pat = re.compile('[a-z]')
res = pat.match("computer") #match : 왼쪽부터 매치시킴
print(res)

text = "에러 1004 : 레퍼런스 에러 \n 에러 1247:코드 오류"
text2 = "기타 사항은 전화번호 : 02-1234-5678로 연락 주세요"
regex2 = re.compile("\d\d-\d\d\d\d-\d\d\d\d")         #전화번호 정규식 :\d\d-\d\d\d\d-\d\d\d\d => 숫자의 갯수가 맞지 않으면 찾을 수 없다
res2 = regex2.search(text2)
pNumber = res2.group()
print(pNumber)


regex = re.compile("1247")
res = regex.search(text)            # search는 왼쪽부터 매치된 1개만 찾는다
# print(res)
if res !=None :
    print(res.group())
    #group()으로 매치된 결과를 확인할 수 있다.(findall에선 사용할 수 없다.) => <re.Match object; span=(0, 1), match='c'> : 에서 match='c'의 c만 얻어내는 명령
else:
    print('매칭 안됨')

text3 = "에러 1237 : 레퍼런스 에러 \n 에러 4427:코드 오류"
regex3 = re.compile("에러\s\d+")
res3 = regex3.findall(text3)
print(res3)


text4 = "기타 사항은 전화번호 : 02-1234-5678로 연락 주세요"
regex4 = re.compile("(\d{2})-(\d{4}-\d{4})")  # 그룹화 함 : () 사용
    # regex4 = re.compile("\d{2}-\d{4}-\d{4}")  # 일반적인 표현방식
res4 = regex4.search(text2)
# pNumber = res4.group()              #02-1234-5678
pNumber = res4.group(0)                #02-1234-5678
# pNumber = res4.group(1)             #02
# pNumber = res4.group(2)             # 1234-5678
print(pNumber)

text5 = "기타 사항은 전화번호 : 02-1234-5678로 연락 주세요"
regex5 = re.compile("(?P<area>\d{2})-(?P<number>\d{4}-\d{4})")          #그룹에 명명법 :?P<그룹명>
res5 = regex5.search(text2)
pNumber = res5.group(0)
print(pNumber)
print(res5.group("area"), res5.group("number"))
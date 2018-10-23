#"\sox" \s 가 정규식 문자로 있기 때문에 ox로만 인식하게 됨

import re
re.compile('\\white')               #\white : \부터 문자로 인식
pat = re.compile('Java|Python')             # | : or의 의미
res =  pat.match("Python")
print(res)
res =  pat.match("Java")
print(res)
res =  pat.match("JavaPython")
print(res)
res =  pat.match("PythonJava")
print(res)
res =  pat.match("PythonRuby")
print(res)
res =  pat.match("RubyJava")
print(res)
res =  pat.match("JavaRuby")
print(res)

print(re.search("How","How are you"))
print(re.search("are","How are you"))
print(re.match("are","How are you"))
print(re.search("^How","How are you"))
print(re.search("^are","How are you"))              #'^' 를 사용하였기 때문에 가장 앞에서 사용되는 문자열이여야 매치한다.

print(re.search("you$","How are you"))
print(re.search("you$","How are you. Hi"))          #'$' 를 사용하였기 때문에 가장 뒤에서 사용되는 문자열이여야 매치한다.

pat = re.compile('(ABC)+')                          #ABC가 계속 반복되는 경우
res = pat.search("ABCABCABCABEFDHYF OK?")
print(res)
print(res.group())

pat = re.compile('(\w+)\s+((\d+)[-](\d+[-]\d+))')       #group : 왼쪽에 1부터 순서가 부여
res = pat.search("kim 010-1234-5678")
print(res.group(1))
print(res.group(2))
print(res.group(3))                                 #소괄호의 번호는 외부의 소괄호 번호가 끝나면 다음 번호부터 넘버링
print(res.group(4))


#sub : 정규식과 매칭되는 부분을 다른 것으로 대치
pat =  re.compile('(어제 |오늘|내일)')
print(pat.sub('DAY','어제 날씨 그리고 오늘 날씨',count=2))         #매칭되는 치환대상 중 몇개나 치환할 것인가 지정

"""
웹 텍스트 스크래핑 -> 치환/삭제(sub) -> 형태소 분석기(형태소 단위로 분해,8개 품사, )
ex) 오늘 뉴스 사건  사고.....
{ '오늘' : 5,'뉴스' : 1, '사건': 10,....} => 딕셔너리 구조로 나타남
"""

pat = re.compile("(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# res = pat.search("kim 010-1234-5678")
# print(res.group('name'))
# print(pat.sub( ,"kim 010-1234-5267"))                   #name과 phone의 순서를 바꿔서 기재하고 싶을때
print(pat.sub("\g<phone> \g<name>",'kim 010-1234-5678'))
print(pat.sub("\g<2> \g<1>",'kim 010-1234-5678'))

"""
정규 표현식 예
^Test : Test로 시작하는 문자열
test$ :  test로 끝나는 문자열
^XYZ$ : XYZ로 시작하고 끝나는 문자열 ( XYZ만 사용해도 해당됨)
abc :  abc가 들어 있는 문자열

ab*: a뒤에 b가 0개 이상 있는 문자열(a,ab,abbbbbbbb)
ab+ : a뒤에 b가 1개 이상 있는 문자열(ab,abbbbb)
ab? : b가 1개 있을 수도 있고 없을 수도 있는 문자열(ab,a)
a?b+$:a는 있을 수도 있고 없을 수도 있고. 그 뒤에 반드시 한개 이상의 b로 끝나는 문자열

ab{2} : a뒤에 b가 2개 있는 문자열(abb)
ab{3,} : a뒤에 b가 3개 이상 있는 문자열(abbb,abbbbbb,abbbbbbbbbbb)
ab{2,4} : a뒤에 b가 2개 이상 4개 이하의 b가 있는 문자열(abb,abbb,abbbb)

a(bc)* : a뒤에 bc가 0번 이상 반복되는 문자열
a(bc){1,3} : a뒤에 bc가 1번 이상 3번 이하로 반복되는 문자열


hi|bye : hi또는 bye가 있는 문자열
(a|bc)de : ade또는 bcde문자열
(a|b)*c : a와 b가 뒤섞여 0번 이상 반복되며(*때문에 a,b는 없어도 된다.), 그 뒤에 c가 있는 문자열

.: 한 문자
..:두 문자
...: 세 문자

a.[0-9] : a뒤에 문자가 1개 있으며, 그 뒤에 숫자가 붙는 문자열
^.{3}$ : 반드시 세문자로 시작하고 세문자로 끝나는 문자열=>(세문자)

[ab] : a또는 b ( a|b와 같음)
[a-d] : 소문자 a~d (a|b|c|d또는 [abcd]와 같음)
^[a-zA-Z] ; 영문자로 시작하는 문자열
[0-9]% : % 문자 앞에 하나의 숫자가 있는 문자열
[0-9]$ :  숫자로 끝나는 문자열
[a-zA-Z0-9]$ :  영문자, 숫자로 끝나는 문자열

XML : 확장 가능한 마크업 언어(사용자가 태그를 정의)
    -태그 : 웹 문서를 작성할때 사용되는 마커(보통 사전에 정의 되어진다.)
<전국 날씨>
    <지역>
        서울
    </지역>
    <기온>
        35
    </기온>
</전국 날씨>
 : 태그 형태 => XML

"""





















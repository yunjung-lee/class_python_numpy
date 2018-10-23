"""
1.
    search() : 문자열 전체를 검색, 정규식 매치 조사
    match() : 문자열 왼쪽부터 검색, 정규식 매치 조사 => 매치되지 않는 사항이 나오면 바로 중단
    findall() : 정규식과 매치되는 모든 문자열을 리스트로 리턴
    finditer() : 정규식 매치되는 모든 문자열을 iterator객체로 리턴
    span=(,) : 매치가 되어진 위치


2.컴파일 옵션
    1)re.I 옵션(Ignore case): upper case, lower case와 관계없이 (대소문자 무시) 매칭
    2) . 옵션 :  모든 문자와 매치 (\n 제외)
        - re.DOTALL 또는 re.S  : 동일한 의미
    3) re.M(Multiline) : ^(문자열의 처음),$(문자열의 마지막)
    4) re.X(Verbose) :  주석을 라인단위로 추가할때

"""
#
# import re
# p = re.compile('[A-Za-z]+')
# m = p.match("7 java 9")
#
# print(m)
# #None
#
# m2 = p.search("9 java 7")
# print(m2)
# #<re.Match object; span=(2, 6), match='java'>
#
# res = p.findall("How are you?")
# print(res)
# #['How', 'are', 'you']
#
# res2 = p.finditer("How are you?")
# print(res2)
# #<callable_iterator object at 0x0386A950>
# #iterator object : 반복 가능한 객체
# #res2에는 'How', 'are', 'you'라는 3개의 문자열 리스트가 객체로 저장되어 있음
# for r in res2 :
#    # print(r)
# # <re.Match object; span=(0, 3), match='How'>
# # <re.Match object; span=(4, 7), match='are'>
# # <re.Match object; span=(8, 11), match='you'>
#    # print(r.group())
# # How
# # are
# # you
# #     print(r.start())
# # 0
# # 4
# # 8
#
#    # print(r.start())
#    # print(r.span())
#
#
# #m2 = re.match('[A-Za-z]+',"7 java 9")  #compile과 match를 결합하여 사용할 수 있다.

# import re
# pat = re.compile('a.k',re.DOTALL)
# res = pat.match('alk')
# #<re.Match object; span=(0, 3), match='alk'>
# # res = pat.match('ak')
# # None
# # res = pat.match('a\nk')
# # None
# # res = pat.match('asdk')
# # None
# # res = pat.match('a\nk')
# #  # re.compile('a.k',re.DOTALL) 을 사용해서 :  여러줄로 구성된 문자열에서 \n에 상관없이 검색하고자 할 때
# # <re.Match object; span=(0, 3), match='a\nk'>
# print(res)

# import re
# pat = re.compile('[a-z]',re.I)          #대소문자와 관계없이 매치
# print(pat.match('test'))
# print(pat.match('Test'))
# print(pat.match('TEST'))

import re
# pat = re.compile("^python\s\w+",re.M)                #^ :문자열의 시작이 python 으로 시작되는 문자열(한줄 만 나온다) 매치  + multiline option 필요
# # \s : space, tap     \w :  숫자&문자
pat = re.compile("\w+\spython$",re.M)               #$ :  python$으로 끝나는 문자열을 매치
text = '''python java
python c ruby r
seoul ganseo python
python one two three
'''

print(pat.findall(text))




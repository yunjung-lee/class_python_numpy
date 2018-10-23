#정규 표현식(정규식) : 일정한 규칙을 갖는 문자열을 표현하는 방법,
#거의 대부분의 언어가 지원.

"""
복잡한 문자열에서 특정 규칙을 만족하는 문자열을 검색한 다음
전처리(문자열 변경, 치환, 삽입 등)의 연산.
주어진 문자열이 규칙이 맞는지 확인하고자 하는 경우.
REGular EXpression; REGEX
수고를 덜어준다.
"""

jumin = """
kim 980102-1234567
park 970807-2345679
"""
res = []
for line in jumin.split('\n'):
    # print(line)
    word_res = []
    for word in line.split(" "):

        # print(len(word))
        if len(word)==14 and word[:6].isdigit() and word[8:].isdigit():
            # print(word[7:])
            word=word[:7]+'*******'
        word_res.append(word)
    res.append(" ".join(word_res))
print('\n'.join(res))




# print(jumin)

# sj = jumin.split()
# print(sj)

# sj = jumin.split('\n')
# print(sj)


import re           # 정규식과 관계된 함수 re
jumin = """
kim 980102-1234567
park 970807-2345679
"""
pattern = re.compile("(\d{6})[-]\d{7}")         #정규식 안에 쓰이는 본래의 뜻이 아닌 다른 뜻으로 사용되는 특수문자->메타문자 : (),{},[],|,\등
print(pattern.sub("\g<1>-*******",jumin))

#문자 메타
#[] : []사이에는 모든 문자가 들어갈 수 있음
#ex) 정규식이 [x,y,z]라면 x,y,z중 한개의 문자와 매치
#"a" : 정규식 x,y,z중에 없기 때문에 매치가 안됨
#"text" : 정규식 x,y,z중 일치하는 'x'문자 있음 -> 매치
#"y" : 정규식에 매치
#부분이라도 포함되어 있으면 매치
#ex) 정규식이 [A-Z]라면, A~Z까지의 모든 문자
#ex) 정규식이 [a-zA-Z]라면, 모든 알파벳
#ex) 정규식이 [0-9]라면,숫자 전체


import re
# p=re.compile('[xyz]')
p=re.compile('a[.]b')       # . 은 모든 문자를 의미
#a와 b사이에 어떤 문자가 들어가도 매치가 된다
#주의사항 :  a[.]b는 문자 그대로 .의 의미
m=p.match("a36.b")
print(m)
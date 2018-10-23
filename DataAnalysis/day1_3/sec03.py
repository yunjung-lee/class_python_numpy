"""
한글 코드

가~힇 :  한글의 범위
"""

# import re
#
# def hangulTest():
#     s="大韓민국에서 살고 있어요. 한국어는 very nice해요. English 싫어요 ㅋㅋㅋ"
#     hangul=re.compile('[^ 가-힣]+')
#     #한글 , 띄어쓰기를 제외한 모든 글자
#     #^ 은 반대의 의미 : 공백을 포함하면 적용되지 않는다
#     res2 = hangul.sub('',s)             # 한글, 띄어쓰기를 제외한 모든 글자들을 ''로 만들어버려라
#     print(res2)
#
#     res = hangul.findall(s)
#     print(res)
#
# hangulTest()

import re

pat = re.compile("""
&[#]
(
0[0-7]+
)
;
""",re.VERBOSE)             #re.VERBOSE : 표현식이 복잡하여 나눠서 보고 싶을 때 사용











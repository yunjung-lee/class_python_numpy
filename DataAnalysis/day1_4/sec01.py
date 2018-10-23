#parser : 주어진 문서에서 원하는 내용만 추출
#parser 종류 :dome, 제이슨(가벼워서 웹에서 사용),
#beautifulsope : 파워풀해서 많이 사용


import re

emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']


p=re.compile('^[a-zA-Z0-9+-_+.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')              # 정규표현식 안의 부호의 문자화 사용: \+부호



"""
아이드 @ 도메인 .최상위 도메인
"""





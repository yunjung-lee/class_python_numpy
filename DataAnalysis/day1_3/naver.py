import os
import sys
import urllib.request
token = "YOUR_ACCESS_TOKEN"
header = "Bearer " + token # Bearer 다음에 공백 추가
url = "https://openapi.naver.com/blog/listCategory.json"
request = urllib.request.Request(url)
request.add_header("Authorization", header)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# 네이버 블로그 Open API 예제 - 글쓰기
import os
import sys
import urllib.request
token = "YOUR_ACCESS_TOKEN"
header = "Bearer " + token # Bearer 다음에 공백 추가
url = "https://openapi.naver.com/blog/writePost.json"
title = urllib.parse.quote("네이버 블로그 api Test Python")
contents = urllib.parse.quote("네이버 블로그 api로 글을 블로그에 올려봅니다.")
data = "title=" + title + "&contents=" + contents
request = urllib.request.Request(url, data=data.encode("utf-8"))
request.add_header("Authorization", header)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

#  Blog mulipart upload - python
import os
import sys
import requests

token = "YOUR_ACCESS_TOKEN"
header = "Bearer " + token # Bearer 다음에 공백 추가
url = "https://openapi.naver.com/blog/writePost.json"

title = "네이버 블로그 api Test Python"
contents = "<font color='red'>python multi-part</font>로 첨부한 글입니다. <br> python 이미지 2개 첨부 <br> <img src='#0' /> <img src='#1' />";
data = {'title': title, 'contents': contents}
files = [
    ('image', ('YOUR_FILE_1', open('YOUR_FILE_1', 'rb'), 'image/jpeg', {'Expires': '0'})),
    ('image', ('YOUR_FILE_2', open('YOUR_FILE_2', 'rb'), 'image/jpeg', {'Expires': '0'}))
    ]

headers = {'Authorization': header }
response = requests.post(url, headers=headers, files=files, data=data)

rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)

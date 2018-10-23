#file open/close

f = open("test.txt","w")  #파일이 없으면 새로 만들어낸다.
#W : 쓰기, R:읽기, A(APPEND) : 추가 쓰기
# 파일 처리

for i in range(1,11):
    data = "%d번째 줄 입니다. \n" % i # 텍스트 파일 저장 : 인코딩방식 지정해야함(인코딩과 디코딩방식이 같아야함) <> 바이너리 저장(2진수) : .exe
    # 인코딩 : 텍스트파일을 저장한다. =>텍스트들을 코드(부호화)로 변환하여 저장한다  : ascii코드처럼
    # print(data)
    f.write(data)


f.close()
#파일 종료 : 메모리의 파일 삭제


f = open("test.txt","r")
print(f) # test 파일의 오픈 정보를 보여준다. : <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp949'>
while True:
    line = f.readline()
    if not line :   #상시구문처럼 사용 line 안에 정보가 없을 때 란 의미
        break
    print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
f.close()


lines = f.readlines()
# print(lines)
# #['1번째 줄 입니다. \n', '2번째 줄 입니다. \n', '3번째 줄 입니다. \n', '4번째 줄 입니다. \n', '5번째 줄 입니다. \n', '6번째 줄 입니다. \n', '7번째 줄 입니다. \n', '8번째 줄 입니다. \n', '9번째 줄 입니다. \n', '10번째 줄 입니다. \n']
for line in lines :
    print(line)


f = open("test.txt","r")
data = f.read()  #하나의 문자열로 읽어진다.(list 아님)
print(data)
f.close()

f= open("test.txt","a")
for i in  range(11,15):
    data = "%d번째 줄 입니다. \n" % i
    f.write(data)

f.close()

#다음과 같이 총 5줄로 구성된 input.txt파일이 있다.
#모든 숫자를 읽어 총합과 평균을 구하고 화면에 출력,
#result.txt파일에도 출력(평균)

#input.txt 파일 내용
#70
#55
#90
#87
#38

f = open("input.txt","w")
f.write('70\n55\n90\n87\n38')
f.close()
f=open("input.txt","r")
data = f.read()
f.close()
data2=data.split("\n")
sum = 0
for i in data2 :
    sum = sum+int(i)
print(sum)
avg = sum/len(data2)
print(avg)

f=open("result.txt","w")
f.write(str(avg))
f.close()

# f = open("input.txt","w")
# f.write('70\n''55\n''90\n''87\n''38')
# f.close()
# f=open("input.txt","r")
# lines = f.readlines()
# print(lines)
# f.close()
# sum=0
# for line in lines:
#     sum = sum +int(line)
# print(sum)


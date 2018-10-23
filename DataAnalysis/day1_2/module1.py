#용어 정리
#클래스(class) : 실체는 없는 틀만 존재하는 개념=> 객체를 만들어서 처리 : 빅데이터는 의미 없음
#모듈(module) :  클래스, 변수, 함수를 모아놓은 파일 (.py)

def sum(x,y):
    return x+y
#자동 형변환 int+flot => flot + flot으로 자동적으로 형변환

def ssum(x,y):
    if type(x)!=type(y):  #타입 비교
        print("데이터 형이 서로 다르므로 연산 불가")
        return
    else:
        ret = sum(x,y)
        return ret
#함수 정의만 있고 호출이 없기 때문에 다른 곳에서 호출해야만 사용이 된다.

if __name__ == "__main__" : #__name__ 라는 특별한 변수가 있음. 자기자신(module1)
                            #시키게 되면  __name-- 변수의 값으로는  __main__ dl wjwkd
                            #자기 자신을 제외한 (module1이 아닌) 다른 파일에서 module을 실행시키면
                            #__name__ 변수 값에는 "module1"이라는 모듈명이 문자값으로 저장됨

    # 메인 호출로 지정되어있기 때문에 모듈로 호출되지 않음
    print(ssum('k',5))
    print(ssum(1,5))
    print(sum(50,3.14))

#타입확인
#print(type(x))
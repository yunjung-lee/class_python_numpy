#matplotlib : 시각화를 위한 패키지. 여러 서브패키지를 갖고 있다.
import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

plt.title('Plot')
# 라인플롯 기본
# plt.plot([10,20,30,40],[1,4,9,16],'bD-.')                       #b:blue,....
# plt.ylim(-10,30)
# plt.xlim(0,50)
# x=np.linspace(-np.pi,np.pi,256)
# c=np.cos(x)
# plt.plot(x,c)
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi]['a','b','c','d','e'])
# plt.yticks([-1,0,1],['low','zreo','high'])


#여러 선 그리기
# t=np.arange(0.,5.,0.2)
# plt.plot(t,t,'r--',t,0.5*t**2,'bs:',t,0.2*t**3,'g^-')

# x=np.linspace(-np.pi,np.pi,256)
# c,s = np.cos(x),np.sin(x)
# plt.plot(x,c,ls='--',label = 'cosine')                          # ls= : 라인 정보,label =:범례 정보
# plt.plot(x,s,ls=':',label = 'sine')
# plt.legend(loc =5)
# #plt.legend()   디폴트(best==>loc =0):가장 적절한 위치에 범례 출력, 0~10까지 지정 가능
#
# plt.xlabel('xlabel')            # x축 이름
# plt.ylabel('ylabel')            # Y축 이름
# plt.show()
#
# # matplotlib :  figure, axis, axes 객체로 구성
# # figure ;  1개 이상의  axes로 구성
# # axes : 1개 이상의 axis로 구성(화면 분할 가능)


# f1=plt.figure(figsize=(10,2))            #그림의 크기
# plt.plot(np.random.randn(100))

f1=plt.figure(1)
# plt.plot([1,2,3,4],'ro:')

f2 = plt.gcf()                             #plt.gcf() : 이전의 figure에 대한 복사
print(f1,id(f1))
print(f2,id(f2))                             #f1의 복사본으로 주소도 id도 동일

# 화면 나누기 (subplot)
x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(2,1,1)                              #subplot(2,1,1) : 열=>2개창,행=>1개창, 첫번째 창
plt.plot(x1,y1,'yo-' )

plt.subplot(2,1,2)                              #subplot(2,1,1) : 열=>2개창,행=>1개창, 두번째 창
plt.plot(x2,y2,'r.:')

# print(x1)
plt.show()





















































































































































































































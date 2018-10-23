from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager,rc
import platform
#시각화시 한글이 깨짐 문자

#한글 깨짐 현상을 없애주는 문장 : 법칙처럼 사용
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname = 'c:/Windows/Fonts/malgun.ttf').get_name()
    rc('font',family = font_name)
matplotlib.rcParams['axes.unicode_minus']=False

# open("output_final.txt",'r')
# font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)
# matplotlib.rcParams['axes.unicode_minus']=False

#시각화
f=open("output_final.txt", "r")
i=1
news_word=[]
word_cnt=[]
while True:
    line=f.readline()
    word, count=line.split(" ")
    news_word.append(word)
    word_cnt.append(int(count[0]))
    if i==10 : break
    i+=1
f.close()
print(news_word)
print(word_cnt)


#그래프 그리는 공식
xs=[i+0.1 for i,_ in enumerate(news_word)]
#enumerate 순환하며 인덱스를 가져오는 공식
plt.bar(xs,word_cnt)
plt.ylabel('등장 단어의 수')
plt.title('오늘의 날씨 키워드')
plt.xticks([i+0.2 for i, _ in enumerate(news_word)],news_word)

plt.show()
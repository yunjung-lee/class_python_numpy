#from bayes import BayesianFilter
import bayes
bf = bayes.BayesianFilter()         #: BayesianFilter호출: __init__함수 호출
#bf = BayesianFilter()
#텍스트 학습
bf.fit("파격 세일 - 오늘까지 30% 할인합니다.","광고")
bf.fit("쿠폰 선물 & 무료 배송.","광고")
bf.fit("현대 백화점 세일.","광고")
bf.fit("여름과 함께 찾아온 시원한 신제품 소식.","광고")
bf.fit("인기 제품 기간 한정 세일.","광고")
bf.fit("김부장님 프로젝트 진행 상황 보고 입니다..","중요")
bf.fit("오늘 일정 확인하세요.","중요")
bf.fit("계약 잘 부탁드립니다.","중요")
bf.fit("회의 일정이 등록되었습니다.","중요")
bf.fit("오늘 일정이 없습니다.","중요")




#예측
bf.predict("오늘의 일정 중에서 신제품 홍보가 있습니다.")
pre, scorelist = bf.predict("재고 정리 할인, 무료 배송.")
print("결과 = ",pre)
print(scorelist)
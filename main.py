# 파일이름 : 파이썬 스마트 물류 센터
# 작 성 자 : 60232294 신지웅
print("파이썬 스마트 물류 센터에 오신 것을 환영합니다!")

Labels = [['제품명', '문자열'], ['기초 재고량', '정수, 단위 : 개'], ['오늘 판매량', '정수, 단위 : 개'], ['제품 단가', '정수, 단위 :원'], ['예상 마진율', '소수점(예 : 0.15)']]

product_data =  []

for i in range(len(Labels)):

    info = input(f"{Labels[i][0]}({Labels[i][1]})을(를) 입력하세요 : ") 

    product_data.append(info)

 

print()

print()

 

#input 내용 정수화, 실수화

stock_quantity = int(product_data[1])

daily_sales = int(product_data[2])

unit_price = int(product_data[3])

margin_rate = float(product_data[4])

 

#잔여 재고, 총 재고가치 계산

remaining_stock = stock_quantity - daily_sales

total_value = remaining_stock * unit_price

 

#발주 시급성 계산 및 등급 판정

if remaining_stock > 0:

    risk_score = (daily_sales * 10 / remaining_stock )* 30 + (margin_rate * 20)

else:

    risk_score = 200 #잔여 재고가 0이면, 계산이 불가하므로 최고 점수(S등급) 부여

 

 

if risk_score >= 100 :

    urgent_grade = 'S'

    status_msg = "긴급 발주가 필요한 긴급 상황입니다!"

elif risk_score >= 60 :

    urgent_grade = 'A'

    status_msg = "재고 부족이 예상되니 발주를 준비하세요."

elif risk_score >= 30 :

    urgent_grade = 'B'

    status_msg = "재고 수준이 보통입니다."

elif risk_score >= 10 :

    urgent_grade = 'C'

    status_msg = "재고가 비교적 넉넉한 편입니다"

else :

    urgent_grade = 'F'

    status_msg = "재고가 매우 충분하여 관리가 불필요합니다. \n수요에 비해 공급이 너무 많은 것은 아닌지 고민해보세요!"

 

# 제품 종합 정보 제공

print(f"제품명 : {product_data[0]}")

print(f"기초 재고량 : {stock_quantity:,} 개")

print(f"오늘 판매량 : {daily_sales:,} 개")

print(f"제품 단가 : {unit_price:,} 원")

print(f"예상 마진율 : {margin_rate}")

 

#물류 진단 리포트 제공

print()

print("-"*40)

print(f"{product_data[0]} 물류 진단 레포트")

print("-"*40)

print(f"현재 잔여 재고 : {remaining_stock:,}개")

print(f"총 재고가치 : {total_value:,}원")

print(f"발주 위험 점수 : {risk_score:.2f}점")

print(f"최종 발주 등급 : {urgent_grade}등급")

print(f"진단 결과 : {status_msg}")

print()

 

#골든타임 알림

if urgent_grade == 'S' and margin_rate >= 0.2:

    print("[골든타임 알림]")

    print("이 품목은 수익성이 높고 재고가 부족한 핵심 관리 대상입니다!")

    print("발주 후 입고 시간을 고려해 최우선적으로 추가 주문을 진행해주세요!")

 

#종료 알림

print("-"*40)

print("진단이 종료되었습니다. 파이썬 스마트 물류 센터를 이용해주셔서 감사합니다.")
# 파일이름 : 파이썬 스마트 물류 센터
# 작 성 자 : 60232294 신지웅

things_count = 0
Labels = [['제품명', '문자열'], ['기초 재고량', '정수, 단위 : 개'], ['오늘 판매량', '정수, 단위 : 개'], ['제품 단가', '정수, 단위 : 원'], ['예상 마진율', '소수점(예 : 0.15)']]

product_data = [] #정보 입력 시 저장 리스트
product_name_data = [] #상품명 저장 리스트
product_stock_data = [] #입고량 저장 리스트
product_sales_data = [] #판매량 저장 리스트
product_cost_data = [] #단가 저장 리스트
product_margin_rate = [] #마진율 저장 리스트
product_risk_score = [] #상품별 긴급 발주 점수
product_urgent_grade = [] #상품별 긴급 발주 등급 저장 리스트
product_remaining_data = [] #상품별 잔여 재고 리스트
product_total_value = [] #총 자산 가치
product_status_msg = [] #제품별 상태 메시지
product_low_stock = [] #S등급 상품 저장 리스트




#시스템 메뉴 출력 함수
def start_system():
    print("-"*30)
    if things_count == 0:
        print("파이썬 스마트 물류 센터에 오신 것을 환영합니다!")
    else:
        print("필요한 기능의 번호를 입력해주세요.")
    print("-"*30)

    print("""
    1. 제품 정보 입력 및 계산하기
    2. 제품 항목별 결과보기
    3. 최종 결과 보기(종료)
    """)

#정보 입력 함수
def insert_information():
    global things_count, product_data
    product_data = [] #정보 입력 시 리스트 초기화



    for i in range(len(Labels)):
        while True :
            info = input(f"{Labels[i][0]}({Labels[i][1]})을(를) 입력하세요 : ")
    
            if i > 0 :
                if not info.replace(".",'').replace("-",'').isdigit():
                    print(f"{Labels[i][0]}은(는) 숫자만 입력해야 합니다. 다시 입력하세요.")
                    continue
                if float(info) < 0 :
                    print(f"{Labels[i][0]}은(는) 0 이상의 숫자여야 합니다. 다시 입력하세요.")
                    continue
            
            if i == 0:
                product_name_data.append(info)
            elif i == 1:
                product_stock_data.append(int(info))
            elif i == 2:
                product_sales_data.append(int(info))
            elif i == 3:
                product_cost_data.append(int(info))
            elif i == 4:
                product_margin_rate.append(float(info))
            
            product_data.append(info)
            break

    things_count += 1



# 계산 함수
def calculating_information():
    stock_quantity = int(product_data[1])
    daily_sales = int(product_data[2])
    unit_price = int(product_data[3])
    margin_rate = float(product_data[4])

    #잔여 재고, 총 재고가치 계산
    remaining_stock = stock_quantity
    remaining_stock -= daily_sales
    product_remaining_data.append(remaining_stock)

    total_value = remaining_stock * unit_price
    product_total_value.append(total_value)

    #발주 시급성 계산 및 등급 판정

    if remaining_stock > 0:
        risk_score = (daily_sales * 10 / remaining_stock) * 30 + (margin_rate * 20)
    else:
        risk_score = 200 #잔여 재고가 0이면, 계산이 불가하므로 최고 점수(S등급) 부여
    
    if risk_score >= 100 :
        urgent_grade = 'S'
        status_msg = "긴급 발주가 필요한 긴급 상황입니다!"
        product_low_stock.append(product_name_data[things_count - 1])   
    elif risk_score >= 60 :
        urgent_grade = 'A'
        status_msg = "재고 부족이 예상되니 발주를 준비하세요."

    elif risk_score >= 30 :
        urgent_grade = 'B'
        status_msg = "재고 수준이 보통입니다."
    
    elif risk_score >= 10 :
        urgent_grade = 'C'
        status_msg = "재고가 비교적 넉넉한 편입니다."
    
    else:
        urgent_grade = 'F'
        status_msg = "재고가 매우 충분하여 관리가 불필요합니다. \n수요에 비해 공급이 너무 많은 것은 아닌지 고민해보세요!"
    

    product_risk_score.append(risk_score)
    product_urgent_grade.append(urgent_grade)
    product_status_msg.append(status_msg)


# 제품 목록 선택 함수
def list_of_products():
    for i in range(len(product_name_data)):
        print(f"{i+1}. {product_name_data[i]}")
    
    select_product = int(input("점검할 제품의 번호를 입력해주세요 : "))
    return select_product

#개별 점검 보고서 함수
def midterm_inspection(midterm_choice):
    idx = midterm_choice - 1
    print(f"""
    {idx+1}번 {product_name_data[idx]}를 선택하셨습니다.
    제품명 : {product_name_data[idx]}
    기초 재고량 : {product_stock_data[idx]}개
    오늘 판매량 : {product_sales_data[idx]}개
    제품 단가 : {product_cost_data[idx]}원
    예상 마진율 : {product_margin_rate[idx]}
    현재 재고량 : {product_remaining_data[idx]}개
    발주 시급성 점수 : {product_risk_score[idx]:.2f}점
    발주 시급성 등급 : {product_urgent_grade[idx]}
    상태 메시지 : {product_status_msg[idx]}
    """)

#최종 보고서 함수
def view_final_report():
    print(f"""
    [파이썬 스마트 물류 센터 최종 리포트]
    입고된 제품 목록 {",".join(product_name_data)}
    총 재고 수량 : {sum(product_remaining_data)}개
    총 자산 가치 : {sum(product_total_value)}
    최고가 제품 : {max(product_cost_data)}원
    최저가 제품 : {min(product_cost_data)}원""")
    if len(product_low_stock) == 0:
        print("""품절 임박 제품(S등급)이 없습니다.""")
    else:
        print(f"""품절 임박 제품(S등급) : {",".join(product_low_stock)}""")
    print("""파이썬 스마트 물류 시스템을 종료합니다.""")

#메인 실행 루프
while True :
    start_system()
    choice = int(input("선택한 메뉴의 번호만 입력해주세요.(예시 : 1 / 2 / 3 ) : "))

    if choice == 1 :
        insert_information()
        calculating_information()
    
    elif choice == 2 :
        if things_count == 0:
            print("어떠한 정보도 기입하지 않았습니다. 정보를 입력한 후 선택해주세요.")
            continue
        idx_product = list_of_products()
        midterm_inspection(idx_product)
    
    elif choice == 3 :
        if things_count == 0:
            print("어떠한 정보도 기입하지 않았습니다. 정보를 입력한 후 선택해주세요.")
            continue
        view_final_report()
        break


# 파일이름 : 파이썬 스마트 물류 센터
# 작 성 자 : 60232294 신지웅

things_count = 0
Labels = [['제품명', '문자열'], ['기초 재고량', '정수, 단위 : 개'], ['오늘 판매량', '정수, 단위 : 개'], ['제품 단가', '정수, 단위 : 원'], ['예상 마진율', '소수점(예 : 0.15)']]
total_inventory_data= [] 


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
def insert_and_calculate_information():
    global things_count

    temp_data = [] #임시 데이터 리스트


    for i in range(len(Labels)):
        while True :
            try:
                info = input(f"{Labels[i][0]}({Labels[i][1]})을(를) 입력하세요 : ")
        
                if i == 0:
                    temp_data.append(info)
                elif i == 4:
                    temp_data.append(float(info))#마진율
                else:
                    if int(info) < 0 :
                        print(f"{Labels[i][0]}은(는) 0 이상의 숫자여야 합니다. 다시 입력하세요.")
                        continue
                    temp_data.append(int(info))
                break

            except ValueError:
                print("잘못된 입력입니다. 형식에 맞는 숫자를 입력해주세요.")

    name = temp_data[0]
    stock_quantity = temp_data[1]
    daily_sales = temp_data[2]
    unit_price = temp_data[3]
    margin_rate = temp_data[4]
    
    remaining_stock = stock_quantity - daily_sales
    total_value = remaining_stock * unit_price


    if remaining_stock > 0:
        risk_score = (daily_sales * 10 / remaining_stock) * 30 + (margin_rate * 20)
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
        status_msg = "재고가 비교적 넉넉한 편입니다."
    
    else:
        urgent_grade = 'F'
        status_msg = "재고가 매우 충분하여 관리가 불필요합니다. \n수요에 비해 공급이 너무 많은 것은 아닌지 고민해보세요!"
    

    product_record = [name, stock_quantity, daily_sales, unit_price, margin_rate, remaining_stock, total_value, risk_score, urgent_grade, status_msg]
    total_inventory_data.append(product_record)
    things_count += 1
    print(f"\n[{name}] 제품의 정보가 성공적으로 등록되었습니다!\n")




#제품 전체 점검
def view_all_products():
    print()
    print("="*40)
    print("전체 제품 보고서")
    print("="*40)


    for i in range(len(total_inventory_data)):
        print(f"""
              [{i+1}번 제품] : {total_inventory_data[i][0]}
              - 기초 재고량 : {total_inventory_data[i][1]}개 | 오늘 판매량 : {total_inventory_data[i][2]}개 | 현재 재고량 : {total_inventory_data[i][5]}개
              - 제품 단가 : {total_inventory_data[i][3]} | 예상 마진율 : {total_inventory_data[i][4]}
              - 발주 시급성 점수 : {total_inventory_data[i][7]:.2f}점 | 등급 : {total_inventory_data[i][8]}
              - 상태 메시지 : {total_inventory_data[i][9]}
              """)
        print("-"*40)

#최종 보고서 함수
def view_final_report_and_save():
    names= []
    total_remaining = 0
    total_assets = 0
    prices = []
    s_grade_items = []

    for p in total_inventory_data:
        names.append(p[0])
        total_remaining += p[5]
        total_assets += p[6]
        prices.append(p[3])
        
        if p[8] == 'S':
            s_grade_items.append(p[0])

    max_price = max(prices)
    min_price = min(prices)

    print(f"""
    [파이썬 스마트 물류 센터 최종 리포트]
    입고된 제품 목록 {",".join(names)}
    총 잔여 재고 수량 : {total_remaining}개
    총 자산 가치 : {total_assets}
    최고가 제품 : {max_price}원
    최저가 제품 : {min_price}원""")

    if len(s_grade_items) == 0:
        print("""품절 임박 제품(S등급)이 없습니다.""")
    else:
        print(f"""품절 임박 제품(S등급) : {",".join(s_grade_items)}""")
    
    try:
        with open("smart_logistics_data.txt", "w", encoding = "utf-8") as file:
            file. write("제품명, 기초재고량, 오늘 판매량, 제품단가, 예상 마진율, 현재 재고량, 총 자산가치, 위험 점수, 등급\n ")
            for i in range(len(total_inventory_data)):
                p = total_inventory_data[i]
                file.write(f"{p[0]},{p[1]},{p[2]},{p[3]},{p[4]},{p[5]},{p[6]},{p[7]},{p[8]}\n")
        print(f"\n데이터가 'smart_logistics_data.txt' 파일로 안전하게 저장되었습니다.")
    except:
        print("\n데이터 저장 중 오류가 발생했습니다.")
    
    print("""파이썬 스마트 물류 시스템을 종료합니다.""")

#메인 실행 루프
while True :
    start_system()
    
    try:
        choice = int(input("선택한 메뉴의 번호만 입력해주세요.(예시 : 1 / 2 / 3 ) : "))
    
    except ValueError:
        print("\n[오류] 숫자로만 입력해주세요.")
        continue
    
    
    
    if choice == 1 :
        insert_and_calculate_information()

    
    elif choice == 2 :
        if things_count == 0:
            print("어떠한 정보도 기입하지 않았습니다. 정보를 입력한 후 선택해주세요.")
            continue
        view_all_products()

    
    elif choice == 3 :
        if things_count == 0:
            print("어떠한 정보도 기입하지 않았습니다. 정보를 입력한 후 선택해주세요.")
            continue
        view_final_report_and_save()
        break
    
    else:
        print("\n[오류] 1, 2, 3 중에서 선택해주세요!")

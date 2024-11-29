try:
    print("교통카드 단말기입니다.")
    balance = int(input("현재 교통카드 잔액을 입력하세요 (원): "))
    fare = int(input("요금을 입력하세요 (원): "))

    if balance < fare:
        raise ValueError("잔액이 부족합니다.")
    balance -= fare
    print("결제 완료! 남은 잔액: (원)".format(balance))

except ValueError as err:
    print(err)
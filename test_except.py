class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
try:
    while(True):
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
        elif order > chicken or order > 10:
            raise SoldOutError
        else:
            print("[대기번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError:
    print("재고가 소진되어 더 이상 주문을 받을 수 없습니다.")


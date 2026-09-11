class History():
    def __init__(self):
        self.history = []

    def add_history(self):
        print("===== 이력 기록 =====")
        menu = input("메뉴 : ")

        if menu.strip() == "":
            print("메뉴를 입력해주세요.")
            return

        try:
            price = int(input("가격 : "))
        except ValueError:
            print("숫자로 입력해주세요.")
            print()
            return

        if price <= 0:
            print("가격은 0보다 큰 숫자로 입력해주세요.")
            return

        self.history.append({"menu":menu, "price":price})
        
        print()
        print("기록되었습니다!")
        print(f"{menu} / {price}원")

        return self.history
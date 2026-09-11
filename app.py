from lunchmenu import LunchMenu
from history import History
from coffee import Coffee
from budget import BudgetManager
from calories import Calories

class App:
    def __init__(self):
        self.lunchmenu = LunchMenu()
        self.history = History()
        self.coffee = Coffee()
        self.budget = BudgetManager()

    def select_menu(self):
        print()
        print("1. 점메추 2. 이력 3. 커피내기 4. AI 칼로리 계산기 5. 예산관리 0. 종료")
        return input("메뉴를 선택해 주세요: ")

    def run(self):
        while True:
            # 메뉴 선택
            menu = self.select_menu()
            if menu == "1":
                # 점메추
                self.lunchmenu.run()
            elif menu == "2":
                # 이력
                self.history.add_history()
            elif menu == "3":
                # 커피내기
                self.coffee.run()
            elif menu == "4":
                # 예산 관리
                self.budget.run()
            elif menu == "5":
                # AI 칼로리 계산기
                self.calories.run()
            elif menu == "0":
                print()
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 번호입니다. 다시 선택해주세요.")

# test
# app = App()
# app.run()
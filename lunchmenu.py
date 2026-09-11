import random


class LunchMenu():
    def __init__(self):
        self.menus = {
            "한식": ["김치찌개", "제육볶음", "돈까스", "쌀국수", "된장찌개"],
            "중식": ["짜장면", "짬뽕", "탕수육", "볶음밥", "마파두부"],
            "일식": ["돈카츠", "초밥", "우동", "라멘", "규동"],
            "분식": ["떡볶이", "김밥", "순대", "튀김", "라볶이"]
        }

    def run(self):
        while True:
            print("\n===== 메뉴 종류 선택 ======")
            print("1. 한식")
            print("2. 중식")
            print("3. 일식")
            print("4. 분식")
            print("5. 전체 랜덤")
            print("0. 종료")

            s = int(input("메뉴 번호를 선택해주세요: "))

            if s == 1:
                menu = random.choice(self.menus["한식"])
                print(f"오늘의 한식 추천: {menu}")

            elif s == 2:
                menu = random.choice(self.menus["중식"])
                print(f"오늘의 중식 추천: {menu}")

            elif s == 3:
                menu = random.choice(self.menus["일식"])
                print(f"오늘의 일식 추천: {menu}")

            elif s == 4:
                menu = random.choice(self.menus["분식"])
                print(f"오늘의 분식 추천: {menu}")

            elif s == 5:
                category = random.choice(list(self.menus.keys()))
                menu = random.choice(self.menus[category])
                print(f"오늘의 랜덤 추천: {category} - {menu}")

            elif s == 0:
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 번호입니다. 다시 선택해주세요.")
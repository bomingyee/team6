import json
from datetime import datetime
from pathlib import Path


class History:
    FILE_PATH = Path(__file__).with_name("history.json")

    def __init__(self):
        self.history = []

    def add_history(self):
        print("\n===== 이력 기록 =====")
        menu = input("메뉴: ")
        price = int(input("가격: "))

        self.history.append({"menu":menu, "price":price})
        
        print()
        self.history = self.load()

    def load(self):
        if not self.FILE_PATH.exists():
            return []

        try:
            with self.FILE_PATH.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            return []

        return data if isinstance(data, list) else []

    def record(self, menu, price):
        record = {
            "menu": menu,
            "price": price,
            "recorded_at": datetime.now().isoformat(timespec="seconds"),
        }
        self.history.append(record)

        with self.FILE_PATH.open("w", encoding="utf-8") as file:
            json.dump(self.history, file, ensure_ascii=False, indent=2)

        return record

    def has_today_record(self):
        today = datetime.now().date().isoformat()
        for record in self.history:
            if record.get("recorded_at", "").startswith(today):
                return True
        return False

    def record_meal(self):
        if self.has_today_record():
            print("오늘의 점심은 이미 기록되었습니다.")
            print("내일 다시 기록해 주세요.")
            return

        print("===== 이력 기록 =====")
        menu = input("메뉴 : ")

        while True:
            try:
                price = int(input("가격 : "))
                if price < 0:
                    print("가격은 0원 이상 입력해 주세요.")
                    continue
                break
            except ValueError:
                print("가격은 숫자로 입력해 주세요.")

        record = self.record(menu, price)

        print("기록되었습니다!")
        print(f"{record['menu']} / {record['price']}원")
        return record

    def show(self):
        print("===== 점심 이력 =====")
        if len(self.history) == 0:
            print("저장된 이력이 없습니다.")
            print("총 소비 비용: 0원")
            return self.history

        total_cost = 0
        for record in self.history:
            recorded_at = record.get("recorded_at", "").replace("T", " ")
            menu = record.get("menu", "")
            price = int(record.get("price", 0))
            print(f"날짜: {recorded_at}")
            print(f"메뉴: {menu} / 금액: {price:,}원")
            print()
            total_cost += price

        print("------------------------------")
        print(f"총 소비 비용: {total_cost:,}원")

        return self.history

    def run(self):
        while True:
            print()
            print("1. 점심기록 2. 점심이력 3. 돌아가기")
            menu = input("메뉴를 선택해 주세요: ")
            print()

            if menu == "1":
                self.record_meal()
            elif menu == "2":
                self.show()
            elif menu == "3":
                break
            else:
                print()
                print("잘못된 메뉴입니다. 1~3 중에서 선택해 주세요.")
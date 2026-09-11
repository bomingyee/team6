class BudgetManager():
    def __init__(self):
        self.budget = 0

    def run(self):
        while True:
            try:
                self.budget = int(input("이번 달 목표 식비 예산을 입력하세요 : "))

                if self.budget <= 0:
                    print("0보다 큰 금액을 입력해주세요.")
                    continue

                print(f"목표 예산이 {self.budget:,}원으로 설정되었습니다.")
                break

            except ValueError:
                print("숫자만 입력해주세요.")

    def show_budget(self, history):
        if self.budget == 0:
            print("먼저 목표 예산을 설정해주세요.")
            return

        total = 0

        for item in history:
            total += item["price"]

        remain = self.budget - total
        rate = total / self.budget * 100

        print()
        print("===== 월 식비 예산 관리 =====")
        print(f"목표 예산 : {self.budget:,}원")
        print(f"현재 지출 : {total:,}원")
        print(f"남은 예산 : {remain:,}원")
        print(f"예산 사용률 : {rate:.1f}%")

        if rate >= 100:
            print("예산을 초과했습니다!")
        elif rate >= 80:
            print("예산을 80% 이상 사용했습니다.")
        else:
            print("아직 예산에 여유가 있습니다.")
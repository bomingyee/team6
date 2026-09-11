import time
import random


class Coffee():
    def __init__(self):
        pass

    def run(self):
        print("\n===== 커피내기 =====")

        people = []

        count = int(input("참여 인원 수: "))

        for i in range(count):
            name = input(str(i + 1) + "번: ")
            people.append(name)

        winner = random.choice(people)

        messages = [
            "오늘의 커피 요정으로 선정되었습니다!",
            "동료들의 카페인을 책임져 주세요!",
            "카드는 가볍게, 마음은 무겁게...",
            "축하합니다! 오늘의 커피 담당입니다!",
            "다음 기회에는 꼭 피하시길 바랍니다!"
        ]

        message = random.choice(messages)

        print()

        for i in range(4):
            print("두구두구...")
            time.sleep(1)

        print()
        print("커피 당첨자는...")
        print()
        print(winner)
        print()
        print("오늘 커피는", winner + "님이 쏩니다!!!!!")

        print()
        print("☕ 오늘의 한마디")
        print(message)
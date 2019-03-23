
import random


NUMBER_LINES = 6
MIN = 1
MAX = 45


def main():
    number_quick_picks = int(input('How many quick picks? '))
    while number_quick_picks < 0:
        print('Invalid input. Try again.')
        number_quick_picks = int(input('How many quick picks? '))

    for i in range(number_quick_picks):
        quick_pick = []
        for j in range(NUMBER_LINES):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
            quick_pick.sort()
        # print(quick_pick)
        print(" ".join("{:6}".format(number) for number in quick_pick))


main()


import random


NUMBER_LINES = 6
MIN = 1
MAX = 45

quick_pick = []
number_quick_picks = int(input('How many quick picks? '))
for i in range(number_quick_picks):
    number = random.randint(MIN, MAX)
    quick_pick.append(number)

print(quick_pick)

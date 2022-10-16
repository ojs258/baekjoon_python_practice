dice = list(map(int,(input().split())))

if dice.count(dice[1]) == 3:
    print(dice[1] * 1000 + 10000)
elif dice.count(dice[1]) == 2:
    print(dice[1] * 100 + 1000)
elif dice.count(dice[2]) == 2:
    print(dice[2] * 100 + 1000)
else:
    print(max(dice)*100)
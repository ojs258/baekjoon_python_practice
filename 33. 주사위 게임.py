n = int(input())
ans = []
for i in range(n):
    dice = list(map(int, input().split()))
    if dice.count(dice[1]) == 3:
        ans.append(dice[1] * 1000 + 10000)
    elif dice.count(dice[1]) == 2:
        ans.append(dice[1] * 100 + 1000)
    elif dice.count(dice[2]) == 2:
        ans.append(dice[2] * 100 + 1000)
    else:
        ans.append(max(dice)*100)
print(max(ans))
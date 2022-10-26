import sys

num = []; ans = []

for i in range(7):
    num.append(int(sys.stdin.readline()))
for i in num:
    if i % 2 != 0:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans), min(ans), sep="\n")
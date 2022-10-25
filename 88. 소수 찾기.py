import sys
sys.stdin.readline()

num = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in num:
    cond = 1
    for x in range(2,i):
        if i % x == 0:
            cond = 0
    if i == 1:
        pass
    elif cond == 1:
        cnt = cnt + 1
print(cnt)
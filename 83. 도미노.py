import sys
ans = 0
for i in range(1, int(sys.stdin.readline().rstrip('\n'))+1):
    sum = 0
    for x in range(1, i+1):
        sum = sum + x + i
    ans = ans + sum + i
print(ans)
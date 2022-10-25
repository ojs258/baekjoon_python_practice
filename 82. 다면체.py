import sys
ans = []
for i in range(int(sys.stdin.readline())):
    a, b = map(int,sys.stdin.readline().split())
    ans.append(abs(a-b-2))

for x in ans:
    print(x)
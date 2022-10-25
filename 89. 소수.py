import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
prime = []
for i in range(m, n+1):
    cond = 1
    for x in range(2,i):
        if i % x == 0:
            cond = 0
    if i == 1:
        pass
    elif cond == 1:
        prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime), min(prime), sep='\n')
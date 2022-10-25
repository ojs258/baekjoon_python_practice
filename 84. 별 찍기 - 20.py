import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    if i % 2 != 0:
        for x in range(n):
            print('*', end=' ')
    if i % 2 == 0:
        for x in range(n): 
            print(' ', end='*')
    print()
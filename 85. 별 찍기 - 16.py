import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    for x in range(n-i): 
        print(' ', end='')

    for x in range(i):
        print('*', end=' ')
    print()
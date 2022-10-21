n = int(input())
for i in range(n, 0, -1):
    for x in range(i):
        print('*', end='')
    print()
    for z in range(n-i+1):
        print(' ',end='')
n = int(input())
for i in range(n,0,-1):
    for z in range(n-i,0,-1):
        print(' ',end='')
    for x in range(i+(i-1)):
        print('*', end = '')
    print()
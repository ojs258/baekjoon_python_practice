n = int(input())
for i in range(n, 0,-1):
    for x in range(n-i+1,0,-1):
        print('*',end='')
    for y in range(i+(i-2)):
        print(' ', end = '')
    for z in range(n-i+1,0,-1):
        print('*',end='')
    print()

for i in range(2, n+1):
    for x in range(n-i+1,0,-1):
        print('*',end='')
    for y in range(i+(i-2)):
        print(' ', end = '')
    for z in range(n-i+1,0,-1):
        print('*',end='')
    print()
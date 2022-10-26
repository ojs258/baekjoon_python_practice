import sys
for i in range(3):
    cond = list(map(int,sys.stdin.readline().split())).count(0)
    if cond == 1:
        print('A')
    elif cond == 2:
        print('B')
    elif cond == 3:
        print('C')
    elif cond == 4:
        print('D')
    else:
        print('E')
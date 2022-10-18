quadrl = [0, 0, 0, 0, 0]

for i in range(int(input())):
    a, b = map(int,input().split())

    if a == 0 or b == 0:
        quadrl[4] = quadrl[4] + 1
    elif a > -1:
        if b > -1:
            quadrl[0] = quadrl[0] + 1
        elif b < 1:
            quadrl[3] = quadrl[3] + 1
    elif a < 1:
        if b > -1:
            quadrl[1] = quadrl[1] + 1
        elif b < 1:
            quadrl[2] = quadrl[2] + 1

for x in range(0, len(quadrl)-1):
    print('Q',x+1,': ',quadrl[x], sep='')
print('AXIS:',quadrl[4])
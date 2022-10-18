factor = []
while(True):
    a = int(input())
    if a == -1:
        break
    for i in range(1, a):
        if a % i == 0:
            factor.append(i)
    if sum(factor) == a:
        print(a,'=',factor[0], end =' + ')
        for i in range(1, len(factor)-1):
            print(factor[i], end=' + ')
        print(factor[len(factor)-1])
    else:
        print(a,'is NOT perfect.')
    factor = []

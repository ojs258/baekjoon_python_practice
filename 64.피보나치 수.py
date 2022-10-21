a = 0; b = 1; tmp = 0

n = int(input())
if n == 1:
    print(1)
else:
    for i in range(n-1):
        tmp = a + b
        a = b
        b = tmp    
    print(tmp)
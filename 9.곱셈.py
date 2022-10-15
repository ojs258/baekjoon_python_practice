a = int(input())
b = int(input())
c = b // 100
d = (b - c*100) // 10
e = (b - c*100 - d*10)
print(a*e, a*d, a*c, a*b, sep='\n', end='')
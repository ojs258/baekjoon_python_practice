import sys
a = 0; b = 1; tmp = 0

for i in range(int(sys.stdin.readline())-1):
    tmp = a + b
    a = b   
    b = tmp

print(b)

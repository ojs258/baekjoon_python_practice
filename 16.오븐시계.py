a, b = map(int,input().split())
c = int(input())
b = b+c
while(b >= 60):
    b = b - 60
    a = a + 1
    if(a == 24):
        a = 0
print(a,b)
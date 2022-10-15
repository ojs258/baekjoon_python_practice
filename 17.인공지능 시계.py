a, b, c = map(int,input().split())
d = int(input())
c = c + d
while(c >= 60):
    c = c - 60
    b = b + 1
    if(b == 60):
        a = a + 1
        b = 0
    if(a == 24):
        a = 0
print(a,b,c)
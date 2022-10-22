hap=[]
for i in range(int(input())):
    a, b = map(int,input().split())
    hap.append(b % a)
print(sum(hap))
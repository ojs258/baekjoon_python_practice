case=[]
alist=[]
cnt = int(input())
for i in range(0, cnt) :
    a, b = map(int,input().split())
    case.append(a+b)
    alist.append(a)
for i in range(0, cnt):
    print("Case #%d: %d + %d = %d"%(i+1, alist[i], case[i]-alist[i], case[i]))
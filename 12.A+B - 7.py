case=[]
cnt = int(input())
for i in range(0, cnt) :
    case.append(sum(map(int,input().split())))
for i in range(0, cnt):
    print("Case #%d: %d"%(i+1, case[i]))
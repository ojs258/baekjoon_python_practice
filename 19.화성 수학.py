cnt = int(input())
ans=[]
for i in range(cnt):
    a = input()
    marth = a.split()
    for i in range(len(marth)):
        if(marth[i] == '@'):
            marth[0] = float(marth[0]) * 3
        if(marth[i] == '%'):
            marth[0] = float(marth[0]) + 5
        if(marth[i] == '#'):
            marth[0] = float(marth[0]) - 7
    ans.append(marth[0])
for i in range(cnt):
    print("%.2f" % (ans[i]))
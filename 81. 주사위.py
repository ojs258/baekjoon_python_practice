import sys
n = int(sys.stdin.readline())
ans = []
for i in range(n):
    ans.append(sum(list(map(int,sys.stdin.readline().split()))))
for x in range(n):
    print('Case %d: %d'%(x+1, ans[x]))
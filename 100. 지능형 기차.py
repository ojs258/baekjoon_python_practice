import sys

tot_peo = 0
ans=[]
for i in range(4):
    in_peo, out_peo = map(int, sys.stdin.readline().split())
    tot_peo -= out_peo
    tot_peo += in_peo
    ans.append(tot_peo)

print(max(ans))
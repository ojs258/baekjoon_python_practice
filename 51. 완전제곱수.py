import math, sys
ans= []
for i in range(int(input()), int(input())+1):
    if i % math.sqrt(i) == 0:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans),min(ans))
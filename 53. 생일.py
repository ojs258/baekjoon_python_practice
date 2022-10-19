import datetime

tmp = {}
for i in range(int(input())):
    nm, dy, mn, yr = map(str,input().split())
    tmp[datetime.date(int(yr), int(mn), int(dy))] = nm
print(tmp.get(max(tmp)))
print(tmp.get(min(tmp)))
time = []
for i in range(2):
    time.append(list(map(int,input().split(":"))))
time[1] = time[1][0] * 3600 + time[1][1] * 60 + time[1][2]
time[0] = time[0][0] * 3600 + time[0][1] * 60 + time[0][2]

t_sec = time[1] - time[0]

if t_sec < 0:
    t_sec += 86400 # 하루를 초로 환산한 값

h = t_sec // 3600
m = (t_sec % 3600) // 60
s = t_sec % 60

print('%02d:%02d:%02d' %(h, m, s))
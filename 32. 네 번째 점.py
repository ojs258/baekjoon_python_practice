pos_x = []
pos_y = []
for i in range(3):
    x, y = map(int, input().split())
    pos_x.append(x)
    pos_y.append(y)

for i in set(pos_x):
    if pos_x.count(i) == 1:
        print(i, end = ' ')
for x in set(pos_y):
    if pos_y.count(x) == 1:
        print(x)
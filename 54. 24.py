import datetime
misson = []
for i in range(2):
    misson.append(datetime.time.fromisoformat(input()))

print(datetime.datetime(misson[1]))
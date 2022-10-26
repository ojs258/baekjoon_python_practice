import sys

today = int(sys.stdin.readline())
car = list(map(int,sys.stdin.readline().split()))
print(car.count(today))
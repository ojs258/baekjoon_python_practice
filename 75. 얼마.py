def multiple(a):
    return a[0] * a[1]

for i in range(int(input())):
    price = int(input())
    for i in range(int(input())):
        price = price + multiple(list(map(int,input().split())))
    print(price)
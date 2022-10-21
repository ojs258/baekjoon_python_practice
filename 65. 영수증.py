price = [int(input()) for i in range(10)]
print(price[0] - (sum(price) - price[0]))
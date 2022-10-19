A = B = 100

for i in range(int(input())):
    aDice, bDice = map(int,input().split())

    if aDice > bDice:
        B = B - aDice
    elif aDice < bDice:
        A = A - bDice
print(A, B, sep='\n')
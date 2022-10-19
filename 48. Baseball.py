Yscore = 0
Kscore = 0
for i in range(int(input())):
    for i in range(9):
        Y, K = map(int,input().split())

        Yscore = Yscore + Y
        Kscore = Kscore + K

    if Kscore > Yscore:
        print("Korea")
    elif Kscore < Yscore:
        print("Yonsei")
    else:
        print("Draw")
    Yscore = 0
    Kscore = 0
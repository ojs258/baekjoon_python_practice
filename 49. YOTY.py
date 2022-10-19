for i in range(int(input())):
    YOTY = {}
    for x in range(int(input())):
        a, b = map(str,input().split())
        YOTY[int(b)] = a
    print(YOTY.get(max(YOTY)))
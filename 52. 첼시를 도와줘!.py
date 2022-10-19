for i in range(int(input())):
    player = {}
    for i in range(int(input())):
        c, name = map(str,input().split())
        player[int(c)] = name
    print(player.get(max(player)))
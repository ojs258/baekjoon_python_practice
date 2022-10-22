for i in range(int(input())):
    score1 = []
    score2 = []
    for x in range(int(input())):
        a, b  = map(str,input().split())
        score1.append(int(a))
        score2.append(float(b)*float(a))
    print(sum(score1), sum(score2)/sum(score1))
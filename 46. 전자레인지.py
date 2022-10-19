A, B, C = map(int,[300, 60, 10])

T = int(input())

Abtn = T // A; T = T - A*Abtn
Bbtn = T // B; T = T - B*Bbtn
Cbtn = T // C
if T % C == 0:
    print(Abtn, Bbtn, Cbtn)
else:
    print(-1)
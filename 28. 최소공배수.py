import math
#def cust_lcm(big, sml):    
#    while(sml != 0):
#        r = big % sml
#        big = sml
#        sml = r
#    return big
# 최대공약수 공식 - 유쿨리드 호제법 -> 두 수 a와 b중 더 큰 수 a, 작은 수b
# a를 b로 나눈 나머지 r과 b의 최대공약수와 a와 b의 최대공약수는 같다. 

t = int(input())
ans = []
for x in range(t):
    a, b = map(int,input().split())
    ans.append(math.lcm(a, b))
    #if(a > b):
    #    ans.append(int((a * b) / cust_lcm(a,b)))
    #else:
    #    ans.append(int((a * b) / cust_lcm(b,a)))
# 최소공배수 공식 - 두 수의 최소공배수는 두 수의 곱을 최대공약수로 나눈 것과 같다.
     
for z in ans:
    print(z)
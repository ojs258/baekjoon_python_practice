cnt = 0
s = int(input())
while(cnt*(cnt+1)/2 <= s):
#n*(n+m)/2 등차수열 n -> m 까지의 합 공식 이 문제는 시작 숫자 m이 1로 고정
    cnt = cnt + 1
print(cnt-1)
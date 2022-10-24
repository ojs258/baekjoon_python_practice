import sys
# 문제들 중 테스트 케이스의 길이가 길어지거나 테스트 케이스의 개수가 많아지면
# input()메소드로 시간 초과 에러가 뜬다.
# 더 적은 비용을 사용해 입력을받는 sys모듈의 stdin.readline() 메소드를
# 이용해 해결해야한다.
n = int(sys.stdin.readline())
multap = 0
for i in range(n):
    multap = multap + int(sys.stdin.readline())
print(multap - (n - 1))
import sys
input()

grade = 0
score = 1
num = list(map(int,sys.stdin.readline().split()))

if num[0] == 1:
    grade = 1

for i in range(1, len(num)):
    if num[i] == 1:
        if num[i-1] == 1:
            score = score + 1
        grade = grade + score
    else:
        score = 1
print(grade)

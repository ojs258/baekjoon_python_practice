grade=[]
for x in range(5):
    score = int(input())
    if score > 40:
        grade.append(score)
    else:
      grade.append(40)  
print(int(sum(grade)/len(grade)))
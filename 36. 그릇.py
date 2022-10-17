dish = list(input().rstrip())
ans = 10
for i in range(1, len(dish)):
    if dish[i-1] == '(' and dish[i] == '(':
        ans  = ans + 5
    elif dish[i-1] == '(' and dish[i] == ')':
        ans  = ans + 10
    elif dish[i-1] == ')' and dish[i] == ')':
        ans  = ans + 5
    elif dish[i-1] == ')' and dish[i] == '(':
        ans  = ans + 10
print(ans)
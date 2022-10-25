#from math import factorial
import sys


def fac(n):
    if n < 1:
        return 1
    return n * fac(n-1)

print(fac(int(sys.stdin.readline())))

#print(factorial(int(sys.stdin.readline())))
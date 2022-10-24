import sys
for i in range(int(sys.stdin.readline())):
    c, v = map(int, sys.stdin.readline().split())
    print('You get %d piece(s) and your dad gets %d piece(s).' % (c//v, c%v))

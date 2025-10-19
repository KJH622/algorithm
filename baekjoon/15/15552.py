# 빠른 A+B

import sys

t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
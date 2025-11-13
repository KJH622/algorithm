# 소수 찾기

import math

n = int(input())
data = list(map(int, input().split()))
result = 0

for x in data:
    if x == 1:
        continue # 1은 소수 아님

    is_prime = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            break
    
    if is_prime:
        result += 1

print(result)
# 소수

# 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

import math

m = int(input())
n = int(input())

# 0 ~ n 까지 소수 여부 저장
# True : 소수
is_prime = [True] * (n + 1)
is_prime[0] = False # 0은 소수가 아님
is_prime[1] = False # 1은 소수가 아님

for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

primes = [i for i in range(m, n + 1) if is_prime[i]]

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
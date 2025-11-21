# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_3

# 소수를 검사하는 함수를 정의
# 소수인지 아닌지 판단
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return "소수가 아닙니다."
    return "소수입니다."

n = int(input())
print(is_prime_number(n))

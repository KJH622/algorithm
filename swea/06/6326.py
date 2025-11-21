# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_7

# 팩토리얼을 구하는 함수

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

n = int(input())
print(factorial(n))
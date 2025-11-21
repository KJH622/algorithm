# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복_13

# 10진수를 2진수로 변환하는 프로그램

n = int(input())
result = []

while n > 0:
    result.append(str(n % 2))
    n //= 2

result.reverse()
print(''.join(result))
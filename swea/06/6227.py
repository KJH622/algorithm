# [파이썬 프로그래밍 기초 (1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If_8

# 100 ~ 300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마로 구분해 출력하는 프로그램

lst = []
num = []

for i in range(100, 301):
    s = str(i)
    if all(int(c) % 2 == 0 for c in s):
        lst.append(s)

print(",".join(lst))
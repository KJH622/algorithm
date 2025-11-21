# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 - 리스트, 튜플_17

# 콤마로 구분해 여러 원의 반지름을 입력 받아 원의 둘레를 계산해 출력하는 프로그램을 작성하시오.

from math import pi

lst = input().split(', ')
lst_new = []

for i in lst:
    r = float(i)
    result = 2 * r * pi
    lst_new.append(round(result, 2))

print(', '.join(map(str, lst_new)))
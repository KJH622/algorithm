# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복_4

# 1부터 100사이의 숫자 중 홀수를 for문을 이용해 출력하시오.

lst = []

for i in range(1, 101):
    if i % 2 == 1:
        lst.append(str(i))

print(", ".join(lst))
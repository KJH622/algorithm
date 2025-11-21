# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복_6

# 10명의 학생들의 혈액형(A, B, AB, O)
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

lst = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

count = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}

for i in lst:
    count[i] += 1

print(count)
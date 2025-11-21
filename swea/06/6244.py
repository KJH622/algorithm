# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복_7

lst = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
score = 0

while True:
    if len(lst) > 0:
        i = lst.pop()
        if i >= 80:
            score += i
    else:
        break

print(score)
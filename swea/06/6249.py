# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복_10

# 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하시오.

n = input()
lst = [0] * 10

for i in n:
    for j in range(10):
            if int(i) == j:
                lst[j] += 1

print(*range(10)) # 언패킹
print(*lst) # 언패킹
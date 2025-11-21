# [파이썬 프로그래밍 기초 (1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If_7

# 1 ~ 200 사이의 정수 가운데 7의 배수이면서 5의 배수가 아닌 숫자들을 찾아 콤마로 구분한 문자열 

nums = []

for i in range(1, 201):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(str(i))

print(",".join(nums))
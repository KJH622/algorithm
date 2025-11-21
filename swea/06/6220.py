# [파이썬 프로그래밍 기초 (1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If_3

# 대소문자 구분하는 코드를 작성하시오.

test_case = int(input())
for i in range(1, test_case + 1):
    chr = input()
    if chr.isupper():
        print(f"#{i} {chr} 는 대문자 입니다.")
    else:
        print(f"#{i} {chr} 는 소문자 입니다.")
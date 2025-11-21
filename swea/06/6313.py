# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수_6

# ASCII 코드 값을 입력받아 문자를 확인하는 코드 작성하시오.
# ord() : 문자 -> ASCII 코드로 변환
# chr() : ASCII 코드 -> 문자로 변환

n = int(input())
ASC_n = chr(n)

print(f"ASCII {n} => {ASC_n}")
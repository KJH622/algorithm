# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_8

# 숫자에 대해 제곱을 구하는 함수를 정의
# 숫자를 콤마로 구분해 입력하면 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하시오.

def num_square(num1, num2):
    result_num1 = num1 ** 2
    result_num2 = num2 ** 2
    print(f"square({a}) => {result_num1}")
    print(f"square({b}) => {result_num2}")

a, b = map(int, input().split(', '))
num_square(a, b)
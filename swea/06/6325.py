# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_6

# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고 임의의 숫자의 포함 여부를 출력하는 프로그램 작성하시오.

lst = [2, 4, 6, 8, 10]

def find_num(x):
    if x in lst:
        return True
    else:
        return False

print(lst)
print(f"5 => {find_num(5)}")
print(f"10 => {find_num(10)}")
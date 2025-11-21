# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_4

# 피보나치 수열의 결과를 생성하는 프로그램을 작성하시오.

lst = []

def fibonacci(x):
    lst.append(1) # 0번째 인덱스
    lst.append(1) # 1번째 인덱스

    for i in range(2, x):
        lst.append(lst[i - 2] + lst[i - 1])
    
    print(lst)

n = int(input())
fibonacci(n)
# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_10

# 인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의
# 이 함수를 이용해 countdown(0), countdown(10)을 순서대로 실행한다.

def countdown(x):
    if x <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(x, 0, -1):
            print(i)

countdown(0)
countdown(10)
# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 - 리스트, 튜플_6

# 다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하시오.

n = int(input())
lst = []

for i in range(1, n + 1):
    if n % i == 0:
        lst.append(i)

print(lst)
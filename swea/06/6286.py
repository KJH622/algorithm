# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 - 리스트, 튜플_11

# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하시오.

lst = []
lst.append(1) # 0번 인덱스
lst.append(1) # 1번 인덱스

for i in range(2, 10):
    lst.append(lst[i-1] + lst[i - 2])

print(lst)
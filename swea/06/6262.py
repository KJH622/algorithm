# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 3. 자료구조 - 셋, 딕셔너리_10

# 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하시오

n = input()
lst = {}

for i in n:
    count = lst.get(i, 0)
    lst[i] = count + 1

for i, j in lst.items():
    print(f"{i},{j}")
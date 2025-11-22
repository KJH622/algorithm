# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 3. 자료구조 - 셋, 딕셔너리_8

# 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하시오

n = input()
a = 0
b = 0

for i in n:
    if 'a' <= i <= 'z':
        a += 1
    
    elif 'A' <= i  <= 'Z':
        b += 1

print(f"UPPER CASE {b}")
print(f"LOWER CASE {a}")
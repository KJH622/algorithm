# 코딩은 체육과목 입니다

n = int(input()) # 정수

print("long " * (n//4) + "int")

# 다른 풀이
'''
n = int(input())
a = n // 4
result = 0

for i in range(1, a + 1):
    result += i
print("long " * i, end='')
print("int")
'''
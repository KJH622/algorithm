# 홀수

result = 0 # 합
lst = []

for i in range(7):
    n = int(input())
    if n % 2 == 1: # 홀수일 때
        lst.append(n)
        result += n

if len(lst) == 0: # 홀수가 없으면
    print(-1)
else:
    print(result)
    print(min(lst))
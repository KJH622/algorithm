# 방학 숙제

l = int(input()) # 방학 일 수
a = int(input()) # 국어 방학 숙제
b = int(input()) # 수학 방학 숙제
c = int(input()) # 하루에 풀 수 있는 국어 최대 페이지
d = int(input()) # 하루에 풀 수 있는 수학 최대 페이지

sum = 0
result = 0

if a % c == 0:
    sum += (a // c)
elif a % c > 0:
    sum = sum + a // c + 1

if b % d == 0:
    result += b // d
elif b % d > 0:
    result = result + b // d + 1

if sum >= result:
    print(l - sum)
else:
    print(l - result)
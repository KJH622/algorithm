# 함께 문제 푸는 날

# d : 날 수
# a, b, c : 방문 주기

a, b, c = map(int, input().split())
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1

print(d)

# 3의 배수 (3 6 9 12 15 18 21 24 27 30 ... 60 63)
# 7의 배수 (7 14 21 28 35 42 49 56 63 70)
# 9의 배수 (9 18 27 36 45 54 63 72 81 90)

# n % 3 != 0: 3의 배수가 아닌 것은 True, 3의 배수면 false
# n % 7 != 0: 7의 배수가 아닌 것은 True, 7의 배수면 false
# n % 9 != 0: 9의 배수가 아닌 것은 True, 9의 배수면 false

# while문의 조건이 거짓일 때 while문은 종료된다.
# or은 하나라도 True이면 True가 된다.
# 즉, day % a == 0 and day % b == 0 and day % c == 0인 순간 while문은 종료된다.
# 수 나열하기_3

# a : 시작 값
# m : 곱할 값
# d : 더할 값
# n : 몇 번째인지를 나타내는 정수

a, m, d, n = map(int, input().split())
sum = a
for i in range(2, n+1):
    sum = sum * m + d

print(sum)
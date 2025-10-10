# 수 나열하기_2

# a : 시작 값
# r : 등비
# n : 몇 번째인지를 나타내는 정수

a, r, n = map(int, input().split())
sum = a
for i in range(2, n+1):
    sum *= r

print(sum)
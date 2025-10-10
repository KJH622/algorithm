# 수 나열하기_1

# 수열 : 어떤 규칙에 따라 수를 순서대로 나열한 것

# a : 시작 값
# d : 등차
# n : 몇 번째인지 나타내는 정수

a, d, n = map(int, input().split())
sum = a
for i in range(2, n+1):
    sum += d

print(sum)
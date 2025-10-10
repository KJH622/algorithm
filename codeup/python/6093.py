# 이상한 출석 번호 부르기_2

# n : 번호를 부른 횟수
# k : n개의 랜덤 번호

n = int(input())
k = input().split()

for i in range(0, n):
    k[i] = int(k[i])

d = []
for i in range(23):
    d.append(0)

for i in range(n-1, -1, -1): # n-1, n-2, ..., 3, 2, 1, 0
    print(k[i], end=' ')
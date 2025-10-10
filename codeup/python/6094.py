# 이상한 출석 번호 부르기_3

# n : 번호를 부른 횟수
# k : n개의 랜덤 번호

n = int(input())
k = input().split()

for i in range(0, n):
    k[i] = int(k[i])

min = k[0]
for i in range(0, n):
    if k[i] < min:
        min = k[i]

print(min)
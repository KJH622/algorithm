# 점수계산

# 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산
# 연속으로 문제의 답이 맞는 경우는 두 번째 문제는 2점, K번째 문제는 K점으로 계산
# 틀린 문제는 0점으로 계산

n = int(input()) # 문제의 개수
sum = 0 # 앞의 문제가 맞았는지 틀렸는지 여부
total = 0 # 전체 합계

k = list(map(int, input().split()))

for i in range(n):
    if k[i] == 1:
        sum += 1
        total += sum
    else:
        sum = 0

print(total)
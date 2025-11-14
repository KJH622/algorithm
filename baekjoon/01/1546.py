# 평균

n = int(input()) # 시험 본 과목의 개수
data = list(map(int, input().split()))
result = 0

for i in data:
    score =  i/max(data) * 100
    result += score

print(result/n)
# 대지

# n: 옥구슬의 위치
# 임씨에게 돌아갈 대지의 넓이를 계산하는 프로그램

n = int(input()) # 점의 개수
x_line = []
y_line = []

for i in range(n):
    x, y = map(int, input().split())
    x_line.append(x)
    y_line.append(y)

print((max(x_line) - min(x_line)) * ((max(y_line) - min(y_line))))
# X보다 작은 수

n, x = map(int, input().split())
data = list(map(int, input().split()))

for i in range(len(data)):
    if data[i] < x:
        print(data[i], end=' ')
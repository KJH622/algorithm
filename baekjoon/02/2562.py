# 최댓값

data = []
for _ in range(9):
    n = int(input())
    data.append(n)

print(max(data))
print(data.index(max(data))+1)
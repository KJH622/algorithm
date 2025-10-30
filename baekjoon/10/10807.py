# 개수 세기

n = int(input())
data = list(map(int, input().split()))
v = int(input())

count = 0
for i in range(len(data)):
    if v == data[i]:
        count += 1

print(count)

'''
n = int(input())
data = list(map(int, input().split()))
v = int(input())

for i in range(len(data)):
    if v == data[i]:
        data.count(v)

print(data.count(v))
'''
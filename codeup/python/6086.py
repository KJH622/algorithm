# 거기까지! 이제 그만~

n = int(input())
sum = 0
a = 1

while True:
    sum += a
    a += 1
    if sum >= n:
        break

print(sum)
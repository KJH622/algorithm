# 공 바꾸기

n, m = map(int, input().split())
basket = list(range(1, n+1))

for i in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for i in range(n):
    print(basket[i], end=' ')
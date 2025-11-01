# 파티가 끝나고 난 뒤

l, p = map(int, input().split())
news = list(map(int, input().split()))

for i in range(len(news)):
    print(news[i] - l*p, end=' ')
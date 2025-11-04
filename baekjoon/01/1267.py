# 핸드폰 요금

n = int(input()) # 동호가 저번 달에 이용한 통화의 개수
lst = list(map(int, input().split()))

y = m = 0

# 60이라고 해도 초수로 인해 60이 넘은 상태이기 때문에 +1을 해야 함.
for i in lst:
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15

if y > m:
    print("M", m)
elif y < m:
    print("Y", y)
else:
    print("Y M", m)
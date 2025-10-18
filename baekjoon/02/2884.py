# 알람 시계

H, M = map(int, input().split()) # H시 M분
if 45 <= M <= 59:
    H = H
    M -= 45
elif 0 <= M < 45:
    if 0 < H <= 23:
        H -= 1
        M = 60 - (45 - M)
    elif H == 0:
        H = 23
        M = 60 - (45 - M)
print(H, M)

# 다른 방법
'''
h, m = map(int, input().split())

j = m - 45
i = 0
if j < 0:
    i = 60 + j
    if h != 0:
        h -= 1
    else:
        h = h + 23
    print(h, i)
else:
    print(h, j)
'''
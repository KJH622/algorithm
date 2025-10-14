# 설탕과자 뽑기

# 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,
# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이다.
# 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1), 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

h, w = map(int, input().split()) # 가로, 세로

m = []
for i in range(h): # 0~h-1
    m.append([])
    for j in range(w): # 0~w-1
        m[i].append(0)

n = int(input()) # 막대의 개수
for i in range(n):
    l, d, x, y = map(int, input().split()) # 막대의 길이, 방향, 막대의 가장 왼쪽, 가장 위쪽
    if d == 0: # 가로
        for j in range(l):
            m[x-1][y+j-1] = 1
    else:
        for j in range(l):
            m[x+j-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(m[i][j], end=' ')
    print()
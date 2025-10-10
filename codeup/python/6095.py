# 바둑판에 흰 돌 놓기

# 바둑판(19*19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성하자.

# n : 바둑판에 올려 놓을 흰 돌의 개수

# 바둑판의 모양(리스트로서 표현)

d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
# 바둑알 십자 뒤집기

# 십자 뒤집기는 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후,
# 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
# 어떤 위치를 골라 십자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.
# 바둑판(19*19)에 흰 돌(1) 또는 검정(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 
# 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

# n : 십자 뒤집기 횟수

d = []
for i in range(19): # 0~18
    d.append([])
    for j in range(19): # 0~18
        d[i].append(0)

for i in range(19): # 0~18
    d[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if d[j][y-1] == 0:
            d[j][y-1] = 1
        else:
            d[j][y-1] = 0
        
        if d[x-1][j] == 0:
            d[x-1][j] = 1
        else:
            d[x-1][j] = 0
    
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()    
# 3 6 9 게임의 왕이 되자

a = int(input())

for i in range(1, a+1):
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=' ')
    else:
        print(i, end=' ')

# 3, 6, 9가 포함된 경우 X로 표시
# 3, 6, 9, 13, 16, 19, ...
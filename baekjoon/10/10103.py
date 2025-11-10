# 주사위 게임

# 게임을 시작하는 시점에서 두 사람의 점수는 모두 100점이다.
# 6면의 주사위를 사용하며, 라운드로 진행된다.
# 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃게 된다.
# 두 사람의 숫자가 같은 경우 아무도 점수를 잃지 않는다.

n = int(input()) # 라운드의 수

chang_score = 100
sang_score = 100

for i in range(n):
    chang, sang = map(int, input().split())

    if chang < sang:
        chang_score -= sang
    elif chang > sang:
        sang_score -= chang
    else:
        pass # 같은 경우 아무도 점수를 잃지 않는다.

print(chang_score)
print(sang_score)
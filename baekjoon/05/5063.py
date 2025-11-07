# TGN

# 광고 효과가 주어졌을 때, 광고를 해야할지 말아야할지 결정하는 프로그램
# r: 광고를 하지 않았을 때 수익
# e: 광고를 했을 때의 수익
# c: 광고 비용
# 광고를 해야하면 "advertise"
# 광고를 하지 않아야 하면 "do not advertise"
# 광고를 해도 수익이 차이가 없다면 "does not matter"

n = int(input()) # 테스트 케이스의 개수

for i in range(n):
    r, e, c = map(int, input().split())
    if r < e - c:
        print("advertise")
    elif r > e - c:
        print("do not advertise")
    else:
        print("does not matter")
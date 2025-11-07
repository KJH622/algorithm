# 직각삼각형

# 주어진 세 변의 길이로 삼각형이 직각인지 아닌지 구분하시오

lines = []

while True:
    a, b, c = list(map(int, input().split()))
    lines = sorted([a, b, c])

    if a == 0 and b == 0 and c == 0:
        break

    if lines[2] ** 2 == lines[0] ** 2 + lines[1] ** 2:
        print("right")
    else:
        print("wrong")
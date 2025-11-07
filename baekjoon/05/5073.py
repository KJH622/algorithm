# 삼각형과 세 변

# Equilateral : 세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# Invalid : 삼각형의 조건을 만족하지 못하는 경우
# 삼각형 조건 : 가장 긴 변의 길이 > 나머지 두 변의 길이의 합

while True:
    a, b, c = list(map(int, input().split()))
    if a == b == c == 0:
        break

    line = sorted([a, b, c])

    if line[2] >= line[0] + line[1]:
        print("Invalid")
    elif line[0] == line[1] == line[2]:
        print("Equilateral")
    elif line[0] == line[1] or line[1] == line[2] or line[2] == line[0]:
        print("Isosceles")
    elif line[0] != line[1] != line[2]:
        print("Scalene")
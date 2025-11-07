# 세 막대

# 각 막대의 길이는 양의 정수이다.
# 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
# 삼각형의 둘레를 최대로 해야 한다.
# 가장 큰 둘레를 구하시오

# 삼각형의 조건: 가장 긴 변 < 나머지 두 변의 합

a, b, c = list(map(int, input().split()))

lines = sorted([a, b, c]) # 길이가 짧음에서 길이가 긴 순으로

if lines[2] < lines[0] + lines[1]:
    print(lines[0] + lines[1] + lines[2])
else:
    need = lines[2] - (lines[0] + lines[1] - 1)
    lines[2] = lines[2] - need
    print(lines[0] + lines[1] + lines[2])
# 배수와 약수

# 1. 첫 번째 숫자가 두 번째 숫자의 약수이다. => factor
# 2. 첫 번째 숫자가 두 번째 숫자의 배수이다. => multiple
# 3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다. => neither

while True:
    one, two = map(int, input().split())
    if one == 0 and two == 0:
        break

    if two % one == 0:
        print("factor")
    elif one % two == 0:
        print("multiple")
    else:
        print("neither")
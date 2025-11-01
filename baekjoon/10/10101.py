# 삼각형 외우기

lst = []
for _ in range(3):
    lst.append(int(input()))

if lst[0] == lst[1] == lst[2] == 60:
    print("Equilateral")
elif lst[0] + lst[1] + lst[2] == 180:
    if lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]:
        print("Isosceles")
    else:
        print("Scalene")
elif lst[0] + lst[1] + lst[2] != 180:
    print("Error")
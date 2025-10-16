# 곱셈

a = int(input())
b = input()
sum = 0

for i in range(2, -1, -1):
    c = a*int(b[i])
    print(c)

print(a*int(b))
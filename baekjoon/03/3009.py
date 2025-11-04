# 네 번째 점

a_num = []
b_num = []

for _ in range(3):
    a, b = map(int, input().split())
    a_num.append(a)
    b_num.append(b)

# 사각형을 만들기 위해 x와 y에 같은 수가 2개씩 존재해야 함.
for i in range(3):
    if a_num.count(a_num[i]) == 1:
        a_1 = a_num[i]
    if b_num.count(b_num[i]) == 1:
        b_1 = b_num[i]

print(a_1, b_1)
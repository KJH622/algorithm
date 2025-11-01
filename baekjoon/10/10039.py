# 평균 점수

lst = []
for i in range(5):
    lst.append(int(input()))

for i in range(5):
    if lst[i] < 40:
        lst[i] = 40

print(sum(lst)//5)
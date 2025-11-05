# 지능형 기차 2

sum = 0
lst = []

for i in range(1, 11):
    off, on = map(int, input().split())
    sum -= off # sum에서 내린 사람 수를 빼기
    sum += on # sum에서 탄 사람 수를 더하기
    lst.append(sum)

print(max(lst))
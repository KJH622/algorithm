# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c) # 문자열로 변환
count = [0] * 10 # 0 ~ 9까지 개수 저장

for x in mul:
    count[int(x)] += 1

for y in count:
    print(y)
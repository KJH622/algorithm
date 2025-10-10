# 이상한 출석 번호 부르기_1

# n : 출석 번호를 부른 횟수

n = int(input())
a = input().split()

for i in range(0, n): # 0 ~ n-1
    a[i] = int(a[i]) # a에 순서대로 저장되어 있는 각 값을 정수로 변환해 다시 저장

l = [] # 빈 리스트 [] 변수 만듦
for i in range(24): # [0, 0, 0, ..., 0, 0] 과 같이 24개의 정수 값 0을 추가
    l.append(0) # 각 값은 l[0], l[1], l[2], ..., l[23] 으로 값을 읽고 저장 가능

for i in range(n): # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
    l[a[i]] += 1

for i in range(1, 24): # 카운트한 값을 공백을 두고 출력
    print(l[i], end= ' ')
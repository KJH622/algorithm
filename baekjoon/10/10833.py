# 사과

n = int(input()) # 학교의 수
apple_rest = 0

for i in range(n):
    student, apple = map(int, input().split()) # 학생 수와 사과 개수
    apple_rest += apple % student

print(apple_rest)
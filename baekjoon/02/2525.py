# 오븐 시계

A, B = map(int, input().split()) # A(시), B(분)
C = int(input()) # 요리하는 데 필요한 시간

A += (B+C) // 60
B = (B+C) % 60

if A > 23:
    A -= 24

print(A, B)
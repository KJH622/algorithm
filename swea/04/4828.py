# [파이썬 S/W 문제해결 기본] 1일차 - min max

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력

T = int(input()) # 테스트 케이스

for i in range(T):
    n = int(input()) # 양수의 개수
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    print(f"#{i+1} {max_a - min_a}")
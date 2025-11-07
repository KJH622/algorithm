# 이진수

# 양의 정수 n이 주어진다.
# 이 수를 이진수로 바꾸었을 때, 1

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T): # 테스트 케이스
    n = int(input())
    pos = 0 # 비트의 위치
    result = []

    while n > 0:
        if n & 1:          # 현재 비트가 1이라면
            result.append(str(pos))
        n >>= 1             # 다음 비트로 이동
        pos += 1

    print(' '.join(result))
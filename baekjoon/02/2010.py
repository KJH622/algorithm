# 플러그

# 콘센트는 1개, N개의 멀티탭, 각 멀티탭은 몇 개의 콘센트로 구성
# 과연 최대 몇 대의 컴퓨터를 전원에 연결 가능?

import sys

n = int(sys.stdin.readline()) # 멀티탭의 개수
total = 0
for _ in range(n):
    total += int(sys.stdin.readline())

print(total - (n - 1))

# input() 으로 할 경우 시간 초과가 뜨기 때문에 sys.stdin.readline() 사용
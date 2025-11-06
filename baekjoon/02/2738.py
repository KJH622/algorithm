# 행렬 덧셈

# N*M 크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램

n, m = map(int, input().split())
matrix = []
matrix_1 = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for _ in range(n):
    row = list(map(int, input().split()))
    matrix_1.append(row)

# 두 행렬을 더해서 출력
for i in range(n):
    for j in range(m):
        print(matrix[i][j] + matrix_1[i][j], end=' ')
    print()

'''
리스트 컴프리헨션 사용

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
'''
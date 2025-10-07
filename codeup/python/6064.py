# 정수 3개 입력받아 가장 작은 값 출력하기

a, b, c = map(int, input().split())
print((a if a < b else b) if ((a if a < b else b) < c) else c)

'''
(a if a > b else b) if ((a if a > b else b) > c) else c
와 같은 계산식을 통해 a, b, c의 값 중 가장 큰 값을 계산할 수 있다.
'''
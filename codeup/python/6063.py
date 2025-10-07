# 정수 2개 입력받아 큰 값 출력하기

a, b = map(int, input().split())
print(a if a > b else b)

'''
x if C else y
C : True 또는 False를 평가할 조건식 또는 값
x : C의 평가 결과가 True일 때 사용할 값
y : C의 평가 결과가 True가 아닐 때 사용할 값
'''


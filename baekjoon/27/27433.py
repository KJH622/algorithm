# 팩토리얼 2

n = int(input())

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(n))

'''
n = int(input())
result = 1

for i in range(1, n+1):
    result *= i

print(result)
'''
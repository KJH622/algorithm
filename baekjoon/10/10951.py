# A + B - 4

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

'''
try:
    실행할 코드
except:
    예외가 발생할 때 실행할 코드
'''
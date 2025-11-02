# 팰린드롬인지 확인하기

data = input()

if data == data[::-1]:
    print("1")
else:
    print("0")
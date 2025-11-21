# [파이썬 프로그래밍 기초 (1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If_4

# 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임
# ["가위", "바위", "보"] 리스트를 활용한다.

m1 = input()
m2 = input()
game = ["가위", "바위", "보"]

if m1 == m2:
    print("Result : Draw")
elif (m1 == game[0] and m2 == game[2]) or (m1 == game[1] and m2 == game[0]) or (m1 == game[2] and m2 == game[1]):
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")
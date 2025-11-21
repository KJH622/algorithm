# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_2

# 사용자 2명으로부터 가위, 바위, 보를 입력 받아 승패를 결정하시오.

lst = []

def game(a, b):
    if a == b:
        print("비겼습니다.")
    elif lst[0] == "바위" and lst[1] == "가위" or lst[0] == "가위" and lst[1] == "바위":
        print("바위가 이겼습니다!")
    elif lst[0] == "가위" and lst[1] == "보" or lst[0] == "보" and lst[1] == "가위":
        print("가위가 이겼습니다!")
    else:
        print("보가 이겼습니다!")
    return

man1 = input()
man2 = input()
man1_result = input()
lst.append(man1_result)
man2_result = input()
lst.append(man2_result)
game(man1_result, man2_result)
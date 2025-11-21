# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초_5

# 리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의
# 이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하시오

def del_lst():
    for i in lst:
        if i not in lst_new:
            lst_new.append(i)
    print(lst)
    print(lst_new)
    return

lst = [1, 2, 3, 4, 3, 2, 1]
lst_new = []
del_lst()
# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 - 리스트, 튜플_2

# 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하시오.

a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
b = 'aeiou'

a_new = [char for char in a if char not in b]

print(''.join(a_new))
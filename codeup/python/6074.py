# 문자 1개 입력받아 알파벳 출력하기

c = ord(input())
i = ord('a')

while i <= c:
    print(chr(i), end=' ')
    i += 1
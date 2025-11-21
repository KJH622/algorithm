# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If_5

# 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경
# 알파벳이 아닐 경우엔 그냥 출력

s = input()

if not s.isalpha():
    print(f"{s}(ASCII: {ord(s)}) => {s}(ASCII: {ord(s)})")
elif s.isupper():
    s_l = s.lower()
    print(f"{s}(ASCII: {ord(s)}) => {s_l}(ASCII: {ord(s_l)})")
else:
    s_u = s.upper()
    print(f"{s}(ASCII: {ord(s)}) => {s_u}(ASCII: {ord(s_u)})")
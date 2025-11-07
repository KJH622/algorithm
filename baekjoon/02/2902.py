# KMP는 왜 KMP일까?

# 알고리즘에는 발견한 사람의 성을 따서 이름을 붙이는 경우가 많다.
# 긴 형태: 성을 모두 쓰고 하이픈(-)으로 이어 붙인 것
# 짧은 형태: 만든 사람의 성의 첫 글자만 따서 부르는 것

name = input()
result = '' # 문자열 초기화

for i in name:
    if i.isupper(): # 대문자이면 True
        result += i

print(result)
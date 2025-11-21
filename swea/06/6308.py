# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수_1

# 이름과 나이를 입력 받아 올해를 기준으로 100세가 되는 해를 표시하는 코드
# 기준이 2019년이다.
# 현재는 2025년이다.

import datetime

name = input()
age = int(input())
future_age = datetime.datetime.now().year - 6 + (100 - age)

print(f"{name}(은)는 {future_age}년에 100세가 될 것입니다.")
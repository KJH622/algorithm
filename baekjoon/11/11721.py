# 열 개씩 끊어 출력하기

n = input()

for i in range(0, len(n), 10):
    print(n[i:i+10]) # 슬라이싱
# 세탁소 사장 동혁

t = int(input()) # 테스트 케이스 개수

coins = [25, 10, 5, 1] # 파이선에서 //와 %는 정수 형태로만 계산 가능

for _ in range(t):
    num = int(input()) # 거스름돈
    result = []

    for coin in coins:
        count = num // coin # 해당 동전 개수
        num %= coin # 남은 금액 정산
        result.append(count)

    print(*result)

# print(*result) 는 파이썬에서 리스트의 요소들을 공백으로 구분해서 출력할 때 사용
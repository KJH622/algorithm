# OX 퀴즈

t = int(input()) # 테스트 케이스

for _ in range(t):
    data = input()
    count = 0
    result = 0

    for x in data:
        if x == 'O':
            count += 1
            result += count
        else:
            count = 0
    
    print(result)
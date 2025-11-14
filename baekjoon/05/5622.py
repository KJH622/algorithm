# 다이얼

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input().strip()
time = 0

for s in a:
    for i, j in enumerate(dial): # i는 요소 순서, j는 값
        if s in j:
            time += i + 3
            break

print(time)
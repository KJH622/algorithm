# 모음의 개수

data = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    count = 0
    a = input()
    if a == '#':
        break
    for i in a:
        if i in data:
            count += 1
    print(count)
# 모음의 개수

lst = ['a', 'e', 'i', 'o', 'u']
sum = 0

s = input()
for i in range(len(s)):
    if s[i] in lst:
        sum += 1

print(sum)
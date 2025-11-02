# 알파벳 개수

s = input()
lst = [0] * 26 # a ~ z이기 때문에 [0] * 26으로 초기화

for i in s:
    lst[ord(i)-97] += 1

print(' '.join(map(str, lst)))
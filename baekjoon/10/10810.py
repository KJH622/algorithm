# 공 넣기

n, m = map(int, input().split())
lst = [0] * n

for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        lst[i] = c

print(" ".join(map(str, lst)))
# " ".join(map(str, lst)) 를 사용하면 빈 칸을 구분자로 해서 list 항목을 출력할 수 있다.
# 공

m = int(input()) # 컵의 위치를 바꾼 횟수
lst = [1, 2, 3]

for i in range(m):
    x, y = map(int, input().split()) # 컵의 번호
    
    # x, y는 컵의 번호이므로 인덱스로 변환하여 swap
    xi = lst.index(x)
    yi = lst.index(y)
    lst[xi], lst[yi] = lst[yi], lst[xi]

print(lst[0])
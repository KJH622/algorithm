# 최댓값

max_value = -1 # 0이 주어질 수 있기 때문에 이보다 작게 초기화
max_row = 0 # 최댓값의 행 번호
max_col = 0 # 최댓값의 열 번호

for r in range(9): # 1행에 1~9열까지 존재
    num = list(map(int, input().split()))
    for c in range(9): # 1~9열까지의 행이 1~9행까지 존재
        if num[c] > max_value: # num[c]의 값이 max_value보다 크면 최댓값 후보
            max_value = num[c]
            max_row = r + 1
            max_col = c + 1

print(max_value)
print(max_row, max_col)
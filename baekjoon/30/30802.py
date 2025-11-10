# 웰컴 키트

# 티셔츠는 S, M, L, XL, XXL, XXXL 6가지 사이즈
# 티셔츠는 같은 사이즈의 T장 묶음으로만 주문 가능
# 펜은 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문 가능
# 티셔츠는 남아도 되지만 부족해서는 안되고 신청한 사이즈대로 나누어주어야 한다.
# 펜은 남거나 부족해서는 안되고 정확히 참가자 수만큼 준비되어야 한다.

# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는가.
# 펜은 P자루씩 최대 몇 묶음 주문할 수 있고 펜을 한 자루씩 몇 개 주문해야 하는가.


n = int(input()) # 참가자 수

N_P = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠: 각 사이즈별로 올림 나눗셈 묶음 수 환산
shirt = sum((x + T - 1) // T for x in N_P)

# 펜: P자루 묶음 최대 개수와 남는 낱개
pen_bundles = n // P
pen_singles = n % P

print(shirt)
print(pen_bundles, pen_singles)

'''
N = int(input())
T_N_input = list(map(int, input().split()))
T_P_input = list(map(int, input().split()))

sum = 0
# 티셔츠
for i in T_N_input:
    if(i % T_P_input[0] == 0):
        sum = sum + (i//T_P_input[0])
    else:
        if(i < T_P_input[0]):
            sum = sum + 1
        else:
            sum = sum + (i//T_P_input[0]) + 1

# 펜
P_set = N//T_P_input[1]
P_each = N%T_P_input[1]

print(sum)
print(P_set, P_each)
'''
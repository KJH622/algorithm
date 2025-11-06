# 윷놀이

# 배(0), 등(1)
# 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개)

# 1의 개수 세기

mapping = {0 : 'D', 1 : 'C', 2 : 'B', 3 : 'A', 4 : 'E'}

for i in range(3): # 3번 반복
    lst = list(map(int, input().split()))
    lst_sum = sum(lst) # 1의 개수
    print(mapping[lst_sum])
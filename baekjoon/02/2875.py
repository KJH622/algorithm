# 대회 or 인턴

# 1팀: 2명의 여학생과 1명의 남학생
# n: 여학생 수
# m: 남학생 수
# k: 인턴쉽에 참여해야 하는 인원

# 풀이 1. 팀을 먼저 만들고, 남는 인원으로 k를 감당 (수식형)

n, m, k = map(int, input().split())

teams = min(n // 2, m)            # 만들 수 있는 최대 팀
leftover = n + m - teams * 3      # 팀 만들고 남는 사람 수

if leftover >= k:
    print(teams)
else:
    need = k - leftover           # 더 부족한 인턴 수
    reduce = (need + 2) // 3      # 팀을 해체해야 하는 수(한 팀 해체 시 3명 확보)
    print(max(0, teams - reduce))

'''
# 풀이 2. 인턴을 한 명씩 빼면서 손해 최소화 (그리디)

n, m, k = map(int, input().split())

while k > 0:
    # 현재 구성에서 여학생이 상대적으로 더 남아 있다면 여학생에서, 아니면 남학생에서 뺀다
    if n // 2 > m:
        n -= 1
    else:
        m -= 1
    k -= 1

print(min(n // 2, m))
'''
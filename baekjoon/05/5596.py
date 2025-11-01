# 시험 점수

min_score = list(map(int, input().split()))
man_score = list(map(int, input().split()))

sum_min = sum(min_score)
sum_man = sum(man_score)

if sum_min < sum_man:
    print(sum_man)
else:
    print(sum_min)
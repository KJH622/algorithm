# 나는 요리사다

# 각 참가자가 얻은 평가 점수는 다른 사람이 평가해 준 점수의 합이다.
# 우승자는 가장 많은 점수를 얻은 사람이다.

max_score = 0
winner = 0

for i in range(5):
    scores = list(map(int, input().split()))
    total = sum(scores)
    if total > max_score:
        max_score = total
        winner = i + 1

print(winner, max_score)
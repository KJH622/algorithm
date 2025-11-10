# 0 = not cute / 1 = cute

n = int(input()) # 설문조사를 한 사람의 수

opinion_zero = 0
opinion_one = 0

for i in range(n):
    opinion = int(input()) # 의견

    if opinion == 1:
        opinion_one += 1
    elif opinion == 0:
        opinion_zero += 1

if opinion_one > opinion_zero:
    print("Junhee is cute!")
elif opinion_one < opinion_zero:
    print("Junhee is not cute!")
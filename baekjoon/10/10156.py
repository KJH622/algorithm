# 과자

k, n, m = map(int, input().split()) 
# k: 과자 한 개 가격, n: 사려고 하는 과자 개수, m: 동수가 가진 돈

if k*n > m:
    print(k*n-m)
else:
    print("0")
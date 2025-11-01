# 영수증

sum_price = int(input())
sum = 0

for i in range(9):
    book_price = int(input())
    sum += book_price

print(sum_price - sum)
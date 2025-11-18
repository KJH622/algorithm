m = int(input())
n = int(input())

def is_prime(n):
    array = [True] * (n + 1)
    array[0] = False
    array[1] = False
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if i == j:
                continue
            else:
                if i % j == 0:
                    array[i] = False
    return array

lst = is_prime(n)

result = [i for i in range(m, n + 1) if lst[i]]

if len(result) >= 1:
    print(sum(result))
    print(min(result))
else:
    print(-1)
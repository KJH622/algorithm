# 나머지

# 집합 자료형
# 중복을 허용하지 않음

result = []

for _ in range(10):
    n = int(input())
    rest = n % 42
    result.append(rest)

result_set = set(result)
print(len(result_set))
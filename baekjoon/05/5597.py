# 과제 안 내신 분

students = [i for i in range(1, 31)] # 리스트 컴프리헨션

for _ in range(28):
    num = int(input())
    students.remove(num)

students.sort()
print(students[0])
print(students[1])

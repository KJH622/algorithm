# 럭비 클럽

while True:
    a, b, c = input().split()
    b = int(b)
    c = int(c)
    if a == "#" and b == 0 and c == 0:
        break
    if b > 17 or c >= 80:
        print(f"{a} Senior")
    else:
        print(f"{a} Junior")
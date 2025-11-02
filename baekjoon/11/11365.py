# !밀비 급일

while True:
    data = input()
    if data == "END":
        break
    else:
        data = data[::-1] # 파이썬에서 리스트나 문자열을 뒤집는 가장 간단한 방법
        print(data)
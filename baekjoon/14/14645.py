# 와이버스 부릉부릉

# n은 출발역과 종착역을 제외한 정거장의 수
# k는 출발역에서 탑승하는 사람의 수
# a는 i번째 정거장에서 탑승하는 인원
# b는 i번째 정거장에서 하차하는 인원

n, k = map(int, input().split())

for i in range(n):
    a, b = map(int, input().split())

print("비와이")
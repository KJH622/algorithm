# [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

# 최소 몇 번의 충전을 해야 종점에 도착할 수 있는가?

T = int(input()) # 노선 수

for i in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장
    # M : 충전기가 설치된 정류장 개수
    K, N, M = map(int, input().split())

    # 충전기가 설치된 정류장 리스트 입력
    station = list(map(int, input().split()))
    # 충전 횟수 count와 현재 위치 current 변수 초기화
    count = current = 0

    # 종점에 도착할 때까지 반복
    while current + K < N:
        # K 범위 안에서 현 위치를 조정하면서 이동
        for step in range(K, 0, -1):
            # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장
            if (current + step) in station:
                # 현재 위치를 변경
                current += step
                # 충전 횟수 + 1
                count += 1
                # for문을 종료
                break
        # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 0을 출력
        else:
            count = 0
            break

    # 결과 출력
    print(f"#{i} {count}")
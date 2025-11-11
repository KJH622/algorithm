# ACM 호텔

t = int(input()) # 테스트 케이스

# h: 호텔의 층 수, w: 각 층의 방 수, n: 몇 번째 손님
for i in range(t):
    h, w, n = map(int, input().split()) 
    
    yy = n % h # 층은 YYXX이다.
    if yy == 0:
        yy = h
        xx = n // h
    else:
        xx = n // h + 1
    
    # 호수가 1자리일 때 0을 붙이고, 2자리면 그대로 출력
    print(f"{yy}{xx:02d}")
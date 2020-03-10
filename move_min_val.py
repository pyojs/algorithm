T = int(input())
for tc in range(1 ,T+1):
    W, H, N = map(int,input().split())
    xy = []
    for n in range(N):
        xy.append(list(map(int,input().split())))
    result = 0
    while len(xy):
        dx = 0
        dy = 0
        # 시작인 경우 처음 값을 start로 함
        # 두번째 시작점은 이전 end 값을 사용
        if result == 0:
            start = xy.pop(0)
        else:
            start = end
        end = xy.pop(0)
        # x, y 움직일 거리 측정
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        # 대각선으로 움직이지 못하는 경우
        if dx*dy < 0:
            result += (abs(dx)+abs(dy))
        # 대각선으로 움직일 수 있는 경우
        else:
            dx = abs(dx)
            dy = abs(dy)
            temp = min(dx, dy)
            result += (dx + dy - temp)
    print('#{} {}'.format(tc, result))
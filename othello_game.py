T = int(input())
# 상, 하, 좌, 우 + 대각선 4개
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    # 정가운데 지점(초기 상태 생성)
    t_N = int(N/2)
    arr[t_N-1][t_N] ,arr[t_N][t_N-1], arr[t_N-1][t_N-1] ,arr[t_N][t_N] = 1, 1, 2, 2
    for n in range(M):
        x, y, c = map(int, input().split())
        arr[y-1][x-1] = c
        # 8방향 탐색
        for p in range(8):
            cnt = 0
            cx = x-1
            cy = y-1
            # 숫자가 있는 경우 진행
            while cx+dx[p] >= 0 and cx+dx[p] < N and cy+dy[p] >= 0 and cy+dy[p] < N and arr[cy+dy[p]][cx+dx[p]]:
                # 진행하면서 같은 숫자를 만난 경우 중간에 다른 색의 돌을 바꾸고 종료
                if abs(arr[cy+dy[p]][cx+ dx[p]] - arr[y-1][x-1]) == 0:
                    for k in range(1, cnt+1):
                        cx = x-1
                        cy = y-1
                        arr[cy+dy[p]*k][cx+dx[p]*k] = c
                    break
                # 다른색의 돌을 만날 경우 cnt를 늘리며 진행
                elif arr[cy+dy[p]][cx+dx[p]] != 0 and abs(arr[cy+dy[p]][cx+dx[p]] - arr[y-1][x-1]) == 1:
                    cnt += 1
                    cy += dy[p]
                    cx += dx[p]
    sum_w = 0
    sum_b = 0
    # 검은색 돌과 흰색 돌의 개수를 체크
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] == 1:
                sum_b += 1
            elif arr[j][i] == 2:
                sum_w += 1
    print('#{} {} {}'.format(t, sum_b, sum_w))
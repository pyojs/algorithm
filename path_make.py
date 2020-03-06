# 등산로가 진행 가능한지 확인하는 함수
def wall(x, y, d):
    if x+dx[d] >= 0 and y+dy[d] >= 0 and x+dx[d] < N and y+dy[d] < N and arr[y][x] > arr[y+dy[d]][x+dx[d]]:
        return True
    return False

# 등산로 최대 길이를 측정하는 함수
def path_cnt(x, y, cnt):
    global max_len_cnt
    if cnt > max_len_cnt:
        max_len_cnt = cnt
    # 4개 방향으로 진행가능한지 확인
    for d in range(4):
        if wall(x, y, d):
            path_cnt(x+dx[d], y+dy[d], cnt+1)

# 우 좌 하 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_len_cnt = 0

    # 현재 등산로에서 최대 높이를 측정하는 반복문
    temp_max_h = 0
    max_h = []
    for j in range(N):
        for i in range(N):
            if arr[j][i] > temp_max_h:
                temp_max_h = arr[j][i]
    # 최대 높이 위치를 찾는 반복문
    for j in range(N):
        for i in range(N):
            if arr[j][i] == temp_max_h:
                max_h.append([i,j])
    # 최대 높이 위치의 개수만큼 반복 실행
    while len(max_h):
        start_x, start_y = max_h.pop()
        for j in range(N):
            for i in range(N):
                # 최대 공사 가능 깊이까지 값을 바꾸며 진행
                for k in range(1, K+1):
                    arr[j][i] -= k
                    path_cnt(start_x, start_y, 1)
                    arr[j][i] += k

    print('#{} {}'.format(t, max_len_cnt))
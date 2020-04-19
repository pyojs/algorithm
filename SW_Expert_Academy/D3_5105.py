# SW Expert Academy 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

# 경계와 벽을 확인하는 함수
def boundary(x, y):
    if x<0 or y<0 or x>N-1 or y>N-1 or maze[y][x] == 1:
        return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발점부터 거리를 저장할 배열
    distance = [[0 for _ in range(N)] for _ in range(N)]
    # 우 좌 하 상
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 시작점과 끝점을 찾아냄
    for j in range(N):
        for i in range(N):
            if maze[j][i] == 3:
                start_x, start_y = i, j
            elif maze[j][i] == 2:
                end_x, end_y = i, j
    result = 0
    q = [[start_x, start_y]]
    maze[start_y][start_x] = 1
    # bfs
    while len(q):
        x, y = q.pop(0)
        # 끝점에 도착하면 결과에 저장하고 종료
        if x == end_x and y == end_y:
            result = distance[y][x] - 1
            break
        # 현재 큐에서 4방향 검사
        for d in range(4):
            if boundary(x+dx[d], y+dy[d]):
                # 지나간 의미로 벽을 세움
                maze[y+dy[d]][x+dx[d]] = 1
                # 거리 저장
                distance[y+dy[d]][x+dx[d]] = distance[y][x] + 1
                q.append([x+dx[d], y+dy[d]])
    print('#{} {}'.format(tc, result))
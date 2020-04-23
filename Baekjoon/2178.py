# BAEKJOON 2178. 미로 탐색

# 경계와 갈 수 있는 길을 확인한는 함수
def boundary(x,y):
    if x>=0 and x<M and y>=0 and y<N and maze[y][x]==1:
        return True
    return False

# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 0,0 에서 시작
q = [[0, 0]]
while len(q):
    x, y = q.pop(0)
    # 현 위체에서 4방향으로 갈 수 있는지 검사
    for d in range(4):
        if boundary(x+dx[d], y+dy[d]):
            # 갈 수 있으면 +1을 해서 해당 칸에 저장
            maze[y+dy[d]][x+dx[d]] = maze[y][x] + 1
            q.append([x+dx[d], y+dy[d]])
# M,N에 있는 결과를 출력
print(maze[N-1][M-1])
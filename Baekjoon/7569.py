# BAEKJOON 7569. 토마토

from collections import deque

# 경계선을 체크할 함수
def boundary(x, y, z):
    if x<0 or y<0 or z<0 or x>M-1 or y>N-1 or z>H-1:
        return False
    return True

# 결과를 계산하는 함수
def check():
    global result
    for k in range(H):
        for j in range(N):
            for i in range(M):
                if tomato[k][j][i] > result:
                    result = tomato[k][j][i]-1
                if tomato[k][j][i] == 0:
                    result = -1
                    return

# 움직이는 방향
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

M, N, H = map(int, input().split())
tomato = list(list(list(map(int, input().split())) for _ in range(N)) for _ in range(H))
# 결과를 저장할 변수
result = -1
# 큐
next_tomato = deque()
# 초기값 설정
for k in range(H):
    for j in range(N):
        for i in range(M):
            if tomato[k][j][i] == 1:
                next_tomato.append([i, j ,k])
# bfs
while next_tomato:
    x, y, z = next_tomato.popleft()
    # 6방향 검사
    for d in range(6):
        # 경계선 내부의 인접한 토마토가 익지 않은 경우 실행
        if boundary(x+dx[d], y+dy[d], z+dz[d]) and tomato[z+dz[d]][y+dy[d]][x+dx[d]] == 0:
            # 영향을 받은 토마토가 익은 날 +1을 저장 후 큐에 추가
            tomato[z+dz[d]][y+dy[d]][x+dx[d]] = tomato[z][y][x] + 1
            next_tomato.append([x+dx[d], y+dy[d], z+dz[d]])
check()
print(result)

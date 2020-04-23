# BAEKJOON 7576. 토마토

from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 우 좌 하 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 일수를 저장할 변수
cnt = -1

# 경계를 확인하는 함수
def boundary(x,y):
    if x<0 or y<0 or x>M-1 or y>N-1 or arr[y][x]:
        return False
    return True

# 일수를 계산할 함수
def bfs(q):
    global cnt
    while q:
        # 한바퀴 돌 때마다 일수 증가
        cnt += 1
        for _ in range(len(q)):
            x ,y = q.popleft()
            for d in range(4):
                if boundary(x+dx[d], y+dy[d]):
                    # 토마토가 익은 것을 표시
                    arr[y+dy[d]][x+dx[d]] = 1
                    # 새로 익은 토마토 위치 저장
                    q.append([x+dx[d], y+dy[d]])
# 큐 사용
q = deque()
for j in range(N):
    for i in range(M):
        if arr[j][i] == 1:
            q.append([i, j])
bfs(q)
# 결과에 일수를 넣음
result = cnt
# 배열을 순회하며 익지 않은 토마토가 있는 경우 결과를 -1로 바꿈
for to in arr:
    if 0 in to:
        result = -1
        break
print(result)
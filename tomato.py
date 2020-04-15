from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = -1

def boundary(x,y):
    if x<0 or y<0 or x>M-1 or y>N-1 or arr[y][x]:
        return False
    return True

def bfs(q):
    global cnt
    while q:
        cnt += 1
        for _ in range(len(q)):
            x ,y = q.popleft()
            for d in range(4):
                if boundary(x+dx[d], y+dy[d]):
                    arr[y+dy[d]][x+dx[d]] = 1
                    q.append([x+dx[d], y+dy[d]])

q = deque()
for j in range(N):
    for i in range(M):
        if arr[j][i] == 1:
            q.append([i, j])
bfs(q)
result = cnt
for to in arr:
    if 0 in to:
        result = -1
        break
print(result)
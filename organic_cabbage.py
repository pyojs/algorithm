def dfs(x, y):
    cabbage[y][x] = 0
    for d in range(4):
        if (x+dx[d] >=0 and x+dx[d] < M and y+dy[d] >= 0 and y+dy[d] < N) and cabbage[y+dy[d]][x+dx[d]]:
            dfs(x+dx[d],y+dy[d])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split())
    cabbage = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        cabbage[Y][X] = 1
    cnt = 0
    for j in range(N):
        for i in range(M):
            if cabbage[j][i] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)
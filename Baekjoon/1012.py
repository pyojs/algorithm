# BAEKJOON 1012. 유기농 배추

# 배추흰지렁이의 필요한 개수를 파악하기 위한 함수
def dfs(x, y):
    # 배열을 0으로 만들어 검사한 것을 표시
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
    # 배추흰지렁이의 필요 개수를 저장할 변수
    cnt = 0
    for j in range(N):
        for i in range(M):
            # 배추가 있는 곳을 발견했을 때 실행
            if cabbage[j][i] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)
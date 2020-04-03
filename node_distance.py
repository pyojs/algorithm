# bfs를 실행할 함수
def bfs(q, cnt, end):
    global result
    next_q = []
    # 현재 큐에 원소가 없을 때까지 진행
    while len(q):
        node = q.pop(0)
        # 끝점에 도달한 경우 종료
        if node == end:
            result = cnt
            return
        # 현재 노드에서 방문을 안한 노드 중 갈 수 있는 노드를 다음 큐에 추가
        for n in range(1, V+1):
            if visited[n] == 0 and pos[node][n] == 1:
                visited[n] = 1
                next_q.append(n)
    # 다음에 실행할 큐에 원소가 없을 경우 종료
    if len(next_q) == 0:
        return
    # 원소가 있으면 bfs 다시 실행
    else:
        bfs(next_q, cnt+1, end)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 간선 정보를 저장할 이차원 배열
    pos = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        pos[y][x] = 1
        pos[x][y] = 1
    start_n, end_n = map(int, input().split())
    # 노드 방문 기록을 저장할 배열
    visited = [0]*(V+1)
    result = 0
    # 초기값 정보 정리
    q = [start_n]
    visited[start_n] = 1
    bfs(q, 0, end_n)
    print('#{} {}'.format(tc, result))
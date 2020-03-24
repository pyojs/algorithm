def dfs(V, k):
    # 노드 개수만큼 방문한 경우 종료
    if k == N:
        return
    else:
        # 입력된 노드가 방문을 안했던 경우 실행
        if visited[V] == 0:
            visited[V] = 1
            dfs_result.append(V)
            # 간선 정보 매트릭스를 인덱스 1부터 방문 -> 정점 번호가 작은 것부터 방문
            for i in range(1, N+1):
                if direction_matrix[V][i] == 1:
                    dfs(i, k+1)
            
def bfs(V):
    # bfs에 사용할 q 생성, 앞에서부터 처리
    q = [V]
    # q의 길이가 0이되면 종료
    while len(q):
        # 방문할 노드 선택
        V = q.pop(0)
        # 노드가 방문을 안했던 경우 실행
        if visited[V] == 0:
            visited[V] = 1
            bfs_result.append(V)
            # 간선 정보 매트릭스를 인덱스 1부터 방문 -> 정점 번호가 작은 것부터 방문
            for i in range(1, N+1):
                if direction_matrix[V][i] == 1:
                    q.append(i)


N, M, V = map(int, input().split())
# 간선의 정보를 입력하기 위한 매트릭스 생성(인덱스 0은 사용 X)
direction_matrix = [[0]*(N+1) for _ in range(N+1)]
# 양방향 정보 입력, 배열은 정점 번호가 작은 것부터 방문 가능
for _ in range(M):
    temp = list(map(int, input().split()))
    direction_matrix[temp[0]][temp[1]] = 1
    direction_matrix[temp[1]][temp[0]] = 1

# dfs에 사용할 방문 배열과 결과 리스트 생성
visited = [0]*(N+1)
dfs_result = []
dfs(V, 0)

# bfs에 사용할 방문 배열과 결과 리스트 생성
visited = [0]*(N+1)
bfs_result = []
bfs(V)

print(*dfs_result)
print(*bfs_result)
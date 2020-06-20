# BAEKJOON 11724. 연결 요소의 개수

# dfs를 실행하는 함수
def dfs(n):
    for i in range(N+1):
        # 간선 정보가 있고 방문하지 않았을 경우
        if graph[n][i] and visited[i] == 0:
            # 방문 여부를 체크하고 재귀
            visited[i] = 1
            dfs(i)

N, M = map(int, input().split())
# 간선 정보를 저장할 배열 생성
graph = list([0]*(N+1) for _ in range(N+1))
# 방문 여부를 저장할 배열 생성
visited = [0]*(N+1)
# 결과를 저장하 변수
result = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
# 연결 요소 개수를 찾기 위한 반복문
for i in range(1, N+1):
    # 해당 노드를 방문하지 않았을 경우
    if visited[i] == 0:
        # 방문 여부 체크
        visited[i] = 1
        # 결과 +1
        result += 1
        # 연결된 노드 검사
        dfs(i)
print(result)
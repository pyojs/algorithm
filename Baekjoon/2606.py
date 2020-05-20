# BAEKJOON 2606. 바이러스

# 바이러스를 퍼트리는 함수
def chain(n):
    global result
    # 바이러스에 걸린 것을 표시
    visited[n] = 1
    for k in range(1, N+1):
        # 현재 컴퓨터 번호와 연결되어 있고 바이러스가 걸리지 않은 경우 실행
        if connect[n][k] and visited[k] == 0:
            # 결과를 +1하고 재귀
            result += 1
            chain(k)

N = int(input())
M = int(input())
# 바이러스 여부을 저장할 배열
visited = [0]*(N+1)
# 연결 정보를 저장할 2차원 배열
connect = list([0]*(N+1) for _ in range(N+1))
for _ in range(M):
    a, b = map(int, input().split())
    connect[a][b] = 1
    connect[b][a] = 1
# 결과를 저장할 변수
result = 0
chain(1)
print(result)
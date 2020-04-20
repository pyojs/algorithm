# SW Expert Academy 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

# 간선의 방향으로 움직이며 방문하는 함수
def move(k):
    global result, V
    # 방문을 안한 노드인 경우 실행
    if visited[k] == 0:
        visited[k] = 1
        for i in range(1, V+1):
            # 간선이 존재하는 경우 다시 실행
            if arr[k][i]:
                move(i)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    # 간선 정보를 저장할 2차원 배열
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        temp = list(map(int, input().split()))
        arr[temp[0]][temp[1]] = 1
    S, G = map(int, input().split())
    # 방문 기록을 저장할 리스트
    visited = [False for _ in range(V+1)]
    # 결과를 기록할 변수
    result = 0
    # 방문 정보를 만듬
    move(S)
    # 도착 노드에 방문을 했으면 결과를 변경
    if visited[G]:
        result = 1

    print('#{} {}'.format(t, result))
# BAEKJOON 10026. 적록색약

from collections import deque

N = int(input())
arr = list(list(map(str, input())) for _ in range(N))
# 움직이는 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# q 사용
q = deque()
# 해당 지점 방문 여부를 표시할 배열
visited = list([0]*N for _ in range(N))
# 적록색약이 아닌 사람의 결과를 저장 하기 위한 변수
result_1 = 0
# 반복문 실행
for j in range(N):
    for i in range(N):
        # 해당 위치에 방문하지 않았을 경우
        if visited[j][i] == 0:
            # 결과 +1
            result_1 += 1
            # bfs 사용
            q.append([i, j])
            visited[j][i] = 1
            while q:
                x, y = q.popleft()
                for d in range(4):
                    if 0 <= x+dx[d] < N and 0 <= y+dy[d] < N and arr[y+dy[d]][x+dx[d]] == arr[j][i] and visited[y+dy[d]][x+dx[d]] == 0:
                        q.append([x+dx[d], y+dy[d]])
                        visited[y+dy[d]][x+dx[d]] = 1

visited = list([0]*N for _ in range(N))
# 적록색약인 사람의 결과를 저장 하기 위한 변수
result_2 = 0
# 적록색약의 표시로 G를 R로 바꿈
for j in range(N):
    for i in range(N):
        if arr[j][i] == 'G':
            arr[j][i] = 'R'
# 반복문 실행
for j in range(N):
    for i in range(N):
        # 해당 위치에 방문하지 않았을 경우
        if visited[j][i] == 0:
            # 결과 +1
            result_2 += 1
            # bfs 사용
            q.append([i, j])
            visited[j][i] = 1
            while q:
                x, y = q.popleft()
                for d in range(4):
                    if 0 <= x+dx[d] < N and 0 <= y+dy[d] < N and arr[y+dy[d]][x+dx[d]] == arr[j][i] and visited[y+dy[d]][x+dx[d]] == 0:
                        q.append([x+dx[d], y+dy[d]])
                        visited[y+dy[d]][x+dx[d]] = 1

print(result_1, result_2)
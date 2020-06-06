# BAEKJOON 2206. 벽 부수고 이동하기

from collections import deque

N, M = map(int, input().split())
arr = list(list(map(int, input())) for _ in range(N))
# 해당 지점까지 움직인 거리와 벽을 부순 정보를 저장하는 배열
distance = list(list([0, 0] for _ in range(M)) for _ in range(N))
# 움직이는 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 결과를 저장할 변수
result = -1
# 큐 사용
q = deque()
# 초기 설정
q.append([0, 0, 0])
distance[0][0][0] = 1
distance[0][0][1] = 1
while q:
    x, y, wall = q.popleft()
    # 목적지에 도착한 경우 저장하고 종료
    if x == M-1 and y == N-1:
        result = distance[y][x][wall]
        break
    # 4방향 탐색
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        # 인덱스 내부이고 거리가 아직 저장 안된 경우
        if 0 <= nx < M and 0 <= ny < N and distance[ny][nx][wall] == 0:
            # 일반 길인 경우
            if arr[ny][nx] == 0:
                # 거리를 저장하고 큐에 추가
                distance[ny][nx][wall] = distance[y][x][wall] + 1
                q.append([nx, ny, wall])
            # 벽을 부수지 않고 않았는데 벽을 만난 경우 실행
            if arr[ny][nx] and wall == 0:
                # 벽을 부순 정보와 거리를 저장하고 큐에 추가
                distance[ny][nx][1] = distance[y][x][wall] + 1
                q.append([nx, ny, 1])
print(result)
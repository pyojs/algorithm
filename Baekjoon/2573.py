# BAEKJOON 2573. 빙산

from collections import deque
# 움직이는 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 빙하를 녹이는 함수
def melt():
    # 녹아야할 지점과 크기를 저장할 딕셔너리
    point = {}
    # 지점을 찾기위한 반복문
    for j in range(N):
        for i in range(M):
            # 빙하가 있는 경우
            if ice[j][i]:
                # 근처 4방향 검사
                for d in range(4):
                    # 바닷물과 접하는 경우 카운트
                    if 0 <= i+dx[d] < M and 0 <= j+dy[d] < N and ice[j+dy[d]][i+dx[d]] == 0:
                        point[(j,i)] = point.get((j,i), 0) + 1
    # 빙하가 녹는 지점과 크기를 줄여줌
    for key, value in point.items():
        # 0보다 작아지면 안되기 때문에 max 사용
        ice[key[0]][key[1]] = max(0, ice[key[0]][key[1]]-value)
        
N, M = map(int, input().split())
ice = list(list(map(int, input().split())) for _ in range(N))
# 시간을 저장할 변수
time = 0
# 결과를 저장할 변수
result = 0
# 반복문 실행
while True:
    # 빙하를 녹임
    melt()
    # 시간 +1
    time += 1
    # 덩어리 계산을 하기 위한 방문 배열 생성
    visited = list([0]*M for _ in range(N))
    # 빙하 덩어리 개수를 저장할 변수
    cnt = 0
    # 반복문 실행
    for j in range(N):
        for i in range(M):
            # 빙하가 있고 방문 안한 경우
            if ice[j][i] and visited[j][i] == 0:
                # 큐 사용
                q = deque()
                # 큐에 추가하고 방문여부 체크
                q.append([i, j])
                visited[j][i] = 1
                # 덩어리 개수 +1
                cnt += 1
                # 연결되어 있는 빙하에 방문여부 체크
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        if 0 <= x+dx[d] < M and 0 <= y+dy[d] < N and ice[y+dy[d]][x+dx[d]] and visited[y+dy[d]][x+dx[d]] == 0:
                            visited[y+dy[d]][x+dx[d]] = 1
                            q.append([x+dx[d], y+dy[d]])
    # 빙하가 없는 경우 종료
    if cnt == 0:
        break
    # 빙하 덩어리 개수가 2개 이상인 경우 시간을 결과에 저장하고 종료
    elif cnt > 1:
        result = time
        break
print(result)
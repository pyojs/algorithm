# BAEKJOON 2468. 안전 영역

from collections import deque

N = int(input())
area = list(list(map(int, input().split())) for _ in range(N))
# 움질일 방향
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# 결과를 저장할 변수
result = 1
# 최대 높이를 저장할 변수
max_h = 0

# 경계선을 검사할 함수
def boundary(x, y):
    if x<0 or y<0 or x>N-1 or y>N-1:
        return False
    return True

# 인접한 안전영역을 이어주는 함수
def bfs(x, y):
    # bfs 사용을 위한 q 생성
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        # 인접한 위치 방문
        for d in range(4):
            # 경계선 내부이고 방문하지 않거나 잠기지 않은 경우 실행
            if boundary(x+dx[d], y+dy[d]) and visited[y+dy[d]][x+dx[d]] == 0:
                visited[y+dy[d]][x+dx[d]] = 1
                q.append([x+dx[d], y+dy[d]])
# 최대 높이를 찾는 반복문
for j in range(N):
    for i in range(N):
        if area[j][i] > max_h:
            max_h = area[j][i]
# 비의 양에 따른 경우를 나누기 위한 반복문
for k in range(2, max_h+1):
    # 잠기거나 방문 여부를 저장할 배열
    visited = list([0]*N for _ in range(N))
    # 임시 결과를 저장할 변수
    temp_result = 0
    # 잠기는 지점을 저장할 반복문
    for j in range(N):
        for i in range(N):
            if area[j][i] < k:
                visited[j][i] = -1
    # 잠기지 않은 부분에서 안전영역의 개수를 검사할 반복문
    for j in range(N):
        for i in range(N):
            # 잠기지 않거나 방문하지 않은 지점인 경우
            if visited[j][i] == 0:
                # 임시 결과 +1하고 방문체크, 인접한 안전영역 방문
                temp_result += 1
                visited[j][i] = 1
                bfs(i, j)
    # 현재 임시 계산 결과가 최종 결과보다 크면 저장
    if temp_result > result:
        result = temp_result
print(result)
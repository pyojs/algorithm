# BAEKJOON 2644. 촌수계산

from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
# 촌수 정보를 저장할 배열
family_matrix = list([0]*(n+1) for _ in range(n+1))
for _ in range(m):
    x, y = map(int, input().split())
    family_matrix[x][y] = 1
    family_matrix[y][x] = 1
# 결과를 저장할 변수(친척 관계가 없다고 가정)
result = -1
# 사람 방문 여부를 기록할 배열
visited = [0]*(n+1)
# 초기 설정
visited[a] = 1
q = deque()
q.append([a,0])
while q:
    x, cnt = q.popleft()
    # 해당하는 사람이 나온 경우
    if x == b:
        # 결과에 촌수를 넣고 종료
        result = cnt
        break
    for i in range(1, n+1):
        # 관계가 있고 아직 방문을 안한 경우 큐에 추가
        if family_matrix[x][i] and visited[i]==0:
            visited[i] = 1
            q.append([i, cnt+1])
print(result)
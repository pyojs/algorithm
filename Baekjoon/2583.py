# BAEKJOON 2583. 영역 구하기

from collections import deque

M, N, K = map(int, input().split())
# 모눈 종이에 정보를 기록할 배열
paper = list([0]*N for _ in range(M))
# 입력된 정보로 반복문을 통해 영역을 나눔
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            paper[M-1-j][i] = 1
# 움직이는 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 영역의 개수를 저장할 변수
cnt = 0
# 영역의 크기를 저장할 배열
result_list = []
# 큐 사용
q = deque()
for j in range(M):
    for i in range(N):
        # 직사강형이 그려져 있지 않은 경우 실행
        if paper[j][i] == 0:
            # 영역 개수 +1
            cnt += 1
            # 큐 활용을 위한 기본 설졍
            q.append([i, j])
            paper[j][i] = 1
            # 현재 영역의 크기를 저장할 변수
            temp_result = 0
            while q:
                # 현재 영역 크기 +1
                temp_result += 1
                x, y = q.popleft()
                # 4방향 탐색
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 인덱스 내부이고 칠해지지 않은 경우 큐에 추가, 영역 색칠
                    if 0 <= nx < N and 0 <= ny < M and paper[ny][nx] == 0:
                        q.append([nx, ny])
                        paper[ny][nx] = 1
            # 현재 영역 크기를 결과에 추가
            result_list.append(temp_result)
# 오름차순 정렬
result_list.sort()
print(cnt)
print(*result_list)
# SW Expert Academy 1249. [S/W 문제해결 응용] 4일차 - 보급로

from collections import deque
# 움직이는 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))
    # 거리를 저장할 배열
    recover = list([float('inf')]*N for _ in range(N))
    # 초기 설정
    recover[0][0] = 0
    # 큐 사용
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        # 4방향 이동
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            # 인덱스 내부이고 복구 시간이 더 짧은 경우 실행
            if 0 <= nx < N and 0 <= ny < N and recover[y][x] + arr[ny][nx] < recover[ny][nx]:
                # 복구 시간을 저장하고 큐에 추가
                recover[ny][nx] = recover[y][x] + arr[ny][nx]
                q.append([nx, ny])
    # 결과 저장
    result = recover[N-1][N-1]
    print('#{} {}'.format(tc, result))
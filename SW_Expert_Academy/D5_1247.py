# SW Expert Academy 1247. [S/W 문제해결 응용] 3일차 - 최적 경로

# 경로를 움직이며 최소 거리를 계산하는 함수
def move(b, k, d):
    global result
    # 고객을 모두 방문한 경우
    if k == N:
        # 현재까지 결과와 마지막 방문 지점과 집의 거리를 더한 것이 결과보다 작은 경우 저장
        if result > d + distance[b][1]:
            result = d + distance[b][1]
    # 계산 도중 현재 결과가 최종 결과보다 커지면 종료
    elif d > result:
        return
    else:
        # 고객의 집을 방문하기 위한 반복문
        for n in range(2, N+2):
            # 아직 방문안한 경우
            if visited[n] == 0:
                # 방문 기록을 남김
                visited[n] = 1
                # 현재 방문한 위치와 거리를 더하여 재귀
                move(n, k+1, d+distance[b][n])
                # 사용이 끝난 경우 방문 배열 0으로
                visited[n] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 입력된 좌표를 나누기 위한 배열
    location = []
    # 입력된 좌표를 지점별로 나누기 위한 반복문
    for i in range(0, len(arr), 2):
        location.append([arr[i], arr[i+1]])
    # 각 좌표들간의 거리를 저장하기 위한 배열
    distance = list([0]*(N+2) for _ in range(N+2))
    # 각 좌표들간의 거리를 저장하는 반복문
    for j in range(len(location)):
        x1, y1 = location[j]
        for i in range(j, len(location)):
            x2, y2 = location[i]
            # 거리 계산
            length = abs(x1- x2) + abs(y1 - y2)
            distance[i][j] = length
            distance[j][i] = length
    # 결과를 저장한 변수
    result = float('inf')
    # 각 지점 방문 여부를 기록한 배열
    visited = [1]*2 + [0]*N
    move(0, 0, 0)
    print('#{} {}'.format(tc, result))
# BAEKJOON 14503. 로봇 청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 청소 여부를 확인할 방문 배열
visited = [[0 for _ in range(M)] for _ in range(N)]
# 북 서 남 동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
# 입력값과 dx, dy의 위치를 맞추기 위한 작업
if d == 1:
    d = 3
elif d == 3:
    d = 1
x, y = c, r
# 결과를 저장할 변수
cnt = 0
# 제자리 회전 횟수를 저장하는 변수
r_cnt = 0
while 1:
    # 현재 위치 청소가 안되있으면 실행
    if visited[y][x] == 0:
        visited[y][x] = 1
        cnt += 1
    # 현재 위치, 방향에서 왼쪽을 검사하고 청소가 안되있는 경우 실행, 이동
    if visited[y+dy[(d+1)%4]][x+dx[(d+1)%4]] == 0 and arr[y+dy[(d+1)%4]][x+dx[(d+1)%4]] == 0:
        r_cnt = 0
        d += 1
        y += dy[d%4]
        x += dx[d%4]
    # 4방향 돌면서 움지이지 못한 경우 실행
    elif r_cnt == 4:
        # 뒤로 움직일 수 없으면 종료
        if arr[y+dy[(d+2)%4]][x+dx[(d+2)%4]]:
            break
        # 뒤로 움직일 수 있으면 이동
        else:
            r_cnt = 0
            y += dy[(d+2)%4]
            x += dx[(d+2)%4]
    # 제자리 회전
    else:
        d += 1
        r_cnt += 1
print(cnt)

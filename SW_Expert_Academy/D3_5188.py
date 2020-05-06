# SW Expert Academy 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

# 경계선을 확인하는 함수
def boundary(x, y):
    if x > N-1 or y > N-1:
        return False
    return True

# 판을 움직이며 합을 구하는 함수
def move(x, y, s):
    global result
    # 오른쪽 아래에 도착한 경우
    if x == N-1 and y == N-1:
        # 합이 현재 결과보다 작은 경우 저장
        if s < result:
            result = s
    # 판을 움직이며 이미 합이 현재 결과보다 커진 경우 종료
    elif s > result:
        return
    else:
        # 움직일 방향(우, 하)
        for d in range(2):
            # 경계선 내부인 경우 실행
            if boundary(x+dx[d], y+dy[d]):
                move(x+dx[d], y+dy[d], s+arr[y+dy[d]][x+dx[d]])

T = int(input())
# 움직일 수 있는 방향(우, 하)
dx = [1, 0]
dy = [0, 1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 결과를 저장할 변수
    result = 987654321
    # 왼쪽 위에서 시작
    move(0, 0, arr[0][0])
    print('#{} {}'.format(tc, result))
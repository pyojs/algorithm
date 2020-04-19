# SW Expert Academy 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

def find(n,s):
    global minv
    # 숫자 선택이 끝난 경우
    if n == N:
        # 합이 최소보다 작은 경우 저장
        if minv > s:
            minv = s
        return
    # 합이 이미 최소보다 커진 경우 종료
    elif minv <= s:
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                find(n+1, s+arr[n][i])
                visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minv = 987654321
    find(0, 0)
    print('#{} {}'.format(t, minv))
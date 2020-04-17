# SW Expert Academy 1861. 정사각형 방

# 방향 설정 / 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 움직일 수 있는 방향을 체크하는 함수
def boundary(x, y):
    if x >= N or y >= N or x < 0 or y < 0 or (arr[y][x] - arr[y-dy[d%4]][x-dx[d%4]] != 1):
        return False
    return True

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    # 처음 시작한 숫자를 기록할 idx, 움직일 수 있는 개수를 저장할 cnt
    result_idx = 987654321
    result_cnt = 0
    # 움직일 수 있는 숫자를 체크하는 배열
    check_move = [0]*(N*N+2)
    
    # 움직일 수 있는 위치를 검사
    for j in range(N):
        for i in range(N):
            for d in range(4):
                if boundary(i+dx[d], j+dy[d]):
                    check_move[arr[j][i]] = 1
                    break
    # 움직일 수 있는 방의 개수를 저장할 변수
    cnt = 0
    for i in range(N*N+1):
        # 움직일 수 있으면 cnt를 증가
        if check_move[i]:
            cnt += 1
        # 움직이는 것이 멈춤 경우 결과 비교
        elif cnt:
            # 최종 값 비교, 저장
            if cnt > result_cnt:
                result_cnt = cnt
                result_idx = i-cnt
            if cnt == result_cnt:
                result_idx = min(result_idx, i-cnt)
            cnt = 0
            
    print('#{} {} {}'.format(t, result_idx, result_cnt+1))
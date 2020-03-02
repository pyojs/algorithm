# 움직일 수 있는 방향을 체크하는 함수
def wall(x, y):
    if x >= N or y >= N or x < 0 or y < 0 or (arr[y][x] - arr[y-dy[d%4]][x-dx[d%4]] != 1):
        return False
    return True

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    # 방향 설정 / 우, 좌, 하, 상
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 처음 움직인 숫자를 기록할 idx, 움직일 수 있는 개수를 저장할 cnt
    result_idx = 10000
    result_cnt = 0
    temp = []
    
    # 완전 탐색 모든 경우를 검색함
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            testx = i
            testy = j
            cnt = 1
            temp_cnt = 0
            d = 0
            # 한 지점에서 네 방향을 둘러볼 수 있도록 함
            while temp_cnt < 4:
                if wall(testx + dx[d%4], testy + dy[d%4]):
                    cnt += 1
                    temp_cnt = 0
                    testx += dx[d%4]
                    testy += dy[d%4]
                else: 
                    temp_cnt += 1
                d += 1
            # 최종 값 비교, 저장
            if cnt > result_cnt:
                result_cnt = cnt
                result_idx = arr[j][i]
            if cnt == result_cnt:
                result_idx = min(result_idx, arr[j][i])
            
    print('#{} {} {}'.format(t, result_idx, result_cnt))
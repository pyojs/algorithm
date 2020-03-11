T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    home_arr = [list(map(int, input().split())) for _ in range(N)]
    max_home_cnt = 0
    K = 1
    # K가 (N//2)*2+1인 경우 배열의 중심을 기준으로 N크기 배열을 가득 채움
    while K <= (N//2)*2+1:
        cost = K*K +(K-1)*(K-1)
        for j in range(N):
            for i in range(N):
                center_x = i
                center_y = j
                revenue = 0
                cnt = 0
                # 중심을 기준으로 상,하,좌,우 K-1칸씩 움직이도록
                for y in range(-K+1, K):
                    for x in range(-K+1, K):
                        if i+x>=0 and j+y>=0 and i+x<N and j+y<N:
                            # 그 중에서 x, y의 절대값을 더한게 K-1 보다 작을 때 실행
                            if abs(x)+abs(y) <= K-1 and home_arr[j+y][i+x] == 1:
                                revenue += M
                                cnt += 1
                benefit = revenue - cost
                # 이익이 0 이상인 경우 결과값 저장
                if benefit >= 0:
                    if cnt > max_home_cnt:
                        max_home_cnt = cnt
        K += 1
    print('#{} {}'.format(tc, max_home_cnt))
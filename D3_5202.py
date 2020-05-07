# SW Expert Academy 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

T = int(input())
for tc in range(1, T+1):
    N  = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간을 기준으로 정렬을 함
    time.sort(key=lambda x: x[1])
    end = time[0][0]
    # 최대 대수를 저장할 변수
    cnt = 1
    for i in range(1, N):
        # 종료 시간이 다음 시작시간보다 빠르거나 같게 끝나는 경우 실행
        if end <= time[i][0]:
            # 종료 시간을 다음 종료 시간으로 변경
            end = time[i][1]
            # 개수 증가
            cnt += 1

    print('#{} {}'.format(tc, cnt))

# SW Expert Academy 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    num = list(map(int, input().split()))
    # 정류장 충전기 존재 여부를 남길 배열
    bus_stop = [0] * (N+1)
    # 결과를 저장할 변수
    result = 0
    # 현재 움직임을 기록할 변수
    move = 0
    for n in num:
        bus_stop[n] = 1

    for _ in range(N):
        move += K
        # 마지막 정류장을 지나면 종료
        if move >= N:
            break
        for _ in range(0, K):
            # 최대로 간 정류장에 충전기가 없는 경우 뒤로 1칸씩 이동
            if bus_stop[move] != 1:
                move -= 1
            # 충전기가 있으면 결과 +1, 종료하고 다음 반복문 실행
            elif bus_stop[move] == 1:
                result += 1
                break
        # 반복문이 끝난 경우(최대 움직일 수 있는 거리 내에 충전기가 없을 때) 결과를 0으로하고 종료
        else:
            result = 0
            break

    print('#{} {}'.format(tc, result))

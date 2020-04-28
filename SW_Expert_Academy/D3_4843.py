# SW Expert Academy 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    # 앞에서 10개(0~9)까지만 정렬
    for i in range(10):
        # 최대, 최소값 지정( 1 <= a <= 100 )
        min_val = 101
        max_val = 0
        # 1, 3, 5, 7, 9번째 숫자
        if i % 2:
            # 현재 위치 이후의 최소값을 찾아 자리 변경
            for j in range(i, N):
                if a[j] < min_val:
                    min_val = a[j]
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        # 0, 2, 4, 6, 8번째 숫자
        else:
            # 현재 위치 이후의 최대값을 찾아 자리 변경
            for j in range(i, N):
                if a[j] > max_val:
                    max_val = a[j]
                    max_idx = j
            a[i], a[max_idx] = a[max_idx], a[i]

    print('#{} '.format(tc), end = '')
    # 앞에서 10개 출력
    print(*a[:10])
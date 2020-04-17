# SW Expert Academy 5688. 세제곱근을 찾아라

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = -1
    k = 0
    # 세제곱근 찾기
    while k**3 < N:
        k += 1
        # 입력된 수의 세제곱근과 같은 경우 결과 반환
        if k**3 == N:
            result = k
            break
    print('#{} {}'.format(tc, result))
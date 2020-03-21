T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = -1
    k = 1
    # 입력된 수와 가장 근접한 세제곱근 찾기
    while k**3 < N:
        k += 1
    # 입력된 수와 같은 경우 결과 반환
    if k**3 == N:
        result = k
    print('#{} {}'.format(tc, result))
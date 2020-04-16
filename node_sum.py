T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)
    for _ in range(M):
        index, value = map(int, input().split())
        arr[index] = value
    i = N - M
    while arr[L] == 0:
        if 2*i + 1 > N:
            arr[i] = arr[2*i]
        else:
            arr[i] = arr[2*i] + arr[2*i + 1]
        i -= 1
    print('#{} {}'.format(tc, arr[L]))
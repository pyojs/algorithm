# SW Expert Academy 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)
    for _ in range(M):
        index, value = map(int, input().split())
        arr[index] = value
    # 뒤의 노드부터 값 저장을 위한 초기 변수
    i = N - M
    # 찾을 노드에 값이 저장될 때까지 진행
    while arr[L] == 0:
        # 자식 노드가 1개인 경우
        if 2*i + 1 > N:
            arr[i] = arr[2*i]
        # 자식 노드가 2개인 경우
        else:
            arr[i] = arr[2*i] + arr[2*i + 1]
        i -= 1
    print('#{} {}'.format(tc, arr[L]))
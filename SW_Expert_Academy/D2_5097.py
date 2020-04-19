# SW Expert Academy 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 맨 앞의 수를 빼고 맨 뒤에 추가함
    for m in range(M):
        arr.append(arr.pop(0))
    # 맨 앞의 수를 출력
    print('#{} {}'.format(tc, arr[0]))
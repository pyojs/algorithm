T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 배열을 순회
    for j in range(N-M+1):
        for i in range(N-M+1):
            total = 0
            # M x M의 크기에 있는 파리 수 검사
            for y in range(j, j+M):
                for x in range(i, i+M):
                    total += fly[y][x]
            # 현재 결과보다 큰 경우 저장
            if total > result:
                result = total
    print('#{} {}'.format(tc, result))
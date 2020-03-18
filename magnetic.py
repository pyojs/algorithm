T = 10
for t in range(1 ,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 배열 전체를 순회
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            move_y = 0
            # N극 성질을 가진 자성체 선택
            if arr[j][i] == 1:
                # 다른 자성체를 만날 때까지 진행
                while j+move_y < 99:
                    move_y += 1
                    # 같은 N극일 경우 종료
                    if arr[j+move_y][i] == 1:
                        break
                    # 다른 극일 경우 결과 +1 후 종료
                    elif arr[j+move_y][i] == 2:
                        result += 1
                        break
    print('#{} {}'.format(t, result))
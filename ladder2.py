for t in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 결과를 저장할 변수
    result = 0
    result_cnt = 10000000
    # 모든 출발점을 검사
    for n in range(100):
        if arr[0][n] == 1:
            cnt = 0
            x, y = n, 0
            while 1:
                # 오른쪽으로 가는 경우 움직인 뒤 한칸 내려감
                if x < 99 and arr[y][x+1]:
                    while x < 99 and arr[y][x+1]:
                        x += 1
                        cnt += 1
                    else:
                        y += 1
                # 왼쪽으로 가는 경우 움직인 뒤 한칸 내려감
                elif x > 0 and arr[y][x-1]:
                    while x > 0 and arr[y][x-1]:
                        x -= 1
                        cnt += 1
                    else:
                        y += 1
                # 밑으로 내려감
                # 밑으로 내려가는 횟수는 모두 같으므로 cnt 증가 X
                elif arr[y+1][x] == 1:
                    y += 1
                # 도착점에 간 경우 움직인 횟수 검사 후 저장
                if y == 99:
                    if result_cnt >= cnt:
                        result_cnt = cnt
                        result = n
                    break
    print('#{} {}'.format(t,result))
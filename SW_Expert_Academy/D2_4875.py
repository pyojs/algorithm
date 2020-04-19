# SW Expert Academy 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # 출벌과 도착 지점 찾기
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] == 2:
                start_x = i
                start_y = j
            elif arr[j][i] == 3:
                end_x = i
                end_y = j
    # 우 좌 하 상
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 스택 연산에 활용할 리스트
    stack_d = []
    # 결과를 저장할 변수(기본으로 도착 불가능하다고 설정)
    result = 0
    # 시작점부터 움직이기 시작
    move_x = start_x
    move_y = start_y
    while 1:
        # 4방향 검사
        for d in range(4):
            # 인덱스 내인 경우 실행
            if move_y+dy[d] >= 0 and move_y+dy[d] < len(arr) and move_x+dx[d] >=0 and move_x+dx[d] < len(arr):
                # 이동한 곳이 벽이 아닌 경우 스택에 추가
                if arr[move_y+dy[d]][move_x+dx[d]] != 1:
                    stack_d.append([move_y+dy[d], move_x+dx[d]])
                    # 지나간 의미로 벽을 세움
                    arr[move_y][move_x] = 1
        # 스택에 저장된 것이 없는 경우 종료(도착 불가)
        if len(stack_d) == 0:
            break
        # 스택의 마지막 원소에서 다시 시작
        else:
            temp = stack_d.pop()
            move_x = temp[1]
            move_y = temp[0]
            # 도착지점인 경우 결과를 바꾸고 종료
            if arr[move_y][move_x] == 3:
                result = 1
                break

    print('#{} {}'.format(t, result))
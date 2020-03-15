def pos(x,y):
    if x < 0 or x > W-1 or y < 0 or y > H-1 or map_arr[y][x] != '.':
        return False
    return True

T = int(input())
for tc in range(1, T+1):
    H, W = map(int,input().split())
    map_arr = [list(input()) for _ in range(H)]
    N = int(input())
    N_list = list(input())
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    front = 0

    # 반복문을 끝내기 위한 변수
    temp_end = False
    # 현재 전차가 바라보는 방향을 검사
    for j in range(H):
        for i in range(W):
            start_x, start_y = i, j
            if map_arr[j][i] == '^':
                front = 0
                temp_end = True
            elif map_arr[j][i] == 'v':
                front = 1
                temp_end = True
            elif  map_arr[j][i] == '<':
                front = 2
                temp_end = True
            elif map_arr[j][i] == '>':
                front = 3
                temp_end = True
            if temp_end:
                break
        if temp_end:
            break
    
    # 입력된 동작을 수행
    for k in range(len(N_list)):
        # 전차가 바라보는 방향을 바꿈
        if N_list[k] == 'U':
            front = 0
        elif N_list[k] == 'D':
            front = 1
        elif N_list[k] == 'L':
            front = 2
        elif N_list[k] == 'R':
            front = 3

        # 포탄을 발사하며 동작을 수행
        if N_list[k] == 'S':
            shot_x = start_x + dx[front]
            shot_y = start_y + dy[front]
            while 1:
                if shot_x < 0 or shot_x > W-1 or shot_y < 0 or shot_y > H-1:
                    break
                elif map_arr[shot_y][shot_x] == '*':
                    map_arr[shot_y][shot_x] = '.'
                    break
                elif map_arr[shot_y][shot_x] == '#':
                    break
                else:
                    shot_x += dx[front]
                    shot_y += dy[front]
        # 움직이는 동작인 경우 갈 수 있는지 검사하고 진행
        elif pos(start_x+dx[front], start_y+dy[front]):
            map_arr[start_y][start_x] = '.'
            start_x += dx[front]
            start_y += dy[front]

        # 바라보는 방향에 맞추어 전차 배치
        if front == 0:
            map_arr[start_y][start_x] = '^'
        elif front == 1:
            map_arr[start_y][start_x] = 'v'
        elif front == 2:
            map_arr[start_y][start_x] = '<'
        elif front == 3:
            map_arr[start_y][start_x] = '>'

    print('#{}'.format(tc), end=' ')
    for n in range(H):
        print(''.join(map_arr[n]))
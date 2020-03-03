# 진행할 방향이 가능한 방향인지를 확인하는 함수
def wall(R, C):
    if R > N-1 or C > M-1 or R < 0 or C < 0 or arr[R][C] == 0:
        return False
    return True

# 갈 수 있는 위치를 추가하기 위한 함수
def check(R, C, last):
    # 소요 시간이 될 경우 멈춤
    if last == L:
        return
    # 배열이 0이 아닌 경우 실행
    elif arr[R][C]:
        # 현재 위치에서 움직일 수 있는 방향만큼 반복문 실행
        for d in direction_list[arr[R][C]-1]:
            # 움직일 위치가 방향이 가능한지 확인
            if wall(R+dy[d], C+dx[d]) and (arr[R+dy[d]][C+dx[d]] in direction_pos[d]):
                # 나중에 값을 돌려주기 위한 임시 변수
                temp = arr[R][C]
                # 한 방향으로 진행하면서 이전 자리와 왔다갔다 하지 않도록 하기 위해 0으로 바꿈
                arr[R][C] = 0
                if [R+dy[d],C+dx[d]] not in result:
                    # 결과값에 추가가 안되어 있는 경우만 추가
                    result.append([R+dy[d],C+dx[d]])
                check(R+dy[d], C+dx[d], last+1)
                # 한 방향으로 검사가 끝나면 다시 구조물에 해당하는 숫자 넣어줌
                arr[R][C] = temp

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 상, 하, 좌, 우
    dx =[0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 각 숫자의 해당하는 구조물들이 움직일 수 있는 방향을 표시함(인덱스 차이가 있어서 나중에 활용할 때는 -1을 해줌)
    direction_list = [[0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
    # 해당 방향으로 움직였을 때 갈 수 있는 구조물인지를 표시함(ex 밑으로 움직이려 할 때 밑에 있는 구조물이 1, 2, 5, 6이 아닌 경우 못감)
    direction_pos = {0 : [1, 2, 5, 6], 1: [1, 2, 4, 7], 2: [1, 3, 4, 5], 3: [1, 3, 6, 7]}
    # 출발 위치를 결과에 넣고 시작
    result = [[R,C]]
    check(R,C,1)
    
    print('#{} {}'.format(t, len(result)))
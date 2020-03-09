# 톱니바퀴를 회전시키는 함수
def rotation(n, d):
    # 시계방향
    if d == 1:
        mag_arr[n].insert(0, mag_arr[n].pop(-1))
    # 반시계방향
    elif d == -1:
        mag_arr[n].append(mag_arr[n].pop(0))

def right(n,d):
    # 인덱스가 3이 넘어가는 경우 종료
    if n == 3:
        return
    # 3번째랑 7번째 비교(인덱스로는 2, 6)
    elif mag_arr[n][2] != mag_arr[n+1][6]:
        rotaion_list.append([n+1, d])
        right(n+1, d*-1)

def left(n,d):
    # 인덱스가 0보다 작아지는 경우 종료
    if n == 0:
        return
    # 3번째랑 7번째 비교(인덱스로는 2, 6)
    elif mag_arr[n-1][2] != mag_arr[n][6]:
        rotaion_list.append([n-1, d])
        left(n-1, d*-1)

# 0 : N, 1 : S
T = int(input())
for t in range(1, T+1):
    K = int(input())
    mag_arr = []
    for n in range(4):
        mag_arr.append(list(map(int,input().split())))
    rat_arr = []
    for k in range(K):
        rat_arr.append(list(map(int,input().split())))
    for k in range(K):
        # 회전을 시킬 톱니바퀴 배열 생성
        rotaion_list= [[rat_arr[k][0]-1, rat_arr[k][1]]]
        # 선택된 톱니바퀴의 오른쪽 탐색(톱니바퀴는 반대로 돌아감으로 방향 * -1)
        right(rat_arr[k][0]-1, rat_arr[k][1]*-1)
        # 선택된 톱니바퀴의 왼쪽쪽 탐색(톱니바퀴는 반대로 돌아감으로 방향 * -1)
        left(rat_arr[k][0]-1, rat_arr[k][1]*-1)
        # 선택이 완료된 경우 회전
        for i in range(len(rotaion_list)):
            rotation(rotaion_list[i][0], rotaion_list[i][1])
    result = 0
    # 결과값 저장
    for i in range(len(mag_arr)):
        result += mag_arr[i][0]*(2**i)
    print('#{} {}'.format(t,result))
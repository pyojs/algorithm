# 인덱스 범위를 제한해주기 위한 함수
def boundary(x, y):
    if x < 0 or y < 0 or x > W-1 or y > H-1:
        return False
    return True

# 벽돌에 구슬이 맞았을 때 벽돌을 제거하기 위한 함수
def remove(c, copy_arr):
    q = []
    r = 0
    # 구슬을 쏜 colum에서 첫번째로 있는 벽돌을 검사
    while boundary(c, r) and copy_arr[r][c] == 0:
        r += 1
    # 구슬을 쏜 colum에서 첫번째로 있는 벽돌이 없으면 종료
    if r == H:
        return
    # 해당 벽돌 위치를, q에 추가
    q.append([c, r])
    # 연쇄 적으로 없어지는 벽돌을 없애기 위한 반복문
    while len(q):
        x, y = q.pop(0)
        # 벽돌에 적힌 숫자를 저장하고 0으로 변경
        k = copy_arr[y][x]
        copy_arr[y][x] = 0
        # 4방향 진행
        for d in range(4):
            # 벽돌에 적힌 숫자-1 까지 진행
            for n in range(1, k):
                if boundary(x+n*dx[d],y+n*dy[d]):
                    # 인덱스 내부일 경우 q에 추가하여 다시 진행
                    q.append([x+n*dx[d],y+n*dy[d]])

# 구슬을 쏘고 정렬하기 위한 함수
def shot():
    # 배열을 copy (구슬을 새로 쏠 때마다)
    copy_arr = [[0]*W for _ in range(H)]
    for j in range(H):
        for i in range(W):
            copy_arr[j][i] = arr[j][i]
    # 구슬 개수만큼 진행
    for k in range(N):
        remove(p[k], copy_arr)
        # 구슬 하나를 쏘고 나서 벽돌을 밑으로 정렬
        for x in range(W):
            for y in range(H-1, 0, -1):
                temp = y
                while(temp >= 1 and copy_arr[temp][x] == 0):
                    temp -=1
                if temp != y:
                    copy_arr[y][x] = copy_arr[temp][x]
                    copy_arr[temp][x] = 0
    # 남아 있는 벽돌 개수 체크
    cnt = 0
    for j in range(H):
        for i in range(W):
            if copy_arr[j][i]:
                cnt += 1
    return cnt

# 구슬을 쏘는 위치를 정하는 함수
def npr(n):
    global count
    # 구슬을 쏘는 위치를 모두 정하였을 때 실행
    if n == N:
        result = shot()
        if result < count:
            count = result
    else:
        # 구슬을 쏘는 위치를 중복순열로 생성
        for i in range(W):
            p[n] = i
            npr(n+1)
            if count == 0:
                return

T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    # 우, 좌, 하, 상
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    p = [0] * N
    # 벽돌개수의 최고값 부여
    count = H*W
    npr(0)
    print('#{} {}'.format(t, count))
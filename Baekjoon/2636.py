# BAEKJOON 2636. 치즈

from collections import deque
# 움직이는 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int ,input().split())
cheeze = list(list(map(int, input().split())) for _ in range(N))
# 모두 녹는 시간을 저장할 변수
time = 0
# 반복문 종료 조건으로 활용할 변수
end_condition = 1
# 큐 사용
q = deque()
# 반복문 사용
while end_condition:
    # 치즈의 각 위치의 방문 여부를 저장할 배열
    visited = list([0]*M for _ in range(N))
    # 공기와 접촉된 치즈를 저장시키기 위한 초기 조건
    q.append([0, 0])
    visited[0][0] = 1
    # 공기에 접촉된 치즈를 저장할 배열
    melt = []
    while q:
        x, y = q.popleft()
        # 4방향 검사
        for d in range(4):
            # 인덱스 내부인 경우 실행
            if 0 <= x+dx[d] < M and 0 <= y+dy[d] < N:
                # 방문을 안한 경우 실행
                if visited[y+dy[d]][x+dx[d]] == 0:
                    # 방문 여부 체크
                    visited[y+dy[d]][x+dx[d]] = 1
                    # 치즈인 경우 melt에 추가
                    if cheeze[y+dy[d]][x+dx[d]]:
                        melt.append([x+dx[d], y+dy[d]])
                    # 이어져 있는 공기인 경우 q에 추가
                    else:
                        q.append([x+dx[d], y+dy[d]])
    # 현재 치즈 개수를 저장할 변수(시간과 따지면 모두 녹기 한 시간 전 개수)
    cnt = 0
    for j in range(N):
        for i in range(M):
            # 치즈가 있으면 +1
            if cheeze[j][i]:
                cnt += 1
    # 현재 녹아야하는 치즈 개수를 저장할 임시 변수
    temp_cnt = 0
    # melt에 있는 치즈를 0으로 바꾸며 개수 체크
    while melt:
        x, y = melt.pop()
        cheeze[y][x] = 0
        temp_cnt += 1
    # 종료 조건 = 현재 치즈 개수와 녹아야 하는 치즈 개수가 같으면 종료
    end_condition = cnt - temp_cnt
    # 시간 +1
    time += 1

print(time)
print(cnt)
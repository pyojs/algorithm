# # 경계와 갈 수 있는 길을 확인한는 함수
# def boundary(x,y):
#     if x<0 or y<0 or x>M-1 or y>N-1 or maze[y][x]==0:
#         return False
#     return True
# # dfs를 구현한 함수
# def path(x, y, s):
#     global result
#     # M,N에 도착한 경우 값 비교
#     if x==M-1 and y==N-1:
#         if s < result:
#             result = s
#     # 중간에 값이 더 커진 경우 미리 종료
#     elif s >= result:
#         return
#     else:
#         # 4방향 탐색
#         for d in range(4):
#             if boundary(x+dx[d], y+dy[d]):
#                 # 지나간 길 표시
#                 maze[y][x] = 0
#                 path(x+dx[d], y+dy[d], s+1)
#                 # 다시 복구
#                 maze[y][x] = 1

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# N, M = map(int, input().split())
# maze = [list(map(int, input())) for _ in range(N)]

# # 결과를 저장할 변수
# result = 987654321
# path(0, 0, 1)
# print(result)

# 경계와 갈 수 있는 길을 확인한는 함수
def boundary(x,y):
    if x>=0 and x<M and y>=0 and y<N and maze[y][x]==1:
        return True
    return False

# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 0,0 에서 시작
q = [[0, 0]]
while len(q):
    x, y = q.pop(0)
    # 현 위체에서 4방향으로 갈 수 있는지 검사
    for d in range(4):
        if boundary(x+dx[d], y+dy[d]):
            # 갈 수 있으면 +1을 해서 해당 칸에 저장
            maze[y+dy[d]][x+dx[d]] = maze[y][x] + 1
            q.append([x+dx[d], y+dy[d]])
# M,N에 있는 결과를 출력
print(maze[N-1][M-1])
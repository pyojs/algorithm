# BAEKJOON 2667. 단지번호붙이기

# 경계선과 집을 확인하는 함수
def boundary(x,y):
    if x<0 or y<0 or x>N-1 or y>N-1 or arr[y][x]==0:
        return False
    return True

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 방문을 했는지 확인하는 배열
visited = [[0 for _ in range(N)] for _ in range(N)]
# 결과들을 저장할 배열
result_list = []
for j in range(N):
    for i in range(N):
        # 집이 있고 방문을 안했을 경우 실행
        if arr[j][i] == 1 and visited[j][i] == 0:
            # BFS 활용
            result = 0
            q = [[i,j]]
            visited[j][i] = 1
            while len(q):
                x, y = q.pop(0)
                result += 1
                # 근처 4방향 검사
                for d in range(4):
                    # 방문을 안한 집이 있을 경우 실행
                    if boundary(x+dx[d], y+dy[d]) and visited[y+dy[d]][x+dx[d]]==0:
                        visited[y+dy[d]][x+dx[d]] = 1
                        q.append([x+dx[d], y+dy[d]])
            result_list.append(result)
print(len(result_list))
# 정렬
result_list.sort()
for n in result_list:
    print(n)

# dfs를 활용하는 경우
# def boundary(x, y):
#     if x<0 or y<0 or x>N-1 or y>N-1 or arr[y][x] == 0:
#         return False
#     return True

# def dfs(x, y):
#     global temp_result
#     for d in range(4):
#         if boundary(x+dx[d], y+dy[d]) and visited[y+dy[d]][x+dx[d]] == 0:
#             visited[y+dy[d]][x+dx[d]] = 1
#             temp_result += 1
#             dfs(x+dx[d], y+dy[d])

# N = int(input())
# arr = [list(map(int,input())) for _ in range(N)]
# visited = [[0 for _ in range(N)] for _ in range(N)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# result_list = []
# for j in range(N):
#     for i in range(N):
#         if arr[j][i] == 1 and visited[j][i] == 0:
#             temp_result = 1
#             visited[j][i] = 1
#             dfs(i, j)
#             result_list.append(temp_result)
# result_list.sort()
# cnt = len(result_list)
# print(cnt)
# for i in range(cnt):
#     print(result_list[i])
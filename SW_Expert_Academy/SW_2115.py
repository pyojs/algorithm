# SW Expert Academy 2115. [모의 SW 역량테스트] 벌꿀채취

def collect(a, s_list):
    global result
    if a == 2:
        # 각 배열에 사용할 조합을 적용
        total = [0, 0]
        temp_result = [0, 0]
        for k in range(len(visited_arr[p[0]])):
            if visited_arr[p[0]][k]:
                total[0] += s_list[0][k]
                temp_result[0] += s_list[0][k]**2
                if total[0] > C:
                    return
        for k in range(len(visited_arr[p[1]])):
            if visited_arr[p[1]][k]:
                total[1] += s_list[1][k]
                temp_result[1] += s_list[1][k]**2
                if total[1] > C:
                    return
        if sum(temp_result) > sum(result):
            result = temp_result
    else:
        # 각 배열에 사용할 조합을 순열로 작성
        for i in range(len(visited_arr)):
            p[a] = i
            collect(a+1, s_list)
# 벌꿀을 채집할 조합을 만드는 함수
def ncr(a):
    c = [1, 0]
    if a == M:
        if sum(visited) != 0:
            visited_arr.append(list(visited))
    else:
        for i in range(2):
            visited[a] = c[i]
            ncr(a+1)
# 벌꿀을 채집할 배열을 만드는 함수
def sel(k, x, y):
    if k == 2:
        collect(0, sel_result)
    else:
        for j in range(y, N):
            for i in range(x, N-M+1):
                sel_result[k] = honey_arr[j][i:i+M]
                sel(k+1, i+M, j)
            x = 0

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*M
    visited_arr = []
    # 벌꿀을 채집할 조합 만듬
    ncr(0)
    # 고른 배열(M)을 저장할 리스트
    sel_result = [[],[]]
    # 각 배열의 값을 저장할 리스트
    result = [0, 0]
    # 순열을 만들기 위한 값 설정
    p = [0] * 2
    sel(0, 0, 0)
    print('#{} {}'.format(t, sum(result)))
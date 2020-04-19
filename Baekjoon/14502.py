# BAEKJOON 14502. 연구소

# 경계선을 검사하는 함수
def boundary(x,y):
    if x<0 or y<0 or x>M-1 or y>N-1:
        return False
    return True

# 벽을 3개 세우고 바이러스가 퍼진 뒤 안전 영역을 구하는 함수
def virus(k, x, y):
    global result
    # 벽 3개가 세워졌을때 시작
    if k==3:
        # 임시 배열과 결과 생성
        temp_institute = [[0 for _ in range(M)] for _ in range(N)]
        temp_result = 0
        # 배열 복사 및 0개수 저장
        for j in range(N):
            for i in range(M):
                temp_institute[j][i] = institute[j][i]
                if temp_institute[j][i] == 0:
                    temp_result += 1
        # 바이러스를 퍼트리는 반복문
        for j in range(N):
            for i in range(M):
                # 바이러스가 있는 곳을 찾앗을 때 실행
                if temp_institute[j][i] == 2:
                    q = [[i,j]]
                    # 바이러스를 퍼트림
                    while len(q):
                        temp = q.pop(0)
                        for d in range(4):
                            # 경계선 내부에서 2에 붙어있는 0에 바이러스를 퍼트림
                            if boundary(temp[0]+dx[d], temp[1]+dy[d]) and temp_institute[temp[1]+dy[d]][temp[0]+dx[d]] == 0:
                                # 퍼진 바이러스는 -1로 표시(재검사 방지)
                                temp_institute[temp[1]+dy[d]][temp[0]+dx[d]] = -1
                                # 0의 개수가 적어짐으로 -1
                                temp_result -= 1
                                q.append([temp[0]+dx[d], temp[1]+dy[d]])
        # 임시결과를 비교하며 클 경우 최종 결과 저장
        if temp_result > result:
            result = temp_result
    # 벽 3개를 세우기 위한 dfs
    else:
        for j in range(y, N):
            for i in range(x, M):
                if institute[j][i] == 0:
                    institute[j][i] = 1
                    virus(k+1, i+1, j)
                    institute[j][i] = 0
            x = 0

N, M = map(int, input().split())
institute = [list(map(int, input().split())) for _ in range(N)]
# 우 좌 하 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 결과를 저장할 변수
result = 0
virus(0, 0, 0)
print(result)
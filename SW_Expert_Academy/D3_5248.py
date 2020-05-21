# SW Expert Academy 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

# 조를 형성하는 함수
def group(k):
    for n in range(1, N+1):
        # 조에 선정이 안되고 지목 당하거나 지목한 경우 실행
        if visited[n] == 0 and pair_matrix[k][n]:
            # 조 선정 여부를 1로 바꾸고 재귀
            visited[n] = 1
            group(n)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))
    # 조 선정여부를 기록할 배열
    visited = [0]*(N+1)
    # 지목 상황을 저장할 배열
    pair_matrix = list([0]*(N+1) for _ in range(N+1))
    # 지목당하거나 지목한 경우 1로 기록
    for i in range(0, len(pair), 2):
        pair_matrix[pair[i]][pair[i+1]] = 1
        pair_matrix[pair[i+1]][pair[i]] = 1
    # 결과를 저장할 변수
    result = 0
    for n in range(1, N+1):
        # 조에 선정이 안된 경우
        if visited[n] == 0:
            # 조 선정 여부를 1로 바꾸고 결과 +1
            visited[n] = 1
            result += 1
            # 같은 조를 형성하기 위해 함수 실행
            group(n)

    print('#{} {}'.format(tc, result))
# SW Expert Academy 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

def distance(k, d):
    global result
    # 마지막 연결지점에 도착한 경우
    if k == N:
        # 현재 거리과 결과보다 작은 경우 저장
        if d < result:
            result = d
    # 계산 도중 결과보다 현재 거리가 커지면 종료
    elif d > result:
        return
    # 마지막 연결지점에 도착 안한 경우 실행
    else:
        # 간선 연결 정보를 술회
        for i in range(len(node_dict[k])):
            # 방문 안한 노드일 경우 실행
            if visited[node_dict[k][i][0]] == 0:
                # 노드 방문 여부를 체크하고 재귀 실행
                visited[node_dict[k][i][0]] = 1
                distance(node_dict[k][i][0], d+node_dict[k][i][1])
                # 사용이 끝난 경우 방문 여부 해제
                visited[node_dict[k][i][0]] = 0

T = int(input())
for tc in range(1, T+1):
    N, E = map(int ,input().split())
    # 간선 정보를 저장할 딕셔너리
    node_dict = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        if s in node_dict:
            node_dict[s].append([e, w])
        else:
            node_dict[s] = [[e, w]]
    # 노드 방문을 기록할 배열
    visited = [1] + [0]*N
    # 결과를 저장할 변수
    result = 987654321
    distance(0, 0)

    print('#{} {}'.format(tc, result))
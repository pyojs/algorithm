# SW Expert Academy 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용

# 공장을 선택하고 생산비용을 계산하는 함수
def permutation(k, total):
    global result
    # N곳의 공장에 제품을 다 고른 경우
    if k == N:
        # 현재 계산한 비용이 최종 생산 비용보다 작은 경우 저장
        if total < result:
            result = total
    # 계산 중간에 생산 비용이 최종 생산 비용보다 커지면 종료
    elif total > result:
        return
    else:
        # N종의 제품을 공장에 배분하는 반복문
        for i in range(N):
            # 공장 사용을 안한 경우 실행
            if visited[i] == 0:
                # 공장 사용을 체크하고 재귀 실행
                visited[i] = 1
                permutation(k+1, total+cost[k][i])
                # 공장 사용이 끝난 경우 0으로 변경
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    # 공장 사용 여부를 저장할 배열
    visited = [0] * N
    # 최종 생산 비용을 저장할 변수
    result = 987654321
    permutation(0, 0)

    print('#{} {}'.format(tc, result))
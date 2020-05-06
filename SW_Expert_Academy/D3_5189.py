# SW Expert Academy 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

# 관리구역 방문 순서를 정하며 배터리 소비량을 계산하는 함수
def per(k, s):
    global result
    # 방문 순서가 다 정해진 경우
    if k == N-1:
        # 배터리 소비량 합이 현재 결과보다 작은 경우 저장
        if s+energy[move[-1]][0] < result:
            result = s+energy[move[-1]][0]
    else:
        # 방문해야할 관리구역(1~N)
        for i in range(1, N):
            # 방문하지 않은 경우 추가하고 재귀 실행
            if i not in move:
                move.append(i)
                per(k+1, s+energy[move[-2]][i])
                move.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    energy = [list(map(int, input().split())) for _ in range(N)]
    # 방문 순서를 저장할 배열
    move = [0]
    # 배터리 최소 소비량을 저장할 변수
    result = 987654321
    per(0, 0)
    print('#{} {}'.format(tc, result))
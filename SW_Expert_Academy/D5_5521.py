# SW Expert Academy 5521. 상원이의 생일파티

# 초대될 사람을 선정할 함수
def invite(k, d):
    # 친구의 친한 친구까지 고른 경우 종료
    if d == 2:
        return
    else:
        # 초대할 친구를 구하기 위한 반목문
        for n in range(2, N+1):
            # 친한 친구 목록에 있는 경우
            if friedns_matrix[k][n]:
                # 초대하고 재귀 실행
                invited[n] = 1
                invite(n, d+1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    friends = list(list(map(int, input().split())) for _ in range(M))
    # 친한 친구 관계를 기록할 배열
    friedns_matrix = list([0]*(N+1) for _ in range(N+1))
    # 친한 친구 관계 기록
    for friend in friends:
        friedns_matrix[friend[0]][friend[1]] = 1
        friedns_matrix[friend[1]][friend[0]] = 1
    # 초대 여부를 표시할 배열
    invited = [0]*(N+1)
    # 초기 설정
    invited[1] = 1
    invite(1, 0)
    # 초대된 사람의 수를 결과에 저장
    result = sum(invited) - 1

    print('#{} {}'.format(tc, result))
# SW Expert Academy 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    # N개의 피자를 미리 넣어둠
    q = list(range(N))
    while len(q):
        # 가장 먼저 들어온 피자를 검사
        check = q.pop(0)
        # 치즈를 반으로 나눈 뒤 결과 검사
        C[check] = C[check]//2
        # 치즈가 다 녹은 경우
        if C[check] == 0:
            # 더 넣을 피자가 있는지 검사
            if N < M:
                # 있으면 새로운 피자를 넣음
                q.append(N)
                # 다음에 넣을 피자 번호 생성
                N += 1
        # 다 녹지 않은 경우 다시 넣음
        else:
            q.append(check)
    print('#{} {}'.format(tc,check+1))
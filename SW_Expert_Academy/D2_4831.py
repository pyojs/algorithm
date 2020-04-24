# SW Expert Academy 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 결과를 저장할 변수
    temp_result = ''
    # 회문 길이를 저장할 변수
    cnt = 0
    # 회문을 찾았는지 검사하는 변수
    find = False
    # 글자판 검사
    for j in range(N):
        for i in range(N-M+1):
            # 가로 검사
            if arr[j][i] == arr[j][i+M-1]:
                # 회문 검사 시작
                for k in range(M):
                    if arr[j][i+k] == arr[j][i+M-1-k]:
                        temp_result += arr[j][i+k]
                        cnt += 1
                    # 회문이 아니면 종료
                    else:
                        temp_result = ''
                        cnt = 0
                        break
                # 회문 길이가 충족된 경우 저장하고 종료
                if cnt == M:
                    result = temp_result
                    find = True
                    break
            # 세로 검사
            if arr[i][j] == arr[i+M-1][j]:
                # 회문 검사 시작
                for k in range(M):
                    if arr[i+k][j] == arr[i+M-1-k][j]:
                        temp_result += arr[i+k][j]
                        cnt += 1
                    # 회문이 아니면 종료
                    else:
                        temp_result = ''
                        cnt = 0
                        break
                # 회문 길이가 충족된 경우 저장하고 종료
                if cnt == M:
                    result = temp_result
                    find = True
                    break
            if find:
                break
        if find:
            break
    print('#{} {}'.format(tc, result))
# SW Expert Academy 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 숫자 방문 여부와 갈 때 걸린 횟수를 저장할 변수
    num = [0] * 1000001
    # 연산을 하기 위한 큐
    q = deque()
    # 초기값 설정
    num[N] = 1
    q.append([N, 0])
    # 결과를 저장할 변수
    result = 0
    while q:
        # 현재 숫자와 걸린 횟수를 뽑아냄
        x, cnt = q.popleft()
        # 현재 숫자와 M이 같으면
        if x == M :
            # 횟수를 저장하고 종료
            result = cnt
            break
        # 숫자가 다른 경우
        else:
            # 횟수르 1회 증가
            cnt += 1
            # *2 연산을 하는 경우 추가
            next_x = x*2
            if next_x <= 1000000 and num[next_x] == 0:
                num[next_x] = 1
                q.append([next_x, cnt])
            # +1 연산을 하는 경우 추가
            next_x = x+1
            if next_x <= 1000000 and num[next_x] == 0:
                num[next_x] = 1
                q.append([next_x, cnt])
            # -1 연산을 하는 경우 추가
            next_x = x-1  
            if 1 <= next_x and num[next_x] == 0:
                num[next_x] = 1
                q.append([next_x, cnt])
            # -10 연산을 하는 경우 추가
            next_x = x - 10
            if 1 <= next_x and num[next_x] == 0:
                num[next_x] = 1
                q.append([next_x, cnt])

    print('#{} {}'.format(tc, result))
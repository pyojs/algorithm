# SW Expert Academy 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

T = int(input())
for tc in range(1, T+1):
    # 1부터 12까지 숫자를 원소로 가진 집합 A 생성
    A = [x for x in range(1, 13)]
    N, K = map(int, input().split())
    # 결과 개수를 저장할 변수
    result = 0
    # 비트 연산사용
    for i in range(1<<len(A)):
        cnt = 0
        total = 0
        for j in range(len(A)):
            if i & (1<<j):
                cnt += 1
                total += A[j]
        # N개 원소 합이 K인 경우 결과 +1
        if cnt == N and total == K:
            result += 1
    print('#{} {}'.format(tc, result))

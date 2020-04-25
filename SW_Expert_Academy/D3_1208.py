# SW Expert Academy 1208. [S/W 문제해결 기본] 1일차 - Flatten

T = 10
for tc in range(1, T+1):
    dump = int(input())
    h = list(map(int, input().split()))

    # 덤프 횟수만큼 진행
    for _ in range(dump):
        # 최고 높이와 최소높이의 인덱스를 찾아 값 변경
        h[h.index(max(h))] -= 1
        h[h.index(min(h))] += 1
    
    # 최대높이와 최소높이 차이를 구함
    result = max(h) - min(h)
    print('#{} {}'.format(tc, result))
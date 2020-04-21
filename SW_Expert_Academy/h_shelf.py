# SW Expert Academy 1486. 장훈이의 높은 선반

# 점원들이 탑을 쌓는 경우를 만드는 함수
def check(k, s):
    global min_val
    # 직원들의 키를 합한 값이 최소보다 큰 경우 종료
    if s >= min_val:
        return
    # 직원들의 키가 선반보다 높은 경우 실행
    elif k >= N:
        if s >= B and s < min_val:
            min_val = s
        return
    # 직원들의 조합을 만드는 부분
    else:
        visited[k] = 1
        check(k+1, s + visited[k]*H[k])
        visited[k] = 0
        check(k+1, s + visited[k]*H[k])
        
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    
    # 결과를 저장할 변수
    min_val = 987654321
    # 점원을 사용했는지 체크하는 배열
    visited = [0]*N

    check(0, 0)
    print('#{} {}'.format(tc, min_val-B))

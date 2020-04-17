# SW Expert Academy 4613. 러시아 국기 같은 깃발

# 색 조합을 만드는 함수
def comb(k):
    global result
    if k == N:
        # 색 조합이 완성되었을 때 실행(구조상 R이 있으면 완성) 
        if 'R' in c_comb:
            temp_result = 0
            # 선택한 색과 다른 색이 있다면 +1
            for j in range(N):
                for i in range(M):
                    if c_comb[j] != c_arr[j][i]:
                        temp_result += 1
            # 결과와 비교하여 값 저장
            if temp_result < result:
                result = temp_result
    else:
        # B가 없을 때 선택지는 W, B
        if not 'B' in c_comb:
            color = ['W', 'B']
            for i in range(2):
                c_comb[k] = color[i]
                comb(k+1)
                c_comb[k] = ''
        # B가 있고 R이 없을 때 선택지는 B, R
        elif 'B' in c_comb and not 'R' in c_comb:
            color = ['B', 'R']
            for i in range(2):
                c_comb[k] = color[i]
                comb(k+1)
                c_comb[k] = ''
        # R이 있을 때 선택지는 R
        elif 'R' in c_comb:
            color = ['R']
            for i in range(1):
                c_comb[k] = color[i]
                comb(k+1)
                c_comb[k] = ''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    c_arr = [list(input()) for _ in range(N)]
    # 처음 시작은 W로 해야함
    c_comb = ['W']+['']*(N-1)
    result = 987654321
    comb(1)
    print('#{} {}'.format(tc,result))
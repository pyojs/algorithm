# SW Expert Academy 1865. 동철이의 일 분배

# 최대 확률을 저장할 변수
max_per = 0
# 겹치지 않게 일을 분배하는 함수(순열 생각)
def per(a, s):
    global max_per
    # 확률을 곱할수록 작아짐으로 이미 구한 값보다 작은 경우 바로 종료
    if max_per < s:
        if a == N:
            # 더 높은 확률이 나온 경우 결과 수정
            if s > max_per:
                max_per = s
        else:
            for i in range(N):
                if check[i] == 0:
                    check[i] = a+1
                    per(a+1, s * arr[i][a]/100)
                    check[i] = 0
                    
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    per(0, 1)
    # 퍼센트로 맞추기 위해 100을 곱함
    max_per *= 100

    print('#{} {:.6f}'.format(t, max_per))
# SW Expert Academy 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

# 종이를 붙이는 경우를 찾기 위한 함수
def paper(n):
    # dp 활용 / 10X20을 만드는 경우 1가지, 20X20을 만드는 경우 3가지
    p = [1, 3]
    for i in range(2, n+1):
        # 점화식
        p.append(p[i-1] + 2*p[i-2])
    return p[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, paper(N//10-1)))
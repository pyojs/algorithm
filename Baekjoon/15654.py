# BAEKJOON 15650. N과 M (3)

def comb(k):
    # 수열의 길이가 M이 되었을 때 출력
    if k == M:
        print(*result)
    # 수열의 길이가 M이 안될 때
    else:
        # 1부터 N까지의 숫자를 차례로 넣음
        for i in range(1,N+1):
            # 결과에 추가하고 재귀 실행
            result.append(i)
            comb(k+1)
            # 사용이 끝난 경우 제거
            result.pop()

N, M = map(int, input().split())
# 결과를 저장할 배열
result = []
comb(0)
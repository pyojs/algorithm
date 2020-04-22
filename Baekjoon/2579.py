# BAEKJOON 2579. 계단 오르기

# 해당 계단까지 갈 때 최대 점수를 계산하는 함수
def score(n):
    # 첫번째 계단까지 가는 최대 점수
    scores.append(stairs[0])
    # 계단이 1개이면 종료
    if n == 1:
        return
    # 두번째 계단까지 가는 최대 점수
    scores.append(stairs[0] + stairs[1])
    # 계단이 2개이면 종료
    if n == 2:
        return
    # 세번째 계단까지 가는 최대 점수
    scores.append(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))
    # 이후 계단까지 가는 최대 점수
    for i in range(3, N):
        scores.append(max(scores[i-3] + stairs[i-1] + stairs[i], scores[i-2] + stairs[i]))

N = int(input())
stairs = [int(input()) for _ in range(N)]
# 결과값들을 저장할 리스트
scores = []
score(N)
print(scores[-1])
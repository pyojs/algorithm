# BAEKJOON 2798. 블랙잭

# 카드를 선택하고 합을 비교하는 함수
def select(k, total):
    global result
    # 카드 3개를 골랐을 경우
    if k == 3:
        # 카드 합이 M을 초과하지 않고 현재 결과보다 큰 경우 저장
        if total <= M and total > result:
            result = total
    # 계산 도중 카드 합이 M을 초과한 경우 종료
    elif total > M:
        return
    # 카드 3개를 아직 못 고른 경우
    else:
        for i in range(N):
            # 아직 선택하지 않은 카드인 경우 실행
            if used[i] == 0:
                # 카드 사용 여부 표시 후 재귀 실행
                used[i] = 1
                select(k+1, total+card[i])
                # 사용이 끝난 경우 사용 여부 취소
                used[i] = 0

N, M = map(int, input().split())
card = list(map(int, input().split()))
# 결과를 저장할 변수
result = 0
# 카드 사용여부를 표시할 배열
used = [0]*N
select(0, 0)
print(result)